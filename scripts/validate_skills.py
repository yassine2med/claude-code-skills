"""Check that every skill folder holds a valid SKILL.md.

Usage:
    python scripts/validate_skills.py [skills_dir]

Rules: front matter with name and description, name equals the folder name,
description 40 to 400 characters, a "Done means" section, no private data
(email addresses, phone numbers), no em or en dashes.
Exit code 0 when every skill passes, 1 when any problem is found.
"""
import re
import sys
from pathlib import Path

EMAIL = re.compile(r"[\w.+-]+@[\w-]+\.[\w.-]+")
PHONE = re.compile(r"\(?\d{3}\)?[ -]\d{3}-\d{4}")
DASHES = (chr(8212), chr(8211))


def parse(text):
    match = re.match(r"---\n(.*?)\n---\n(.*)", text, re.S)
    if not match:
        return None, text
    meta = {}
    for line in match.group(1).splitlines():
        if ":" in line:
            key, value = line.split(":", 1)
            meta[key.strip()] = value.strip()
    return meta, match.group(2)


def check_skill(folder):
    problems = []
    path = folder / "SKILL.md"
    if not path.exists():
        return [f"{folder.name}: SKILL.md is missing"]
    meta, body = parse(path.read_text(encoding="utf-8"))
    if meta is None:
        return [f"{folder.name}: front matter is missing"]
    if meta.get("name") != folder.name:
        problems.append(f"{folder.name}: name '{meta.get('name')}' does not match the folder")
    desc = meta.get("description", "")
    if not 40 <= len(desc) <= 400:
        problems.append(f"{folder.name}: description must be 40 to 400 characters (is {len(desc)})")
    if "## Done means" not in body:
        problems.append(f"{folder.name}: no 'Done means' section")
    text = path.read_text(encoding="utf-8")
    if EMAIL.search(text) or PHONE.search(text):
        problems.append(f"{folder.name}: contains an email address or phone number")
    if any(d in text for d in DASHES):
        problems.append(f"{folder.name}: contains an em or en dash")
    return problems


def validate(skills_dir):
    folders = sorted(p for p in Path(skills_dir).iterdir() if p.is_dir())
    problems = []
    for folder in folders:
        problems.extend(check_skill(folder))
    return len(folders), problems


def main(argv=None):
    argv = sys.argv[1:] if argv is None else argv
    skills_dir = argv[0] if argv else "skills"
    if not Path(skills_dir).is_dir():
        print(f"folder not found: {skills_dir}")
        return 2
    count, problems = validate(skills_dir)
    for problem in problems:
        print("FAIL", problem)
    print(f"{count} skills checked, {len(problems)} problem(s)")
    return 1 if problems else 0


if __name__ == "__main__":
    raise SystemExit(main())
