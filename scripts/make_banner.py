"""Make a README banner (SVG) for a repository.

Usage:
    python scripts/make_banner.py NAME "Tagline text" --category "Dev tools" --tags python cli --out docs/banner.svg

Standard library only. The ring pattern is seeded by the name, so every repo gets its own.
"""
import argparse
import hashlib
import html
import math
from pathlib import Path

PALETTE = ["#5ea8ff", "#c79bff", "#8fb08a", "#ffc66b", "#ff8f6b", "#5fd6c8", "#ff7a9c"]


def wrap(text, width):
    lines, cur = [], ""
    for word in text.split():
        if len(cur) + len(word) + 1 > width and cur:
            lines.append(cur)
            cur = word
        else:
            cur = (cur + " " + word).strip()
    if cur:
        lines.append(cur)
    return lines


def tagline_lines(text, width=62):
    lines = wrap(text, width)
    if len(lines) <= 2:
        return lines
    last = lines[1][:58]
    if " " in last and len(lines[1]) > 58:
        last = last[: last.rfind(" ")]
    return [lines[0], last.rstrip(" ,;.") + "..."]


def make_banner(name, tagline, category="Project", tags=(), color=None):
    seed = int(hashlib.md5(name.encode()).hexdigest(), 16)
    col = color or PALETTE[seed % len(PALETTE)]
    esc = html.escape
    width, height = 1280, 340
    title = name if len(name) <= 30 else name[:29] + "..."
    size = 56 if len(name) <= 24 else 44
    sub = "".join(
        f'<text x="64" y="{196 + 30 * i}" font-size="22" fill="#aeb8ae">{esc(line)}</text>'
        for i, line in enumerate(tagline_lines(tagline))
    )
    chips, x = [], 64
    for tag in list(tags)[:4]:
        w = 18 + len(tag) * 10
        chips.append(
            f'<rect x="{x}" y="276" width="{w}" height="32" rx="16" fill="{col}" fill-opacity="0.12" '
            f'stroke="{col}" stroke-opacity="0.55"/>'
            f'<text x="{x + w / 2}" y="297" text-anchor="middle" font-size="15" fill="{col}">{esc(tag)}</text>'
        )
        x += w + 10
    cx, cy, radii = 1060, 170, (130, 98, 66, 34)
    art = [
        f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="{col}" '
        f'stroke-opacity="{0.10 + 0.07 * i:.2f}" stroke-width="{1 + i}"/>'
        for i, r in enumerate(radii)
    ]
    for i in range(7):
        angle = ((seed >> (i * 5)) % 360) * math.pi / 180
        r = radii[(seed >> (i * 3)) % 4]
        art.append(
            f'<circle cx="{cx + r * math.cos(angle):.1f}" cy="{cy + r * math.sin(angle):.1f}" '
            f'r="{5 + (seed >> i) % 6}" fill="{col}" fill-opacity="0.9"/>'
        )
    art.append(f'<circle cx="{cx}" cy="{cy}" r="10" fill="{col}"/>')
    pill = 20 + len(category) * 9.6
    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="{width}" height="{height}" role="img" aria-label="{esc(name)}: {esc(tagline[:120])}">
<defs>
<linearGradient id="bg" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#0d1013"/><stop offset="1" stop-color="#171d21"/></linearGradient>
<radialGradient id="glow" cx="0.83" cy="0.5" r="0.55"><stop offset="0" stop-color="{col}" stop-opacity="0.28"/><stop offset="1" stop-color="{col}" stop-opacity="0"/></radialGradient>
<pattern id="dots" width="28" height="28" patternUnits="userSpaceOnUse"><circle cx="2" cy="2" r="1.2" fill="#ffffff" fill-opacity="0.06"/></pattern>
</defs>
<g font-family="'JetBrains Mono','SFMono-Regular',Consolas,'Liberation Mono',monospace">
<rect width="{width}" height="{height}" rx="22" fill="url(#bg)"/><rect width="{width}" height="{height}" rx="22" fill="url(#dots)"/><rect width="{width}" height="{height}" rx="22" fill="url(#glow)"/>
<rect x="1" y="1" width="{width - 2}" height="{height - 2}" rx="21" fill="none" stroke="{col}" stroke-opacity="0.35"/>
<rect x="64" y="52" width="{pill:.0f}" height="30" rx="15" fill="{col}"/>
<text x="74" y="73" font-size="15" font-weight="700" fill="#0d1013">{esc(category.upper())}</text>
<text x="64" y="150" font-size="{size}" font-weight="700" fill="#f1f5ef">{esc(title)}</text>
{sub}
{''.join(chips)}
{''.join(art)}
</g></svg>
"""


def main(argv=None):
    parser = argparse.ArgumentParser(description="Make a README banner SVG.")
    parser.add_argument("name")
    parser.add_argument("tagline")
    parser.add_argument("--category", default="Project")
    parser.add_argument("--tags", nargs="*", default=[])
    parser.add_argument("--color", default=None, help="hex colour such as #8fb08a")
    parser.add_argument("--out", default="banner.svg")
    args = parser.parse_args(argv)
    out = Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(make_banner(args.name, args.tagline, args.category, args.tags, args.color), encoding="utf-8", newline="\n")
    print(f"wrote {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
