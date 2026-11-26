---
{
  "module": "OAI/Algorithms/SubexponentialSAT/Subexp/BasisTransposePlanProgram.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/Subexp/BasisTransposePlanProgram.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/Subexp/BasisTransposePlanProgram.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Physical transpose read-plan generation

Two unary countdowns visit columns and rows in decreasing order. Each visit
constructs the unary physical index by repeated copying and emits one actual
framed record. Prepending these visits produces the increasing transpose
read order directly. All counters are runtime stacks and the code is fixed.


### `DownSpec`

 This specification contains a real evaluation of the fixed body for
each remaining counter value. It is instantiated below by copying and
framing programs, never by an opaque arithmetic callback. 

### `program_run`

 The physical plan is emitted in forward transpose order. The unary
dimension is preserved, every scratch stack is empty, and all registers are
reset for the following gather call. 
