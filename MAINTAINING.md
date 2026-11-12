# Maintaining the README-powered website

## Activate GitHub Pages once

Open the repository's **Settings → Pages**. Under **Build and deployment**, choose **Deploy from a branch**, select **main** and **/(root)**, and save. GitHub will build the Jekyll site. The intended address is `https://kauroy1994.github.io/AAAI-Symposium-Concept/`; do not advertise it as live until the deployment succeeds. See https://docs.github.com/en/pages/getting-started-with-github-pages/creating-a-github-pages-site .

`index.md` includes `README.md` and converts it to HTML. `_layouts/default.html` supplies the frame; `assets/style.css` supplies the UA-inspired styling. The README remains the single source of substantive homepage content. It is excluded as a separately published page but remains available to Jekyll's include step. No paid service, tracking script, external font, or JavaScript framework is required.

## Edit content

Update `README.md`, preserving the main section names so navigation anchors stay valid. Dates from AAAI must be distinguished from proposed local dates. Never change “proposed” to “accepted” without actual acceptance. Never add a confirmed speaker or participant without evidence and appropriate consent. Public company or university profiles verify affiliations, not agreement to organize.

The committee comprises five faculty/research organizers and two student organizers: Kaushik Roy, Alessandro Oltramari, Shahram Rahimi, Subash Neupane, Noorbakhsh Amiri Golilarz, Himanshu Tripathi, and Ashraf Abdul-Muumin. Nigel Glenday and Raj Krishnan are invited speakers and belong only in the Speakers section. When changing the roster, update `README.md`, `proposal/proposal.md`, `proposal/submission-checklist.md`, `SOURCES.md`, and the expected names in `scripts/validate.py`, then rebuild the proposal PDF. Validation checks that the seven organizers and two speakers appear in the correct sections of the README, proposal source, and PDF. Do not infer student email addresses, degree programs, or biographies.

## Maintain the call for papers

`cfp.html` is a standalone static page, published at `/AAAI-Symposium-Concept/cfp.html`; it carries its own responsive styles and needs no Jekyll front matter. Keep its poster-session policy and proposed contribution formats consistent with the Participation section in `README.md` and `proposal/proposal.md`. `_layouts/default.html` links to it from site navigation. The page and homepage use the same expression-of-interest form; email remains an alternative contact. Keep paper-submission deadlines and portal details pending until acceptance and coordination with AAAI. Form responses remain private; publishing a form does not fulfill the participant-interest requirement.

## Rebuild the proposal

Install the pinned build requirements and run:

```sh
python -m pip install -r requirements.txt
python scripts/build_proposal.py
python scripts/validate.py
```

The editable source is `proposal/proposal.md`; the output is `proposal/proposal.pdf`. Explicit page-break markers keep the proposal organized into five pages. If text is expanded, the builder refuses to silently publish an overlength document. Shorten/reflow content while preserving the required participant-interest list. Inspect all five rendered pages before committing the PDF.

The proposal is deliberately separate from the longer website; update both when changing the title, organizers, confirmed facts, or agenda. A validation workflow checks source structure and rebuilds the proposal, but does not certify factual accuracy or submission readiness. After rebuilding, commit both the edited source and the updated PDF; the workflow does not write to the repository automatically.

## Privacy and evidence

Keep consent replies and participant-interest records in a private institutional location. `private/` is ignored by Git as a safeguard, not an access-control mechanism. Do not force-add private files. The CSV in `resources/` contains headers only and is a template, not a participant list. Obtain separate permission for the proposal-reviewed list and any public display.

## Preview and design

The site is a standard Jekyll site without third-party plugins. It can be previewed with Jekyll locally or after Pages activation. The design uses UA Crimson Flame, Capstone Gray, white, responsive tables, keyboard focus styles, a skip link, and reduced-motion support. Colors do not imply institutional endorsement. The SVG banner is original diagram artwork; no external photograph or font license is required.

The shared program reserves Tuesday, March 23, 16:00–17:00 for posters. Keep the times and the policy for accepted papers consistent across the homepage, call, proposal, and case-study guide. The validator compares the website and proposal program text and checks the rendered PDF sessions. Refresh the PDF link version after each revision to avoid showing a cached copy.

The program must explicitly name Lab 1 (Monday 14:00–15:30) and Lab 2 (Tuesday 11:00–12:30). Nigel Glenday is assigned to Monday 09:20–10:00 and Raj Krishnan to Tuesday 09:00–09:40. Do not invent talk titles. The Speakers navigation item links to the speaker biographies on the homepage; the call and PDF carry the same assignments.
