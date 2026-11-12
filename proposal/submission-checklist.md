# Submission checklist

Reviewed November 12, 2026 against the [official AAAI 2027 Spring Symposium call](https://aaai.org/conference/spring-symposia/aaai-2027-spring-symposium-series-call-for-proposal/).

**Status: files prepared; participant-interest list still required.** This package has not been submitted to EasyChair.

## Prepared

- [x] Title, scope, research questions, and format.
- [x] Full preliminary program for March 22-24, 2027 at Santa Clara University; invited-speaker slots unassigned.
- [x] All eight organizers in the website, Markdown proposal, and PDF: Kaushik Roy, Nigel Glenday, Raj Krishnan, Alessandro Oltramari, Shahram Rahimi, Subash Neupane, Himanshu Tripathi, and Ashraf Abdul-Muumin.
- [x] All eight organizer emails. Five verified against public professional sources; Raj's, Himanshu's, and Ashraf's supplied by the lead organizer on November 12, 2026.
- [x] Agreement to serve: the lead organizer confirmed on November 12, 2026 that all eight have said yes. AAAI specifies agreement, not a signed form or separate consent-document upload. Retain replies privately and circulate the final proposal for committee review.
- [x] Live [symposium website URL](https://kauroy1994.github.io/AAAI-Symposium-Concept/) included in the proposal.
- [x] Regenerated five-page PDF, including references; all pages visually reviewed.
- [x] Attendance target distinguished from actual interest; relationship to the existing NeSy conference explained.

## Required before submission

- [ ] Supply the required list of **contacted potential participants who expressed interest**. No qualifying responses were supplied or found in the repository. Add actual names and affiliations to the proposal within the five-page limit. Outreach targets and attendance goals are not expressions of interest. AAAI does not require attendance commitments or specify a minimum number of names in the public call. Organizer agreement alone does not establish a separate participant-interest list.
- [ ] Rebuild and inspect the PDF after adding the interest list; keep the complete proposal within **2-5 pages**.
- [ ] Follow the EasyChair link on the official call; inspect portal-specific fields and upload restrictions, upload the final PDF, submit, and save the receipt. The public call sets **November 17, 2026**, with no submission timezone stated. Decisions are scheduled for **December 8, 2026**.

## Affiliation review

Raj Krishnan's AI For Services affiliation and Ashraf Abdul-Muumin's UA affiliation are retained as lead-organizer-supplied details; current independent institutional verification was not available. Ask them to approve the wording during final review. Raj's previously asserted Founder/CEO title has been removed. The other six affiliations have public primary-source support. These provenance limits are not additional AAAI paperwork requirements.

Confirmed keynotes and sponsors are not prerequisites in the public call. AAAI encourages committee collaboration and feedback from prospective participants.

## Evidence handling

Keep replies and correspondence privately. Use `resources/interest-register-template.csv` as a local register under the ignored `private/` directory. Distinguish reviewer-facing inclusion from public listing; a public participant list is optional. If respondents do not approve public disclosure, prepare the reviewer-facing interest list privately rather than committing it here.

## Validation

Run `python scripts/build_proposal.py` and `python scripts/validate.py`. The validator checks all eight organizer names in source and PDF, local website links and portraits, program arithmetic, and page count. Source provenance and remote URL results appear in [SOURCES.md](../SOURCES.md). Check main-branch validation and Pages deployment in [GitHub Actions](https://github.com/kauroy1994/AAAI-Symposium-Concept/actions).
