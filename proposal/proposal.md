# Reasoning to Readiness
## Neuro-Symbolic and Causal Architectures for Reliable AI Agents

**Proposal for the AAAI 2027 Spring Symposium Series**

March 22–24, 2027 · Santa Clara University, Santa Clara, California

**Lead contact:** Dr. Kaushik Roy, The University of Alabama · kroy2@ua.edu

**Webpage:** [Symposium website](https://kauroy1994.github.io/AAAI-Symposium-Concept/)

**Proposal prepared November 12, 2026.**

## 1. Motivation, scope, and community

We propose a working symposium on a focused question: **what architectural and empirical evidence should justify moving an AI agent from a demonstration to a bounded, accountable industrial pilot?** Cognitive architectures connect memory, learning, and action [1]; neuro-symbolic methods connect learned representations with explicit knowledge [2]; causal models formalize assumptions about interventions [3]. Language-agent research offers mechanisms for reasoning and acting [4], but evaluation must also address operating cost, reproducibility [5], and the security implications of interacting with untrusted tool outputs [6]. Together, these perspectives connect architectural design to the evidence needed for operational decisions.

The symposium will develop a proposed **deployment evidence contract**: a concise, inspectable record linking intended use, architectural claims, authorized actions, causal assumptions, evaluation conditions, unresolved risks, and human accountability. Teams will challenge this contract against common cases and identify where it fails to support decisions. The contract will make claims comparable, expose limitations, and identify the domain-specific validation still needed.

Four areas define the scope: (i) cognitive architectures and adaptive memory; (ii) knowledge-grounded neuro-symbolic reasoning and verifiable action; (iii) causal and counterfactual decision support; and (iv) industry readiness, including integration, recovery, resource efficiency, and human oversight. Technical questions include separating remembered evidence from generated hypotheses, revising stale knowledge, enforcing action boundaries, testing counterfactual assumptions, and evaluating the cost of stronger reasoning. Speculative ideas, work in progress, and negative results are welcome when their evidential status is explicit.

We propose 50–65 participants, within AAAI's published target of 40–75. Recruitment will connect AI researchers, industrial developers, operations owners, assurance practitioners, and students. The 2.5-day format will support sustained critique and joint artifact development that a sequence of short presentations would not provide.

**Relationship to existing activities.** R2R is a new meeting focused on evidence for bounded deployment. NeSy, an established annual conference, included an industry track in 2026 [8]. R2R complements that broader forum through sustained work on shared cases: participants will jointly specify acceptance criteria, challenge architectural claims, and document tests and unresolved disagreements. The aim is to connect researchers and operational decision-makers around a common evaluation practice.

<!-- PAGEBREAK -->

## 2. Scientific questions and industry-readiness method

**Architecture and memory.** Which combinations of working memory, persistent knowledge, planning, and reflection support inspectable adaptation? What evidence distinguishes reusable abstractions from task-specific shortcuts? Participants will examine state provenance, memory revision, cross-task degradation, and the compute and maintenance costs of reuse. Architectural complexity must be justified against a simpler baseline rather than assumed to improve reliability.

**Grounding and action.** Where should knowledge graphs, ontologies, constraints, and executable models intervene in an agent's workflow? Participants will separate what a model proposes from what an independent component checks or authorizes. Each check must state its assumptions and coverage. Invalid, contradictory, or missing knowledge must be represented in the evaluation plan.

**Causality and uncertainty.** What assumptions permit a prediction, intervention estimate, or counterfactual conclusion? Participants will distinguish causal models from descriptive process graphs and articulate identification limits. Where assumptions or evidence are insufficient, clarification, abstention, or escalation should be evaluated as deliberate behaviors, not automatically counted as failures.

**Operational adoption.** How should system boundaries, organizational responsibility, and economic value influence architecture? We will discuss approval workflows, integration with existing systems, residual risk ownership, and recovery after partial completion. NIST AI RMF 1.0 provides a risk-management reference for this assessment [7].

### Proposed evidence-contract dimensions

| Dimension | Evidence to request and discuss |
| --- | --- |
| Knowledge and data | Source lineage, permissions, versioning, coverage, and missing-evidence behavior. |
| Reasoning and causal validity | Claim-specific tests, explicit assumptions, constraint checks, and abstention. |
| Authority and security | Tool permissions, human approvals, isolation, and adversarial tests. |
| Reliability and recovery | Drift and failure detection, escalation, rollback, and partial-failure recovery. |
| Efficiency and value | Success, latency, compute, cost, and operator effort against credible baselines. |
| Human oversight | Named decision owners, change control, incident response, and user feedback. |

Evidence will be recorded as demonstrated within scope, partial, unsupported, or not applicable with justification. A single composite score will not be used to conceal a critical deficiency. Proposed evaluations should report test populations, repeated trials where relevant, uncertainty, and limitations. Comparisons should match information access and resource budgets across manual or scripted workflows, retrieval-based systems, and agentic alternatives, as appropriate to the case.

**Shared cases and labs.** Lab A will use a synthetic supplier-delay and approval scenario to connect knowledge representation to authorized action. Lab B will introduce stale evidence, contradictory instructions, missing approvals, and tool failures; a second service-operations case will probe transfer. Groups will distinguish constraint violations from interventions and specify recovery behavior. Groups will document the exercises and their evaluation limits. Public, synthetic, or explicitly authorized data will be used; no production access or customer information is required. Paper worksheets and lightweight local examples will permit contribution without paid APIs or specialized hardware.

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

**Interaction design.** The explicitly collaborative blocks total 570 of 840 technical-session minutes (approximately 68%), excluding breaks, lunch, reception, and plenary. Talk blocks include additional discussion. Short contributed presentations will be paired with respondents; mixed research–industry groups will have facilitators and rapporteurs. A common worksheet will connect architectural claims to evidence and record disagreements. Coding is optional; demonstrations will be assessed through the same evidence-based discussion as other contributions.

<!-- PAGEBREAK -->

## 4. Proposed organizing committee and execution

The proposed committee brings together six faculty and industry organizers and two student organizers. All eight have agreed to serve, as confirmed by the lead organizer on November 12, 2026. Roles below describe the proposed division of work.

**Dr. Kaushik Roy - lead organizer and scientific program.** Assistant Professor of Computer Science, The University of Alabama. His work on neuro-symbolic learning and reasoning informs the scientific scope. Proposed responsibilities: program coordination, reviewing, academic recruitment, and AAAI liaison. **Email:** kroy2@ua.edu. [UA profile](https://eng.ua.edu/eng-directory/dr-kaushik-roy/).

**Nigel Glenday - industry problems and operational design.** Founder and CEO, Graphite Atlas. Proposed responsibilities: practitioner outreach, operational problem framing, and the knowledge-to-action clinic. **Email:** nglenday@graphiteatlas.com. [Company](https://www.graphiteatlas.com/); [professional contact](https://github.com/nigelglenday/).

**Raj Krishnan - enterprise integration and adoption.** AI For Services (affiliation supplied by the lead organizer). Proposed responsibilities: service-workflow cases, integration requirements, and business-value evaluation. **Email:** raj@aiforservices.com.

**Dr. Alessandro Oltramari - neuro-symbolic architecture and research translation.** Senior Manager, Bosch Research; President, Carnegie Bosch Institute. Proposed responsibilities: architecture discussions, academic-industry exchange, and the deployment review panel. **Email:** aoltrama@andrew.cmu.edu. [Institute profile](https://carnegiebosch.cmu.edu/team/bios/oltramari-alessandro.html).

**Dr. Shahram Rahimi - scientific leadership and community development.** Professor and Head of Computer Science, The University of Alabama. Proposed responsibilities: cross-disciplinary AI discussion, research recruitment, and academic-industry engagement. **Email:** srahimi1@ua.edu. [UA profile](https://eng.ua.edu/eng-directory/dr-shahram-rahimi/).

**Dr. Subash Neupane - trustworthy AI and applied evaluation.** Assistant Professor, The University of Alabama. His research addresses trustworthy, explainable AI in healthcare and other high-impact applications. Proposed responsibilities: evaluation design and reliability discussions. **Email:** sneupane4@ua.edu. [UA profile](https://eng.ua.edu/eng-directory/dr-subash-neupane/).

**Himanshu Tripathi - student organizer, The University of Alabama.** Proposed responsibilities: student participation and lab coordination. [UA lab profile](https://sites.ua.edu/brains/team/). **Email:** htripathi@crimson.ua.edu.

**Ashraf Abdul-Muumin - student organizer, The University of Alabama (lead-organizer supplied).** Proposed responsibilities: session coordination and community resources. **Email:** aashraf@crimson.ua.edu.

### Recruitment, review, and participation

Recruitment will address neuro-symbolic AI, cognitive systems, knowledge representation, causality, agent evaluation, and industrial operations communities. The proposed committee spans academic research, industrial AI, and operational practice. We will seek a balanced mix of research and operational perspectives, including students and practitioners who do not normally publish conference papers.

After acceptance, proposed formats are long research/position papers and operational cases (up to 4 pages), short papers and demonstrations (up to 2 pages), and poster abstracts and participation statements (up to 1 page). Poster acceptance and presentation selection are separate; some posters may be accepted without a presentation slot. Final deadlines, templates, archival options, and proceedings arrangements will be coordinated with AAAI. At least two non-conflicted reviewers are planned for paper and case submissions. Selection will emphasize relevance, clarity, evidence and limitations, and discussion value; early-stage work should state its assumptions and open questions. Organizers will recuse themselves from conflicts and arrange independent handling where necessary.

All presenters, invited speakers, and panelists must attend in person; all participants, including organizers, must register under AAAI policy. Accessibility requests will be coordinated with AAAI and the venue. Accessible worksheets, structured discussion, and written contributions within in-person sessions will support participation. AAAI's event Code of Conduct will apply.

<!-- PAGEBREAK -->

## 5. Execution, community development, and outcomes

**Community development.** Outreach will connect cognitive systems, knowledge representation, causal reasoning, agent evaluation, and industrial operations communities. Organizers will circulate the draft to prospective participants for comment and use their feedback to refine the cases and scientific questions. Expressions of interest will inform the balance of research and practitioner perspectives.

**Execution and outputs.** The committee will prepare calls for participation and registration, publicize the event beyond AAAI, review participation requests, provide invitee and accepted-author lists for registration, finalize the program, and supply information requested by AAAI's proceedings team. AAAI will handle local arrangements and logistical support under its call. We propose four outputs: a deployment evidence-contract template; a failure-and-recovery taxonomy; a comparative case matrix; and a research roadmap that preserves unresolved disagreements. An organizer-edited synthesis is planned within six weeks after the event, subject to contributor review and consent. Publication and resource-release arrangements will be settled with AAAI and contributors.

**Website and program.** The [symposium website](https://kauroy1994.github.io/AAAI-Symposium-Concept/) presents the agenda, program, committee, and interest contact. The [draft call for papers](https://kauroy1994.github.io/AAAI-Symposium-Concept/cfp.html) details contribution formats, evidence expectations, and review; submissions will open after acceptance. The program covers the full two and a half days using the [AAAI series timetable](https://aaai.org/conference/spring-symposia/aaai-2027-spring-symposium-series/). Invited-speaker slots remain unassigned.

**Continuing work.** Working groups will identify experiments that compare architectural choices under common information and resource budgets. The synthesis will distinguish findings supported by the case exercises from questions requiring larger studies. Participants will be invited to revise the evidence contract and contribute reusable evaluation materials after the meeting.

### Selected references

[1] J. E. Laird, C. Lebiere, and P. S. Rosenbloom. 2017. A Standard Model of the Mind: Toward a Common Computational Framework across Artificial Intelligence, Cognitive Science, Neuroscience, and Robotics. AI Magazine 38(4), 13–26. [doi:10.1609/aimag.v38i4.2744](https://doi.org/10.1609/aimag.v38i4.2744).

[2] A. d'Avila Garcez and L. C. Lamb. 2023. Neurosymbolic AI: the 3rd wave. Artificial Intelligence Review. [doi:10.1007/s10462-023-10448-w](https://doi.org/10.1007/s10462-023-10448-w).

[3] B. Schölkopf et al. 2021. Toward Causal Representation Learning. Proceedings of the IEEE. [doi:10.1109/JPROC.2021.3058954](https://doi.org/10.1109/JPROC.2021.3058954).

[4] S. Yao et al. 2023. ReAct: Synergizing Reasoning and Acting in Language Models. ICLR. [NSF record](https://par.nsf.gov/biblio/10451467-react-synergizing-reasoning-acting-language-models).

[5] S. Kapoor, B. Stroebl, Z. S. Siegel, N. Nadgir, and A. Narayanan. 2024. AI Agents That Matter. arXiv:2407.01502. [Cited preprint](https://arxiv.org/abs/2407.01502).

[6] E. Debenedetti et al. 2024. AgentDojo: A Dynamic Environment to Evaluate Prompt Injection Attacks and Defenses for LLM Agents. NeurIPS, Datasets and Benchmarks. [doi:10.52202/079017-2636](https://doi.org/10.52202/079017-2636).

[7] NIST. 2023. Artificial Intelligence Risk Management Framework (AI RMF 1.0). NIST AI 100-1. [doi:10.6028/NIST.AI.100-1](https://doi.org/10.6028/NIST.AI.100-1).

[8] NeSy 2026. Call for Papers, including Industry Track. [Official call](https://2026.nesyconf.org/call-for-papers/). Sources checked November 12, 2026.
