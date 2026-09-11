#!/usr/bin/env python3
"""Retrieve mechanisms from the precedent atlas without pretending weak matches are knowledge.

The script is deliberately dependency-free. It combines exact-token evidence with a
small controlled ontology. Literal subject matches are useful, but a card only becomes
an `ATLAS_MATCH` when it covers more than one meaningful query concept. Otherwise the
correct output is a research gap plus, when available, analogical leads.
"""

from __future__ import annotations

import argparse
import json
import re
import unicodedata
from dataclasses import dataclass
from pathlib import Path


FIELD_WEIGHTS = {
    "problem": 6,
    "mechanism": 6,
    "applicability": 1,
    "tags": 5,
    "function": 4,
    "scene_space": 4,
    "transferable_principle": 4,
    "departments": 3,
    "observable": 2,
    "system_reading": 2,
}

COVERAGE_FIELDS = {
    "problem", "mechanism", "function", "transferable_principle", "observable",
    "system_reading", "tags", "departments", "scene_space",
}

# Some ontology words are especially polysemous. ``transformar`` can describe
# an invalid inference ("sem transformar variedade em prova") rather than a
# narrative transformation, and ``objeto`` can mean a media file rather than an
# object-led film. These concepts only count as covered when they appear in
# fields that state the mechanism/discipline explicitly. Exact-token score may
# still use the broader fields, but it cannot promote semantic coverage.
CONCEPT_COVERAGE_FIELDS = {
    "transformation": {
        "mechanism", "function", "transferable_principle", "system_reading",
        "tags", "departments", "scene_space",
    },
    "object_led": {
        "mechanism", "function", "transferable_principle", "tags",
        "departments", "scene_space",
    },
}

STOP = {
    "a", "as", "o", "os", "um", "uma", "uns", "umas", "de", "da", "do", "das", "dos",
    "e", "em", "no", "na", "nos", "nas", "num", "numa", "para", "por", "com", "que",
    "como", "sobre", "ser", "ter", "filme", "video", "commercial", "comercial", "publicidade",
    "precisa", "quero", "queremos", "fazer", "usar", "coisa", "coisas", "parecer", "pode", "ou",
}

NEGATION_MARKERS = {"sem", "nao", "evitar", "evite", "longe", "contra"}

# These are useful brief words, but they are not subject/category identifiers.
# The list only supports the conservative fallback below; production callers
# should pass ``--subject`` from the structured project intake.
NON_SUBJECT_TERMS = {
    "responsavel", "etica", "etico", "real", "reais", "humana", "humano",
    "narrativo", "narrativa", "motor", "claro", "clara", "coletiva", "coletivo",
    "seguranca", "consequencia", "comeca", "vira", "costurando", "costurar", "continuidade",
    "efeito", "elenco", "pequeno", "pequena", "uma", "locacao", "comunitaria",
    "comunitario", "narram", "mostrar", "mudanca", "produto", "beneficio",
    "film", "campanha", "campaign", "quadro", "apetitoso", "apetitosa", "conduzido",
    "conduzida",
}

# Each key is a concept, not a stylistic preset. Expansions are intentionally small
# and auditable; adding a synonym changes retrieval behavior and should be tested.
ONTOLOGY = {
    "aquatic": {"piscina", "pool", "agua", "aquatico", "aquatica", "subaquatico", "underwater", "swimming", "natacao", "mergulho"},
    "education": {"escola", "escolar", "educacao", "education", "classroom", "sala", "aula", "aprendizado", "learning", "professor", "teacher", "aluno", "student"},
    "technology": {"tecnologia", "technology", "tech", "engenharia", "engineering", "dispositivo", "device", "ferramenta", "tool", "interface"},
    "transformation": {"transformacao", "transformar", "mudanca", "mudar", "change", "reveal", "virada", "before", "after", "reclassificacao"},
    "tension": {"tensao", "suspense", "risco", "perigo", "danger", "risk", "consequencia", "threat", "ameaca", "anticipation"},
    "joy_play": {"diversao", "divertido", "alegria", "joy", "play", "brincadeira", "ludico", "celebracao", "celebration"},
    "camera": {"camera", "enquadramento", "framing", "movimento", "movement", "pov", "lente", "lens", "static", "estatica", "handheld"},
    "color": {"cor", "cores", "color", "colour", "paleta", "palette", "contraste", "contrast", "grade", "grading"},
    "sound": {"som", "sound", "musica", "music", "silencio", "silence", "voz", "voice", "ambiencia", "impacto"},
    "product_demo": {"produto", "product", "demonstracao", "demo", "atributo", "funcional", "functional", "packshot", "beneficio"},
    "low_budget": {"barato", "barata", "baixo", "baixa", "orcamento", "low", "budget", "contido", "contida", "contained"},
    "archive": {"arquivo", "archive", "stock", "acervo", "historico", "found", "footage"},
    "community": {"comunidade", "community", "coletivo", "collective", "uniao", "unity", "rede", "network", "juntos", "together"},
    "performance": {"atuacao", "performance", "casting", "ator", "atriz", "personagem", "character", "coreografia", "choreography"},
    "space": {"espaco", "space", "cenario", "set", "locacao", "location", "ambiente", "environment"},
    "proof": {"prova", "proof", "evidencia", "evidence", "real", "verdadeiro", "demonstrar", "mostrar"},
    "ethics_representation": {"representacao", "representation", "cultura", "cultural", "religiao", "race", "genero", "gender", "identidade", "identity", "responsavel", "responsible", "deficiencia", "disability", "inclusao", "inclusion"},
    "food": {"comida", "food", "alimento", "culinaria", "culinary", "apetite", "appetite", "sabor", "taste", "textura", "texture", "tabletop"},
    "automotive": {"automovel", "automotive", "carro", "car", "veiculo", "vehicle", "moto", "motorcycle"},
    "public_health": {"saude", "health", "publica", "public", "clinica", "clinical", "prevencao", "prevention", "vacina", "vaccine"},
    "fashion": {"moda", "fashion", "roupa", "clothing", "wardrobe", "figurino", "garment"},
    "invisible_vfx": {"compositing", "composicao", "cleanup", "stitch", "costura", "invisivel", "invisible", "roto", "tracking", "reprojecao"},
    "object_led": {"objeto", "objetos", "object", "objects", "sem-pessoas", "no-people", "tabletop", "still-life"},
    "nonprofessional_casting": {"nao-profissional", "nonprofessional", "non-professional", "pessoas-reais", "real-people", "nao-atores", "non-actors"},
    "retail": {"varejo", "retail", "loja", "store", "oferta", "offer", "preco", "price", "cta", "promocao", "promotion"},
    "practical_effects": {"pratico", "pratica", "practical", "in-camera", "fisico", "physical", "efeito-pratico", "practical-effect"},
    "human_centered": {"humano", "humana", "human", "human-centered", "human-centred", "presenca", "presence", "empatia", "empathy"},
    "beauty": {"beauty", "beleza", "cosmetico", "cosmetics", "maquiagem", "makeup", "skin", "pele"},
}

REQUIRED_CONCEPTS = {
    "aquatic", "education", "technology", "low_budget", "archive", "ethics_representation",
    "food", "automotive", "public_health", "fashion", "invisible_vfx", "object_led",
    "nonprofessional_casting", "retail", "practical_effects", "human_centered", "beauty",
}

GAP_IF_UNCOVERED = {"food", "public_health", "object_led"}

# Subject coverage is intentionally separate from scene/mechanism coverage.
# A beauty film set in a school does not become a precedent for the education
# category merely because classrooms appear in the mise-en-scene.
SUBJECT_COVERAGE_BY_WORK = {
    "shiseido-high-school-girl-2015": {"beauty"},
    "nzta-mistakes-2014": {"automotive", "public_health"},
    "apple-welcome-home-2018": {"technology", "product_demo", "human_centered"},
    "libresse-viva-la-vulva-2018": {"public_health", "human_centered"},
    "honda-cog-2003": {"automotive", "product_demo", "object_led"},
    "cadbury-gorilla-2007": {"food", "product_demo"},
    "burberry-open-spaces-2021": {"fashion"},
    "apple-1984": {"technology"},
    "levis-drugstore-1994": {"fashion"},
}

# A broad ontology concept is not proof of a specialized execution mechanism.
# For example, a card about invisible cleanup does not cover a continuity stitch
# unless the card itself explicitly carries both halves of that mechanism.
SPECIALIZED_MECHANISM_PATTERNS = {
    "continuity_stitch": (
        r"\b(?:stitch|stitching|costura|costurar|costurando)\b",
        r"\b(?:continuity|continuidade)\b",
    ),
}

MECHANISM_EVIDENCE_FIELDS = {
    "problem", "mechanism", "function", "transferable_principle", "observable",
    "system_reading", "tags", "departments",
}

SURFACE_CONSTRAINTS = {
    "futurism": {"futurismo", "futurista", "futuristic", "holograma", "hologramas", "hologram", "holograms", "neon", "interface", "interfaces"},
    "lifestyle": {"lifestyle", "resort", "turismo", "travel", "luxo", "luxury"},
    "voiceover": {"locucao", "voiceover", "voice-over", "narracao", "narrator", "narrador"},
    "spectacle": {"espetaculo", "spectacle", "hero", "showreel", "voo", "flight", "flying", "impossible", "impossivel"},
    "people": {"people", "pessoas", "person", "pessoa", "character", "personagem", "performance", "performer", "casting", "actor", "atriz", "ator", "corpo", "body"},
    "vfx": {"vfx", "cgi", "compositing", "composicao", "cleanup", "roto", "tracking", "digital"},
    "animal": {"animal", "animais", "dog", "dogs", "cat", "cats", "gato", "gatos", "cachorro", "cachorros", "horse", "cavalo"},
    "water": {"water", "agua", "pool", "piscina", "underwater", "subaquatico", "mar", "rio"},
    "children": {"child", "children", "crianca", "criancas", "minor", "menor", "student", "aluno"},
}

SAFETY_VOCAB = {
    "child": {"child", "children", "crianca", "criancas", "minor", "minors", "menor", "menores"},
    "animal": SURFACE_CONSTRAINTS["animal"],
    "water": SURFACE_CONSTRAINTS["water"],
    "vehicle": ONTOLOGY["automotive"] | {"traffic", "transito", "road", "estrada", "drive", "dirigir"},
    "health_claim": ONTOLOGY["public_health"] | {"claim", "alegacao", "tratamento", "treatment"},
    "intimacy_identity": {"intimidade", "intimacy", "nudez", "nude", "sexo", "sex", "gender", "genero", "trans", "identity", "identidade"},
}


def normalize(value: object) -> str:
    text = json.dumps(value, ensure_ascii=False) if not isinstance(value, str) else value
    text = unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode("ascii")
    return re.sub(r"[^a-z0-9]+", " ", text.lower()).strip()


def word_set(value: object) -> set[str]:
    return set(normalize(value).split())


def raw_tokens(text: str) -> list[str]:
    return [token for token in normalize(text).split() if len(token) > 1 and token not in STOP]


def detect_concepts(query_words: set[str], original_query: str = "") -> dict[str, set[str]]:
    found: dict[str, set[str]] = {}
    for concept, vocabulary in ONTOLOGY.items():
        hits = query_words & vocabulary
        if hits:
            found[concept] = hits
    normalized = normalize(original_query)
    phrase_rules = {
        "object_led": (r"\b(?:sem|without|no)\s+(?:pessoas|people|actors|atores|cast|elenco)\b", "no_people"),
        "nonprofessional_casting": (r"\b(?:nao|non)\s+(?:profissional|professional|atores|actors)\b|\b(?:pessoas|people)\s+reais\b", "nonprofessional_casting"),
        "practical_effects": (r"\b(?:efeito|effects?)\s+(?:pratico|practical)\b|\bin\s+camera\b", "practical_effects"),
        "human_centered": (r"\bhuman\s+(?:centered|centred)\b|\bcentrad[ao]\s+em\s+pessoas\b", "human_centered"),
        "invisible_vfx": (r"\b(?:vfx|cgi|efeito)\s+(?:invisivel|invisible)\b|\bcosturando\s+continuidade\b", "invisible_vfx"),
    }
    for concept, (pattern, label) in phrase_rules.items():
        if re.search(pattern, normalized):
            found.setdefault(concept, set()).add(label)
    return found


def detect_constraints(text: str) -> tuple[dict[str, set[str]], set[str]]:
    constraints: dict[str, set[str]] = {}
    negated: set[str] = set()
    # Punctuation defines the scope more reliably than an arbitrary four-token window.
    for clause in re.split(r"[.;!?:\n]+", text):
        tokens = normalize(clause).split()
        marker_positions = [index for index, token in enumerate(tokens) if token in NEGATION_MARKERS or token in {"sem", "without", "no"}]
        for index in marker_positions:
            if tokens[index] == "nao" and index + 1 < len(tokens) and tokens[index + 1] in {"profissional", "atores", "ator"}:
                continue
            span = tokens[index + 1:]
            for stop_word in ("mas", "porem", "however", "but"):
                if stop_word in span:
                    span = span[:span.index(stop_word)]
            negated.update(span)
            window = set(span)
            for name, vocabulary in SURFACE_CONSTRAINTS.items():
                hits = window & vocabulary
                if hits:
                    constraints.setdefault(name, set()).update(hits)
    return constraints, negated


def detect_safety(words: set[str], constraints: dict[str, set[str]]) -> list[str]:
    flags: list[str] = []
    constrained_domains = set(constraints)
    for name, vocabulary in SAFETY_VOCAB.items():
        if words & vocabulary and name not in constrained_domains:
            flags.append(name)
    return sorted(flags)


def detect_requested_mechanisms(query: str) -> set[str]:
    """Return specialized mechanisms explicitly requested by the brief."""
    normalized = normalize(query)
    requested: set[str] = set()
    for name, patterns in SPECIALIZED_MECHANISM_PATTERNS.items():
        if all(re.search(pattern, normalized) for pattern in patterns):
            requested.add(name)
    return requested


def card_mechanism_coverage(card: dict, requested: set[str]) -> set[str]:
    """Require explicit card evidence for specialized mechanisms.

    Generic concept/tags such as ``vfx`` or ``invisible`` are deliberately not
    enough. Coverage must be visible in the evidence-facing card fields.
    """
    evidence_text = normalize([card.get(field, "") for field in MECHANISM_EVIDENCE_FIELDS])
    covered: set[str] = set()
    for name in requested:
        patterns = SPECIALIZED_MECHANISM_PATTERNS[name]
        if all(re.search(pattern, evidence_text) for pattern in patterns):
            covered.add(name)
    return covered


def detect_unknown_subject_terms(query: str, explicit_subject: str | None = None) -> list[str]:
    """Expose an unknown primary subject instead of letting mechanisms hide it.

    The reliable route is an explicit subject supplied by the project-state
    intake. For backwards-compatible free text, a deliberately narrow heuristic
    catches a single unknown lead term before the first comma/semicolon/colon
    (for example ``plutonio, beauty...``). It does not pretend to perform open
    vocabulary noun classification.
    """
    source = explicit_subject
    if source is None:
        # Free text has no authoritative subject field. Only recognize the
        # narrow, explicit shape ``single-term, mechanisms...``. Other unknown
        # words remain warnings for live intake, not status-changing guesses.
        if not re.search(r"[,;:]", query):
            return []
        lead = re.split(r"[,;:]", query, maxsplit=1)[0]
        if len(raw_tokens(lead)) != 1:
            return []
        source = lead

    terms = set(raw_tokens(source)) - NEGATION_MARKERS - NON_SUBJECT_TERMS
    known = set().union(*ONTOLOGY.values(), *SAFETY_VOCAB.values(), *SURFACE_CONSTRAINTS.values())
    unknown = sorted(terms - known)
    if explicit_subject is not None:
        return unknown
    return unknown if len(unknown) == 1 else []


def evidence_maturity(card: dict) -> int:
    level = 0
    for item in card.get("evidence", []):
        path = str(item.get("source_path", "")).lower()
        if "/reviews/" in path:
            level = max(level, 3)
        elif "technical_pass" in path or "/review-packs/" in path:
            level = max(level, 2)
        elif "first_pass" in path or "/batches/" in path or "/sources/" in path:
            level = max(level, 1)
    return level


@dataclass
class RankedCard:
    score: int
    card: dict
    exact: set[str]
    concepts: set[str]
    violated_constraints: set[str]
    maturity: int

    @property
    def dimensions(self) -> int:
        return len(self.concepts) + (1 if self.exact else 0)


def score_card(
    card: dict,
    query_terms: set[str],
    query_concepts: dict[str, set[str]],
    constraints: dict[str, set[str]],
) -> RankedCard:
    total = 0
    exact: set[str] = set()
    concepts: set[str] = set()
    violated: set[str] = set()

    searchable_words: set[str] = set()
    for field, weight in FIELD_WEIGHTS.items():
        words = word_set(card.get(field, ""))
        searchable_words.update(words)
        field_exact = query_terms & words
        if field_exact:
            total += weight * len(field_exact)
            exact.update(field_exact)

        for concept, vocabulary in ONTOLOGY.items():
            if concept not in query_concepts:
                continue
            if words & vocabulary:
                # One concept match per field avoids synonym stuffing.
                total += max(1, weight - 1)
                allowed_fields = CONCEPT_COVERAGE_FIELDS.get(concept, COVERAGE_FIELDS)
                if field in allowed_fields:
                    concepts.add(concept)

    do_not_copy_words = word_set(card.get("do_not_copy", ""))
    for name, vocabulary in SURFACE_CONSTRAINTS.items():
        if name not in constraints:
            continue
        if searchable_words & vocabulary and not do_not_copy_words & vocabulary:
            total -= 100
            violated.add(name)

    # A card with several kinds of support is more useful than a token repeated
    # across fields. This bonus is bounded by the number of query concepts.
    total += 4 * len(concepts)
    return RankedCard(total, card, exact, concepts, violated, evidence_maturity(card))


def result_status(
    rows: list[RankedCard],
    query_concepts: dict[str, set[str]],
    minimum: int,
    safety_flags: list[str],
    unknown_subject_terms: list[str] | None = None,
    subject_concepts: set[str] | None = None,
    subject_covered: set[str] | None = None,
    requested_mechanisms: set[str] | None = None,
    covered_mechanisms: set[str] | None = None,
) -> tuple[str, list[str]]:
    if not rows:
        return "RESEARCH_GAP", ["no_match"]
    top = rows[0]
    concept_count = len(query_concepts)
    concept_coverage = len(top.concepts) / concept_count if concept_count else 0.0
    required = set(query_concepts) & REQUIRED_CONCEPTS
    uncovered_required = required - top.concepts
    uncovered_any = set(query_concepts) - top.concepts
    blocking_safety = [flag for flag in safety_flags if flag != "intimacy_identity"]
    reasons: list[str] = []

    if concept_count == 0:
        reasons.append("no_controlled_concept")
    elif concept_count == 1:
        reasons.append("single_concept_query_requires_live_research")

    if top.score < minimum:
        reasons.append("score_below_threshold")
    if top.dimensions < 2:
        reasons.append("single_dimension_match")
    if concept_count and concept_coverage < 0.60:
        reasons.append("low_top_result_concept_coverage")
    if uncovered_required:
        reasons.append("required_concept_uncovered")
    if uncovered_any:
        reasons.append("concept_uncovered")
    if subject_concepts and subject_concepts - (subject_covered or set()):
        reasons.append("subject_concept_uncovered")
    if requested_mechanisms and requested_mechanisms - (covered_mechanisms or set()):
        reasons.append("specialized_mechanism_uncovered")
    if unknown_subject_terms:
        reasons.append("subject_domain_unknown")
    if top.violated_constraints:
        reasons.append("top_result_violates_constraint")
    if top.maturity < 2:
        reasons.append("evidence_maturity_below_match_gate")
    if blocking_safety:
        reasons.append("human_safety_review_required")

    if reasons:
        # Several simultaneous safety domains or a missing central category mean
        # the Atlas is not a recommendation source; at most it provides leads.
        if len(blocking_safety) >= 2:
            return "RESEARCH_GAP", reasons
        if uncovered_required & GAP_IF_UNCOVERED:
            return "RESEARCH_GAP", reasons
        if "aquatic" in uncovered_required and len(uncovered_required) >= 2:
            return "RESEARCH_GAP", reasons
        if top.score >= max(10, minimum // 2) and top.dimensions >= 2:
            return "ATLAS_PARTIAL_NEEDS_LIVE_RESEARCH", reasons
        if top.score >= max(10, minimum // 2) and top.concepts:
            return "ATLAS_PARTIAL_NEEDS_LIVE_RESEARCH", reasons
        return "RESEARCH_GAP", reasons
    return "ATLAS_MATCH", []


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("query")
    parser.add_argument("--limit", type=int, default=8)
    parser.add_argument("--min-score", type=int, default=24)
    parser.add_argument(
        "--subject",
        help="Primary project subject/category from structured intake; unknown terms cap the result below MATCH",
    )
    parser.add_argument("--atlas", type=Path, default=Path(__file__).resolve().parent.parent / "references" / "repertoire" / "research" / "atlas" / "precedents.ndjson")
    args = parser.parse_args()

    words = raw_tokens(args.query)
    constraints, negated_tokens = detect_constraints(args.query)
    query_terms = set(words) - NEGATION_MARKERS - negated_tokens
    query_concepts = detect_concepts(query_terms, args.query)
    subject_terms = set(raw_tokens(args.subject)) if args.subject else set()
    detected_subject_concepts = detect_concepts(subject_terms, args.subject or "")
    for concept, hits in detected_subject_concepts.items():
        query_concepts.setdefault(concept, set()).update(hits)
    subject_concepts = set(detected_subject_concepts)
    query_safety_flags = detect_safety(query_terms, constraints)
    # An explicit subject is positive project scope, not a negated query span.
    # It must independently activate safety even when it is absent from the
    # free-text mechanism query (for example ``--subject crianca``).
    subject_safety_flags = detect_safety(subject_terms, {})
    safety_flags = sorted(set(query_safety_flags) | set(subject_safety_flags))
    unknown_subject_terms = detect_unknown_subject_terms(args.query, args.subject)
    requested_mechanisms = detect_requested_mechanisms(args.query)
    ranked: list[RankedCard] = []
    excluded: list[RankedCard] = []
    for raw in args.atlas.read_text(encoding="utf-8").splitlines():
        if not raw.strip():
            continue
        item = score_card(json.loads(raw), query_terms, query_concepts, constraints)
        if item.violated_constraints:
            excluded.append(item)
        elif item.score > 0:
            ranked.append(item)

    ranked.sort(key=lambda item: (item.score, item.maturity, len(item.concepts), len(item.exact), item.card["id"]), reverse=True)
    excluded.sort(key=lambda item: (len(item.violated_constraints), item.score, item.card["id"]), reverse=True)
    top_subject_covered = (
        subject_concepts & SUBJECT_COVERAGE_BY_WORK.get(ranked[0].card["work_id"], set())
        if ranked else set()
    )
    top_mechanisms_covered = (
        card_mechanism_coverage(ranked[0].card, requested_mechanisms)
        if ranked else set()
    )
    status, reasons = result_status(
        ranked, query_concepts, args.min_score, safety_flags, unknown_subject_terms,
        subject_concepts, top_subject_covered, requested_mechanisms,
        top_mechanisms_covered,
    )
    top_score = ranked[0].score if ranked else 0
    covered = sorted(ranked[0].concepts) if ranked else []
    uncovered = sorted(set(query_concepts) - set(covered))
    print(json.dumps({
        "status": status,
        "top_score": top_score,
        "minimum_score": args.min_score,
        "query_terms": sorted(query_terms),
        "query_concepts": sorted(query_concepts),
        "subject": args.subject,
        "subject_concepts": sorted(subject_concepts),
        "unknown_subject_terms": unknown_subject_terms,
        "constraints": {key: sorted(value) for key, value in constraints.items()},
        "negated_terms_removed_from_scoring": sorted(negated_tokens),
        "query_safety_flags": query_safety_flags,
        "subject_safety_flags": subject_safety_flags,
        "safety_flags": safety_flags,
        "human_review_required": bool(safety_flags),
        "uncovered_concepts": uncovered,
        "subject_covered": sorted(top_subject_covered),
        "subject_uncovered": sorted(subject_concepts - top_subject_covered),
        "requested_mechanisms": sorted(requested_mechanisms),
        "mechanisms_covered": sorted(top_mechanisms_covered),
        "mechanisms_uncovered": sorted(requested_mechanisms - top_mechanisms_covered),
        "reasons": reasons,
        "excluded_counterexamples": [
            {
                "id": row.card["id"],
                "violated_constraints": sorted(row.violated_constraints),
                "label": "CONTRAEXEMPLO_PROIBIDO",
            }
            for row in excluded[:5]
        ],
        "next_action": "use_atlas_then_live_research" if status == "ATLAS_MATCH" else "run_live_project_research_before_recommending",
    }, ensure_ascii=False))

    # Return diverse works first; repeated cards from one work remain available
    # only after the first card of other relevant works.
    selected: list[RankedCard] = []
    deferred: list[RankedCard] = []
    seen_works: set[str] = set()
    for row in ranked:
        work_id = row.card["work_id"]
        if work_id in seen_works:
            deferred.append(row)
        else:
            selected.append(row)
            seen_works.add(work_id)
    selected.extend(deferred)

    for row in selected[: args.limit]:
        card = row.card
        displayed_words = word_set([
            card.get("problem", ""), card.get("mechanism", ""),
            card.get("transferable_principle", ""), card.get("limits", ""),
        ])
        print(json.dumps({
            "score": row.score,
            # Keep the evidence shown to callers auditable: a reported exact
            # term must be visible in the fields returned below. Other support
            # can still affect score through matched_concepts.
            "matched_terms": sorted(row.exact & displayed_words),
            "matched_concepts": sorted(row.concepts),
            "violated_constraints": sorted(row.violated_constraints),
            "evidence_maturity": row.maturity,
            "id": card["id"],
            "card_type": card["card_type"],
            "work": f"{card['brand']} — {card['work_title']}",
            "problem": card["problem"],
            "mechanism": card["mechanism"],
            "transfer": card["transferable_principle"],
            "do_not_copy": card["do_not_copy"],
            "limits": card["limits"],
            "evidence": card["evidence"],
        }, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
