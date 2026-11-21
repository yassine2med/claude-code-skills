---
name: root-cause-fix
description: Find and fix the real cause when something fails. Use on any error, failed check, flaky test, tool that hangs, a wrong number, or when the same step has failed twice.
---

# Root cause first, proof last

No fix before the cause is known. No "fixed" before the original symptom is tested again.

## 1. Look (change nothing yet)
1. Read the whole error. The line number and message usually name the cause.
2. Reproduce it once with the smallest command. If you cannot reproduce it, collect more facts. Do not guess.
3. Ask what changed last: `git log --oneline -5` and `git diff HEAD~1 --stat`.
4. Check whether this failure happened before (a notes file, a lessons log, the issue tracker).

## 2. Find the cause
1. Follow the data one step at a time (input, the function, what it writes, what reads that) until the first wrong value.
2. Say the cause in one sentence: "X happens because Y". If the sentence needs "maybe", keep looking.
3. Two attempts failed: stop trying variations. Your model of the problem is wrong. Go back to step 1.

## 3. Fix
1. Make the smallest change at the cause, not at the symptom. One change at a time.
2. A blocked hook or a failing guard is a rule working, not a fault. Never route around it. If the rule is wrong, say so.
3. A missing tool: say what is missing, show the install command, continue after the user agrees.

## 4. Prove and keep
1. Run the original failing command again. It must pass.
2. Run the full test suite. If a bug slipped past the tests, add a test for it.
3. Write one line in a lessons log: what broke and the fix. A cause seen twice becomes a check or a hook.

## Report (three lines)
What broke. What it affected. What you did. No story of the hunt unless asked.

## Done means
The original command passes, the suite is green, and the lesson is logged.
