---
{
  "module": "OAI/Computability/VPVNP/RAMTapeRun.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMTapeRun.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMTapeRun.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Deterministic routines inside a branching tape program

A run contains only one-record rows. Executing it consumes its recorded number
of transitions and preserves the multiplicity of all continuations.


### `Runs`

 An exact finite run of deterministic two-tape commands between named configurations. 

### `cells`

 A two-way tape specified by the cells to the left and at or to the right of the head. 

### `tapeList`

 The head points to the stack top and every cell on its left is blank. 
