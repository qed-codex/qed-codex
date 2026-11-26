# Contributed informalization check

Seven informalization changes passed the local PR checker, one code-only change passed through to ordinary code review, and 17 invalid changes failed. The fixtures use temporary Git commits on divergent branches and the real QED Codex module and declaration tables. Two runs produced byte-identical JSON. [Fixture results](informalization-checks.json)

A valid example places `fixture-reader.md` under the `src/Main.lean` informalization directory, identifies `fixture-reader` as its author, names `riemannHypothesis` and declares the pinned source revision and `CC-BY-4.0` license. A fixture naming `GlobalTheory.Mem.Top.Bl.anyGeometry` in that module exited with status 1. Editing, deleting or moving another handle’s file also failed. [Checker](../../tools/check_informalization_pr.py) · [Fixture generator](../../tools/test_informalization_pr.py)

For a pull request targeting main, the workflow uses the authenticated pull request opener’s GitHub login, the event’s base SHA and its head SHA. It checks out the trusted base and reads proposed Markdown from Git blobs. A three-dot diff identifies the contributed paths. Renames count as a deletion and an addition so both paths receive the ownership check. Module and declaration ownership come from a database compiled from the base’s pinned inputs. An explicit agreement references the current base version of a peer informalization by its SHA-256.

The validation job has read access to repository contents. A separate job attaches the `Informalization contribution` status to the PR head. This Gate 4 evidence comes from local execution of the validator. [Workflow](../../.github/workflows/informalization-pr.yml) · [GitHub’s PR target event](https://docs.github.com/en/actions/reference/security/securely-using-pull_request_target)

Run the replay from the repository root with the compiled database path.

```bash
LC_ALL=C .venv/bin/python tools/test_informalization_pr.py build/rh.sqlite3 > inputs/informalization-checks.json
cmp reports/gate-4/informalization-checks.json inputs/informalization-checks.json
```
