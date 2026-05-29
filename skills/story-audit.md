# Skill: Story Audit

## Purpose

Use this skill when asked to evaluate, diagnose, improve, rewrite, or strengthen a story, chapter, screenplay, treatment, scene, outline, premise, or manuscript.

The goal is to identify what is working, what is weak, and what concrete changes will make the story more emotionally compelling.

## Inputs

The user may provide:

- A premise.
- A scene.
- A chapter.
- A manuscript excerpt.
- A screenplay excerpt.
- A treatment.
- A series concept.
- A rough outline.
- A genre target.
- A comparison title.
- A desired tone.

If inputs are incomplete, infer reasonable assumptions and proceed.

## Audit Order

### 1. Dramatic Engine

Identify:

- Who is the story about?
- What do they want?
- Why do they want it now?
- What happens if they fail?
- Who or what opposes them?
- What pressure escalates?

Diagnosis:

- If the protagonist has no clear want, the story lacks forward motion.
- If the opposition is weak, the story lacks pressure.
- If the stakes are vague, the story lacks urgency.
- If there is no "why now," the story lacks momentum.

### 2. Character Design

For each major character, identify:

- External want.
- Internal need.
- Wound, fear, hunger, shame, or false belief.
- Contradiction.
- Pressure point.
- Defining choice.

Use this test:

> Could another character make the same choices in the same scenes?

If yes, the character is under-specific.

### 3. Plot Causality

Convert the plot into a cause-and-effect chain.

Prefer:

> Because A happens, the character chooses B. Because they choose B, C becomes worse.

Avoid:

> A happens, then B happens, then C happens.

Flag any section where events are sequential but not causal.

### 4. Scene Function

For each scene or major beat, determine:

- Who wants what.
- What blocks them.
- What tactic they use.
- What turns.
- What changes.

Flag scenes that only provide exposition, atmosphere, or backstory without changing the dramatic situation.

### 5. Stakes

Identify the story's stakes:

- Physical.
- Emotional.
- Moral.
- Social.
- Relational.
- Spiritual.
- Practical.
- Temporal.

Recommend adding at least one internal or relational stake to every major external stake.

### 6. Theme

State the theme as a dramatic question.

Weak:

> The theme is revenge.

Strong:

> Can revenge restore dignity, or does it make the victim resemble the abuser?

Identify which characters represent competing answers to the theme.

### 7. Dialogue

Check whether dialogue is doing action.

Dialogue should:

- Pursue.
- Hide.
- Test.
- Threaten.
- Seduce.
- Evade.
- Confess.
- Dominate.
- Surrender.
- Bond.
- Betray.

Flag dialogue that states exactly what the character feels when subtext would be stronger.

### 8. Prose or Screen Execution

For prose, inspect:

- Point of view.
- Voice.
- Sensory detail.
- Rhythm.
- Specificity.
- Interiority.
- Paragraph movement.

For screenplay or film, inspect:

- Visual action.
- Image systems.
- Scene transitions.
- Compression.
- Behavior over explanation.
- Cinematic reveal.

For TV, inspect:

- Episode engine.
- Ensemble dynamics.
- Act turns.
- Repeatable conflict.
- Season escalation.
- Relationship reversals.

## Output Format

Return the audit in this format:

```markdown
# Story Audit

## One-Sentence Diagnosis

State the core problem or strength in one sentence.

## What Is Working

List the strongest elements.

## Main Craft Risks

List the biggest weaknesses in priority order.

For each risk, include:

- Problem
- Why it matters
- Recommended fix

## Dramatic Engine

Describe the protagonist, want, obstacle, stakes, and pressure.

## Character Notes

Analyze major characters.

## Plot / Structure Notes

Analyze causality, escalation, turns, and ending direction.

## Scene-Level Notes

Call out scenes or beats that need strengthening.

## Dialogue / Prose Notes

Identify issues with subtext, voice, rhythm, or clarity.

## Recommended Revision Plan

Give a prioritized revision plan.

## Example Rewrite

When useful, provide a short example rewrite showing the improvement.
```
