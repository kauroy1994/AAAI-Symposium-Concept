# Reasoning to Readiness
## Neuro-Symbolic and Causal Architectures for Reliable AI Agents

**Proposal for the AAAI 2027 Spring Symposium Series**

March 22–24, 2027 · Santa Clara University, Santa Clara, California

**Lead contact:** Dr. Kaushik Roy, The University of Alabama · kroy2@ua.edu

**Webpage:** [Symposium website](https://kauroy1994.github.io/AAAI-Symposium-Concept/)

## 1. Motivation, scope, and participants

**How can we tell when an AI agent is ready for use beyond a demonstration?** This symposium will examine how memory, knowledge, rules, and causal models affect an agent's reliability, and how to evaluate those effects in practical settings.

Cognitive architectures connect memory, learning, and action [1]. Neuro-symbolic AI combines learned models with explicit knowledge and reasoning [2], while causal models help describe the effects of interventions [3]. Language agents offer ways to combine reasoning with action [4]. These approaches raise common questions: what does the agent know, which actions may it take, how does it respond when information is incomplete, and when should a person intervene? Studies of agent evaluation [5] and attacks through tool outputs [6] show why accuracy alone is insufficient.

Participants will compare research and case studies, discuss results, and work through two labs. They will develop a checklist covering intended use, permissions, tests, results, cost, remaining risks, and human responsibility. The purpose is to make evaluations easier to compare and identify the further testing needed before a pilot.

The scope covers cognitive architectures and memory; neuro-symbolic reasoning and action; causal reasoning and decision support; and evaluation for practical use. We welcome early work and negative results as well as completed studies. Authors should explain what their results support and what remains uncertain.

We aim for 50–65 participants from AI research, industry, operations, software testing, and related fields, including students. The two-and-a-half-day meeting will combine talks, posters, discussion, and group work.

### Participant interest

The following invited speakers have expressed interest in participating.

| Name | Affiliation | Role |
| --- | --- | --- |
| Nigel Glenday | Graphite Atlas | Invited speaker |
| Raj Krishnan | AI For Services | Invited speaker |

**Relationship to existing meetings.** R2R is a new meeting. NeSy is an established annual conference and included an industry track in 2026 [8]. R2R will focus more narrowly on evaluating agents through shared cases and discussion between researchers and people responsible for their practical use.

<!-- PAGEBREAK -->

## 2. Research questions and labs

**Architecture and memory.** How should memory, learning, planning, and human review work together? We will discuss where stored information comes from, how outdated knowledge is revised, whether skills transfer across tasks, and whether learning a new task harms earlier capabilities. More complex designs should be compared with simpler alternatives.

**Reasoning and action.** How can knowledge graphs, ontologies, rules, and executable checks improve decisions? Studies should identify which component checks or authorizes an action, what its checks cover, and how the system responds to missing or conflicting information.

**Causal reasoning.** What assumptions support a conclusion about the effects of an action? We will discuss causal models, interventions, counterfactual questions, and uncertainty. Evaluations should include situations in which the agent needs more information or human help.

**Practical use.** How well does the agent work with existing systems and procedures? Relevant questions include access permissions, changes in operating conditions, error detection, recovery, cost, and staff effort. NIST AI RMF 1.0 provides a reference for discussing risk [7].

### What an evaluation should report

| Area | Questions and results to report |
| --- | --- |
| Knowledge and data | Sources, versions, permissions, and known gaps. |
| Reasoning | Assumptions, tests, comparisons, results, and limitations. |
| Permissions and security | Access controls, approval checks, and security tests. |
| Reliability and recovery | Error detection, human intervention, and recovery tests. |
| Cost and usefulness | Task success, response time, computing cost, and staff effort. |
| Human responsibility | Review procedures, responsibilities, and incident handling. |

Reports should describe test conditions, sample sizes, findings, uncertainty, and limits of the evaluation. Comparisons should give competing approaches similar information and resources.

**Lab 1: Designing an agent.** Groups will work with a fictional supplier-delay and approval process. They will identify the information and permissions an agent needs, compare possible designs with a simpler approach, and decide how to test them.

**Lab 2: Testing failures and recovery.** Groups will examine outdated information, conflicting instructions, missing approvals, and tool failures. They will specify how the agent should respond and which decisions require human review. A second case from service operations will test whether the same methods work in a different setting.

Paper worksheets and simple local examples will be available. Coding is optional, and participation will not require paid APIs or specialized hardware. Exercises will use fictional, public, or approved material.

<!-- PAGEBREAK -->

## 3. Preliminary program

All times are local to Santa Clara (Pacific Daylight Time, UTC−7).

### Monday, March 22: Architectures and applications

| Time | Session |
| --- | --- |
| 09:00–09:20 | Welcome and introduction to the symposium questions. |
| 09:20–10:00 | Invited talk and discussion: Nigel Glenday (Graphite Atlas). |
| 10:00–10:30 | Application challenges from research and industry. |
| 10:30–11:00 | Coffee break. |
| 11:00–12:30 | Contributed talks on memory, knowledge representation, and planning, followed by discussion. |
| 12:30–14:00 | Lunch. |
| 14:00–15:30 | Lab 1: designing an agent for supplier delays and approval decisions. |
| 15:30–16:00 | Coffee break. |
| 16:00–17:00 | Group reports and discussion of the proposed designs. |
| 18:00–19:00 | AAAI series reception. |

### Tuesday, March 23: Evaluation and failure analysis

| Time | Session |
| --- | --- |
| 09:00–09:40 | Invited talk and discussion: Raj Krishnan (AI For Services). |
| 09:40–10:30 | Case studies: evaluation results and deployment experience. |
| 10:30–11:00 | Coffee break. |
| 11:00–12:30 | Lab 2: testing outdated information, missing approvals, and tool failures. |
| 12:30–14:00 | Lunch. |
| 14:00–15:30 | Panel and audience discussion: when is an agent ready for a pilot? |
| 15:30–16:00 | Coffee break. |
| 16:00–17:00 | Poster session: accepted papers and poster abstracts, with discussion at each poster. |
| 18:00–19:00 | AAAI series plenary. |

### Wednesday, March 24: Open questions and next steps

| Time | Session |
| --- | --- |
| 09:00–10:30 | Lab reports and discussion of the results. |
| 10:30–11:00 | Coffee break. |
| 11:00–12:00 | Discussion of open research questions and possible joint studies. |
| 12:00–12:30 | Closing discussion and next steps. |

The 90-minute contributed-paper session will include short talks and questions. Accepted papers not selected for an oral talk, together with accepted poster abstracts, will be presented in the Tuesday poster session. Authors will be available to discuss their work at their posters. Both labs are open to all participants; coding is optional.

<!-- PAGEBREAK -->

## 4. Organizing committee and participation

All six organizing committee members and both steering organizers have agreed to serve.

**Dr. Kaushik Roy - lead organizer and scientific program.** Assistant Professor of Computer Science, The University of Alabama. His research covers neuro-symbolic learning and reasoning. He will coordinate the program, reviewing, invitations, and contact with AAAI. **Email:** kroy2@ua.edu. [UA profile](https://eng.ua.edu/eng-directory/dr-kaushik-roy/).

**Dr. Shahram Rahimi - research program and invitations.** Professor and Head of Computer Science, The University of Alabama. He will help recruit researchers and organize discussions across AI research and industry. **Email:** srahimi1@ua.edu. [UA profile](https://eng.ua.edu/eng-directory/dr-shahram-rahimi/).

**Dr. Subash Neupane - evaluation and applications.** Assistant Professor, The University of Alabama. His research addresses trustworthy, explainable AI, including healthcare applications. He will contribute to evaluation design and discussion of reliability. **Email:** sneupane4@ua.edu. [UA profile](https://eng.ua.edu/eng-directory/dr-subash-neupane/).

**Dr. Noorbakhsh Amiri Golilarz - cognitive systems and lab design.** Assistant Professor of Computer Science, The University of Alabama, and Director of the BRAINS Lab. His research includes AI, computer vision, robotics, and cognitive neuroscience. He will contribute to lab design and discussions of cognitive systems and applications. **Email:** namirigolilarz@ua.edu. [UA profile](https://eng.ua.edu/eng-directory/dr-noorbakhsh-amiri-golilarz/); [BRAINS Lab](https://sites.ua.edu/brains/team/).

**Himanshu Tripathi - student organizer, The University of Alabama.** He will help with student participation and group exercises. **Email:** htripathi@crimson.ua.edu. [UA lab profile](https://sites.ua.edu/brains/team/).

**Ashraf Abdul-Muumin - student organizer, The University of Alabama.** He will help coordinate sessions and prepare materials. **Email:** aashraf@crimson.ua.edu.

### Steering Organizers

The steering organizers will guide the symposium's scope and research program.

**Dr. Alessandro Oltramari.** Senior Manager, Bosch Research; President, Carnegie Bosch Institute. His research connects knowledge representation, learning, and neuro-symbolic AI. **Email:** aoltrama@andrew.cmu.edu. [Institute profile](https://carnegiebosch.cmu.edu/team/bios/oltramari-alessandro.html).

**Prof. Amit Sheth.** Professor of Computer Science and Engineering, University of South Carolina, and founding director of its Artificial Intelligence Institute. His research includes knowledge graphs, natural language processing, and AI systems that combine knowledge with learned models. **Email:** amit@sc.edu. [Faculty profile](https://sc.edu/study/colleges_schools/engineering_and_computing/faculty-staff/amitsheth.php).

### Submissions, review, and presentation

After acceptance by AAAI, we plan to invite long papers and case studies (up to 4 pages), short papers and demonstrations (up to 2 pages), and poster abstracts and participation statements (up to 1 page). At least two reviewers without conflicts will assess each paper and case study. Reviews will consider relevance, clarity, the methods and results appropriate to the submission, and its value for discussion.

A limited number of accepted papers will receive an oral slot in the 90-minute contributed-paper session. Other accepted papers and accepted poster abstracts will be presented in the Tuesday poster session, March 23, 16:00–17:00. Authors will be available at their posters. The same review criteria apply to oral and poster papers.

Final deadlines, formatting, and publication arrangements will be coordinated with AAAI. Presentations, including posters, will be in person, and all participants must register. Accessibility requests will be discussed with AAAI and the venue. AAAI's event Code of Conduct applies.

<!-- PAGEBREAK -->

## 5. Invited speakers and meeting plans

**Nigel Glenday - Monday, March 22, 09:20–10:00.** Nigel Glenday is the founder and CEO of Graphite Atlas, which maps business processes and develops automation and AI systems. He previously held CFO and COO roles in asset management. His work connects business operations with the practical use of AI. [Company profile](https://www.graphiteatlas.com/).

**Raj Krishnan - Tuesday, March 23, 09:00–09:40.** Raj Krishnan is the founder and CEO of AI For Services, a company developing AI applications for business processes. Its work includes automating requests for proposals and customer-support workflows, and connecting AI applications with existing enterprise systems. [Company website](https://aiforservices.com/).

Talk titles will be announced.

**Invitations and participation.** The organizers will invite researchers and practitioners working on cognitive systems, knowledge representation, causal reasoning, and agent evaluation. We will also seek participation from operations teams, students, and practitioners who do not regularly submit research papers. We will circulate the draft to prospective participants for comment and use their suggestions to refine the questions and exercises.

**Organizing responsibilities.** The committee will prepare calls for participation and registration, publicize the event, review submissions and participation requests, provide accepted-author and invitee lists, finalize the program, and supply information needed for proceedings. AAAI will provide logistical support and local arrangements.

**Materials and follow-up.** We plan to prepare an evaluation checklist, examples of failures and recovery methods, a comparison of the cases discussed, and a short account of open research questions. The organizers aim to circulate a summary within six weeks of the meeting for contributor review. Publication and release of materials will be agreed with AAAI and the contributors.

**Further research.** Participants will discuss experiments that compare different designs using similar information and resources. The meeting summary will distinguish findings from the exercises from questions that need larger studies. Participants will be invited to contribute further examples and test materials.

### Selected references

[1] J. E. Laird, C. Lebiere, and P. S. Rosenbloom. 2017. A Standard Model of the Mind: Toward a Common Computational Framework across Artificial Intelligence, Cognitive Science, Neuroscience, and Robotics. AI Magazine 38(4), 13–26. [doi:10.1609/aimag.v38i4.2744](https://doi.org/10.1609/aimag.v38i4.2744).

[2] A. d'Avila Garcez and L. C. Lamb. 2023. Neurosymbolic AI: the 3rd wave. Artificial Intelligence Review. [doi:10.1007/s10462-023-10448-w](https://doi.org/10.1007/s10462-023-10448-w).

[3] B. Schölkopf et al. 2021. Toward Causal Representation Learning. Proceedings of the IEEE. [doi:10.1109/JPROC.2021.3058954](https://doi.org/10.1109/JPROC.2021.3058954).

[4] S. Yao et al. 2023. ReAct: Synergizing Reasoning and Acting in Language Models. ICLR. [NSF record](https://par.nsf.gov/biblio/10451467-react-synergizing-reasoning-acting-language-models).

[5] S. Kapoor, B. Stroebl, Z. S. Siegel, N. Nadgir, and A. Narayanan. 2024. AI Agents That Matter. arXiv:2407.01502. [Preprint](https://arxiv.org/abs/2407.01502).

[6] E. Debenedetti et al. 2024. AgentDojo: A Dynamic Environment to Evaluate Prompt Injection Attacks and Defenses for LLM Agents. NeurIPS, Datasets and Benchmarks. [doi:10.52202/079017-2636](https://doi.org/10.52202/079017-2636).

[7] NIST. 2023. Artificial Intelligence Risk Management Framework (AI RMF 1.0). NIST AI 100-1. [doi:10.6028/NIST.AI.100-1](https://doi.org/10.6028/NIST.AI.100-1).

[8] NeSy 2026. Call for Papers, including Industry Track. [Official call](https://2026.nesyconf.org/call-for-papers/).
