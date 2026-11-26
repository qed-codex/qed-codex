---
{
  "module": "OAI/Computability/VPVNP/EvaluatorCellSafety.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/EvaluatorCellSafety.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/EvaluatorCellSafety.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Time and peak storage for one complete label action

A deterministic lookup uses a polynomial number of temporary bits. Once the
lookup returns, its temporary stacks are empty and only one digit's worth of
counter storage is live. The subsequent countdown can invoke exponentially
many callbacks without accumulating any of their work space.


### `cell_bounded`

 All normal returns preserve the scheduler bank outside the evaluator
payload. Both successful and rejecting paths obey the cell clock. 
