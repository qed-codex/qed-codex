---
{
  "module": "OAI/Computability/VPVNP/RAMValidatorControl.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMValidatorControl.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMValidatorControl.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# The local post-call control check of Lemma 10.1

The validator checks that it used every private choice bit. On an internal
successor edge it compares the final cumulative cost and status to the send.
At the last site it requires the computed status to be an accepting halt.


### `finishReports`

 A nonempty suffix rejects immediately. Otherwise the validator scans each
report and event once. The fixed cost covers the end-of-input test, the
status, cost and state comparisons, branching and return. 
