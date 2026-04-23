# Getting Started

Never used a terminal or coding tools before? No problem. This guide gets you from zero to running the AI startup coach.

---

## Step 1: Set up Claude Code

Follow the **[GNV Team Setup Guide](https://github.com/TheGinjaNinja/gnv-team-claude-setup)**. It walks you through everything from scratch:

- Getting a Claude account (Step 1)
- Installing a terminal app (Step 2)
- Installing Claude Code (Step 3)
- Setting permissions (Step 4)
- Configuring your terminal (Step 5)

Complete Steps 1 through 5, then come back here.

---

## Step 2: Download the workshop

In your terminal, paste these two commands one at a time:

```
cd ~/Documents/Claude && git clone https://github.com/TheGinjaNinja/hub201-workshop.git
```

```
cd hub201-workshop
```

If you get a "command not found: git" error, see the [setup guide troubleshooting for Step 6](https://github.com/TheGinjaNinja/gnv-team-claude-setup#step-6-set-up-your-claude-folder).

---

## Step 3: Start the AI coach

```
claude
```

That is it. The AI coach will introduce itself, ask about your startup, and guide you through the exercises. It will challenge your thinking, rate your evidence, and generate professional outputs.

---

## What to expect

The coach will ask you:
1. What your startup does (one sentence)
2. What stage you are at (idea, prototype, MVP, on-market)
3. About your branding (colours, logo, pitch deck) so outputs look like yours
4. Which exercise you want to start with

Then it walks you through the exercise one question at a time, challenges weak answers, and generates a document when you have enough substance.

---

## Tips

- **Talk naturally.** "Let's work on our value proposition" or "I want to do the competition matrix."
- **Share your pitch deck or branding** when asked. Drag files into the terminal or paste file paths.
- **Press Ctrl + C** to stop Claude at any time. Your files are saved in the `/outputs/` folder.
- **To restart,** navigate back to the folder (`cd ~/Documents/Claude/hub201-workshop`) and type `claude`.

---

## Alternative: No install needed

If you cannot or do not want to install anything:

1. Go to [claude.ai](https://claude.ai) and log in
2. Open [CLAUDE.md on GitHub](https://github.com/TheGinjaNinja/hub201-workshop/blob/main/CLAUDE.md)
3. Copy the entire file contents and paste it as your first message in Claude
4. The coach will start guiding you

The web version works for the coaching conversation but cannot save files to your computer. You will need to copy outputs manually.

---

## Cost guide

| Activity | Estimated cost |
|----------|---------------|
| One exercise (30-45 minutes) | USD 0.25-0.50 |
| All 6 exercises | USD 1.50-3.00 |
| Generating the HTML presentation | USD 0.25-0.50 |
| A full workshop day | USD 2.00-5.00 |

Check your usage at [console.anthropic.com](https://console.anthropic.com/) under Billing, or at [claude.ai/settings/billing](https://claude.ai/settings/billing) if you are on a Pro/Max plan.
