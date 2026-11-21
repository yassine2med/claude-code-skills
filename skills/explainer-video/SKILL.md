---
name: explainer-video
description: Make a narrated, animated explainer video on any topic with Manim and a free local text-to-speech voice. Use for 'make me a video on X' or 'animate this'.
---

# Explainer video: script, voice, animation, check, deliver

Everything runs locally with free tools: Manim for animation and any local text-to-speech engine (for example Kokoro or Piper) for the voice.

## 1. Script
1. Default length 60 to 90 seconds, five to seven scenes.
2. Plain, short sentences: one idea each, most under 20 words, active voice.
3. Every fact comes from a source you checked. Never invent numbers.
4. Scene 1 asks the question or names the problem. The last scene gives a one-line takeaway.
5. Save the script as JSON: voice, speed, and a list of scene narrations.

## 2. Scene code
1. One Manim scene class. Each scene: start, animations, finish. The animation time of a scene must be shorter than its narration.
2. Layout: one persistent visual on the left that grows scene by scene, the detail of the current scene on the right. Clear the right side at the end of each scene.
3. Use plain text, not LaTeX, unless LaTeX is installed. Font size 22 or more. One colour per idea, the same in every scene.
4. Picture first: arrows for flow, boxes for things, a tree for hierarchy. Short labels, never a paragraph on screen.

## 3. Build
Render a fast 480p draft first, then the final 1080p. Generate the voice only when the script changed. Add soft captions (an .srt file). Export a contact sheet of six stills.

## 4. Check (never skip)
Look at the contact sheet for overlapping text, text cut at the edge, shapes left over from the previous scene, empty frames and wrong colours. Fix, rebuild, check again. Confirm the narration matches the source facts.

## 5. Deliver
Open the final video for the user. Report the path, the length, the size and one line per scene.

## Done means
The final video exists, the contact sheet looks clean, and the facts match the source.
