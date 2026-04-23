Startup: ShieldByte
Date: 2026-04-23
Exercise: Hypotheses

---

## Current Customer and Problem Statement

ShieldByte believes that Heads of Security at 200-500 person regulated European fintechs spend several hours per phishing triage cycle managing alerts, coordinating analyst response, and chasing down false positives. The team believes these buyers would pay for an automation layer that cuts triage time materially and reduces the false-positive rate, freeing analysts to focus on real threats. This positioning evolved from the Week 2 beachhead (Serbian banks, NIS2 compliance) toward a broader regulated fintech segment across DACH, CEE, and the UK, where the problem statement shifts from compliance-first to operational efficiency-first.

---

## Assumption Inventory

### Desirability (do they want it?)

| # | Assumption | Notes |
|---|---|---|
| D1 | SOC analysts at the target segment spend 3-5 hours per phishing triage cycle [illustrative] | Core ROI premise. Completely untested. |
| D2 | Head of Security (not CISO) is the buyer at 200-500 person company size | Org structure assumption. Varies by firm. |
| D3 | Phishing triage is a top-3 pain for SOC teams at regulated fintechs | Problem-area match. Based on industry reading, not interviews. |
| D4 | Analysts would switch from their current toolchain for materially lower false-positive rates | Switching assumption. No behavioural evidence. |
| D5 | Teams are dissatisfied with their current phishing detection tooling | Dissatisfaction assumption. Not validated. |
| D6 | The problem is consistent across DACH, CEE, and UK regulated fintechs | Geographic assumption. Could vary significantly by market. |

### Feasibility (can we build and deliver it?)

| # | Assumption | Notes |
|---|---|---|
| F1 | ShieldByte can integrate with existing SIEM tooling (Splunk, Microsoft Sentinel, IBM QRadar) [example tools, team to verify fit] without a multi-month deployment | Technical assumption. Not yet prototyped in a real customer environment. |
| F2 | A new security tool can be onboarded in under 60 days at a regulated fintech | Onboarding speed assumption. Compliance approval adds time. |
| F3 | Compliance and InfoSec procurement approval at this company size takes under 90 days | Procurement cycle assumption. Varies by firm. May be longer. |
| F4 | The team can build a reliable false-positive reduction engine with the current team size | Engineering feasibility. Prototype exists but not production-tested. |

### Viability (will they pay, and is the model sustainable?)

| # | Assumption | Notes |
|---|---|---|
| V1 | Buyers will pay GBP 1,000-2,500 per seat per month [illustrative] | Pricing assumption. Completely untested. |
| V2 | The contract structure buyers accept is annual (not monthly, not transactional) | Contract preference assumption. |
| V3 | The sales cycle at this segment is under 90 days from first meeting to signature | Sales cycle assumption. Regulated fintechs often have longer procurement. |
| V4 | The total addressable segment (200-500 person regulated fintechs in DACH, CEE, UK) is large enough to build a business on | TAM assumption. No market sizing done yet. [team to verify with primary source] |

---

## Top 5 Assumptions Ranked by Risk

1. **H1: SOC analysts spend 3-5 hours per phishing triage cycle [illustrative].** If actual triage time is under 30 minutes, the ROI story collapses and there is no compelling reason to buy. This is the single most load-bearing number in the business case.

2. **H2: Head of Security is the budget holder, not CISO or IT Director.** If the real buyer is two levels up (CISO) or across the aisle (IT), the entire GTM motion changes. Wrong buyer title means every outreach message is aimed at the wrong person.

3. **H3: Buyers will pay GBP 1,000-2,500 per seat per month [illustrative].** If the realistic price point is a quarter of this, the unit economics do not work at the team's cost structure. Pricing needs to be tested in conversation, not assumed.

4. **H4: Analysts would switch from their current tools for materially lower false-positive rates.** Switching costs in enterprise security tooling are high. Even a good product needs a clear enough improvement to justify ripping out an embedded stack. This assumption has not been tested.

5. **H5: Mid-market regulated fintechs can onboard a new security tool in under 60 days.** Compliance review, vendor risk assessment, DPIA, and IT approval at a regulated fintech can easily run to 3-6 months [illustrative]. If onboarding is slow, cash flow and churn models break.

---

## PULL Hypotheses

### H1: Analyst triage time

**Population:** SOC analysts and Heads of Security at 200-500 person regulated fintechs (DACH, CEE, UK) who have responded to at least one phishing incident in the last three months.

**Understanding:** We believe these analysts spend 3-5 hours [illustrative] per triage cycle handling a phishing alert, from first detection through investigation, escalation, and closure.

**Learning:** Ask interviewees to walk through the most recent phishing incident in detail: who handled it, what tools they used, how long each step took. Cross-reference with "how many of these does your team handle per week?"

**Limit:** If 7 of 10 interviewees describe triage cycles of under 60 minutes, the ROI story needs to be rebuilt from a different pain. If 7 of 10 describe cycles of 2 hours or more, H1 is directionally validated.

**Kill criteria:** Fewer than 3 of 10 interviewees describe triage as taking more than 60 minutes. Analysts describe it as a minor, easily handled task.

**Validate criteria:** 7 or more of 10 interviewees describe triage cycles of 2 hours or more, cite analyst time as a constraint, and connect it to missed alerts or delayed response.

**Evidence rating:** Assumption. Source: desk reading on SOC analyst workloads [team to verify with primary source]. No customer interviews have tested this yet.

---

### H2: Buyer title

**Population:** 200-500 person regulated fintechs in DACH, CEE, or UK with at least one dedicated SOC analyst on staff.

**Understanding:** We believe the Head of Security (or equivalent: Head of Information Security, Head of IT Security, Security Lead) holds the budget for tooling purchases in this size range, not the CISO (who exists at larger firms) or the IT Director (who focuses on infrastructure, not security operations).

**Learning:** In every interview, ask "who signs off your security tool budget?" as a direct, concrete question. Also ask "walk me through the last security tool your team bought" to surface who was involved in the decision.

**Limit:** If 7 of 10 interviewees confirm the Head of Security (or equivalent) signs off independently, H2 is validated. If multiple interviewees report involving a CISO, CFO, or IT Director as the decision maker, the GTM motion needs to change.

**Kill criteria:** Fewer than 3 of 10 say the Head of Security signs off independently. Most route through IT or Finance for final approval.

**Validate criteria:** 7 or more of 10 confirm the Head of Security has independent signing authority for tools under a specific threshold [team to verify typical threshold in this segment].

**Evidence rating:** Assumption. Source: ShieldByte team's prior experience at a Serbian bank. Different market, different firm size. Has not been tested with this specific segment.

---

### H3: Price point

**Population:** Heads of Security at 200-500 person regulated fintechs with existing security tooling budget.

**Understanding:** We believe buyers in this segment will pay GBP 1,000-2,500 per seat per month [illustrative] for a phishing triage automation tool that materially reduces analyst time and false positives.

**Learning:** Ask "what did you spend on security tooling in the last 12 months? Where did it go?" Do not ask "would you pay X" (opinion). Ask about what they have already spent and on what. Then ask "what would a tool that cut your triage time by half be worth to your team per analyst per month?" to surface their own framing of value.

**Limit:** If interviewees consistently describe existing security tool spend in the GBP 500-2,000 per seat per month range [illustrative], the price window is plausible. If the budget landscape is much lower, the price needs to come down or the buyer needs to be a larger firm.

**Kill criteria:** More than half of interviewees describe security tool spend well below GBP 500 per seat per month [illustrative], or describe phishing triage as outside their current tooling budget category.

**Validate criteria:** 5 or more of 10 interviewees describe existing spend in the right ballpark and frame the value of triage automation in monetary terms without prompting.

**Evidence rating:** Assumption. Source: None. No pricing research has been done on this segment yet.

---

### H4: Switching behaviour

**Population:** SOC analysts at regulated fintechs currently using phishing detection tools (standalone or embedded in broader security platforms).

**Understanding:** We believe analysts would actively switch from their current toolchain if a new tool demonstrably reduced false positives by a material percentage [team to verify what "material" means for this segment]. Current false-positive rates are high enough to be painful, not just inconvenient.

**Learning:** Ask "what's the false-positive rate on your current phishing tooling?" and "what was the last tool your team adopted that actually stuck? Why that one?" and "what's the last tool you tried that got kicked out? Why?" These behavioural questions surface the real switching threshold without asking directly.

**Limit:** If 6 of 10 interviewees describe false positives as a real pain that takes measurable analyst time, and cite at least one previous tool replacement driven by performance rather than cost, H4 is directionally supported.

**Kill criteria:** Interviewees describe their current tools as good enough, or describe switching costs as prohibitive regardless of performance improvement.

**Validate criteria:** 6 or more of 10 describe false positives as a significant time drain, express frustration with current tool accuracy, and describe at least one prior tool switch driven by technical performance.

**Evidence rating:** Assumption. Source: General industry knowledge about SOC analyst complaints. No interviews with target segment yet.

---

### H5: Onboarding speed

**Population:** IT Security and Procurement teams at 200-500 person regulated fintechs in DACH, CEE, or UK.

**Understanding:** We believe a new security tool can be fully onboarded (vendor approval, compliance sign-off, IT integration, and analyst training) in under 60 days at this company size.

**Learning:** Ask "when did your team last go through a compliance audit? What was the worst part?" and "what's the typical timeline from picking a new tool to full deployment for your team?" These surface actual past experience with tool adoption rather than hypothetical timelines.

**Limit:** If 7 of 10 interviewees describe typical tool onboarding as under 90 days, H5 is conditionally supported. If most describe 4-6 month timelines [illustrative], the business model assumptions about cash flow and early revenue need adjusting.

**Kill criteria:** More than half of interviewees describe vendor approval and IT integration alone taking longer than 90 days at a regulated fintech, even for small tooling purchases.

**Validate criteria:** 7 or more of 10 describe prior security tool purchases completing within 90 days from selection to live deployment, with internal compliance sign-off included.

**Evidence rating:** Assumption. Source: ShieldByte team experience at a Serbian bank (different regulatory environment, smaller size). This market is different.

---

## Single Biggest Risk

**H1 is the single biggest risk.** The entire ROI story depends on analyst triage time being long enough that automation creates meaningful value. If the real number is under 30 minutes per cycle, there is no compelling business case. Every other assumption can be adjusted. If H1 is wrong, the product category is wrong.

---

## Evidence Assessment

| Claim | Source | Rating |
|---|---|---|
| SOC analysts spend 3-5 hours per triage cycle | Assumption, desk reading [team to verify] | Assumption |
| Head of Security is the buyer at 200-500 person fintechs | Founder inference from prior experience | Assumption |
| Phishing triage is a top-3 pain for SOC teams | Assumption, industry reading [team to verify] | Assumption |
| Analysts would switch for lower false-positive rates | Assumption, no behavioural evidence | Assumption |
| Buyers will pay GBP 1,000-2,500/seat/month [illustrative] | Assumption, no pricing research | Assumption |
| Onboarding under 60 days at a regulated fintech | Assumption from unrelated market (Serbian banks) | Assumption |
| Problem is consistent across DACH, CEE, UK fintechs | Assumption, no cross-market interviews | Assumption |

**Overall rating: Assumption-Heavy.** This is expected and appropriate at Week 3. The team is entering discovery with a well-formed set of testable hypotheses, not validated claims. The value of this document is in making the assumptions explicit so they can be tested systematically.

---

## Next Steps

1. Interview 3 Heads of Security before next Friday using the Exercise 2 script. Focus every conversation on H1 and H2: how long does triage actually take, and who signs off the budget. These two hypotheses must be tested before any GTM decisions are made.

2. Identify 10 specific targets from the contact list before sending a single outreach message. Targeting matters more than volume at this stage.

3. After interview 3, review H1. If triage time is consistently below 60 minutes, stop and revisit the problem statement before continuing. Do not run 10 interviews on a broken hypothesis.

4. Research existing published data on SOC analyst workloads and false-positive rates before week 4 [team to verify with primary source]. This will help calibrate whether interview findings are representative or outliers.

5. Identify one Hub201 advisor or network contact who can make a warm introduction to a Head of Security at a fintech. A warm intro for interview 1 produces stronger data than cold outreach: the person shows up prepared to be candid rather than guarded.
