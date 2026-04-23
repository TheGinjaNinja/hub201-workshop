# Hub201 Workshop

Public repository for the Hub201 Pre-Acceleration Programme, Belgrade. Weekly AI-coached workshops for 19 cybersecurity startup teams. Each week lives in its own folder and runs two tracks: non-technical (copy the coach prompt into claude.ai) and Claude Code (open the week folder and chat).

## Weeks

- **Week 2: UVP, Differentiation, Value Proposition, Problem-Solution Fit.** See [`week2/`](week2/).
- **Week 3: Customer Discovery and ICP.** See [`week3/`](week3/).

## Two tracks per week

- **Non-technical track.** Open `week<N>/web/index.html` and follow the three-step setup. Works with claude.ai (free) or ChatGPT with a GPT-4 class model.
- **Claude Code track.** Open the week folder with Claude Code. The coach is defined in `week<N>/CLAUDE.md`. See `SETUP.md` at the repo root for installation.

## Repository structure

- `shared/prompt-core/`: universal GNV coach rules inherited by every workshop (coaching rules, evidence scales, founder nightmares, 9 fits model, output conventions)
- `shared/prompt-methodology/`: reusable methodology content (currently: cyber market context + the `discovery/` folder for Week 3-onwards discovery workshops)
- `week<N>/prompt-instance/`: per-week bespoke content (identity, philosophy, exercises, flow, stories)
- `week<N>/web/`: non-tech launcher page + generated mega-prompt
- `week<N>/workshop/`: keynote presentation and speaker notes
- `week<N>/examples/`: worked example artefacts (ShieldByte, ProcureSimple)
- `week<N>/low-tech/`: printable offline artefacts
- `scripts/`: bash build scripts

## Build

The coach files in each `week<N>/CLAUDE.md` and `week<N>/web/prompt.md` are generated from the modular sources. Regenerate after editing source files:

```
scripts/build-claude-md.sh <week-number>
scripts/build-web-prompt.sh <week-number>
```

## Credits

Programme: Tadej Kurepa, Natalija Milicevic, Zarko Antanaskovic at Hub201.

Coaching design: Jamie Reynolds at Ginger Ninja Ventures.

Methodology credits: David J. Bland and Alexander Osterwalder (Testing Business Ideas), Rob Fitzpatrick (The Mom Test), Teresa Torres (Continuous Discovery Habits), Jeroen Coelen (Doctor Market Fit), Rob Snyder (Selling to Learn), Steve Blank (Customer Development), April Dunford, Maja Voje, Roman Pichler, Geoffrey Moore (for Week 2 positioning).
