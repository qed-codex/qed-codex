---
{
  "module": "OAI/Computability/VPVNP/LiveEvaluatorRAMCell.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LiveEvaluatorRAMCell.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LiveEvaluatorRAMCell.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Word-level correctness of the finite evaluator tape scan

The source-indexed tests in the fixed private-RAM template read the old
symbol and its paired destination in memory. Reading all these pairs
checks the full unbounded evaluator tape transition.


### `TapeCellData`

 The numeric fields of one call and its two memory slices. Each bit-field
word has already been unpacked at its agreed memory address. 

### `tapeScan_exec_iff`

 Each native fragment exits precisely on a matching symbol pair. All
fragments together check both endpoints and every proposed tape cell. 
