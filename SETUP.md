# Setup

Common setup for both tracks. Pick the track you want:

- **Non-technical** (claude.ai or ChatGPT). Skip to the per-week launcher: `week<N>/web/index.html`. No installation needed.
- **Claude Code** (terminal). Install Claude Code, then follow the per-week setup.

## Claude Code

1. Install Claude Code: `npm install -g @anthropic-ai/claude-code`
2. Log in: `claude login` (follow the browser flow)
3. Clone this repo: `git clone https://github.com/TheGinjaNinja/hub201-workshop.git`
4. Open the week you want: `cd hub201-workshop && claude code week3/`
5. The coach is defined in `week<N>/CLAUDE.md` and loads automatically. Start the conversation.

## claude.ai or ChatGPT

1. Open `week<N>/web/index.html` in a browser. On GitHub Pages: `https://theginjaninja.github.io/hub201-workshop/week<N>/web/`
2. Click "Copy coach prompt"
3. Open claude.ai or ChatGPT, start a new chat, paste
4. Answer the coach's questions

## Per-week setup

Each week has its own `SETUP.md` with specifics:

- `week2/SETUP.md` (UVP and Differentiation)
- `week3/SETUP.md` (Customer Discovery and ICP)

## If you get stuck

- The coach never refuses to produce an output. If it feels like you don't have enough evidence, ask it to generate a "best-effort draft with the weak spots flagged" and it will.
- If the coach cites a fact you can't verify, treat it as a suggestion. The coach is instructed never to invent, but always sense-check before taking anything into your real interviews.
- Issues or questions: open an issue at `https://github.com/TheGinjaNinja/hub201-workshop/issues`.
