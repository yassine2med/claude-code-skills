---
name: site-ship
description: Change, test, check and release a website. Use when asked to change, fix, 'push', 'deploy', 'make it live' or 'ship it'. Runs update, test, browser check, security, then deploy with proof.
---

# Site ship: update, test, check, secure, stop, deploy

Load this from plain words like "change the heading and put it online".

## 1. Update
Find the text with a search (skip build folders and dependencies). Edit only what was asked. If the request changes locked design, say so and offer a content-only version.

## 2. Test
1. Run the production build. Show the last 15 lines only.
2. Run the end-to-end tests. Show only the passed and failed lines.

## 3. Check in a real browser
1. Serve the built output locally.
2. Take a desktop screenshot and a phone screenshot (390 wide) and look at both.
3. Videos play without errors, there is no sideways scroll on the phone, and the console shows 0 errors.
4. Stop the local server when done.

## 4. Secure
1. Run the dependency audit (summary line only). High or critical findings: list them, fix only with the user's yes.
2. Search the diff for keys, tokens, emails and phone numbers. Any hit: stop and tell the user.

## 5. Stop and show
One table: change, build, tests, browser, security, plus screenshot paths. Wait for the user's "push". A request that already said "push" counts as the yes only if every check passed.

## 6. Deploy
1. Commit only the files this task changed.
2. Push, then confirm the branch matches the remote.
3. Poll the live URL for a unique string from the change (every 20 seconds, up to 15 minutes).
4. Check the CI run. A failure: read the failed log, find the cause (`root-cause-fix`).
5. Report: live yes or no, CI green yes or no.

## Done means
The change is visible on the live URL and CI is green.
