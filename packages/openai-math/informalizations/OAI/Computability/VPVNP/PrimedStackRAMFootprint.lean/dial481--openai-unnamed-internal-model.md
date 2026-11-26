---
{
  "module": "OAI/Computability/VPVNP/PrimedStackRAMFootprint.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PrimedStackRAMFootprint.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PrimedStackRAMFootprint.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Header preservation by the complete parser visit

Successful scratch writes target the depth word, a guarded stack index, a
guarded mark or a guarded production index. The header words below the
rectangle, including the nominated histogram, are therefore available at
their original addresses for the final comparison.


### `Below`

 Agreement of two external memories at every address strictly below the scratch base,
including header words stored there. 

### `protects_readOnly`

 The non-writing opcode blocks retain all external memory words. 

### `completeNode_below`

 The final nomination comparison can read every original header word. This
also holds for an arbitrary initial memory whenever the physical call succeeds. 
