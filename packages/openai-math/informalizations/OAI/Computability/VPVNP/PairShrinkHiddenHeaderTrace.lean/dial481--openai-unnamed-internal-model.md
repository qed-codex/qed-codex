---
{
  "module": "OAI/Computability/VPVNP/PairShrinkHiddenHeaderTrace.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairShrinkHiddenHeaderTrace.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairShrinkHiddenHeaderTrace.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Canonical trace of the hidden-field header

The five external probes in the hidden-field header read offsets of the same
old-level pointer. The compiled address calculation overwrites its temporaries
before each probe. Its trace is therefore independent of the previous register
contents, including the registers used for the owner and private slot geometry.


### `allTicks`

 Each non-read assignment takes one local step, for every initial register file. 

### `headerTrace_congr`

 Fixing the old level pointer determines the complete chronological log.
The word size and the selected stage constants may vary. 

### `canonicalTrace`

 Canonical header trace from its external pointer and memory. 
