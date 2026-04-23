# Personas: ShieldByte

**Date:** 2026-04-07
**Exercise:** Buyer and User Personas (Customer Clarity Canvas)

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

#### Define the Customer

- **Role/Title:** Chief Information Security Officer (CISO)
- **Firmographics:** Banking (commercial and retail), 300-500 employees, Serbia (Belgrade HQ, regional branches). Subject to NIS2. Has had at least one phishing incident in the past 12 months.
- **Role in Purchase:** Champion and Decision Maker. At banks this size, the CISO typically owns the security budget and can approve purchases under EUR 20K without board sign-off.
- **Trigger Event:** The NIS2 Directive compliance deadline. Dragan's board has asked him to demonstrate a security awareness programme by the end of the year. He has no programme, no budget allocated, and needs something he can deploy quickly and report on.
- **Where They Hang Out:** Serbian Banking Association events, LinkedIn (active in local cybersecurity groups), ISACA Serbia chapter meetings, NIS2 compliance webinars (attending, not hosting).
- **Who Influences Them:** National Bank of Serbia regulatory guidance, Big 4 audit firms (who flag gaps during annual audits), peer CISOs at other Serbian banks, Gartner/Forrester reports (read but not subscribed).

#### Define the Use Case

- **Situation Before Your Product:** Dragan knows phishing is the top attack vector but has no structured programme to address it. He runs occasional tests manually and delivers a PowerPoint during onboarding. He has no data on whether any of this works.
- **Current Solution:** Occasional manual phishing tests using free tools. A PowerPoint presentation during onboarding. Annual email reminding staff not to click suspicious links. No platform, no measurement, no follow-up training.
- **Frustrations with Current Approach:** Manual process is inconsistent and time-consuming. Results are not tracked systematically. No way to demonstrate improvement over time. English-language content gets ignored by non-technical staff. Auditors ask for evidence of a programme and he has nothing formal to show.
- **Consequences:** Regulatory risk (NIS2 non-compliance), board exposure (cannot demonstrate security investment is working), personal reputation risk (Dragan is accountable if a phishing breach occurs after failing to implement a programme). Estimated cost of a single successful phishing breach: EUR 50-200K in incident response, regulatory reporting, and remediation.
- **Past Spend:** Has not spent on security awareness tools before. Has budget for security tooling generally (EUR 30-50K/year total security budget at banks this size). Would need to carve out EUR 5-15K for awareness specifically.

#### Define the Problem

- **Jobs to Be Done:**
  1. Implement a documentable security awareness programme that satisfies NIS2 requirements and can be presented to auditors
  2. Reduce the organisation's phishing exposure, which is the source of most security incidents
  3. Demonstrate to the board that security spend is producing measurable outcomes, not just activity (social job: look competent and proactive to leadership)
- **Pain Points (ranked by severity):**
  1. Has no security awareness programme and the compliance deadline is approaching. Would pay to solve this today. (Critical)
  2. Spends personal time running ad-hoc phishing tests because there is no tool and no dedicated staff for this. (Major)
  3. Board asks for security metrics but all he can report is "we had X incidents." No proactive measurement. (Major)
- **How Often They Feel This Pain:** Weekly. Every phishing incident that lands on his desk reminds him. Monthly when preparing board reports. Acutely when auditors visit.
- **Problem Awareness:** High. Dragan knows he has this problem and is actively seeking a solution. The NIS2 deadline has moved him from "aware" to "actively seeking."
- **Why They Would Say No:** Startup risk ("what if ShieldByte folds in 12 months?"), lack of references in Serbian banking, procurement friction if purchase exceeds his signing authority, potential preference for a known brand even at higher cost.

#### Define the Buyers (B2B)

- **Champion:** Dragan himself. He feels the pain, owns the problem, and will advocate internally.
- **Influencer:** IT Security Manager (Milica). She evaluates whether the tool actually works and whether deployment is feasible.
- **Decision Maker:** Dragan at banks under 500 employees. CEO or board at larger banks.
- **Budget Holder:** Dragan for security budget. CFO for unplanned spend above his authority.
- **Saboteur:** Procurement Officer (Jovan). Requires vendor risk assessment, may demand certifications ShieldByte does not yet have.
- **End User:** Milica (configures and runs campaigns). All employees (receive simulations and training).

#### Channels

- Direct outreach via founders' personal network from working at a Serbian bank (can reach 10-15 CISOs directly)
- Serbian Banking Association events (next event: Q3 2026)
- ISACA Serbia chapter meetings (monthly)
- LinkedIn targeted outreach to CISOs at named Serbian banks
- Referral from pilot bank CISOs once pilots are underway

#### Evidence Assessment

| Field | Evidence Source | Strength |
|-------|---------------|----------|
| Customer Profile | 8 interviews across banks in this size range, 5 were CISOs | Moderate |
| Use Case | 5 interviewees described manual processes in detail | Moderate |
| Problem / Pains | 7 of 8 confirmed no formal programme, consistent pain themes | Moderate |
| Trigger Event | All 8 interviewees mentioned NIS2 unprompted | Moderate |
| Buyer Roles | Assumption based on founder experience. No procurement or CFO interviews. | Assumption |

---

### "Overloaded Milica"

**Buying Role:** End User + Influencer
**Early or Ideal Customer:** Early Customer

#### Define the Customer

- **Role/Title:** IT Security Manager (or IT Security Analyst in smaller banks)
- **Firmographics:** Banking, 200-500 employees, Serbia. Part of a 2-3 person IT security team. Responsible for day-to-day security operations including incident response, access management, and (informally) security training.
- **Role in Purchase:** End User and Influencer. Milica evaluates whether the tool works technically and whether deployment is realistic. Her recommendation carries weight with the CISO, but she does not sign the cheque.
- **Trigger Event:** Her CISO has been told to implement a security awareness programme. The task lands on Milica's desk because she is the one who "does security." She now has to run phishing simulations on top of her existing workload.
- **Where They Hang Out:** LinkedIn (follows cybersecurity content but posts rarely), Serbian cybersecurity Slack/Discord communities, OWASP Belgrade chapter meetups, peer recommendations from IT security colleagues at other banks.
- **Who Influences Them:** Her CISO (direct manager), peer IT security managers at other banks, open-source community recommendations, cybersecurity blog posts and tool reviews.

#### Define the Use Case

- **Situation Before Your Product:** Milica juggles incident response, access management, vulnerability patching, and now has been handed "security awareness" as an additional responsibility with no additional headcount or budget.
- **Current Solution:** GoPhish (free, open-source phishing simulation tool) configured manually. Results tracked in an Excel spreadsheet. Follow-up is a personal email from Milica to staff who clicked. No formal training module.
- **Frustrations with Current Approach:** Each campaign takes a full day to configure, send, track, and follow up. Results sit in a spreadsheet that nobody reads. English-language content gets low completion rates among non-technical staff, and Milica gets blamed. No way to show improvement over time.
- **Consequences:** Time cost (1 full day per campaign, roughly 12 days/year). Reputation cost (blamed for low training completion). Stress (adding a programme on top of an already full workload with no extra resource). Security risk (manual approach is inconsistent, leaving gaps between campaigns).
- **Past Spend:** Milica does not control budget. She uses free tools. Her CISO would need to approve any paid tool. She has never requested budget for security awareness tooling before.

#### Define the Problem

- **Jobs to Be Done:**
  1. Run phishing simulations and security training without it consuming all her time
  2. Produce reports that her CISO can present to the board and auditors
  3. Reduce the volume of phishing-related incidents she has to investigate (fewer clicks means fewer incident tickets)
- **Pain Points (ranked by severity):**
  1. Already overloaded with day-to-day security operations. Adding a training programme means something else does not get done. Would pay to automate this. (Critical)
  2. Current phishing tests are manual. She configures emails in a free tool, sends them, manually tracks who clicked, and follows up individually. This takes a full day per campaign. (Major)
  3. Training content available from global vendors is in English. Non-technical bank staff (tellers, branch managers) struggle with it and do not complete modules. Milica gets blamed for low completion rates. (Major)
- **How Often They Feel This Pain:** Daily (general overload), monthly (when running a phishing campaign), quarterly (when reporting to CISO/board).
- **Problem Awareness:** High. Milica knows exactly what is broken. She is not seeking a solution herself because she does not control budget, but she would enthusiastically champion a tool that saves her time.
- **Why They Would Say No:** "I do not have budget authority." "Will this integrate with our email system without a complex deployment?" "I do not have time to learn a new tool on top of everything else." Fear that automation replaces her perceived value.

#### Define the Buyers (B2B)

- **Champion:** Milica herself (advocates for the tool to her CISO based on time savings)
- **Influencer:** Milica (technical evaluation)
- **Decision Maker:** CISO (Dragan)
- **Budget Holder:** CISO or CFO
- **Saboteur:** IT operations (if deployment touches email infrastructure) or procurement
- **End User:** Milica (admin), all employees (receive simulations)

#### Channels

- Reached through the CISO (Dragan introduces Milica during technical evaluation)
- OWASP Belgrade chapter meetups
- Serbian cybersecurity Slack/Discord communities
- Peer-to-peer recommendations from other bank IT security staff

#### Evidence Assessment

| Field | Evidence Source | Strength |
|-------|---------------|----------|
| Customer Profile | 3 of 8 interviewees were IT Security Managers | Moderate |
| Use Case | 3 interviewees described manual processes in detail, 2 mentioned GoPhish | Moderate |
| Problem / Pains | Consistent across the 3 IT Security Manager interviews | Moderate |
| Trigger Event | 2 interviewees described the "delegated task" scenario | Weak |
| Buyer Roles | Assumption based on B2B sales knowledge | Assumption |

---

### "Budget-Gate Jovan"

**Buying Role:** Saboteur (potential)
**Early or Ideal Customer:** N/A (not a buyer, but must be navigated)

#### Define the Customer

- **Role/Title:** Head of Procurement / Procurement Officer
- **Firmographics:** Banking, 300-1000 employees, Serbia. Banks with formal procurement processes requiring vendor assessments, competitive bids, or board-level spend approval.
- **Role in Purchase:** Saboteur. Jovan does not initiate the purchase but can block or delay it through process requirements.
- **Trigger Event:** A purchase request lands on his desk for a cybersecurity tool he has never heard of from a startup with no track record. His job is risk management in vendor selection.
- **Where They Hang Out:** Not relevant for outreach. Encountered during the sales process.
- **Who Influences Them:** Internal compliance policies, bank audit committee, legal department, vendor risk frameworks.

#### Define the Use Case

- **Situation Before Your Product:** Jovan processes vendor approvals for established suppliers with track records. He has a standard checklist and process. A startup vendor does not fit the template.
- **Current Solution:** Standard vendor assessment process designed for large, established suppliers. Not adapted for startup procurement. May default to requiring ISO 27001 certification or equivalent, which ShieldByte does not have.
- **Frustrations with Current Approach:** Pressure to approve quickly because of the compliance deadline, but his process is not designed for speed or for evaluating startups.
- **Consequences:** If he approves a vendor that fails (data breach, company folds), it reflects on his due diligence. If he blocks a vendor the CISO needs, he is seen as an obstacle to compliance.
- **Past Spend:** Not applicable. Jovan controls process, not budget.

#### Define the Problem

- **Jobs to Be Done:**
  1. Ensure the bank is not taking on vendor risk by buying from an unproven company
  2. Follow procurement policy (may require 2-3 competitive quotes, vendor risk assessment, data processing agreements)
  3. Protect the bank's budget by ensuring value for money
- **Pain Points (ranked by severity):**
  1. Pressure to approve quickly because of the compliance deadline, but no established process for buying from startups. (Major)
  2. Cannot evaluate cybersecurity products technically. Relies on the CISO's recommendation but needs to do due diligence. (Major)
  3. Worried about data handling. Phishing simulations involve employee email addresses and behaviour data. GDPR and local data protection concerns. (Major)
- **How Often They Feel This Pain:** Infrequently. Only when a non-standard vendor enters the pipeline. But when it happens, it can block a deal for weeks or months.
- **Problem Awareness:** Low. Jovan does not think of himself as having a problem. He is following process. The startup needs to make his job easy, not convince him he has a problem.
- **Why They Would Say No:** "No ISO 27001." "No references from comparable banks." "Need three competitive quotes." "Data processing agreement does not meet our requirements." "Cannot approve a vendor with less than 2 years of trading history."

#### Define the Buyers (B2B)

- **Champion:** None. Jovan does not champion purchases.
- **Influencer:** Jovan himself (can influence through process requirements)
- **Decision Maker:** Not Jovan, but he has effective veto power
- **Budget Holder:** Not Jovan
- **Saboteur:** Jovan IS the saboteur in this scenario
- **End User:** Not Jovan

#### Channels

- Not relevant for outreach. Encountered during the sales process. The strategy is to prepare materials that satisfy his requirements before he asks for them.

#### Evidence Assessment

| Field | Evidence Source | Strength |
|-------|---------------|----------|
| Customer Profile | Assumption. No procurement officers were interviewed. | Assumption |
| Use Case | Assumption based on founder experience | Assumption |
| Problem / Pains | Assumption based on B2B sales knowledge | Assumption |
| Trigger Event | Assumption based on typical procurement flows | Assumption |
| Buyer Roles | N/A (Jovan is the saboteur role in the buyer map) | Assumption |

**Note:** This persona is entirely assumption-based. The founders have not spoken to a single procurement officer. Both pilot banks bypassed formal procurement because the pilots are free. When ShieldByte starts charging, Jovan will appear. The founders need to prepare for this before the first paid deal.

---

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
