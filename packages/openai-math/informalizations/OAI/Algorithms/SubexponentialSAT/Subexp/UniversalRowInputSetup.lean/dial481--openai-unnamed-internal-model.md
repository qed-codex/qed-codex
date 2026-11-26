---
{
  "module": "OAI/Algorithms/SubexponentialSAT/Subexp/UniversalRowInputSetup.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/Subexp/UniversalRowInputSetup.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/Subexp/UniversalRowInputSetup.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 Actual setup of the bounded row evaluator's 49-stack workspace.

All parameters are read from persistent source stacks.  In particular, the
row count is obtained by popping the stored successor, the prime-field zero
is extracted from the stored zero quartet, and the row width is built by the
runtime block-copy program.  No matrix or correction vector is supplied.


### `seedSlots`

 The ten persistent masters copied before computing derived fields. 

### `inputStacks`

 Exact native input, including the two persistent constants used by the
correction-scalar routine.  All unlisted native stacks are empty. 

### `program_labels`

 The control table does not depend on any source parameter. 
