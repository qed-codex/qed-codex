# Contributing an informalization to QED Codex

Follow [CONTRIBUTING.md](CONTRIBUTING.md) for the submission and licensing rules.

1. Pick a module from the [most-wanted list](https://qedcodex.org/wanted/), or open `/wanted/` on a local preview.
2. Open the module’s source at the package commit in [proof.yml](proofs/rh/proof.yml). Read the declarations and any definitions needed to state their hypotheses and conclusions.
3. Write one Markdown file at `packages/<package>/informalizations/<module-path>/<handle>--<writer-slug>.md`. The module page’s **Add an informalization** form prefills this path. Keep the full original module path, including `.lean`.
4. Cite pinned source lines for the mathematical claims. Use links of the form `https://github.com/<owner>/<repo>/blob/<source_commit>/<module-path>#L<start>-L<end>`. Cite any dependency at its own package revision.
5. Open one pull request per module. Edit your submission alone and leave other entries to their submitters.

## Front matter

New text written or generated for QED Codex is CC BY 4.0. Previously published text shows its source licence. Imported text keeps its own licence, shown beside it. Code is MIT.

Between two lines containing `---`, supply the following fields.

- `module` is the original module path. `declarations` is a list of the exact, qualified Lean names discussed.
- `author` is the submitting GitHub handle. `writer` is the actual model’s credited name for model-generated text.
- Use `origin: generated` for your model’s output. The checker derives `kind: ai` when omitted. Use `ai-reviewed-by-human` when the submitting author has reviewed the model’s text.
- `source_commit` is the full Git commit for the module’s Lean package. New descriptions have `license: CC-BY-4.0`.
- Other origins, a third-party `source`, and optional `agrees_with` references are described in the [contribution guide](CONTRIBUTING.md).

## Check the file

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
