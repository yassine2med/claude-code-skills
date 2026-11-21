---
name: readme-polish
description: Make a code repository look professional on GitHub: description, topics, banner, badges, screenshot and a clear README. Use for 'make my repo look good' or before sharing a project.
---

# README polish: a repo people want to open

## Checklist
1. **One-sentence description** in the repo settings: what it does and for whom. No jargon.
2. **Topics:** 5 to 8 specific ones (the domain, the language, the tool), not only "python".
3. **Banner** at the top of the README: name, one-line tagline, tags. Use `scripts/make_banner.py` for an SVG that matches across all repos.
4. **Badges:** CI status, language version, license. Three is enough.
5. **Screenshot or terminal output** that is real: run the command, capture the output. Never mock it up.
6. **README structure:** what it is for, install (copy and paste), usage table (I want to / command), a worked example with real output, how it works in 4 to 6 steps, limits (an honest list).
7. **Tests and CI:** at least a dozen real tests and a green workflow.
8. **License file** (MIT unless the code is a product).
9. **No private data:** no emails, phone numbers, keys, or employer names the user cannot share.

## Style
- Plain sentences. One idea each.
- No em dashes if the user avoids them.
- Claims must be true. If the code was never run in the real environment, say so.

## Verify
Open the repo page as a visitor (logged out). Check the banner, the badges, the screenshot and the mobile layout.

## Done means
A stranger can understand what the repo does in 10 seconds and run it in 2 minutes.
