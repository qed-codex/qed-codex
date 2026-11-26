---
{
  "module": "OAI/Computability/VPVNP/RAMTapeSpacePaths.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMTapeSpacePaths.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMTapeSpacePaths.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Head positions along a branching physical execution

A path can follow either occupied continuation slot. Its integer indices
measure the total displacement on each tape; applying the displacement bound
to every prefix bounds every cell visited.


### `Choices.contains`

 A command occupies one of the available continuation slots in a physical machine step. 

### `HeadPath`

 A prefix following actual continuing commands, with its physical
head displacement on both tapes. 

### `HeadPath.range`

 Each instruction moves each head by at most one cell. 

### `Travel.suffix`

 An execution that runs at least as long as a deterministic routine
must follow that routine, leaving only its suffix and residual displacement. 
