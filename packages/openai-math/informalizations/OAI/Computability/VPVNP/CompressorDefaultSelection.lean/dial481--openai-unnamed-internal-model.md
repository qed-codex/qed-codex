---
{
  "module": "OAI/Computability/VPVNP/CompressorDefaultSelection.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorDefaultSelection.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorDefaultSelection.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 # A common pre-selection state for the physical compressor

Each motif admits the zero supply vector. This gives a selected level whose
header can be constructed before the first guessed bit, at every input
state and in either kind of compressor pass.


### `defaultSelection`

 The outer term with all supply payload widths zero is admitted independently
of the current demand vector. 
