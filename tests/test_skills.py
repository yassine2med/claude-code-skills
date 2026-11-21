import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import make_banner  # noqa: E402
import validate_skills  # noqa: E402


def write_skill(folder, name, desc, body="## Done means\nIt works.\n"):
    folder.mkdir(parents=True)
    (folder / "SKILL.md").write_text(f"---\nname: {name}\ndescription: {desc}\n---\n\n# T\n\n{body}", encoding="utf-8")


GOOD_DESC = "A valid description that is comfortably longer than forty characters."


def test_repo_skills_all_pass():
    count, problems = validate_skills.validate(ROOT / "skills")
    assert count >= 10
    assert problems == []


def test_valid_skill_passes(tmp_path):
    write_skill(tmp_path / "demo", "demo", GOOD_DESC)
    assert validate_skills.check_skill(tmp_path / "demo") == []


def test_name_must_match_folder(tmp_path):
    write_skill(tmp_path / "demo", "other", GOOD_DESC)
    assert any("does not match" in p for p in validate_skills.check_skill(tmp_path / "demo"))


def test_short_description_fails(tmp_path):
    write_skill(tmp_path / "demo", "demo", "too short")
    assert any("description" in p for p in validate_skills.check_skill(tmp_path / "demo"))


def test_missing_done_section_fails(tmp_path):
    write_skill(tmp_path / "demo", "demo", GOOD_DESC, body="Nothing here.\n")
    assert any("Done means" in p for p in validate_skills.check_skill(tmp_path / "demo"))


def test_email_is_rejected(tmp_path):
    mail = "x" + "@" + "example.com"
    body = "## Done means\nWrite to " + mail + "\n"
    write_skill(tmp_path / "demo", "demo", GOOD_DESC, body=body)
    assert any("email" in p for p in validate_skills.check_skill(tmp_path / "demo"))


def test_em_dash_is_rejected(tmp_path):
    write_skill(tmp_path / "demo", "demo", GOOD_DESC, body="## Done means\nIt works " + chr(8212) + " mostly.\n")
    assert any("dash" in p for p in validate_skills.check_skill(tmp_path / "demo"))


def test_missing_skill_file_reported(tmp_path):
    (tmp_path / "empty").mkdir()
    assert validate_skills.check_skill(tmp_path / "empty") == ["empty: SKILL.md is missing"]


def test_cli_exit_codes(tmp_path):
    write_skill(tmp_path / "demo", "demo", GOOD_DESC)
    assert validate_skills.main([str(tmp_path)]) == 0
    write_skill(tmp_path / "bad", "wrong", GOOD_DESC)
    assert validate_skills.main([str(tmp_path)]) == 1
    assert validate_skills.main([str(tmp_path / "missing")]) == 2


def test_banner_is_valid_svg_and_escapes_text():
    svg = make_banner.make_banner("my<repo>", "Fast & simple", "Dev tools", ["python"])
    assert svg.startswith("<svg") and svg.rstrip().endswith("</svg>")
    assert "my&lt;repo&gt;" in svg and "Fast &amp; simple" in svg


def test_banner_is_deterministic_and_unique_per_name():
    a1 = make_banner.make_banner("alpha", "x")
    a2 = make_banner.make_banner("alpha", "x")
    b = make_banner.make_banner("beta", "x")
    assert a1 == a2 and a1 != b


def test_long_tagline_is_cut_at_a_word():
    text = "word " * 60
    lines = make_banner.tagline_lines(text)
    assert len(lines) == 2 and lines[1].endswith("...") and "wor..." not in lines[1]


def test_banner_cli_writes_file(tmp_path):
    out = tmp_path / "docs" / "b.svg"
    assert make_banner.main(["demo", "A tagline", "--tags", "a", "b", "--out", str(out)]) == 0
    assert out.read_text(encoding="utf-8").startswith("<svg")
