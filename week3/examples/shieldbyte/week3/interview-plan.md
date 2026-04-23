Startup: ShieldByte
Date: 2026-04-23
Exercise: Interview Plan

---

## Target Segment

Head of Security (or Head of Information Security, Head of IT Security, Security Lead) at a 200-500 person regulated European fintech (DACH, CEE, or UK) that has hired at least one SOC analyst in the last 12 months.

---

## Consent Script

Use this verbatim at the start of every interview, before any substantive questions:

> "Thanks for taking the time to participate in our study. Just so you know, the information shared will only be used for internal research purposes. With that, do you mind if I record this session?"

If they decline recording, take notes manually. Do not push back. A declined recording is not a failed interview.

---

## Interview Script

Length guidance: 30-45 minutes. Book 45-minute slots and end early if natural. Do not rush to fit questions in.

Each question is tagged with [Hx] for the hypothesis tested (from hypotheses.md) and [signal] for the Five Signal it elicits.

### Intro (3-4 questions)

1. "What's your job title, and how long have you been in this role?"
   [context | context]
   *Note: establishes seniority, tenure, and how much of the problem they own.*

2. "What's your background before this role?"
   [context | context]
   *Note: surfaces domain credibility and prior tool exposure.*

3. "How big is your security team, and how is it structured?"
   [H2 | concrete behaviour]
   *Note: reveals whether there is a CISO above them, and whether analysts report to them directly.*

4. "Walk me through what a typical week looks like for you."
   [H1 | time and money spent]
   *Note: lets them volunteer what occupies most of their attention before you direct the conversation.*

---

### Industry (2-3 questions)

5. "What are you hearing about phishing threats in your industry right now? Where did you hear it?"
   [signal: awareness level]
   *Note: surfaces market maturity and where they get information. Useful for channel decisions.*

6. "How do the threat patterns you're seeing now compare to 12-18 months ago?"
   [signal: recency and frequency]
   *Note: reveals whether the problem is getting worse (urgency signal) or stable (lower urgency).*

7. "What's the biggest security operations challenge across fintechs your size right now, from your perspective?"
   [signal: problem-area match]
   *Note: open industry question. Do not steer. Let them name the problem category unprompted.*

---

### Business (8-10 questions)

8. "When was the last phishing incident your team triaged? Walk me through exactly what happened."
   [H1 | concrete behaviour]
   *Note: most important question in the script. Step-by-step account of a real incident reveals triage time, tools used, and who was involved. Push for specifics: "Who handled it? What tools did they use? How long did each step take?"*

9. "Show me how you handle these today. What tools, what process, who does what?"
   [H1 | concrete behaviour]
   *Note: if they cannot describe a recent incident, use this as an alternative. Surfaces the current workflow before you describe any solution.*

10. "How many phishing alerts does your team triage per week, roughly?"
    [H1 | recency and frequency]
    *Note: volume multiplied by time per triage gives you the total analyst hours consumed. This is the commercial baseline.*

11. "What's the false-positive rate on your current phishing tooling?"
    [H4 | concrete behaviour]
    *Note: if they know the number, it is a real operational concern. If they do not track it, ask "how do you know when an alert is a false positive?" to surface the process.*

12. "What did you spend on security tooling in the last 12 months? Where did it go?"
    [H3 | time and money spent]
    *Note: do not ask "would you pay X." Ask what they have already paid, and on what. This surfaces the existing budget envelope without triggering a negotiation mindset.*

13. "Who signs off the security tool budget at your firm?"
    [H2 | concrete behaviour]
    *Note: direct question about signing authority. Ask it plainly. Most people will answer it. If they hesitate, follow up with "is there a threshold below which you can sign off independently?"*

14. "Have you bought a new security tool in the last 12 months? Walk me through that process."
    [H2 + H5 | recency and frequency]
    *Note: surfaces the full procurement journey: who initiated it, who approved it, how long it took. If they have not bought anything recently, ask "what was the last security tool purchase you went through?"*

15. "Is automated phishing triage something you have actively looked at, or is it not on your radar yet?"
    [signal: awareness level]
    *Note: market maturity signal. Do not be disappointed by "not on the radar." That is useful data about where the category sits.*

16. "What's the last tool your team adopted that actually stuck? Why that one?"
    [H4 | concrete behaviour]
    *Note: surfaces what makes a tool pass the adoption test. Look for patterns: ease of integration, support quality, measurable outcome, champion buy-in.*

17. "What's the last tool you tried that got kicked out? Why?"
    [H4 | concrete behaviour]
    *Note: switching criteria from real experience. The reason a tool got removed reveals what the current tool must avoid. Do not prompt with "was it cost? performance?" Let them tell you.*

---

### Personal (5-6 questions)

18. "What's taking up most of your team's time this quarter?"
    [H1 | time and money spent]
    *Note: if phishing triage comes up unprompted, that is a strong problem-area match signal. If it does not come up at all, probe: "Where does phishing-related work sit in that picture?"*

19. "How many analysts do you have, and how much of their time is on phishing specifically?"
    [H1 | time and money spent]
    *Note: push for a rough percentage or hours per week. "I'm not sure" is acceptable. "Maybe 20-30% of their week" is a data point you can work with.*

20. "If you could change one thing about your current phishing workflow, what would it be?"
    [signal: awareness level]
    *Note: open invitation to name the pain in their own words. The answer tells you what framing resonates. Do not suggest options.*

21. "When did your team last go through a compliance audit related to security tooling? What was the worst part?"
    [H5 | recency and frequency]
    *Note: surfaces real compliance friction. Onboarding speed assumption lives here. Push for specifics: "How long did vendor approval take? Was there a DPIA? Who ran it?"*

22. "What's the typical timeline from picking a new tool to full deployment for your team?"
    [H5 | concrete behaviour]
    *Note: direct question about onboarding speed. Cross-reference with their actual procurement story from Q14. Consistency is a credibility signal.*

23. "What data or metrics does your team track about phishing response? What do you share upward?"
    [H1 | concrete behaviour]
    *Note: reveals whether triage time is already measured. If they track MTTR (Mean Time to Respond), ask what the current number is. If they do not track it, note that as a signal about problem severity.*

---

### Outro (2-3 questions)

24. "If you had a magic wand for your SOC on Monday morning, what one thing would you fix?"
    [signal: awareness level]
    *Note: the most unguarded question in the script. Ask it last, after 30-40 minutes of conversation. The answer at this point is less filtered than anything they said earlier.*

25. "Is there anyone else in your network I should be talking to about this? Someone who deals with this problem differently, or at a different type of firm?"
    [signal: referral]
    *Note: referral ask at the end of every interview. A warm intro from a peer is the fastest way to the next interview. Ask for a specific name, not a vague "yes, probably."*

26. "What's the one question I should have asked you that I didn't?"
    [signal: awareness level]
    *Note: the closing meta-question. Surfaces blind spots in the script. Update the script before interview 2 if the same gap appears twice.*

---

## Red-Flag Question Patterns to Avoid

These question forms are banned from the script. They generate politeness bias, not evidence.

| Banned pattern | Why it fails | Rewrite |
|---|---|---|
| "Would you use a tool like this?" | Invites hypothetical approval. People say yes to be polite. | "How do you handle this today?" |
| "Don't you find phishing triage really time-consuming?" | Leading question. You have answered it for them. | "Walk me through the last phishing triage your team handled." |
| "How important is it to reduce false positives?" | Importance question gets an importance answer. Useless. | "What does your team do when an alert turns out to be a false positive? Walk me through it." |
| "Would you pay for this if it existed?" | Pure hypothetical. Means nothing. | "What did you spend on security tooling in the last 12 months? Where did it go?" |
| "Is phishing a big problem at your firm?" | Yes/no question, almost always answered yes. | "When was the last phishing incident your team triaged? Walk me through exactly what happened." |

---

## Cadence Plan

| Week | Target | Activity |
|---|---|---|
| Week 1 | 5 interviews | Run interviews 1-5. Update script after interview 1. |
| Week 2 | 5 interviews | Run interviews 6-10. Note emerging patterns. |
| After interview 10 | Affinity mapping session | Cluster insights by theme. Decide whether to continue with the same segment or adjust. |
| Week 3 | 5 interviews | Run interviews 11-15, adjusted script. |
| Week 4 | 5 interviews | Run interviews 16-20. Begin synthesis. |
| Before Week 4 workshop | 20 interviews completed | Arrive with full synthesis, updated hypotheses, and at least 3 named buyers. |

**Script review points:** After interview 1 (catch misunderstood questions), after interview 5 (first round synthesis, remove questions not producing insight), after interview 10 (major affinity map, possible script rebuild).

**Interview target total:** 20 before Week 4. Minimum 10 before drawing conclusions.

---

## Post-Interview Write-Up Template

Complete within 30 minutes of ending the interview. Do not batch. Memories merge fast.

---

**Interview record**

- Date:
- Interviewee title:
- Company size and type:
- Channel (how you got the meeting):
- Duration:
- Was it recorded? Y / N

**Main impressions (2-3 sentences)**
What was the overall signal from this conversation? Was the person inside the target segment? Did they fit the ICP or were they adjacent?

**Strongest evidence from this interview**
The single most concrete, specific thing this person said. Quote if possible, with hypothesis linked. Example: "She said their team spends about three hours per alert on anything that comes in from the email gateway [H1. If confirmed, strong signal]."

**Did the hypothesis change?**
For each of H1-H5, note whether this interview strengthened, weakened, or did not touch the hypothesis.

| Hypothesis | Direction | Key quote or observation |
|---|---|---|
| H1: triage time | stronger / weaker / no data | |
| H2: buyer title | stronger / weaker / no data | |
| H3: price point | stronger / weaker / no data | |
| H4: switching behaviour | stronger / weaker / no data | |
| H5: onboarding speed | stronger / weaker / no data | |

**Biggest surprise**
One thing you did not expect. This is the most valuable part of the write-up. Surprises are where the real learning lives.

**Script gaps**
Were there questions you wished you had asked? Questions that were misunderstood? Note them here and update the script before the next interview.

**Referral**
Did they offer to connect you with anyone? Name and how to follow up:

**Next action from this interview (one specific thing)**

---

## Evidence Assessment

| Claim | Source | Rating |
|---|---|---|
| Script questions cover all five signals | Verified by tagging each question | Strong (structural) |
| Target segment is specific enough for consistent targeting | ICP defined with title, size, region, trigger | Moderate |
| Cadence plan is realistic for a team at this stage | Based on methodology guidance, untested in this market | Assumption |
| 20 interviews will produce sufficient signal on H1-H5 | Industry standard guidance, not calibrated to this segment | Weak |

**Overall rating: Assumption-Heavy at this stage.** The script is well-structured and the questions are behavioural. But this document has not been tested yet. The evidence rating upgrades after interview 1.

---

## Next Steps

1. Send 10 outreach messages using the contact list before Friday. The script is ready. Do not wait for the perfect ICP. Start with the best targets you have now.

2. Run interview 1 this week, ideally with a warm intro target. Debrief for 30 minutes after and update the script before interview 2.

3. After interview 3, review H1 together as a team. If triage time is consistently under 60 minutes across all three conversations, stop and revisit the problem statement before continuing.

4. Book a team session for affinity mapping after interview 10. Block 3 hours. Do not skip this step. The patterns will not be visible until you put the data side by side.
