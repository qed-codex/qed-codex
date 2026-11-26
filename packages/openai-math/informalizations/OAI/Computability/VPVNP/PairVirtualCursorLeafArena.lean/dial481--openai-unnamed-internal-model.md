---
{
  "module": "OAI/Computability/VPVNP/PairVirtualCursorLeafArena.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairVirtualCursorLeafArena.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairVirtualCursorLeafArena.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Cursor rows in the live virtual pair arena

The shared-bit handoff publishes the first row and the role displacement.
Earlier ordinals preserve both fields and the selected role table, so every
cursor read uses the original row address and stays below the terminal header.


### `eventually_virtualCursorStackBudget`

 All private cursor stacks for a selected virtual branch fit at one input-length threshold. 

### `VirtualPairs.CursorLeafArena`

 The actual public cursor tags and private arena used at an ordinal. 

### `VirtualPairs.cursorLeafArena`

 The packed descriptor interval, surviving header publications and the
allocated scalar stacks supply every cursor address and tag bound. 
