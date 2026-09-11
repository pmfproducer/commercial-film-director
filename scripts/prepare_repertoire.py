#!/usr/bin/env python3
"""Build a portable department brief from the recovered research, without new claims."""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import subprocess
import sys
from pathlib import Path

import search_precedents as atlas

SKILL_ROOT = Path(__file__).resolve().parent.parent
BUNDLE = SKILL_ROOT / "references/repertoire"
CURRICULUM = "research/curricula/2026-08-10_DEPARTMENT_CURRICULUM_MAP.md"
ROLE_MAP = {
    "DIRECTOR": (["directing.film"], [4]),
    "RESEARCHER": (["strategy.brand"], [1]),
    "CREATIVE_DIRECTOR": (["creative.direction"], [2]),
    "SCREENWRITER": (["writing.commercial"], [3]),
    "PERFORMANCE_DIRECTOR": (["casting.performance"], [5]),
    "DP": (["cinematography.dp", "lighting.gaffer", "camera.grip.dit"], [6, 7, 8]),
    "PRODUCTION_DESIGNER": (["art.production_design", "appearance.costume_hmu"], [9, 10]),
    "EDITOR": (["post.editing"], [12]),
    "SOUND_DESIGNER": (["sound.design_mix", "music.supervision_score"], [13, 14]),
    "CONTINUITY_SUPERVISOR": (["production.ad_continuity"], [11]),
    "STORYBOARD_ARTIST": (["directing.film", "art.production_design"], [4, 9]),
    "PRODUCER_AD": (["production.executive", "production.ad_continuity"], [11]),
    "VFX_AI_SUPERVISOR": (["vfx.virtual_production"], [15]),
    "POST_QA": (["color.finishing", "post.editing", "sound.design_mix"], [12, 13, 16]),
    "CRITIC": (["critique.independent"], []),
}


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def verify_bundle() -> dict:
    manifest = json.loads((BUNDLE / "manifest.json").read_text())
    errors = []
    for row in manifest["files"]:
        path = BUNDLE / row["path"]
        if not path.is_file() or digest(path) != row["sha256"]:
            errors.append(row["path"])
    cards = [json.loads(s) for s in (BUNDLE / "research/atlas/precedents.ndjson").read_text().splitlines() if s.strip()]
    broken = [{"card": c["id"], "source": e["source_path"]} for c in cards for e in c["evidence"] if not (BUNDLE / e["source_path"]).is_file()]
    return {"ok": not errors and not broken, "files": len(manifest["files"]), "cards": len(cards), "changed_or_missing": errors, "broken_evidence": broken}


def curriculum_sections(numbers: list[int]) -> list[dict]:
    text = (BUNDLE / CURRICULUM).read_text()
    sections = []
    for n in numbers:
        found = re.search(rf"(?ms)^## {n}\. .*?(?=^## |\Z)", text)
        if found:
            sections.append({"section": n, "source_path": CURRICULUM, "text": found.group(0).strip()})
    return sections


def documents(query: str, limit: int = 6) -> list[dict]:
    """Return reading leads, never promote a lexical match to observed evidence."""
    terms = {x for x in atlas.raw_tokens(query) if len(x) > 2}
    if not terms:
        return []
    candidates = []
    for folder in ("films", "people", "sources"):
        for path in (BUNDLE / "research" / folder).rglob("*.md"):
            text = path.read_text()
            normalized = atlas.normalize(text)
            name_words = atlas.word_set(path.stem)
            hits = terms & set(normalized.split())
            if not hits:
                continue
            score = sum(min(normalized.split().count(t), 3) for t in hits) + 6 * len(terms & name_words)
            paragraphs = re.split(r"\n\s*\n", text)
            excerpt = max(paragraphs, key=lambda p: len(terms & atlas.word_set(p)))[:1600]
            candidates.append({"score": score, "source_path": str(path.relative_to(BUNDLE)), "kind": folder, "title": next((s.lstrip('# ') for s in text.splitlines() if s.startswith('# ')), path.stem), "matched_terms": sorted(hits), "excerpt": excerpt, "use": "reading_lead_only; read source and preserve its declared evidence level"})
    candidates.sort(key=lambda x: (-x["score"], x["source_path"]))
    # Reserve access to film studies; otherwise long governance/source documents dominate.
    chosen = [c for c in candidates if c["kind"] == "films"][:2]
    chosen += [c for c in candidates if c["kind"] == "people"][:1]
    for item in candidates:
        if len(chosen) >= limit:
            break
        if item not in chosen:
            chosen.append(item)
    return chosen


def build_packet(role: str, query: str, limit: int = 6) -> dict:
    if role not in ROLE_MAP:
        raise ValueError(f"Unknown department: {role}")
    if not query.strip():
        raise ValueError("A concrete creative question is required")
    if not 1 <= limit <= 20:
        raise ValueError("limit must be between 1 and 20")
    integrity = verify_bundle()
    if not integrity['ok']:
        raise RuntimeError('Recovered repertoire snapshot changed or has missing evidence; repair or explicitly rebuild it before dispatch.')
    manifest = json.loads((BUNDLE / "manifest.json").read_text())
    ids, section_numbers = ROLE_MAP[role]
    contracts = [json.loads((BUNDLE / "research/agents/contracts" / (cid.replace('.', '__') + '.json')).read_text()) for cid in ids]
    found = subprocess.run([sys.executable, str(SKILL_ROOT / 'scripts/search_precedents.py'), query, '--limit', '107'], check=True, capture_output=True, text=True)
    lines = [json.loads(x) for x in found.stdout.splitlines() if x.strip()]
    header, results = lines[0], lines[1:]
    full_cards = {x['id']: x for x in (json.loads(s) for s in (BUNDLE / 'research/atlas/precedents.ndjson').read_text().splitlines() if s.strip())}
    # Keep creative proposals and cautions visible as separate forms of knowledge.
    creative = [r for r in results if r['card_type'] in {'decision', 'principle', 'sequence'}]
    caution = [r for r in results if r['card_type'] not in {'decision', 'principle', 'sequence'}]
    def enrich(row: dict) -> dict:
        source = full_cards[row['id']]
        return {**row, 'timecode': source['timecode'], 'departments': source['departments'], 'observable': source['observable'], 'declared_why': source['declared_why'], 'system_reading': source['system_reading'], 'evidence_paths': [{'source_path': e['source_path'], 'skill_relative_path': 'references/repertoire/' + e['source_path'], 'exists': (BUNDLE / e['source_path']).is_file()} for e in row['evidence']], 'interpretation': 'reference_for_discussion; match is not proof of creative effectiveness or full viewing'}
    docs = documents(query)
    reads = {CURRICULUM, 'research/00_CORPUS_STATUS.md'}
    reads.update('research/agents/contracts/' + cid.replace('.', '__') + '.json' for cid in ids)
    for row in (creative[:limit] + caution[:3]):
        reads.update(e['source_path'] for e in row['evidence'])
    reads.update(row['source_path'] for row in docs)
    evidence_files = []
    for rel in sorted(reads):
        p = BUNDLE / rel
        evidence_files.append({'source_path': rel, 'skill_relative_path': 'references/repertoire/' + rel, 'exists': p.is_file(), 'sha256': digest(p) if p.is_file() else None})
    return {'schema_version': 1, 'role': role, 'question': query, 'snapshot_date': manifest['snapshot_date'], 'skill_root': str(SKILL_ROOT), 'evidence_limits': manifest['limits'], 'contracts': contracts, 'curriculum_sections': curriculum_sections(section_numbers), 'retrieval': header, 'creative_reference_candidates': [enrich(r) for r in creative[:limit]], 'constraints_and_counterexamples': [enrich(r) for r in caution[:3]], 'reading_leads': docs, 'source_files': evidence_files, 'decision_handoff': ['reference and evidence level actually read', 'mechanism considered and why it fits this brief', 'new proposal and contribution of this department', 'what must not be copied or inferred', 'conflict/dependency to discuss with another department', 'alternative and practical test; change after the discussion'], 'limits': ['Original contracts remain provisional; they are instructions, not trained human professionals.', 'Curriculum and source notes are recovered documents, not newly verified web research.', 'Partial evidence may inform a labeled creative hypothesis; do not invent a viewing session, audience effect, or equipment.', 'Raw media and deeper linked research remain in the original archive, outside this lightweight snapshot.']}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--role', choices=sorted(ROLE_MAP))
    parser.add_argument('--query')
    parser.add_argument('--limit', type=int, default=6)
    parser.add_argument('--output', type=Path)
    parser.add_argument('--check', action='store_true')
    args = parser.parse_args()
    if args.check:
        result = verify_bundle()
    else:
        if not args.role or not args.query:
            parser.error('--role and --query are required unless --check is used')
        result = build_packet(args.role, args.query, args.limit)
    text = json.dumps(result, ensure_ascii=False, indent=2) + '\n'
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text)
        print(json.dumps({'output': str(args.output), 'role': args.role, 'bytes': len(text.encode())}, ensure_ascii=False))
    else:
        print(text)
    return 1 if args.check and not result['ok'] else 0


if __name__ == '__main__':
    raise SystemExit(main())
