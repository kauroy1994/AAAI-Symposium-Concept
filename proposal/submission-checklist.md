# Submission checklist

Reviewed November 12, 2026 against the [official AAAI 2027 Spring Symposium call](https://aaai.org/conference/spring-symposia/aaai-2027-spring-symposium-series-call-for-proposal/).

**Status: files prepared; participant-interest list still required.** This package has not been submitted to EasyChair.

## Prepared

- [x] Title, scope, research questions, and format.
- [x] Full preliminary program for March 22–24, 2027 at Santa Clara University.
- [x] Six organizers in the website and proposal: Kaushik Roy, Alessandro Oltramari, Shahram Rahimi, Subash Neupane, Himanshu Tripathi, and Ashraf Abdul-Muumin.
- [x] Email addresses for all six organizers. Himanshu's and Ashraf's addresses were supplied by the lead organizer; the other four have public institutional sources.
- [x] The lead organizer has confirmed agreement to serve for the six current committee members.
- [x] Nigel Glenday is the invited speaker on Monday, March 22, 09:20–10:00; Raj Krishnan is the invited speaker on Tuesday, March 23, 09:00–09:40. Both are listed in Speakers, not Organizers. Talk titles are not yet supplied.
- [x] Lab 1: Monday, March 22, 14:00–15:30. Lab 2: Tuesday, March 23, 11:00–12:30.
- [x] Dedicated poster session: Tuesday, March 23, 16:00–17:00. Accepted papers without an oral slot and accepted poster abstracts will be presented there.
- [x] Website, call, proposal source, and five-page PDF use the same speaker assignments, lab times, and poster policy.
- [x] Published the [website](https://kauroy1994.github.io/AAAI-Symposium-Concept/), [draft call](https://kauroy1994.github.io/AAAI-Symposium-Concept/cfp.html), and [interest form](https://forms.gle/RUvA879SEs7ypqVc9). The form alone does not establish participant interest.

## Required before submission

- [ ] Supply the required list of **contacted potential participants who expressed interest**. No qualifying responses were supplied or found in the repository. Add actual names and affiliations to the proposal within the five-page limit. Outreach targets and attendance goals are not expressions of interest. AAAI does not require attendance commitments or specify a minimum number of names in the public call. Organizer agreement alone does not establish a separate participant-interest list.
- [ ] Rebuild and inspect the PDF after adding the interest list; keep the complete proposal within **2-5 pages**.
- [ ] Follow the EasyChair link on the official call; inspect portal-specific fields and upload restrictions, upload the final PDF, submit, and save the receipt. The public call sets **November 17, 2026**, with no submission timezone stated. Decisions are scheduled for **December 8, 2026**.

## Affiliation review

Ashraf Abdul-Muumin's UA affiliation remains based on the lead organizer's information. Raj Krishnan's association with AI For Services is supported by the company profile; no specific title is asserted. The speaker assignments were supplied by the lead organizer. Biographical details and source links are recorded in SOURCES.md.

Confirmed keynotes and sponsors are not prerequisites in the public call. AAAI encourages committee collaboration and feedback from prospective participants.

## Evidence handling

Keep replies and correspondence privately. Use `resources/interest-register-template.csv` as a local register under the ignored `private/` directory. Distinguish reviewer-facing inclusion from public listing; a public participant list is optional. If respondents do not approve public disclosure, prepare the reviewer-facing interest list privately rather than committing it here.

## Validation

Run `python scripts/build_proposal.py` and `python scripts/validate.py`. The validator checks six organizers and two speakers in the correct sections, both lab sessions, the poster session, identical website and proposal schedules, local links, portraits, and the PDF page count. Source provenance and remote URL results appear in [SOURCES.md](../SOURCES.md). Check main-branch validation and Pages deployment in [GitHub Actions](https://github.com/kauroy1994/AAAI-Symposium-Concept/actions).
