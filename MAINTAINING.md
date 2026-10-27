# Maintaining the README-powered website

## Activate GitHub Pages once

Open the repository's **Settings → Pages**. Under **Build and deployment**, choose **Deploy from a branch**, select **main** and **/(root)**, and save. GitHub will build the Jekyll site. The intended address is `https://kauroy1994.github.io/AAAI-Symposium-Concept/`; do not advertise it as live until the deployment succeeds. See https://docs.github.com/en/pages/getting-started-with-github-pages/creating-a-github-pages-site .

`index.md` includes `README.md` and converts it to HTML. `_layouts/default.html` supplies the frame; `assets/style.css` supplies the UA-inspired styling. The README remains the single source of substantive homepage content. It is excluded as a separately published page but remains available to Jekyll's include step. No paid service, tracking script, external font, or JavaScript framework is required.

## Edit content

Update `README.md`, preserving the main section names so navigation anchors stay valid. Dates from AAAI must be distinguished from proposed local dates. Never change “proposed” to “accepted” without actual acceptance. Never add a confirmed speaker or participant without evidence and appropriate consent. Public company or university profiles verify affiliations, not agreement to organize.

The committee currently comprises four main organizers and two UA student organizers, Himanshu Tripathi and Ashraf Abdul-Muumin. Keep the student-organizer section distinct from the main organizing roles. When changing the roster, update `README.md`, `proposal/proposal.md`, `proposal/submission-checklist.md`, `SOURCES.md`, and the expected names in `scripts/validate.py`, then rebuild the proposal PDF. Validation checks that all six names appear in the README, editable proposal, and generated PDF. Do not infer student email addresses, degree programs, or biographies.

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
