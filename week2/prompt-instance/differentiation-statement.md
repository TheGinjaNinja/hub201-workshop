# Differentiation Statement

## Purpose

Guide the founder to articulate a clear, defensible differentiation statement that separates them from competitors in a way customers actually care about. The output is a structured differentiation statement they can use in pitch decks, sales conversations, and investor meetings.

## Framework: True Differentiators (Maja Voje)

Every startup has assets: product features, team strengths, company capabilities, domain knowledge. Not all of these are differentiators. Each asset must pass two tests:

1. **Competitors do not have it.** If competitors offer the same thing, it is a qualifier (table stakes). You need it to play, but it does not set you apart.
2. **Customers value it.** If customers do not care about it, it is irrelevant. Technical elegance that buyers ignore is not differentiation.

Only assets that pass both tests are true differentiators. Build your positioning around these.

The price trap: if you cannot differentiate on value, you end up competing on price. There can only be one cheapest provider, and that is not a startup strategy. Price competition is a race to the bottom.

**Coaching approach:** Have the founder list 5-10 assets. For each one, ask: "Do your competitors also have this?" and "Have customers told you this matters to them?" Ruthlessly discard anything that fails either test. Most founders will find they have 1-2 genuine differentiators at most.

**Cybersecurity example:** "SOC 2 compliance" is a qualifier. Every serious security vendor has it. "Real-time attack path mapping for OT/IT convergence environments" might be a differentiator if competitors focus only on IT networks and customers in industrial sectors need this.

## Framework: Minimum Viable Positioning (Two-Track)

Use this lightweight positioning framework before doing a full positioning exercise. It has two parallel tracks that converge into a single statement.

### Market Track (demand side)
- **Champion:** Who is the internal buyer pushing for this? (e.g., CISO at mid-market financial services firms)
- **Company Type:** What kind of organisation are they in? (e.g., regulated fintech with 200-500 employees)
- **Use Case:** What are they trying to do? (e.g., pass their annual penetration test without hiring a full-time red team)
- **Problem:** What is broken today? (e.g., external pen testing firms take 6 weeks and deliver a static PDF that is outdated before anyone reads it)

### Product Track (supply side)
- **Product Category:** What shelf do you sit on? (e.g., continuous penetration testing platform)
- **Most Compelling Capability:** What can you do that matters most? (e.g., automated attack simulation against live production environments)
- **Most Compelling Feature:** What specific feature delivers this? (e.g., real-time vulnerability retest after remediation)
- **Main Benefit:** What outcome does the customer get? (e.g., always-current security posture with 80% less manual testing time)

### Convergence

Both tracks combine into a positioning statement. Use this template:

> For [Champion] at [Company Type] who need to [Use Case], [Product] is a [Category] that [Main Benefit]. Unlike [Competitive Alternative], we [Key Differentiator].

**Coaching approach:** Work through each track separately. Do not let the founder skip steps. If they cannot name a specific champion, they have not talked to enough customers. If they cannot name a category, they need to decide whether they are creating a new category or positioning within an existing one.

## Framework: Defensibility

Defensibility is what stops a well-funded competitor from copying your approach. Ranked from strongest to weakest:

1. **Network effects.** Each new user makes the product more valuable for all users. Hard to replicate because the network itself is the asset. (Example: a threat intelligence platform where more customers contributing anonymised threat data improves detection for everyone.)
2. **Proprietary data.** Data you have collected that competitors cannot easily reproduce. (Example: 3 years of labelled attack telemetry from 500 enterprise environments.)
3. **Regulatory/compliance advantage.** Certifications, approvals, or regulatory relationships that take years to obtain. (Example: being the only vendor pre-approved under a specific national cybersecurity framework.)
4. **Switching costs.** Deep integration into customer workflows that makes replacement painful. (Example: your SIEM replacement has 200+ custom detection rules built by each customer's security team.)
5. **Brand/trust.** Reputation and credibility built over time, especially important in cybersecurity where buyers are risk-averse. (Example: being the vendor CISOs recommend to each other in private Slack communities.)
6. **Speed to market.** Being first. This is the weakest form of defensibility because it is temporary. A funded competitor can close a 6-month head start quickly.

**Coaching approach:** Most pre-seed startups will not have strong defensibility yet. That is fine. The exercise is about identifying which type of defensibility they are building toward. Ask: "In 18 months, which of these will you have?" If the answer is "none," the startup has a strategy problem.

## Framework: Three Paths to Market

Every startup enters the market through one of three paths. Identifying which path you are on shapes your differentiation story.

1. **Whitespace.** Nobody has tried this yet. You are creating a new category or solving a problem nobody else recognised. Rare and risky, but the highest upside if you are right. (Example: a security platform for a new device class that incumbents have not noticed.)
2. **Adjacency.** You are more than one product-line extension away from a major player. The incumbent could build what you do, but it would require entering a genuinely new market. Cost and customer sharing with the incumbent is less than 90%. (Example: taking enterprise threat detection and rebuilding it specifically for healthcare IoT devices, a market CrowdStrike does not serve.)
3. **10x Better.** You do what competitors do, but so much better it warrants customers switching. This needs to be measurably, dramatically better, not incrementally better. (Example: reducing mean time to detect from 48 hours to 30 minutes through a fundamentally different architecture.)

**Coaching approach:** If a founder says "we are 10x better," ask for the specific metric and the evidence. Feelings and opinions do not count. If they say "whitespace," ask why nobody else has done this. Sometimes the reason is that nobody wants it. If they say "adjacency," check that the incumbent genuinely cannot add this feature to their existing product in a quarter.

## Coaching Questions

Use these to pressure-test the founder's differentiation claim:

- What do you do that no competitor does? Be specific, not abstract.
- Why should a customer choose you over [name a specific competitor]? If you cannot answer this for a named competitor, you have not done enough competitive research.
- If a well-funded competitor copied your approach tomorrow, how long would it take them to reach parity? What specifically stops them?
- Is your differentiation about product (technical capability), market position (who you serve), or business model (how you charge/deliver)?
- What evidence do you have that customers value this difference? "We think they will" is not evidence. Quotes from interviews, pilot results, or purchase decisions are.
- Can you describe your product in one sentence? If not, you may be building Frankensoft.

### The Frankensoft Test

From the Startup Operating Model: "You cannot build a product for everyone. You try to build for every possible customer segment instead of dominating a beachhead. Every conversation adds a feature. Every potential customer gets a promise. The product becomes an unusable Swiss Army knife, part CRM, part marketplace, part analytics tool, that does nothing well."

Warning signs that differentiation has been lost to Frankensoft:
- The feature list grows after every customer meeting
- You cannot describe your product in one sentence
- Different team members give different descriptions of what you do
- Your onboarding takes more than 15 minutes to explain

If any of these are true, the founder needs to go back to beachhead market selection before working on differentiation.

## Output Format

The founder's completed differentiation statement should be saved to `/outputs/differentiation-statement.md` with this structure:

```markdown
# Differentiation Statement

## What We Do Differently
[1-2 sentences. What is the core thing you do that competitors do not?]

## Evidence for Differentiation
[What proof do you have? Customer quotes, pilot data, win/loss analysis, market research.]

## Defensibility
- **Type:** [Network effects / Proprietary data / Regulatory advantage / Switching costs / Brand-trust / Speed to market]
- **Current strength:** [None yet / Early signs / Established]
- **Building toward:** [What defensibility will you have in 18 months?]

## Path
- **Path:** [Whitespace / Adjacency / 10x Better]
- **Rationale:** [Why this path? What evidence supports it?]

## Full Differentiation Statement (MVP Format)
For [Champion] at [Company Type] who need to [Use Case],
[Product] is a [Category] that [Main Benefit].
Unlike [Competitive Alternative], we [Key Differentiator].

## Evidence Assessment
- [ ] Customers have confirmed this differentiator matters (interviews, surveys, or purchase decisions)
- [ ] We can name specific competitors who lack this capability
- [ ] Our differentiator cannot be copied in less than 6 months
- [ ] We can describe our product in one sentence
- [ ] Team members give consistent descriptions of what we do

## Next Steps
[What needs to happen to strengthen or validate the differentiation?]
```

## Red Flags

Watch for these during the coaching session. If you spot one, name it directly and help the founder address it.

- **"We use AI."** In 2026, every vendor claims AI. This is not a differentiator. The question is: AI applied to what problem, with what data, producing what outcome? Push the founder to be specific about what their AI does that others' does not.
- **"We are faster/easier/cheaper" without quantification.** Vague comparative claims are not differentiation. How much faster? Measured how? Compared to what baseline? If they cannot quantify it, it is marketing fluff.
- **Feature-based differentiation that is copyable in months.** If a competitor could ship the same feature in a single sprint, it is not defensible differentiation. Push toward structural advantages.
- **Frankensoft: trying to differentiate by doing everything.** If the product tries to cover too many use cases or segments, the differentiation is diluted to nothing. "We do everything" is the opposite of differentiation.
- **No customer evidence the differentiator matters.** The founder believes the differentiator is important, but no customer has confirmed it. This is a hypothesis, not a differentiation statement. Label it as such and set a validation plan.
- **Confusing qualifiers with differentiators.** "We are SOC 2 compliant" or "we have a great team" are not differentiators. They are table stakes. Help the founder distinguish between what gets them in the conversation and what wins it.

## Value Equation Connection (Hormozi)

When a founder struggles to articulate differentiation, the Hormozi Value Equation can help them think about where their advantage sits:

**Value = (Dream Outcome x Perceived Likelihood of Achievement) / (Time Delay x Effort and Sacrifice)**

Ask which lever they are pulling hardest:
- Do you deliver a bigger outcome than competitors?
- Do customers believe you are more likely to deliver than alternatives?
- Do you deliver faster?
- Do you require less effort from the customer?

The strongest differentiators often pull multiple levers simultaneously.
