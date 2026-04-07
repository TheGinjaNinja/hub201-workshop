# Personas: ShieldByte

**Date:** 2026-04-07
**Exercise:** Buyer and User Personas

## Beachhead Definition

**Segment:** Serbian banks with 200-1000 employees that do not currently have a formal security awareness programme and face NIS2 compliance deadlines.

**Why this segment first:**
- The founders spent 3 years working in IT security at a Serbian bank. They have direct relationships and credibility in this community.
- NIS2 creates a regulatory trigger that forces action. Banks cannot ignore this indefinitely.
- Serbian banks in this size range are too small for KnowBe4's enterprise sales motion but too regulated to do nothing.
- Bank CISOs and IT Security Managers in Serbia attend the same conferences and know each other. Word of mouth works.

**Target list size:** Estimated 40-60 banks in Serbia in this employee range. The founders can currently name 15 by name. This needs to be expanded and verified. If the actual count is below 30, the beachhead should expand to include Croatia and Bosnia.

**Adjacent segments for expansion:**
1. Banks in Croatia, Bosnia, North Macedonia, and Montenegro (same NIS2 pressure, similar language, similar bank sizes)
2. Insurance companies and other regulated financial services firms in Serbia (same regulation, different vertical)
3. Larger Serbian enterprises (1000-5000 employees) once case studies and references are established

## Persona Cards

### "Compliance-First Dragan"

**Buying Role:** Champion + Decision Maker
**Early or Ideal Customer:** Early Customer

**Role/Title:** Chief Information Security Officer (CISO)
**Company Profile:**
- Size: 300-500 employees
- Industry: Banking (commercial and retail)
- Geography: Serbia (Belgrade HQ, regional branches)
- Qualifying characteristics: Subject to NIS2. Has had at least one phishing incident in the past 12 months. No formal security awareness programme in place.

**Trigger Event:** The NIS2 Directive compliance deadline. Dragan's board has asked him to demonstrate a security awareness programme by the end of the year. He has no programme, no budget allocated, and needs something he can deploy quickly and report on.

**Jobs to Be Done:**
1. Implement a documentable security awareness programme that satisfies NIS2 requirements and can be presented to auditors
2. Reduce the organisation's phishing exposure, which is the source of most security incidents
3. Demonstrate to the board that security spend is producing measurable outcomes, not just activity

**Pain Points (ranked):**
1. Has no security awareness programme and the compliance deadline is approaching. Would pay to solve this today. (Critical)
2. Spends personal time running ad-hoc phishing tests because there is no tool and no dedicated staff for this. (Major)
3. Board asks for security metrics but all he can report is "we had X incidents." No proactive measurement. (Major)

**Current Solution:** Occasional manual phishing tests using free tools. A PowerPoint presentation during onboarding. Annual email reminding staff not to click suspicious links. No platform, no measurement, no follow-up training.

**Channels:**
- Serbian Banking Association events and conferences
- LinkedIn (active in local cybersecurity groups)
- ISACA Serbia chapter meetings
- Personal network from the founders' time at a Serbian bank
- Webinars on NIS2 compliance (attending, not hosting)

**Evidence Assessment:**
| Field | Evidence Source | Strength |
|-------|---------------|----------|
| Role/Title | 5 of 8 interviewees were CISOs or equivalent | Moderate |
| Company Profile | 8 interviews across banks in this size range | Moderate |
| Trigger Event | All 8 interviewees mentioned NIS2 | Moderate |
| Jobs to Be Done | Consistent theme across 6+ interviews | Moderate |
| Pain Points | 7 of 8 confirmed no formal programme | Moderate |
| Current Solution | 5 interviewees described manual processes | Moderate |
| Channels | Assumption based on founder knowledge of the market | Assumption |

---

### "Overloaded Milica"

**Buying Role:** End User + Influencer
**Early or Ideal Customer:** Early Customer

**Role/Title:** IT Security Manager (or IT Security Analyst in smaller banks)
**Company Profile:**
- Size: 200-500 employees
- Industry: Banking
- Geography: Serbia
- Qualifying characteristics: Part of a 2-3 person IT security team. Responsible for day-to-day security operations including incident response, access management, and (informally) security training.

**Trigger Event:** Her CISO has been told to implement a security awareness programme. The task lands on Milica's desk because she is the one who "does security." She now has to run phishing simulations on top of her existing workload.

**Jobs to Be Done:**
1. Run phishing simulations and security training without it consuming all her time
2. Produce reports that her CISO can present to the board and auditors
3. Reduce the volume of phishing-related incidents she has to investigate (fewer clicks means fewer incident tickets)

**Pain Points (ranked):**
1. Already overloaded with day-to-day security operations. Adding a training programme means something else does not get done. Would pay to automate this. (Critical)
2. Current phishing tests are manual. She configures emails in a free tool, sends them, manually tracks who clicked, and follows up individually. This takes a full day per campaign. (Major)
3. Training content available from global vendors is in English. Non-technical bank staff (tellers, branch managers) struggle with it and do not complete modules. Milica gets blamed for low completion rates. (Major)

**Current Solution:** GoPhish (free, open-source phishing simulation tool) configured manually. Results tracked in an Excel spreadsheet. Follow-up is a personal email from Milica to staff who clicked. No formal training module.

**Channels:**
- LinkedIn (follows cybersecurity content but posts rarely)
- Serbian cybersecurity Slack/Discord communities
- Peer recommendations from IT security colleagues at other banks
- OWASP Belgrade chapter meetups

**Evidence Assessment:**
| Field | Evidence Source | Strength |
|-------|---------------|----------|
| Role/Title | 3 of 8 interviewees were IT Security Managers | Moderate |
| Company Profile | Same interview pool | Moderate |
| Trigger Event | 2 interviewees described this exact scenario (task delegated from CISO) | Weak |
| Jobs to Be Done | Inferred from pain point discussions | Weak |
| Pain Points | 3 interviewees described manual processes in detail | Moderate |
| Current Solution | 2 interviewees specifically mentioned GoPhish | Weak |
| Channels | Assumption based on founder network | Assumption |

---

### "Budget-Gate Jovan"

**Buying Role:** Saboteur (potential)
**Early or Ideal Customer:** N/A (not a buyer, but must be navigated)

**Role/Title:** Head of Procurement / Procurement Officer
**Company Profile:**
- Size: 300-1000 employees
- Industry: Banking
- Geography: Serbia
- Qualifying characteristics: Banks with formal procurement processes requiring vendor assessments, competitive bids, or board-level spend approval

**Trigger Event:** A purchase request lands on his desk for a cybersecurity tool he has never heard of from a startup with no track record. His job is risk management in vendor selection.

**Jobs to Be Done:**
1. Ensure the bank is not taking on vendor risk by buying from an unproven company
2. Follow procurement policy (may require 2-3 competitive quotes, vendor risk assessment, data processing agreements)
3. Protect the bank's budget by ensuring value for money

**Pain Points (ranked):**
1. Pressure to approve quickly because of the compliance deadline, but no established process for buying from startups. (Major)
2. Cannot evaluate cybersecurity products technically. Relies on the CISO's recommendation but needs to do due diligence. (Major)
3. Worried about data handling. Phishing simulations involve employee email addresses and behaviour data. GDPR and local data protection concerns. (Major)

**Current Solution:** Standard vendor assessment process designed for large, established suppliers. Not adapted for startup procurement. May default to requiring ISO 27001 certification or equivalent, which ShieldByte does not have.

**Channels:** Not relevant for outreach. Encountered during the sales process.

**Evidence Assessment:**
| Field | Evidence Source | Strength |
|-------|---------------|----------|
| Role/Title | Assumption. No procurement officers were interviewed. | Assumption |
| Trigger Event | Assumption based on founder experience | Assumption |
| Pain Points | Assumption based on B2B sales knowledge | Assumption |
| Current Solution | Assumption. Need to validate procurement process at pilot banks. | Assumption |

**Note:** This persona is entirely assumption-based. The founders have not spoken to a single procurement officer. Both pilot banks bypassed formal procurement because the pilots are free. When ShieldByte starts charging, Jovan will appear. The founders need to prepare for this before the first paid deal.

---

## Buyer Map (B2B)

| Role | Person/Title | Motivation | Potential Objection |
|------|-------------|------------|-------------------|
| Champion | CISO ("Dragan") | Needs to demonstrate NIS2 compliance. Wants a solution he can deploy quickly and report on. | "I want this but I need to justify buying from a startup with no track record." |
| Influencer | IT Security Manager ("Milica") | Wants to automate manual phishing tests that consume her limited time. | "Will this actually integrate with our email system? I do not have time for a complex deployment." |
| Decision Maker | CISO ("Dragan") or CEO at smaller banks | Board pressure to address cybersecurity. Compliance deadline creates urgency. | "What happens if this startup folds in 12 months? Where does our data go?" |
| Budget Holder | CFO or CISO (depending on bank size) | Needs to justify spend. Looking for cost-effective solution relative to enterprise alternatives. | "Can we not just use a free tool? Or get our IT consultancy to do this for less?" |
| Saboteur | Procurement Officer ("Jovan") | Following process. Risk-averse by role. | "This vendor has no ISO 27001, no references, and no track record. I cannot approve this." |

## Evidence Assessment

- **Overall rating:** Moderate (for Dragan and Milica), Assumption-Heavy (for Jovan and the buyer map)
- **Strongest evidence:** The CISO persona (Dragan) is grounded in 8 interviews. The NIS2 trigger, the lack of a formal programme, and the manual workaround pain are consistent across multiple conversations.
- **Biggest assumption:** The procurement saboteur (Jovan) is entirely fabricated from B2B sales instinct. This is a significant blind spot. If procurement at these banks is more rigid than assumed, the sales cycle could be 3-6 months longer than expected.
- **Evidence gaps:** No interviews with procurement officers, CFOs, or board members. No interviews with IT Security Managers at banks where the CISO is not the decision maker. The buyer map above the CISO level is assumption-heavy.

## Next Steps

1. During the two pilots, identify and interview the procurement officer at each bank. Understand their vendor assessment process. Ask what they would need to approve a paid contract. This is the fastest way to validate or kill the Jovan persona.
2. Interview 2-3 more IT Security Managers to strengthen the Milica persona. Two data points on the "delegated task" trigger is not enough. Specifically ask about their current tools (confirm GoPhish usage), time spent per campaign, and what would make them advocate internally for a paid tool.
3. Build a named target list of 50 Serbian banks in the 200-1000 employee range. Verify the count. If it is below 30, expand the beachhead definition to include Croatia and Bosnia and build equivalent personas for those markets.
4. Interview one bank CFO to understand budget allocation for cybersecurity tools. The assumption that "enterprise pricing is too expensive" needs validation with the person who actually controls the budget, not just the CISO who believes it.
