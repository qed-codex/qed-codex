---
{
  "module": "OAI/Computability/VPVNP/CompressorRecordsShrinkRankArena.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorRecordsShrinkRankArena.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorRecordsShrinkRankArena.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Running the packed rank and list arena from arbitrary memory

The preliminary placement rows and old incidence precede the fresh rank
arena. Clear its count column, then run classification, append, uniform key
gather and ranking. Every preceding memory cell remains available to later
shrinking passes, including a second placement scan in the chosen layout.


### `shape`

 Set the rank arena's dimensions from the state's base vertex count, degree exponent, and
residual lane width, with allocation beginning at the supplied origin. 

### `finalMemory`

 Memory at the end of each of the five report segments. 

### `Run`

 Actual stored ranks, keys, and old port widths. 

### `build`

 Initialize the bounded count lists, run all four ranking stages, and retain
the earlier arrays below the arena. 
