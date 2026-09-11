#!/usr/bin/env python3
"""Regression tests for evidence-aware atlas retrieval."""

from __future__ import annotations

import json
import subprocess
import sys
import unittest
from pathlib import Path


SCRIPT = Path(__file__).with_name("search_precedents.py")

BLIND_BENCHMARK = [
    ("school_human_tech", "tecnologia humana na escola sem futurismo nem hologramas; mostrar transformacao real do aprendizado", "ATLAS_PARTIAL_NEEDS_LIVE_RESEARCH"),
    ("pool_turn", "piscina comeca como alegria e brincadeira e vira tensao e consequencia; sem resort", "ATLAS_PARTIAL_NEEDS_LIVE_RESEARCH"),
    ("retail", "varejo com beneficio funcional, oferta e packshot claro", "ATLAS_PARTIAL_NEEDS_LIVE_RESEARCH"),
    ("low_budget", "baixo orcamento, uma locacao, elenco pequeno e efeito pratico", "ATLAS_PARTIAL_NEEDS_LIVE_RESEARCH"),
    ("sound", "som e silencio como motor narrativo, sem locucao", "ATLAS_PARTIAL_NEEDS_LIVE_RESEARCH"),
    ("nonprofessional", "casting nao profissional, pessoas reais e comunidade", "ATLAS_PARTIAL_NEEDS_LIVE_RESEARCH"),
    ("beauty_identity", "beauty, transformacao e reveal de identidade responsavel", "ATLAS_MATCH"),
    # A single Atlas card covers archive+proof but not transformation; the v3
    # gate deliberately stays partial instead of composing sufficiency across
    # unrelated works.
    ("archive", "arquivo historico e found footage como prova de mudanca coletiva", "ATLAS_PARTIAL_NEEDS_LIVE_RESEARCH"),
    ("invisible_vfx", "VFX invisivel costurando continuidade, sem espetaculo", "ATLAS_PARTIAL_NEEDS_LIVE_RESEARCH"),
    ("food", "comida com apetite, textura, prova de produto e som", "RESEARCH_GAP"),
    ("automotive", "automovel, seguranca, tensao e consequencia, sem hero spectacle", "ATLAS_PARTIAL_NEEDS_LIVE_RESEARCH"),
    ("public_health", "saude publica, prova real, comunidade e representacao etica", "RESEARCH_GAP"),
    ("fashion", "moda, baixo orcamento, performance, cor e uma locacao", "ATLAS_PARTIAL_NEEDS_LIVE_RESEARCH"),
    ("object_led", "filme sem pessoas; cenario, objetos, camera e som narram", "RESEARCH_GAP"),
    ("child_animal_water", "crianca, animal e agua; alegria, risco e seguranca", "RESEARCH_GAP"),
    ("school_long_negative", "escola e tecnologia humana; evitar futurismo, neon, holograma e locucao", "ATLAS_PARTIAL_NEEDS_LIVE_RESEARCH"),
    ("community_pool", "piscina comunitaria, baixo orcamento e casting nao profissional; sem luxo nem resort", "RESEARCH_GAP"),
]

# External benchmark frozen by the blind audit. Archive intentionally remains
# expected MATCH here even though the current single-card policy returns PARTIAL;
# the acceptance gate allows one conservative miss but may not rewrite it away.
EXTERNAL_FROZEN_BENCHMARK = [
    ("school_human_tech", "filme para escola sobre tecnologia como ferramenta humana, sem futurismo nem hologramas", "ATLAS_PARTIAL_NEEDS_LIVE_RESEARCH"),
    ("pool_turn", "comercial de piscina começa com alegria e brincadeira, vira tensão e consequência, sem lifestyle de resort", "ATLAS_PARTIAL_NEEDS_LIVE_RESEARCH"),
    ("retail", "filme de varejo demonstra benefício funcional de um produto e termina em packshot claro", "ATLAS_PARTIAL_NEEDS_LIVE_RESEARCH"),
    ("low_budget", "filme de baixo orçamento, uma locação, elenco pequeno e efeito prático", "ATLAS_PARTIAL_NEEDS_LIVE_RESEARCH"),
    ("sound", "filme conduzido por som, silêncio e desenho sonoro, sem locução", "ATLAS_PARTIAL_NEEDS_LIVE_RESEARCH"),
    ("nonprofessional", "história com casting não profissional, presença real e comunidade", "ATLAS_PARTIAL_NEEDS_LIVE_RESEARCH"),
    ("beauty_identity", "beauty film com transformação e reveal de identidade, representação de gênero responsável", "ATLAS_MATCH"),
    ("archive", "filme construído com arquivo histórico e found footage para provar mudança coletiva", "ATLAS_MATCH"),
    ("invisible_vfx", "VFX invisível para costurar continuidade de câmera sem parecer espetáculo", "ATLAS_PARTIAL_NEEDS_LIVE_RESEARCH"),
    ("food", "comercial de comida apetitoso com prova de produto, textura e som", "RESEARCH_GAP"),
    ("automotive", "filme de automóvel sobre segurança, tensão e consequência, sem hero shots espetaculares", "ATLAS_PARTIAL_NEEDS_LIVE_RESEARCH"),
    ("public_health", "campanha de saúde pública com prova real, comunidade e representação ética", "RESEARCH_GAP"),
    ("fashion", "fashion film de baixo orçamento guiado por performance, cor e uma única locação", "ATLAS_PARTIAL_NEEDS_LIVE_RESEARCH"),
    ("object_led", "filme sem pessoas no quadro; cenário, objetos, câmera e som contam a história", "RESEARCH_GAP"),
    ("child_animal_water", "filme com criança, animal e água; alegria, risco e segurança", "RESEARCH_GAP"),
    ("school_long_negative", "tecnologia escolar humana, evitar futurismo, neon, holograma e locução", "ATLAS_PARTIAL_NEEDS_LIVE_RESEARCH"),
    ("community_pool", "piscina comunitária, baixo orçamento, casting real, sem luxo, resort ou turismo", "RESEARCH_GAP"),
]


def query(text: str) -> tuple[dict, list[dict]]:
    result = subprocess.run(
        [sys.executable, str(SCRIPT), text, "--limit", "8"],
        check=True,
        capture_output=True,
        text=True,
    )
    lines = [json.loads(line) for line in result.stdout.splitlines() if line.strip()]
    return lines[0], lines[1:]


def query_with_subject(text: str, subject: str) -> tuple[dict, list[dict]]:
    result = subprocess.run(
        [sys.executable, str(SCRIPT), text, "--subject", subject, "--limit", "8"],
        check=True,
        capture_output=True,
        text=True,
    )
    lines = [json.loads(line) for line in result.stdout.splitlines() if line.strip()]
    return lines[0], lines[1:]


class SearchAtlasTests(unittest.TestCase):
    def test_pool_brief_does_not_promote_camera_only_match(self) -> None:
        header, rows = query(
            "filme sobre piscina que começa como diversão e vira tensão; "
            "câmera revela risco sem parecer propaganda de resort"
        )
        self.assertNotEqual(header["status"], "ATLAS_MATCH")
        self.assertIn("aquatic", header["uncovered_concepts"])
        self.assertTrue(rows)

    def test_school_technology_retrieves_cross_category_proof(self) -> None:
        header, rows = query(
            "tecnologia na escola sem holograma ou interface futurista; "
            "mostrar transformação real do aprendizado"
        )
        self.assertIn(header["status"], {"ATLAS_MATCH", "ATLAS_PARTIAL_NEEDS_LIVE_RESEARCH"})
        ids = {row["id"] for row in rows[:5]}
        # Retrieval returns one card per work before deferred sibling cards, so
        # assert the cross-category Shiseido precedent rather than a specific
        # sibling mechanism.
        self.assertTrue(any(card_id.startswith("shiseido-") for card_id in ids))
        self.assertIn("futurism", header["constraints"])

    def test_exact_tokens_use_words_not_substrings(self) -> None:
        _, rows = query("prova real de transformação")
        for row in rows:
            if "real" in row["matched_terms"]:
                searchable = " ".join((row["problem"], row["mechanism"], row["transfer"], row["limits"]))
                self.assertIn("real", searchable.lower())

    def test_output_carries_evidence_and_copy_warning(self) -> None:
        _, rows = query("produto funcional com plantio e payoff")
        self.assertTrue(rows)
        self.assertTrue(rows[0]["evidence"])
        self.assertTrue(rows[0]["do_not_copy"])

    def test_blind_benchmark_statuses(self) -> None:
        for name, brief, expected in BLIND_BENCHMARK:
            with self.subTest(name=name):
                header, _ = query(brief)
                self.assertEqual(header["status"], expected)

    def test_external_frozen_benchmark_quality_gate(self) -> None:
        correct = 0
        predicted_matches = 0
        correct_matches = 0
        for name, brief, expected in EXTERNAL_FROZEN_BENCHMARK:
            with self.subTest(name=name):
                header, _ = query(brief)
                correct += header["status"] == expected
                if header["status"] == "ATLAS_MATCH":
                    predicted_matches += 1
                    correct_matches += expected == "ATLAS_MATCH"
                self.assertIn(
                    header["next_action"],
                    {
                        "use_atlas_then_live_research",
                        "run_live_project_research_before_recommending",
                    },
                )

        self.assertGreaterEqual(correct, 16)
        self.assertGreater(predicted_matches, 0)
        self.assertGreaterEqual(correct_matches / predicted_matches, 0.90)

    def test_negative_span_terms_never_score_positively(self) -> None:
        header, rows = query(
            "escola e tecnologia humana; evitar futurismo, neon, holograma e locucao"
        )
        removed = set(header["negated_terms_removed_from_scoring"])
        self.assertTrue({"futurismo", "neon", "holograma", "locucao"} <= removed)
        for row in rows:
            self.assertFalse(set(row["matched_terms"]) & removed)

    def test_hard_constraint_violators_are_counterexamples_not_recommendations(self) -> None:
        header, rows = query("filme sem pessoas; cenario, objetos, camera e som narram")
        recommended = {row["id"] for row in rows}
        excluded = {row["id"] for row in header["excluded_counterexamples"]}
        self.assertFalse(recommended & excluded)
        self.assertTrue(all(row["label"] == "CONTRAEXEMPLO_PROIBIDO" for row in header["excluded_counterexamples"]))

    def test_match_never_leaves_required_concept_uncovered(self) -> None:
        for name, brief, _ in BLIND_BENCHMARK:
            with self.subTest(name=name):
                header, _ = query(brief)
                if header["status"] == "ATLAS_MATCH":
                    self.assertNotIn("required_concept_uncovered", header["reasons"])

    def test_match_never_leaves_any_extracted_concept_uncovered(self) -> None:
        header, _ = query("som, cor e performance")
        self.assertNotEqual(header["status"], "ATLAS_MATCH")
        self.assertIn("color", header["uncovered_concepts"])
        self.assertIn("concept_uncovered", header["reasons"])

    def test_unknown_lead_subject_cannot_disappear_behind_strong_mechanisms(self) -> None:
        header, _ = query("plutonio, beauty, transformacao e identidade responsavel")
        self.assertNotEqual(header["status"], "ATLAS_MATCH")
        self.assertEqual(header["unknown_subject_terms"], ["plutonio"])
        self.assertIn("subject_domain_unknown", header["reasons"])

    def test_explicit_unknown_subject_caps_match(self) -> None:
        result = subprocess.run(
            [
                sys.executable,
                str(SCRIPT),
                "beauty, transformacao e identidade responsavel",
                "--subject",
                "plutonio",
                "--limit",
                "1",
            ],
            check=True,
            capture_output=True,
            text=True,
        )
        header = json.loads(result.stdout.splitlines()[0])
        self.assertNotEqual(header["status"], "ATLAS_MATCH")
        self.assertEqual(header["unknown_subject_terms"], ["plutonio"])

    def test_explicit_risk_subjects_activate_safety_and_block_match(self) -> None:
        cases = (
            ("crianca", "child"),
            ("animal", "animal"),
            ("agua", "water"),
            ("automovel", "vehicle"),
            ("saude publica", "health_claim"),
        )
        for subject, expected_flag in cases:
            with self.subTest(subject=subject):
                header, _ = query_with_subject(
                    "beauty, transformacao e identidade responsavel", subject
                )
                self.assertIn(expected_flag, header["subject_safety_flags"])
                self.assertIn(expected_flag, header["safety_flags"])
                self.assertTrue(header["human_review_required"])
                self.assertNotEqual(header["status"], "ATLAS_MATCH")
                self.assertIn("human_safety_review_required", header["reasons"])

    def test_explicit_known_subject_must_be_covered(self) -> None:
        for subject, expected_concept in (("escola", "education"), ("piscina", "aquatic"), ("escola tecnologia", "technology")):
            with self.subTest(subject=subject):
                result = subprocess.run(
                    [
                        sys.executable,
                        str(SCRIPT),
                        "beauty, transformacao e identidade responsavel",
                        "--subject",
                        subject,
                        "--limit",
                        "1",
                    ],
                    check=True,
                    capture_output=True,
                    text=True,
                )
                header = json.loads(result.stdout.splitlines()[0])
                self.assertNotEqual(header["status"], "ATLAS_MATCH")
                self.assertIn(expected_concept, header["subject_uncovered"])
                self.assertIn("subject_concept_uncovered", header["reasons"])

    def test_free_text_filler_words_do_not_become_subjects(self) -> None:
        briefs = [
            "beauty film, transformacao e reveal de identidade responsavel",
            "filme conduzido por som e silencio como motor narrativo sem locucao",
            "VFX invisivel para costurar continuidade sem espetaculo",
            "campanha de saude publica com prova real e comunidade",
        ]
        for brief in briefs:
            with self.subTest(brief=brief):
                header, _ = query(brief)
                self.assertEqual(header["unknown_subject_terms"], [])

        beauty, _ = query("beauty film, transformacao e reveal de identidade responsavel")
        self.assertEqual(beauty["status"], "ATLAS_MATCH")

    def test_continuity_stitch_is_not_covered_by_generic_invisible_vfx(self) -> None:
        header, rows = query(
            "VFX invisivel para costurar continuidade de camera sem parecer espetaculo"
        )
        self.assertEqual(header["status"], "ATLAS_PARTIAL_NEEDS_LIVE_RESEARCH")
        self.assertEqual(header["requested_mechanisms"], ["continuity_stitch"])
        self.assertEqual(header["mechanisms_covered"], [])
        self.assertEqual(header["mechanisms_uncovered"], ["continuity_stitch"])
        self.assertIn("specialized_mechanism_uncovered", header["reasons"])
        self.assertTrue(rows)

    def test_child_animal_water_sets_three_safety_flags(self) -> None:
        header, _ = query("crianca, animal e agua; alegria, risco e seguranca")
        self.assertEqual(set(header["safety_flags"]), {"animal", "child", "water"})
        self.assertTrue(header["human_review_required"])
        self.assertEqual(header["status"], "RESEARCH_GAP")


if __name__ == "__main__":
    unittest.main()
