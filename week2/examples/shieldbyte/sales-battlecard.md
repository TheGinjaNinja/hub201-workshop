# Sales Battlecard: ShieldByte

**Date:** 2026-04-07
**Exercise:** Sales Battlecard

---

## Competitor: KnowBe4

### Overview
KnowBe4 is the world's largest security awareness training platform, offering phishing simulations, training modules, and compliance reporting. Taken private by Vista Equity Partners in 2023 for approximately $4.6B. Over 65,000 customers globally, primarily mid-market to enterprise. They pioneered the security awareness training category and have massive brand recognition.

### Their Positioning
"The world's largest security awareness training and simulated phishing platform." They lead with scale: 15,000+ phishing templates, the largest training content library, and integrations with every major email and SIEM platform. Their marketing emphasises ease of use, broad content, and "human risk management."

### Where They Win
- Content library size. 15,000+ phishing templates versus ShieldByte's ~50. In a feature comparison, this is not even close.
- Brand recognition and trust. CISOs know the name. Analysts include them in reports. Procurement teams are comfortable approving a vendor of this size.
- Breadth of integrations. Native integrations with Microsoft 365, Google Workspace, every major SIEM, and most HR platforms.
- Established compliance reporting for SOC 2, ISO 27001, GDPR, HIPAA, and other global frameworks.
- Customer success infrastructure. Dedicated CSMs, 24/7 support, onboarding programmes. ShieldByte has two founders.

### Where We Win
| Our Advantage | Their Limitation | Customer Outcome |
|---------------|-----------------|------------------|
| Serbian and Balkan language simulations and training content | No Serbian language content. All templates in English or major European languages. | Bank employees engage with training they can actually read. Higher completion rates. Fewer "I did not understand the email" excuses after a real phishing incident. |
| NIS2 compliance reporting mapped to Southeast European regulatory context | Generic compliance reporting. No specific NIS2 mapping for Serbian/Balkan regulatory implementation. | CISO hands auditors a report that directly addresses their requirements instead of a generic compliance dashboard that needs manual interpretation. |
| Pricing for 200-1000 employee organisations | Per-user pricing starts at USD 18-25/user/year. For a 500-person bank, that is USD 9,000-12,500/year before enterprise upsells. | ShieldByte can price at EUR 5-8/user/year and still build a viable regional business. The bank gets comparable core functionality at 50-60% less cost. |
| Adaptive difficulty that increases as employees improve | Static campaign difficulty. Admins manually select template difficulty. Most run the same difficulty repeatedly. | Employees face progressively harder simulations. No "training plateau" where staff learn to recognise the same patterns and stop improving. |

### Common Objections and Responses
| Objection | Response | Evidence |
|-----------|----------|----------|
| "KnowBe4 has thousands of templates. You have 50." | "You are right. They have an enormous library. The question is whether your employees need 15,000 English-language templates or 50 Serbian-language templates based on real phishing attacks targeting Balkan banks. We built ours from actual attack patterns we handled when we worked in bank IT security. Generic volume versus specific relevance." | Moderate (based on founder experience with actual bank phishing attacks, but no comparative engagement data yet) |
| "KnowBe4 is an established vendor. You are a startup. What if you disappear?" | "Fair concern. Two things: first, your data stays yours. We can export everything at any time. Second, the bigger risk for your bank is not that we disappear. It is that you have no programme at all when the auditor arrives. KnowBe4 has a 6-8 week enterprise sales cycle minimum. We can have you running simulations in Serbian within a week." | Weak (the deployment time claim is based on prototype, not production deployments) |
| "We are already evaluating KnowBe4." | "Good. That means you have already decided you need a programme. Ask your KnowBe4 rep two questions: can they deliver simulations in Serbian, and can they map compliance reporting to NIS2 as implemented in Serbia? If the answer is no, you will need to build that layer yourself on top of their platform." | Moderate (based on confirmed lack of Serbian content on KnowBe4's platform) |

### Killer Questions
1. "When you run phishing simulations, do your employees receive the training content in Serbian or in English? What completion rates do you see for English-language training among branch staff?"
2. "How does your current tool adapt the difficulty of simulations based on how employees perform? Or does every employee get the same test regardless of their track record?"
3. "When your auditor asks for evidence of your NIS2 security awareness programme, what exactly do you show them today?"

### Landmines
1. "It is worth asking any vendor about language support. Not just the interface language, but the actual simulation content. A phishing simulation in English is easy to spot for a Serbian-speaking employee, not because they are security-aware, but because they know their bank does not send internal communications in English. The simulation needs to feel real in the employee's working language to be a valid test."
2. "One thing to check: how does pricing scale? Some vendors charge per-user with no volume discount for organisations under 1,000 employees. At your bank size, that can add up quickly. Worth comparing the total 3-year cost, not just the headline per-user rate."

---

## Competitor: Do Nothing / Manual Training (Status Quo)

### Overview
The prospect continues with their current approach: no formal security awareness programme, occasional manual phishing tests run by the IT security team using free tools like GoPhish, and a PowerPoint presentation during employee onboarding. This is the most common competitor at ShieldByte's stage. More deals will be lost to inaction than to KnowBe4.

### Why They Choose Inaction
- **Budget:** "We do not have budget allocated for security awareness tools." Security awareness training is a new spend category for most Serbian mid-market banks. There is no existing line item to replace.
- **Other priorities:** "We have bigger security problems to solve first." Endpoint protection, network security, and incident response feel more urgent than employee training.
- **Perceived adequacy:** "We already do phishing tests. It is fine." Running manual tests feels like "doing something" even if there is no measurement or follow-up training.
- **Complexity:** "Implementing another tool means getting procurement, IT, and HR involved. That takes months." The overhead of buying feels heavier than the pain of the status quo.
- **NIS2 ambiguity:** "We are not sure exactly what NIS2 requires yet. We will wait for clearer guidance." Regulatory ambiguity is a convenient reason to delay.

### Cost of Inaction
| Current Approach | Time Cost | Money Cost | Risk Cost |
|-----------------|-----------|------------|-----------|
| Manual phishing tests (GoPhish) | 8-16 hours per campaign for setup, delivery, tracking, and follow-up. Run quarterly at best. | Free tool, but IT Security Manager time at EUR 30-50/hour = EUR 960-3,200/year in staff time per campaign. 4 campaigns = EUR 3,800-12,800. | No adaptive difficulty. No behaviour tracking. No audit trail. Employees learn to spot the same patterns but remain vulnerable to novel attacks. |
| Onboarding PowerPoint | 2 hours to deliver per session. No update cycle. | Minimal direct cost. Opportunity cost: employees who "completed" training in 2023 have no refresher and no measurable retention. | Creates a false sense of compliance. If an auditor asks "when was your last training update?" and the answer is "2023," that is a finding. |
| No programme at all | Zero time invested. | Zero direct cost. | Full regulatory exposure under NIS2. Average cost of a successful phishing attack for a mid-market bank: EUR 50,000-200,000 in incident response, legal, and remediation (industry estimate, not ShieldByte-specific data). |

### Objections and Responses
| Objection | Response | Evidence |
|-----------|----------|----------|
| "We do not have budget for this." | "Understood. Is there budget for NIS2 compliance? Because security awareness is a specific requirement under Article 21. The question is not whether you will spend on this. It is whether you spend now on a planned programme or later on remediation after an audit finding." | Moderate (NIS2 Article 21 does require security awareness measures. The specific audit risk is an assumption.) |
| "We already run phishing tests with GoPhish." | "Good. That shows you recognise the need. Can I ask: what happened after the last test? Did employees who clicked receive targeted training? Do you have trend data showing click rates improving over time? Most teams we talk to run the test but do not have the follow-up loop. The test without the training is measurement without improvement." | Moderate (5 interviewees described this exact gap: testing without follow-up) |
| "We will address this next quarter." | "What changes next quarter? If it is waiting for NIS2 guidance, the directive is already published and the compliance deadline is fixed. If it is budget timing, a 90-day pilot starting now means you have results and data before budget season. Waiting means starting from zero when the deadline arrives." | Moderate (NIS2 timeline is factual. The urgency framing is reasonable but could be stronger with specific local enforcement data.) |
| "Our staff are technical. They do not fall for phishing." | "That is what most security teams believe until they test it. Industry average click rates for first-time simulations are 25-35%, even at technology companies. Can I ask: what was your click rate on the last test? If you have not measured it, this is an assumption, not a fact." | Weak (industry average is cited but not specific to Serbian banks. ShieldByte has no proprietary data yet.) |

### Questions That Create Urgency
1. "Walk me through what happens today when an employee clicks a phishing link. Step by step, from click to resolution. How long does that take, and who is involved?"
2. "How many phishing-related incidents did your team handle in the past 12 months? What did each one cost in staff hours to investigate and remediate?"
3. "When is your next compliance review? What will you present as evidence of your security awareness programme?"
4. "Your NIS2 compliance deadline is fixed. If you start a programme today, you have 90 days of data to show auditors. If you start next quarter, you have 30 days. Which position would you rather be in?"

---

## Evidence Assessment

- **Overall rating:** Assumption-Heavy with Moderate pockets
- **Strongest evidence:** The NIS2 compliance trigger is real and confirmed across 8 interviews. The lack of Serbian language content from global vendors is verifiable. These two anchors give the battlecard a foundation.
- **Biggest gap:** ShieldByte has not yet competed against KnowBe4 in a real deal. Every "where we win" claim and every objection response is based on desk research and assumptions about how competitive conversations will play out. Until the founders have actually lost (or won) a deal against KnowBe4, the battlecard is theory.
- **Competitor knowledge depth:** Moderate for KnowBe4 (based on website research, pricing pages, and G2 reviews). The founders have not spoken to any KnowBe4 customers or seen a KnowBe4 demo. This is a significant gap. The "Do Nothing" battlecard is stronger because it is based on direct conversations with prospects who are currently doing nothing.

## Next Steps

1. Request a KnowBe4 demo. Sign up for their free trial or request a sales demo posing as a buyer. See the product firsthand. Understand their pitch, their onboarding flow, and their actual Serbian language capabilities (or lack thereof). Do not compete against a product you have never seen.
2. After the first pilot bank converts to paid (or does not), document the full sales conversation. What objections came up? Who was involved in the decision? What almost killed the deal? This real data replaces the assumptions in these battlecards.
3. Talk to 2-3 companies that evaluated KnowBe4 but did not buy. Understand why. These conversations will reveal whether ShieldByte's assumed advantages match the actual reasons prospects reject KnowBe4.
4. Build a one-page "NIS2 compliance checklist" document that maps ShieldByte's capabilities to specific NIS2 articles. This becomes a leave-behind in every sales conversation and directly addresses the "Do Nothing" competitor by making the regulatory requirement concrete and unavoidable.
5. Collect and document the actual incident response cost at the two pilot banks. Ask them what their last phishing incident cost to remediate. Real numbers from real banks replace the "EUR 50,000-200,000 industry estimate" with specific, credible data.
