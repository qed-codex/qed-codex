---
{
  "module": "OAI/Computability/VPVNP/RAMTapeSuccessorScan.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMTapeSuccessorScan.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMTapeSuccessorScan.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# The eight-word tag pass of a successor validator

The finite control scans word seven down to word zero. It stores each tag
on return from the preserving scan and immediately starts the next word.
The eight input stacks and the common scratch stack are restored on exit.


### `TagState`

 Control for the eight-word tag scan, retaining the word index, accumulated tags, and
current word scan state. 

### `tagEntry`

 Start at word seven with all tag slots zero and the single-word scanner at its first bit. 

### `tagCode`

 Install the eight scans at their respective word ports. The last empty
scratch pop of each scan goes directly to its continuation. 

### `tag_run`

 The complete field pass classifies all eight words and preserves the caller's
stacks. Only the temporary stack must be distinct from each data port. 
