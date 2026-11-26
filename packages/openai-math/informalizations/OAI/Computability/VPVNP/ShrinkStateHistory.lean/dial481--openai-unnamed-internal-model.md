---
{
  "module": "OAI/Computability/VPVNP/ShrinkStateHistory.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/ShrinkStateHistory.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/ShrinkStateHistory.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# History bounds for the actual dyadic shrinking pass

For each admissible selection the records contain its resident maps,
absorbed fields and map arguments together with all old and new half-wire
fields. The bound for this substep depends only on the two degree exponents
and the fixed conversion block. It applies uniformly at every packed site.


### `shrinkExtraRecords`

 Records of the selected six-party kernels before adding the actual
old and new incident half-words. 

### `shrinkHistoryFactor`

 The fixed per-substep history growth factor. `K` counts old positions
and `r = dQ` counts occurrences of each packed role. 

### `shrinkStatePass_bounded`

 The exact state pass has the bounded local histories used in Theorem 7.1. 
