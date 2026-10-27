# Reasoning to Readiness
## Neuro-Symbolic and Causal Architectures for Reliable AI Agents

**Proposal for the AAAI 2027 Spring Symposium Series**

March 22–24, 2027 · Santa Clara University, Santa Clara, California

**Lead contact:** Dr. Kaushik Roy, The University of Alabama · kroy2@ua.edu

**Webpage:** [GitHub-hosted symposium page](https://github.com/kauroy1994/AAAI-Symposium-Concept)

**Organizer-review draft, October 27, 2026.** The proposal is not ready to submit until the organizer confirmations and verified contact details, and the participant-interest list described on page 5 have been completed. No symposium acceptance or speaker commitment is asserted.

## 1. Motivation, scope, and community

We propose a working symposium on a focused question: **what architectural and empirical evidence should justify moving an AI agent from a demonstration to a bounded, accountable industrial pilot?** Cognitive architectures connect memory, learning, and action [1]; neuro-symbolic methods connect learned representations with explicit knowledge [2]; causal models formalize assumptions about interventions [3]. Language-agent research offers mechanisms for reasoning and acting [4], but evaluation must also address operating cost, reproducibility [5], and the security implications of interacting with untrusted tool outputs [6]. These perspectives motivate a joint scientific and operational discussion, not a claim that any particular architecture is deployment-ready.

The symposium will develop a proposed **deployment evidence contract**: a concise, inspectable record linking intended use, architectural claims, authorized actions, causal assumptions, evaluation conditions, unresolved risks, and human accountability. Teams will challenge this contract against common cases and identify where it fails to support decisions. Its role is to make claims comparable and limitations visible; it is neither a certification scheme nor a substitute for domain-specific validation.

Four areas define the scope: (i) cognitive architectures and adaptive memory; (ii) knowledge-grounded neuro-symbolic reasoning and verifiable action; (iii) causal and counterfactual decision support; and (iv) industry readiness, including integration, recovery, resource efficiency, and human oversight. Technical questions include separating remembered evidence from generated hypotheses, revising stale knowledge, enforcing action boundaries, testing counterfactual assumptions, and evaluating the cost of stronger reasoning. Speculative ideas, work in progress, and negative results are welcome when their evidential status is explicit.

We propose 50–65 participants, within AAAI's published target of 40–75. Recruitment will connect AI researchers, industrial developers, operations owners, assurance practitioners, and students. These are planning targets, not confirmed attendees. The 2.5-day format will support sustained critique and joint artifact development that a sequence of short presentations would not provide.

**Relationship to existing activities.** This is proposed as a new, focused meeting, not a continuation of an established series. Neuro-symbolic AI already has an annual conference, and NeSy 2026 included an industry track [8]. We therefore do not claim novelty for industrial neuro-symbolic AI in general. Our narrower contribution is a working community around a shared evidence contract for bounded deployment, stress-tested across academic and operational perspectives. The case-driven synthesis, explicit disagreements, and jointly specified tests distinguish the intended activity from a broad topical workshop.

<!-- PAGEBREAK -->

## 2. Scientific questions and industry-readiness method

**Architecture and memory.** Which combinations of working memory, persistent knowledge, planning, and reflection support inspectable adaptation? What evidence distinguishes reusable abstractions from task-specific shortcuts? Participants will examine state provenance, memory revision, cross-task degradation, and the compute and maintenance costs of reuse. Architectural complexity must be justified against a simpler baseline rather than assumed to improve reliability.

**Grounding and action.** Where should knowledge graphs, ontologies, constraints, and executable models intervene in an agent's workflow? Participants will separate what a model proposes from what an independent component checks or authorizes. A check provides evidence only within its assumptions and coverage; a symbolic component is not a blanket guarantee of correctness. Invalid, contradictory, or missing knowledge must be represented in the evaluation plan.

**Causality and uncertainty.** What assumptions permit a prediction, intervention estimate, or counterfactual conclusion? Participants will distinguish causal models from descriptive process graphs and articulate identification limits. Where assumptions or evidence are insufficient, clarification, abstention, or escalation should be evaluated as deliberate behaviors, not automatically counted as failures.

**Operational adoption.** How should system boundaries, organizational responsibility, and economic value influence architecture? We will discuss approval workflows, integration with existing systems, residual risk ownership, and recovery after partial completion. The proposed assessment draws on the documented NIST AI RMF 1.0 as a risk-management reference [7], without implying endorsement, legal compliance, or certification.

### Proposed evidence-contract dimensions

| Dimension | Evidence to request and discuss |
| --- | --- |
| Knowledge and data | Source lineage, permissions, versioning, coverage, and missing-evidence behavior. |
| Reasoning and causal validity | Claim-specific tests, explicit assumptions, constraint checks, and abstention. |
| Authority and security | Tool permissions, human approvals, isolation, and adversarial tests. |
| Reliability and recovery | Drift and failure detection, escalation, rollback, and partial-failure recovery. |
| Efficiency and value | Success, latency, compute, cost, and operator effort against credible baselines. |
| Human oversight | Named decision owners, change control, incident response, and user feedback. |

Evidence will be recorded as demonstrated within scope, partial, unsupported, or not applicable with justification. A single composite score will not be used to conceal a critical deficiency. Proposed evaluations should report test populations, repeated trials where relevant, uncertainty, and limitations. Comparisons should match information access and resource budgets across manual or scripted workflows, retrieval-based systems, and agentic alternatives, as appropriate to the case. No performance improvement or return-on-investment figure is asserted in this proposal.

**Shared cases and labs.** Lab A will use a synthetic supplier-delay and approval scenario to connect knowledge representation to authorized action. Lab B will introduce stale evidence, contradictory instructions, missing approvals, and tool failures; a second service-operations case will probe transfer. Groups will distinguish constraint violations from interventions and specify recovery behavior. These are planned exercises, not an existing validated benchmark. Public, synthetic, or explicitly authorized data will be used; no production access or customer information is required. Paper worksheets and lightweight local examples will permit contribution without paid APIs or specialized hardware.

<!-- PAGEBREAK -->

## 3. Preliminary full program

All times are local to Santa Clara (Pacific Daylight Time, UTC−7). Session blocks follow AAAI's published general timetable. Activities are proposed; invited speakers and panelists are not confirmed. Series reception and plenary are AAAI activities, not additional R2R sessions.

### Monday, March 22: architectures meet operational requirements

| Time | Activity and intended outcome |
| --- | --- |
| 09:00–09:20 | Welcome; agree terminology, intended-use boundaries, and the shared case. |
| 09:20–10:00 | Invited research perspective and discussion; speaker to be confirmed. |
| 10:00–10:30 | Research–industry problem statements; surface operational questions. |
| 10:30–11:00 | AAAI break. |
| 11:00–12:30 | Contributed research and position talks with structured discussion. |
| 12:30–14:00 | Lunch break. |
| 14:00–15:30 | Lab A: knowledge-to-action clinic; draft evidence contracts. |
| 15:30–16:00 | AAAI break. |
| 16:00–17:00 | Cross-group critique; revise assumptions and test plans. |
| 18:00–19:00 | AAAI series reception. |

### Tuesday, March 23: stress-test the path to deployment

| Time | Activity and intended outcome |
| --- | --- |
| 09:00–09:40 | Invited industry perspective and discussion; speaker to be confirmed. |
| 09:40–10:30 | Evidence-centered case reports, limitations, and negative results. |
| 10:30–11:00 | AAAI break. |
| 11:00–12:30 | Lab B: failure, intervention, and recovery; specify stress tests. |
| 12:30–14:00 | Lunch break. |
| 14:00–15:30 | Deployment review panel and open challenge of case evidence. |
| 15:30–16:00 | AAAI break. |
| 16:00–17:00 | Working groups on evaluation, governance, and cross-domain transfer. |
| 18:00–19:00 | AAAI series plenary. |

### Wednesday, March 24: consolidate a research agenda

| Time | Activity and intended outcome |
| --- | --- |
| 09:00–10:30 | Cross-domain synthesis and artifact review; revise the contract. |
| 10:30–11:00 | AAAI break. |
| 11:00–12:00 | Prioritize research questions, experiments, and resource needs. |
| 12:00–12:30 | Community review, unresolved issues, and closing. |

**Interaction design.** The explicitly collaborative blocks total 570 of 840 technical-session minutes (approximately 68%), excluding breaks, lunch, reception, and plenary. Talk blocks include additional discussion. Short contributed presentations will be paired with respondents; mixed research–industry groups will have facilitators and rapporteurs. A common worksheet will connect each architectural claim to evidence and record dissent rather than force artificial consensus. Coding is optional. No commercial demonstration will receive a protected sales slot.

<!-- PAGEBREAK -->

## 4. Proposed organizing committee and execution

Four main organizers and two UA student organizers are proposed across academic, industrial research, and entrepreneurial settings. Responsibilities below are assignments for agreement, not representations that consent has already been obtained. Institutional affiliations do not imply sponsorship. Public professional contact details are used where verified.

**Dr. Kaushik Roy — lead organizer and scientific program.** Assistant Professor of Computer Science, The University of Alabama. UA lists neuro-symbolic AI, knowledge-based learning and reasoning, AI systems, and AI for social good among his research areas. He will coordinate scientific scope, reviewing, academic recruitment, and AAAI liaison. **Email:** kroy2@ua.edu. [UA profile](https://eng.ua.edu/eng-directory/dr-kaushik-roy/); [research areas](https://cs.ua.edu/faculty-staff/our-new-fall-2025-faculty/).

**Nigel Glenday — industry problems and operational design.** Founder and CEO, Graphite Atlas, as identified on the company website. His public professional profile describes knowledge-graph-based maps of business operations. He will lead operational problem framing, practitioner outreach, and the knowledge-to-action clinic. **Email:** nglenday@graphiteatlas.com, publicly listed on his professional GitHub profile. [Company](https://www.graphiteatlas.com/); [public profile](https://github.com/nigelglenday/).

**Raj Krishnan — enterprise integration and adoption.** Founder and CEO, AI For Services, as supplied by the lead organizer. Independent verification of this exact title and affiliation, a verified organizer email, and an approved biography remain outstanding. The proposed role covers service-workflow cases, integration constraints, adoption barriers, and business-value evaluation. **Email:** to be provided and verified before submission; interim coordination through kroy2@ua.edu. [Company profile](https://www.linkedin.com/company/aiforservices). No quantified deployment or client claim is made.

**Dr. Alessandro Oltramari — neuro-symbolic architecture and research translation.** Senior Manager at Bosch Research and President of the Carnegie Bosch Institute, verified by Bosch and the Institute. His research connects knowledge systems, learning, and reasoning. He will coordinate architecture discussions, academic–industry translation, and the deployment review panel. **Email:** aoltrama@andrew.cmu.edu. [Institute profile](https://carnegiebosch.cmu.edu/team/bios/oltramari-alessandro.html); [Bosch profile](https://www.bosch.com/research/about-bosch-research/our-research-experts/alessandro-oltramari/).

### Student organizers

**Himanshu Tripathi — student organizer, The University of Alabama.**

**Ashraf Abdul-Muumin — student organizer, The University of Alabama.**

Professional email addresses and agreements to serve will be recorded before submission; interim coordination is through kroy2@ua.edu.

### Recruitment, review, and participation

Recruitment will address neuro-symbolic AI, cognitive systems, knowledge representation, causality, agent evaluation, and industrial operations communities. Each organizer will contribute relevant networks, subject to agreement. We will seek a balanced mix of research and operational perspectives, including students and practitioners who do not normally publish conference papers. Target attendance is not evidence of interest; the required contacted-and-interested list is addressed separately on page 5.

After acceptance, proposed contribution formats are 2–4-page research/position papers and case reports, 2-page demonstrations, and 1-page participation statements. These are proposed local formats, not AAAI requirements. Final deadlines, templates, archival options, and proceedings arrangements will be coordinated with AAAI. At least two non-conflicted reviewers are planned for paper and case submissions. Selection will emphasize relevance, clarity, evidence and limitations, and discussion value; speculative work will be assessed as speculative work. Organizers will recuse themselves from conflicts and arrange independent handling where necessary.

All presenters, invited speakers, and panelists must attend in person; all participants, including organizers, must register under AAAI policy. We will not promise remote presentations, fee waivers, travel support, or a livestream. Accessibility requests will be coordinated with AAAI and the venue. Accessible worksheets, structured discussion, and written contributions within in-person sessions will support participation. AAAI's event Code of Conduct will apply.

<!-- PAGEBREAK -->

## 5. Participant-interest evidence, responsibilities, and outcomes

**Participant-interest evidence — required before submission.** No documented list of contacted participants who expressed interest was supplied for this draft. An outreach plan is not a substitute for that list. Before submission, this paragraph must be replaced with actual names and affiliations of interested respondents, with dates and private evidence references retained by the lead organizer. Respondents need not commit to attend. Consent to include a name in the AAAI-reviewed proposal must be distinguished from consent to public listing. Public repository files must not contain private correspondence or contact registers.

**Organizer agreement — required before submission.** Each named organizer must explicitly agree to serve, approve the final role and affiliation, and review the proposal. Raj Krishnan's verified email and title, and verified professional emails for both student organizers, must be supplied. These are substantive completion requirements; the current draft does not assert that they have been met. No keynote, panelist, sponsor, or accepted participant is represented as confirmed.

**Execution and outputs.** The committee will prepare calls for participation and registration, publicize the event beyond AAAI, review participation requests, provide invitee and accepted-author lists for registration, finalize the program, and supply information requested by AAAI's proceedings team. AAAI will handle local arrangements and logistical support under its call. We propose four outputs: a deployment evidence-contract template; a failure-and-recovery taxonomy; a comparative case matrix; and a research roadmap that preserves unresolved disagreements. An organizer-edited synthesis is planned within six weeks after the event, subject to contributor review and consent. No special issue, archival venue, dataset release, or external partnership is promised.

**Submission and status.** The official proposal deadline is November 17, 2026; decisions are scheduled for December 8, 2026. Submit through the EasyChair link on the [official AAAI call](https://aaai.org/conference/spring-symposia/aaai-2027-spring-symposium-series-call-for-proposal/), not a guessed portal address. The call requests 2–5 pages; this draft includes references within five pages. Its website is the [public repository README](https://github.com/kauroy1994/AAAI-Symposium-Concept). The GitHub Pages presentation may be activated from repository settings. The program follows the [official series timetable](https://aaai.org/conference/spring-symposia/aaai-2027-spring-symposium-series/). The call does not specify a submission timezone or require the main-conference paper template; any additional portal instructions must be checked at submission.

### Selected references

[1] J. E. Laird, C. Lebiere, and P. S. Rosenbloom. 2017. A Standard Model of the Mind: Toward a Common Computational Framework across Artificial Intelligence, Cognitive Science, Neuroscience, and Robotics. AI Magazine 38(4), 13–26. [doi:10.1609/aimag.v38i4.2744](https://doi.org/10.1609/aimag.v38i4.2744).

[2] A. d'Avila Garcez and L. C. Lamb. 2023. Neurosymbolic AI: the 3rd wave. Artificial Intelligence Review. [doi:10.1007/s10462-023-10448-w](https://doi.org/10.1007/s10462-023-10448-w).

[3] B. Schölkopf et al. 2021. Toward Causal Representation Learning. Proceedings of the IEEE. [doi:10.1109/JPROC.2021.3058954](https://doi.org/10.1109/JPROC.2021.3058954).

[4] S. Yao et al. 2023. ReAct: Synergizing Reasoning and Acting in Language Models. ICLR. [NSF record](https://par.nsf.gov/biblio/10451467-react-synergizing-reasoning-acting-language-models).

[5] S. Kapoor, B. Stroebl, Z. S. Siegel, N. Nadgir, and A. Narayanan. 2024. AI Agents That Matter. arXiv:2407.01502. [Cited preprint](https://arxiv.org/abs/2407.01502).

[6] E. Debenedetti et al. 2024. AgentDojo: A Dynamic Environment to Evaluate Prompt Injection Attacks and Defenses for LLM Agents. NeurIPS, Datasets and Benchmarks. [doi:10.52202/079017-2636](https://doi.org/10.52202/079017-2636).

[7] NIST. 2023. Artificial Intelligence Risk Management Framework (AI RMF 1.0). NIST AI 100-1. [doi:10.6028/NIST.AI.100-1](https://doi.org/10.6028/NIST.AI.100-1). Specific version cited; not a claim about the latest revision.

[8] NeSy 2026. Call for Papers, including Industry Track. [Official call](https://2026.nesyconf.org/call-for-papers/). Event and affiliation sources checked October 27, 2026.
