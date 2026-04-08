# Personas Coaching Guide

## Purpose

Help cybersecurity startup founders define specific buyer and user personas grounded in evidence, not imagination. Personas built on assumptions are fiction. Personas built on evidence are targeting tools.

The output of this exercise is a completed personas document in `/outputs/personas.md` that includes persona cards, a buyer map, a beachhead definition, and an evidence assessment. These personas become the interview targets for Week 3 discovery work.

## Framework: Early Customer vs. Ideal Customer (Maja Voje)

Early customers and ideal customers are fundamentally different people. Most founders confuse them. This distinction matters because it changes who you target, how you sell, and what you build first.

### Early Customers (Early Customer Profile)

- Tolerate rough edges, bugs, and missing features
- Self-onboard without hand-holding or documentation
- Give generous, honest feedback because they care about the problem
- Love new technology and want to be first
- Will endorse you publicly and make introductions
- Shorter sales cycles because they decide fast
- Great beta testers and design partners
- Innovators and early adopters on the adoption curve

### Ideal Customers (Ideal Customer Profile)

- Require proof: case studies, references, certifications
- Longer sales cycles with procurement, legal, and compliance reviews
- Need structured onboarding and support
- Commit long-term once they are in
- Represent the scalable, repeatable market segment
- Would make great logos on your website
- Their profile matches a large addressable market

### Why This Matters

Most teams at this stage should focus on early customer personas first. You need first pilots, first feedback, and first revenue. Chasing ideal customers too early leads to long sales cycles, feature bloat, and running out of cash before you close a single deal.

Build separate persona cards for early customers and ideal customers. Label them clearly. Your immediate outreach targets should be early customer personas.

### Coaching Approach

When a founder describes their persona, ask: "Is this your early customer or your ideal customer?" If they say "both," push back. The person who will tolerate your MVP next month is not the same person who will sign an enterprise contract in 18 months. Separate them.

## Framework: B2B Buyer Map

In B2B cybersecurity, the person who uses your product is rarely the person who signs the cheque. Every deal involves multiple roles. If you only build a persona for the user, you will build a great product that nobody buys.

### The Five Buying Roles

**Champion:** Fights for your product internally. This is the person who feels the pain most acutely, discovers your solution, and sells it inside their organisation before you ever get a meeting with leadership. Without a champion, you have no deal.

**Influencer:** Shapes the decision but does not make it. Technical evaluators, team leads, analysts, or advisors who assess whether the product actually works. They can veto on technical grounds.

**Decision Maker:** Has final authority to approve the purchase. Signs off or kills the deal. Often not the person who evaluated the product.

**Budget Holder:** Controls the budget line the purchase comes from. Sometimes the same person as the decision maker. Sometimes not. If the budget holder has already allocated spend elsewhere, your deal is dead regardless of how good the product is.

**Saboteur:** Blocks or delays the deal. This could be IT (integration concerns), procurement (vendor risk assessment), legal (contract terms), a competitor's internal champion, or simply someone who prefers the status quo. Identifying the saboteur early saves months of wasted pipeline.

### Cybersecurity Buyer Map Patterns

**Mid-market companies (200-1000 employees):**
- CISO is often champion AND decision maker
- IT Director may be the influencer (technical evaluation)
- CFO is frequently the budget holder
- Procurement is lighter but still exists
- Sales cycles: 1-3 months

**Enterprise companies (1000+ employees):**
- CISO champions but CFO or CTO decides
- Security team leads and architects are influencers
- Procurement runs formal vendor risk assessments and can kill deals on process alone
- Legal reviews contracts and DPAs
- IT operations evaluates integration and deployment impact
- Sales cycles: 6-18 months

**Startups and scale-ups (under 200 employees):**
- CTO or technical co-founder is often champion, influencer, and decision maker in one person
- CEO controls budget
- No formal procurement. Fastest sales cycles.

### Coaching Approach

For every persona the founder creates, ask: "What is this person's buying role?" If they only have a user persona, ask: "Who writes the cheque? Have you built a persona for that person?" If they only have a buyer persona, ask: "Who actually uses this product every day? What do they care about?"

A complete B2B persona set needs at minimum one buyer persona and one user persona. If buyer and user are the same person (common in small companies), that is fine, but the founder must explicitly confirm it, not assume it.

## Framework: Beachhead (Geoffrey Moore)

A beachhead is one specific market segment you plan to dominate first before expanding to adjacent segments. It is the foundation of a focused go-to-market strategy. The opposite of a beachhead is "spray and pray," which dilutes effort across too many segments with weak results.

### What Makes a Good Beachhead

- Specific enough to build a target list of 50-100 companies by name
- Small enough to dominate with limited resources
- Large enough to sustain early revenue and prove the model
- Defined by geography, industry, company size, AND a qualifying characteristic
- Has a common trigger event that creates urgency
- Companies in the segment talk to each other (word of mouth works)

### Beachhead Specificity Test

Too broad: "European mid-market financial services." This describes thousands of companies across dozens of countries with different regulations, languages, and buying behaviours.

Still too broad: "Banks in Southeast Europe." Which banks? What size? What problem?

Good beachhead: "Serbian banks with 200-1000 employees that have had a phishing incident in the past 12 months." You can name specific companies. They share a common pain. They are subject to the same regulations. They attend the same events.

Another good example: "Series A-C fintech companies in DACH that need SOC 2 certification before their next enterprise sales push." Specific trigger, specific segment, common urgency.

### The Bowling Alley

Beachhead first, then expand. Geoffrey Moore's Bowling Alley strategy:

1. **Pin 1 (Beachhead):** Dominate one niche. Get 3-5 reference customers. Build deep expertise.
2. **Pin 2-3 (Adjacent):** Use beachhead credibility to expand into closely related segments. "We secured Serbian banks. Now we secure Croatian banks." Or: "We secured fintech compliance. Now we secure healthtech compliance."
3. **Broader market:** Only after you have a track record in multiple niches.

### Coaching Approach

When a founder describes their target market, apply the specificity test: "Can you name 10 specific companies in this segment right now?" If they cannot, the definition is too vague. Push harder.

Ask: "Why this segment first? What makes them more likely to buy than any other segment?" The answer should reference urgency, access, or a specific advantage the founder has in reaching these companies.

## Persona Card Template (Customer Clarity Canvas)

Each persona card follows the Customer Clarity Canvas structure. This ensures founders think through the full picture of their customer, not just demographics. For every field, the founder must identify the evidence source and rate its strength.

```
### [Persona Nickname] (e.g., "Viktor the SOC Lead")

**Buying Role:** [Champion / Influencer / Decision Maker / Budget Holder / End User]
**Early or Ideal Customer:** [Early Customer / Ideal Customer]

#### Define the Customer

- **Role/Title:** [Specific job title]
- **Firmographics:** [Industry, company size (employees), revenue range, geography, funding stage]
- **Role in Purchase:** [Champion / User / Buyer / Decision-maker, or multiple]
- **Trigger Event:** [What causes this person to look for a solution NOW]
- **Where They Hang Out:** [LinkedIn groups, conferences, publications, communities, Slack groups, podcasts, events]
- **Who Influences Them:** [Brands, people, analysts, publications they trust]

#### Define the Use Case

- **Situation Before Your Product:** [What is their world like today without you?]
- **Current Solution:** [What tools, processes, or workarounds do they use today? Include "do nothing" if applicable.]
- **Frustrations with Current Approach:** [What specifically is broken, slow, painful, or missing?]
- **Consequences:** [What does this cost them in money, time, reputation, or stress?]
- **Past Spend:** [Have they spent money on solutions before? What is their budget range?]

#### Define the Problem

- **Jobs to Be Done:**
  1. [Primary functional job]
  2. [Secondary job]
  3. [Social or emotional job, if relevant]
- **Pain Points (ranked by severity):**
  1. [Critical] - would pay to solve today
  2. [Major]
  3. [Minor]
- **How Often They Feel This Pain:** [Daily / Weekly / Monthly / Quarterly]
- **Problem Awareness:** [High (actively seeking) / Medium (aware but not seeking) / Low (needs education)]
- **Why They Would Say No:** [Price, risk, switching costs, timing, inertia, competing priorities]

#### Define the Buyers (B2B)

- **Champion:** [Who advocates internally for finding a solution?]
- **Influencer:** [Who shapes the decision but does not make it?]
- **Decision Maker:** [Who has final authority to approve?]
- **Budget Holder:** [Who controls the budget?]
- **Saboteur:** [Who might block or slow down the purchase? Why?]
- **End User:** [Who actually uses the product day-to-day?]

#### Channels

- [How and where to reach 50 of this persona in the next two weeks]

#### Evidence Assessment

| Field | Evidence Source | Strength |
|-------|---------------|----------|
| Customer Profile | [e.g., 5 interviews with SOC leads] | [Strong/Moderate/Weak/Assumption] |
| Use Case | [e.g., Observed in 2 demos] | [Strong/Moderate/Weak/Assumption] |
| Problem / Pains | [e.g., 3 interviews confirmed this ranking] | [Strong/Moderate/Weak/Assumption] |
| Trigger Event | [e.g., Assumption based on market research] | [Strong/Moderate/Weak/Assumption] |
| Buyer Roles | [e.g., Assumption, no procurement interviews] | [Strong/Moderate/Weak/Assumption] |
```

### Coaching Notes on the Template

**Persona nickname:** Make it memorable and specific. "Viktor the SOC Lead at a Serbian Bank" is better than "IT Manager." The nickname should instantly recall who this person is.

**Trigger event:** This is the most important field. No trigger means no urgency. No urgency means no sale. A trigger is a specific event or change in circumstances that causes the person to actively seek a solution. Examples: a phishing breach last quarter, a compliance audit deadline in 90 days, a new regulation taking effect, a board mandate to reduce risk. "They need better security" is not a trigger. "Their cyber insurance premium doubled after a ransomware incident" is a trigger.

**Current solution and use case:** Always fill these in. "Do nothing" is a valid current solution and is often the biggest competitor. The use case section forces founders to think about the customer's world before and after the product. If they cannot describe the frustrations and consequences of the current approach, they have not done enough discovery.

**Consequences and past spend:** These fields reveal willingness to pay. If the consequences are low or the customer has never spent money on this problem, the pain may not be severe enough to build a business around.

**Problem awareness:** This determines go-to-market approach. High awareness means inbound and search marketing can work. Low awareness means you need education-first sales, which is expensive and slow.

**Why they would say no:** Founders hate this question. But the reasons for rejection are often more useful than the reasons for interest. Objections reveal switching costs, risk tolerance, and competitive dynamics.

**Evidence per field:** Different fields will have different evidence strengths. A founder might have strong evidence for pain points (from interviews) but weak evidence for the trigger event (assumption). This is fine. The point is to be honest about what is validated and what is not.

## Coaching Questions (Sequential Flow)

Work through these questions one at a time. Do not dump them all at once. Ask one, challenge the answer, then move to the next.

### Opening

"Who is the first person you would sell to? Not a segment. A person. Give me a name, a title, and a company."

If they cannot name a specific person, flag this: "You do not have a persona yet. You have a demographic label. Let us build from evidence."

### Building the Persona

1. **"Have you spoken to someone matching this persona? How many?"**
   If zero: "You are building fiction. That is fine as a starting hypothesis, but be honest that every field is an assumption until you validate it."
   If fewer than 5: "You have early signal, not pattern. Note which fields come from interviews and which are extrapolation."
   If 10+: "Good. Let us ground every field in what they actually told you."

2. **"Can you name a specific person at a specific company who matches this persona?"**
   If yes: great, use them as the anchor for the persona card.
   If no: the persona is aspirational, not evidence-based. Label it accordingly.

3. **"What is the trigger event? What makes this person look for a solution right now?"**
   No trigger means no urgency means no sale. If the founder says "they always need better security," push back: "That is a chronic condition, not a trigger. Chronic conditions get deprioritised. What event makes this URGENT?"

4. **"Who else is in the buying decision?"**
   If they only describe one person, ask about each buying role: champion, influencer, decision maker, budget holder, potential saboteur. For each role, ask if they have spoken to someone in that role.

5. **"Is this your early customer or your ideal customer?"**
   Force the distinction. If they say both, challenge: "The person who tolerates your buggy MVP this quarter is not the same person who needs three case studies and an ISO certification before they will take a call."

6. **"What does this person do today without your product?"**
   Current solution reveals competitive landscape and switching costs. If "do nothing" is the current solution, the founder needs to explain why the persona would change behaviour now.

7. **"Where do you find this person? Can you reach 50 of them in the next two weeks?"**
   If they cannot describe concrete channels for reaching the persona, the persona is theoretical. A good persona leads directly to an outreach plan.

### Beachhead Definition

8. **"What is your beachhead segment?"**
   Apply the specificity test. Can they list 10 companies by name? If not, too vague.

9. **"Why this segment first?"**
   Look for: founder has access or connections, segment has acute pain, short sales cycle, companies talk to each other, regulatory pressure creates urgency.

10. **"What is your second segment after you win the beachhead?"**
    This tests whether the beachhead is a dead end or a stepping stone. A good beachhead has natural adjacencies.

## Output Format

Generate the completed personas as `/outputs/personas.md` using this structure:

```markdown
# Personas: [Company Name]

**Date:** [Today's date]
**Exercise:** Buyer and User Personas (Customer Clarity Canvas)

## Beachhead Definition

**Segment:** [Specific description]
**Why this segment first:** [Reasoning]
**Target list size:** [Can you name 50-100 companies?]
**Adjacent segments for expansion:** [Next segments after beachhead]

## Persona Cards

### [Persona 1 Nickname]

**Buying Role:** [Role]
**Early or Ideal Customer:** [Early/Ideal]

#### Define the Customer

- **Role/Title:** [Title]
- **Firmographics:** [Industry, company size, revenue range, geography, funding stage]
- **Role in Purchase:** [Champion / User / Buyer / Decision-maker]
- **Trigger Event:** [Specific trigger]
- **Where They Hang Out:** [Channels, communities, events]
- **Who Influences Them:** [Trusted brands, people, publications]

#### Define the Use Case

- **Situation Before Your Product:** [Their world without you]
- **Current Solution:** [What they do today]
- **Frustrations with Current Approach:** [What is broken]
- **Consequences:** [Cost in money, time, reputation, stress]
- **Past Spend:** [Have they paid for solutions before? Budget range?]

#### Define the Problem

- **Jobs to Be Done:**
  1. [Job 1]
  2. [Job 2]
  3. [Job 3]
- **Pain Points (ranked by severity):**
  1. [Critical pain]
  2. [Major pain]
  3. [Minor pain]
- **How Often They Feel This Pain:** [Daily/Weekly/Monthly]
- **Problem Awareness:** [High/Medium/Low]
- **Why They Would Say No:** [Objections, blockers, inertia]

#### Define the Buyers (B2B)

- **Champion:** [Who]
- **Influencer:** [Who]
- **Decision Maker:** [Who]
- **Budget Holder:** [Who]
- **Saboteur:** [Who and why]
- **End User:** [Who]

#### Channels

- [How to reach 50 of this persona in the next two weeks]

#### Evidence Assessment

| Field | Evidence Source | Strength |
|-------|---------------|----------|
| Customer Profile | [Source] | [Rating] |
| Use Case | [Source] | [Rating] |
| Problem / Pains | [Source] | [Rating] |
| Trigger Event | [Source] | [Rating] |
| Buyer Roles | [Source] | [Rating] |

---

### [Persona 2 Nickname]

[Same structure as above]

---

## Evidence Assessment

- **Overall rating:** [Strong / Moderate / Weak / Assumption-Heavy]
- **Strongest evidence:** [What is most validated]
- **Biggest assumption:** [What could invalidate these personas]
- **Evidence gaps:** [What needs to be validated in Week 3 interviews]

## Next Steps

1. [Who to interview in Week 3, with specific targeting criteria]
2. [What questions to ask to validate the biggest assumption]
3. [Any additional personas needed based on gaps identified]
```

## Red Flags

Challenge the founder immediately if you see any of these patterns.

**Generic personas: "IT managers" with no specifics.** A persona without a company size, industry, geography, and trigger event is a demographic label, not a persona. Push: "Which IT manager? At what company? What happened last quarter that made them care about this problem?"

**Only one persona when buyer and user are different.** In cybersecurity B2B, the SOC analyst who uses the tool daily is rarely the CISO who signs the purchase order. If the founder only has one persona, ask: "Who writes the cheque? Is that the same person who logs into your product every morning?"

**No trigger event.** Without a trigger, there is no urgency. Without urgency, deals stall indefinitely. If the founder says "security is always important," respond: "Then why would they buy THIS quarter instead of next year? What changed?"

**Zero conversations with anyone matching the persona.** A persona built entirely from assumptions is creative writing, not customer discovery. Flag it directly: "You have not spoken to a single person matching this persona. Every field is an assumption. That is your starting hypothesis, not your persona. Go find 5 real people and come back."

**Persona describes the founder's friend, not a market segment.** If the persona is suspiciously easy to describe and matches someone the founder knows personally, probe: "Is this based on one person you know, or a pattern you have observed across multiple people? One data point is an anecdote, not a segment."

**No beachhead. Targeting "the cybersecurity market."** This is spray and pray. Push for specifics: "If you could only sell to one type of company for the next 6 months, who would it be? Name the segment. Name 10 companies in it."

**Buyer map missing the saboteur.** Founders love describing champions and decision makers. They forget the person who kills deals. Ask: "Who in the organisation would block this purchase? IT who does not want another tool? Procurement who needs three competitive bids? A team lead who built an internal solution and does not want it replaced?"

**Confusing "interested" with "would buy."** If the founder describes persona validation as "people said they liked the idea," apply the Commitment Ladder. Interest is the weakest signal. Push: "Did they commit time, reputation, or money? Or did they just nod politely?"
