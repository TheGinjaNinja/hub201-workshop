# Competition Matrix

## Purpose

Map the competitive landscape, identify positioning opportunities, and understand where you actually win. This exercise combines April Dunford's competitive alternatives framework, Maja Voje's qualifier/differentiator sorting, and a structured scoring grid to produce a clear picture of where a startup sits relative to alternatives.

The goal is not to prove you have no competitors. The goal is to find the gap where you win deals.

---

## Step 1: Competitive Alternatives (April Dunford)

Start here. Everything else builds on this.

**Core question:** "If your product disappeared tomorrow, what would your customer do instead?"

This is not "who are your competitors?" That question leads founders to list only software companies that look like them. Competitive alternatives are broader. They include everything a customer might do to solve the problem you solve.

### Categories of alternatives to explore

- **Direct competitors.** Companies solving the same problem for the same buyer. The obvious ones.
- **Adjacent products.** Tools built for a different job that customers stretch to cover your use case. Example: a SIEM vendor whose customers use it for compliance reporting even though it was not designed for that.
- **Manual processes.** Spreadsheets, email chains, shared drives, Word documents. In cybersecurity, many SMEs track vulnerabilities in Excel and manage compliance with shared folders.
- **Consultants and agencies.** Hiring a penetration testing firm, bringing in a compliance consultant, or outsourcing to an MSSP. These are real competitors for budget and attention.
- **Build in-house.** Engineering teams building internal tools. Common in security-conscious organisations that distrust third-party software.
- **Do nothing.** The customer accepts the risk, ignores the problem, or deprioritises it. In cybersecurity, "do nothing" is the most common competitor for non-regulated SMEs.

### Coaching guidance

Push the founder to list at least 6-8 alternatives across these categories. If they only list software competitors, prompt them:

- "What did your last prospect use before they talked to you?"
- "What happens in companies that cannot afford any solution in this space?"
- "If a CISO has no budget for your tool, what do they tell their board they are doing instead?"

**Red flag:** "We have no competitors" is always wrong. Every problem has an existing workaround, even if it is terrible. A founder who cannot name alternatives does not understand their buyer well enough.

---

## Step 2: Competitor Profiles

Select 3-5 competitors from the alternatives list. Prioritise the ones that founders encounter most in sales conversations or that buyers mention during discovery calls.

For each competitor, capture:

| Field | What to capture |
|---|---|
| **Name** | Company or solution name |
| **One-line description** | What they do in a single sentence |
| **Who they serve** | Target customer segment, company size, geography |
| **Headline positioning** | How they describe themselves on their website or pitch deck |
| **Pricing model** | Free, freemium, per-seat, per-asset, enterprise quotes. "Unknown" is acceptable. |
| **Strengths** | 2-3 things they do well. Be honest. |
| **Weaknesses** | 2-3 gaps or complaints. Use G2, Gartner Peer Insights, or customer interviews. |
| **Funding / size** | Funding raised, employee count, or revenue estimates if available |

### Coaching guidance

Push founders to be honest about competitor strengths. If they dismiss every competitor as weak, they are not seeing the market clearly. The best competitive analysis respects what competitors do well and identifies where they fall short.

For cybersecurity startups, useful research sources include: Crunchbase, G2, Gartner Peer Insights, PeerSpot, LinkedIn (employee count and growth), and SEC/Companies House filings where available.

---

## Step 3: Feature/Capability Scoring Grid

This is the structured comparison. It makes subjective opinions visible and debatable.

### How to build the grid

**Rows:** 8-12 key capabilities that matter to the buyer. The coach helps the founder define these based on their ICP and the problem they solve. These are not product features. They are capabilities that drive buying decisions.

Example capabilities for a cybersecurity compliance tool:
- Automated evidence collection
- Multi-framework mapping (ISO 27001, SOC 2, NIS2)
- Continuous monitoring vs. point-in-time assessment
- Integration with existing security stack
- Audit-ready reporting
- Risk scoring and prioritisation
- User experience for non-technical compliance staff
- Time to value (days to deploy, not months)
- API and extensibility
- Pricing transparency

**Columns:** The founder's startup plus 3-5 competitors from Step 2.

**Scoring:** 0 to 5 for each cell.

| Score | Meaning |
|---|---|
| 0 | Does not exist. No capability at all. |
| 1 | Minimal. Exists in name only, or deeply inadequate. |
| 2 | Basic. Works but limited. Customers complain about it. |
| 3 | Adequate. Gets the job done. Nothing special. |
| 4 | Strong. Well-executed, customers are happy. |
| 5 | Best in class. The reason customers choose this product. |

### Example grid format

| Capability | Your Startup | Competitor A | Competitor B | Competitor C |
|---|---|---|---|---|
| Automated evidence collection | 4 | 2 | 5 | 0 |
| Multi-framework mapping | 5 | 3 | 4 | 1 |
| Integration depth | 2 | 4 | 4 | 3 |
| Time to value | 5 | 2 | 3 | 4 |
| ... | ... | ... | ... | ... |

### What to look for

- **Your sweet spot:** Capabilities where you score 4-5 and competitors score 0-2. This is where you win.
- **Table stakes gaps:** Capabilities where competitors all score 3+ and you score below 3. These need fixing before you can compete.
- **Ignored areas:** Capabilities where everyone scores 0-1. Either nobody cares (remove from the grid) or it is a whitespace opportunity (validate with customers).

### Coaching guidance

- If the founder scores themselves 5 on everything, push back. Nobody is best-in-class at everything. Ask: "Which of these would a customer verify in a POC, and would you pass?"
- If the founder scores themselves 0 on nothing, push back. Early-stage startups always have gaps. The value of this exercise is honest assessment.
- Encourage founders to validate scores with evidence: customer feedback, G2 reviews, win/loss analysis, or demo comparisons. Gut feeling is a starting point, not an endpoint.

---

## Step 4: Qualifiers vs. Differentiators (Maja Voje)

Take every capability from the scoring grid and sort it into one of four buckets.

| Category | Definition | What it means |
|---|---|---|
| **Qualifier** | The market expects it. Competitors have it. | Table stakes. You need it to compete, but it will not win you deals. Do not lead with qualifiers in your pitch. |
| **Differentiator** | You have it. Competitors do not (or do it poorly). | This is what wins deals. Build your positioning, messaging, and sales narrative around differentiators. |
| **Irrelevant** | Nobody has it. Nobody is asking for it. | Drop it. Do not build it, do not talk about it. It wastes time and confuses buyers. |
| **Aspiration** | Nobody has it yet, but customers want it. | Opportunity. If you can build it first and it aligns with your ICP's needs, this could become your differentiator. |

### Sorting rules

- A capability where every competitor scores 3-5 is a **qualifier**. You need it, but it does not differentiate you.
- A capability where you score 4-5 and competitors score 0-2 is a **differentiator**. Lead with this.
- A capability where everyone scores 0-1 and no customer has asked for it is **irrelevant**.
- A capability where everyone scores 0-1 but customers keep requesting it is an **aspiration**.

### Coaching guidance

- Most founders overcount their differentiators. Challenge each one: "If I asked five of your customers what makes you different, would they say this?"
- Price is not a differentiator. There can only be one cheapest provider, and competing on price is a race to the bottom (Maja Voje).
- "We use AI" is not a differentiator in 2026. Every cybersecurity vendor claims AI. The question is: AI applied to what problem, with what data, producing what measurable outcome?
- A good startup has 2-3 genuine differentiators. If you have more than 5, you are confusing qualifiers with differentiators.

---

## Step 5: Positioning Opportunity

Based on the scoring grid and qualifier/differentiator sort, identify your competitive position. There are three paths (from the Founders Program):

### Path 1: Whitespace
Nobody does what you do. For some reason, nobody has tried this yet.

- Your scoring grid shows capabilities where you score 4-5 and every competitor scores 0.
- Validate that this whitespace exists because of a real opportunity, not because customers do not want it.
- Cybersecurity example: A compliance automation tool built specifically for NIS2 requirements in Southeast Europe, where global vendors have not localised.

### Path 2: Adjacency (more than one dimension different)
You are different from the nearest major player on at least two dimensions: customer segment, use case, geography, delivery model, pricing model, or technology approach.

- The key test: cost and customer sharing level should be below 90% overlap with the major player. If you share 90%+ of costs and customers, you are a product line extension, not a new business.
- Cybersecurity example: Taking enterprise-grade vulnerability management and rebuilding it for 200-500 employee companies with a self-serve onboarding flow and usage-based pricing.

### Path 3: 10x Better
You do the same thing as competitors but are dramatically superior on a dimension that matters to buyers.

- "Dramatically superior" means measurably, provably better. Not 20% faster. 10x faster, 10x cheaper, 10x easier to deploy.
- This must be on a dimension the buyer actually cares about. Being 10x better at something irrelevant is still irrelevant.
- Cybersecurity example: Reducing SOC 2 audit preparation from 6 months to 2 weeks with automated evidence collection.

### Coaching guidance

Help the founder articulate a 2-3 sentence positioning opportunity statement that answers:
1. What is the competitive gap you are exploiting?
2. Which path are you taking (whitespace, adjacency, or 10x better)?
3. What evidence supports this position?

---

## Output Format

The completed exercise should produce a file at `/outputs/competition-matrix.md` with these sections:

### 1. Competitive Alternatives
Bulleted list of all alternatives the customer could use instead. Grouped by category (direct, adjacent, manual, consultant, in-house, do nothing).

### 2. Competitor Profiles

| | Competitor 1 | Competitor 2 | Competitor 3 | Competitor 4 |
|---|---|---|---|---|
| One-line description | | | | |
| Target customer | | | | |
| Positioning | | | | |
| Pricing model | | | | |
| Strengths | | | | |
| Weaknesses | | | | |
| Funding / size | | | | |

### 3. Scoring Grid

| Capability | Your Startup | Comp 1 | Comp 2 | Comp 3 | Comp 4 |
|---|---|---|---|---|---|
| Capability 1 | _ | _ | _ | _ | _ |
| Capability 2 | _ | _ | _ | _ | _ |
| ... | | | | | |

### 4. Qualifiers vs. Differentiators

**Qualifiers (table stakes):**
- [Capability]: Why it is table stakes

**Differentiators (your edge):**
- [Capability]: Why this wins deals

**Irrelevant:**
- [Capability]: Why this does not matter

**Aspirations:**
- [Capability]: Why this is an opportunity

### 5. Positioning Opportunity Statement
2-3 sentences. Which path (whitespace, adjacency, 10x better), what gap you exploit, why you believe this.

### 6. Evidence Assessment
For each claim in the positioning statement, rate the evidence:
- **Strong:** Customer interviews, win/loss data, or third-party validation
- **Moderate:** Founder experience and market observation, but not formally validated
- **Weak:** Assumption only, needs testing

### 7. Next Steps
3-5 specific actions to strengthen the competitive position. Examples: "Run 5 customer interviews focused on why they chose us over [Competitor X]" or "Build a POC comparison against [Competitor Y] on [Capability Z]."

---

## Red Flags

Watch for these during the exercise. If you spot them, call them out directly.

- **"We have no competitors."** Every problem has an existing workaround. Push the founder to list at least 6 alternatives.
- **Only listing software competitors.** Manual processes, consultants, and "do nothing" are real competitors for budget and attention. Include them.
- **Scoring yourself 5 on everything.** Nobody is best-in-class across the board. Early-stage startups have gaps. The exercise only works with honest scores.
- **Differentiating on features customers do not care about.** A differentiator only counts if the buyer values it. Validate with customer evidence.
- **"We use AI" as a differentiator.** In 2026, every vendor claims AI. Specify: AI applied to what problem, with what data, producing what outcome.
- **Copying a competitor's positioning.** If your positioning statement could describe three other companies, it is not positioning. It is a category description.
- **Ignoring the "do nothing" competitor.** For many cybersecurity SMEs, the biggest competitor is inertia. Your sales process needs to address why now, not just why you.
- **Confusing qualifiers with differentiators.** If every competitor also does it, leading with it in your pitch wastes the buyer's attention. Qualifiers belong on your features page, not in your headline.
