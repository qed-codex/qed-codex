# AGENTS.md

Part 1 is for an agent or a person who proposes an informalization. Part 2 is for an agent or a maintainer who changes the code in `tools/`, `site/`, `proofs/` or `.github/`.

## Part 1. Contributing an informalization

Follow [CONTRIBUTING.md](CONTRIBUTING.md) for the submission and licensing rules.

1. Pick a module from the [most-wanted list](https://qedcodex.org/wanted/), or open `/wanted/` on a local preview.
2. Open the module’s source at the package commit in [proof.yml](proofs/rh/proof.yml). Read the declarations and any definitions needed to state their hypotheses and conclusions.
3. Write one Markdown file at `packages/<package>/informalizations/<module-path>/<handle>--<writer-slug>.md`. The module page’s **Add an informalization** form prefills this path. Keep the full original module path, including `.lean`.
4. Cite pinned source lines for the mathematical claims. Use links of the form `https://github.com/<owner>/<repo>/blob/<source_commit>/<module-path>#L<start>-L<end>`. Cite any dependency at its own package revision.
5. Open one pull request per module. Edit your submission alone and leave other entries to their submitters.

### Front matter

New text written or generated for QED Codex is CC BY 4.0. Previously published text shows its source licence. Imported text keeps its own licence, shown beside it. Code is MIT.

Between two lines containing `---`, supply the following fields.

- `module` is the original module path. `declarations` is a list of the exact, qualified Lean names discussed.
- `author` is the submitting GitHub handle. `writer` is the actual model’s credited name for model-generated text.
- Use `origin: generated` for your model’s output. The checker derives `kind: ai` when omitted. Use `ai-reviewed-by-human` when the submitting author has reviewed the model’s text.
- `source_commit` is the full Git commit for the module’s Lean package. New descriptions have `license: CC-BY-4.0`.
- Other origins, a third-party `source`, and optional `agrees_with` references are described in the [contribution guide](CONTRIBUTING.md).

### Check the file

Use the [README build instructions](README.md#reproduce-the-database-and-local-preview) to prepare the environment and a database from the target branch. From the repository root, set `NOTE` to your file path and `HANDLE` to your GitHub handle. Commit the note, then run the PR checker with the full revision IDs.

```sh
.venv/bin/python tools/check_informalization_pr.py \
  --base "$(git rev-parse origin/main)" --head "$(git rev-parse HEAD)" \
  --author "$HANDLE" --database build/rh.sqlite3
```

Run the same Markdown and math renderer the site uses. Open its output and check formulas, references and attribution before opening your pull request.

```sh
mkdir -p build
PYTHONPATH=tools .venv/bin/python - "$NOTE" > build/informalization-preview.html <<'PY'
import sys
from pathlib import Path
from urllib.parse import quote
from informalizations import render_informalization

note = Path(sys.argv[1])
body = note.read_text(encoding="utf-8").split("---\n", 2)[2]
url = "https://github.com/qed-codex/qed-codex/blob/main/" + quote(note.as_posix())
print('<meta charset="utf-8">')
print(render_informalization(body, url))
PY
```

## Part 2. Changing the code

Every rule below describes the repository as it is. If a rule and the code disagree, say so before you change either.

### What is where

- `site/` is the viewer: static files, plain ES modules and CSS, no framework and no backend. The browser reads the SQLite database over HTTP in gzip pieces.
- `tools/` holds the build (`build.py`, `package.py`), the verifiers (`verify.py`, `verify_directory.py`), the contribution checker and the tests.
- `proofs/<proof>/` holds one proof's pins and links. `packages/<package>/informalizations/` is the ledger, one Markdown file per entry.
- `reports/` holds recorded measurements that the README links to. They stay. Do not commit new screenshots, raw browser logs or other binary files unless a maintainer asks for them.

### Build and test

- Setup and the full build are in the [README](README.md#reproduce-the-database-and-local-preview). The hosted build uses SQLite 3.46.1, Python 3.14.4 and Node 22.22.1.
- These need no database: `.venv/bin/python -m unittest discover -s tools -p 'test_*.py'`, `node tools/test-license-byline.mjs`, `node tools/test-startup-assets.mjs` and `node tools/sweep.mjs --check-inputs`.
- Everything else needs a built database and package. `.github/workflows/compiler.yml` is the list of what must pass. Run its steps locally before you ask for review.
- To preview with the real response headers, run `npx wrangler pages dev build/preview`.
- Before a deployment, run the sweep described in the README. It must finish with zero failures in Chromium, Firefox and WebKit.

### Rules

1. **The site stays static and self-contained.** The Content-Security-Policy is written in `tools/package.py`. It allows no inline script or style and no outside host for scripts, styles, fonts or images. A change that needs a new host changes that policy and says so in the pull request.
2. **Every query is declared and indexed.** Each query the site runs is in `site/queries.json` and has an input in `tools/sweep-inputs.json`. `tools/verify.py` reads the query plans and rejects an unexpected table scan.
3. **Nothing unused in the database.** A change that stops using a table, an index or a full-text option removes it from `tools/schema.sql` in the same change.
4. **Every test file runs in the hosted check.** A new `test_*.py` or `test-*.mjs` file in `tools/` is added to `compiler.yml` in the same change.
5. **The required check does not depend on a third-party site.** The crawl of outside links runs weekly in its own workflow.
6. **The contribution check is closed to the pull request.** `informalization-pr.yml` runs on `pull_request_target`. It never checks out or runs the pull request head, receives no secrets and uses no cache. `compiler.yml` has no paths filter, because it is a required check for every pull request.
7. **The ledger is separate.** A pull request that changes ledger files changes nothing else. Imported entries are not edited by hand.
8. **Permission-only text stays where it is.** Text with `license: with-permission` is shown on the site with its credit, listed in `/informalizations.json` without a link to the raw text, and left out of the mirrors. Do not widen where it appears.
9. **Credit and licence are kept.** Every entry shows its writer, its submitter and its licence. Do not remove or reword a licence, copyright or notice line.
10. **Addresses are permanent.** `/m/?pkg=&p=`, `/d/?pkg=&n=`, `/proofs/<proof>/`, `/m/records/<package>/<id>/` and each entry's anchor keep working.
11. **Numbers come from the build.** No count that changes with a ledger merge is typed by hand into a page or the README.
12. **Agreement never blocks an author.** An `agrees_with` reference that no longer matches is dropped when the database is built. It does not stop another author from changing or removing their own entry.
13. **Pages fit a phone.** No page scrolls sideways at 440, 390 or 320 CSS pixels.
14. **Plain words.** No promotional language on the site or in the repository.
15. **No credit to the tools that worked on this repository.** Do not name an AI model, assistant, tool or vendor as an author, designer or reviewer of this repository's code, pages or documents. That covers `tools/`, `site/`, comments, commit messages and git trailers such as `Co-Authored-By`. A model is named in two places only: as the `writer` of a ledger entry, and where the source of a proof or of an imported text credits it.
16. **One change is one commit on `main`.** It arrives through a pull request with both required checks green. No force push.

### When a request conflicts with these rules

Say so, with the evidence, before you write code. Prefer the smallest change that solves the problem.
