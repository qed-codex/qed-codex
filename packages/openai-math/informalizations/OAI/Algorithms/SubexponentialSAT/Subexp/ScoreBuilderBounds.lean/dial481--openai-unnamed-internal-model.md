---
{
  "module": "OAI/Algorithms/SubexponentialSAT/Subexp/ScoreBuilderBounds.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/Subexp/ScoreBuilderBounds.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/Subexp/ScoreBuilderBounds.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# A uniform bound for the actual complete score builder

The preparation program computes the selected plans. Its proved output-size
bound supplies the pair-payload bound needed by the candidate program.


### `BoundedInputs`

 Bounds on literal input lengths and counts, before selected plans are
computed. The prepared-payload bound is derived inside the theorem. 
