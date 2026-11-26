---
{
  "module": "OAI/Computability/VPVNP/LiveFirstTailOutput.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LiveFirstTailOutput.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LiveFirstTailOutput.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Preserving the outgoing cut during midpoint initialization

The outgoing flag and distributed cut lie below the old configuration. The
new configuration lies between the old configuration and the advice frames.
Initialization of the old tape and the four advice stages therefore preserve
all three inputs to the outgoing router.


### `frameAfterScratch`

 The advice frame follows the five transition-scratch words. 

### `frameOfRanges`

 Pointwise preservation on the two physical ranges surrounding the
incoming bank suffices for the outgoing router's complete input. 

### `initialOutputFrame`

 Compose the control-word write, advice preparation, and the incoming
tape's writes. The outgoing cut is read from the original physical header. 
