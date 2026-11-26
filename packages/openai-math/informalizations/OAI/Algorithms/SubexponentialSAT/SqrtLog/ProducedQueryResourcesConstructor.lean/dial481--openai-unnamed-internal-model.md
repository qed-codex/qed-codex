---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLog/ProducedQueryResourcesConstructor.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/ProducedQueryResourcesConstructor.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/ProducedQueryResourcesConstructor.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 Numerical constructor for an actual query. Rank and maximum head size
are its two geometry arguments; ProducedQueryRank and LayoutProducedHeads
supply them from the actual packing. This module does not assert that an
arbitrary pair of natural numbers has those geometric bounds. 

### `matrixHeight`

 Uniform absolute coefficient-height envelope for the literal pulled
matrix. The ambient dimension is kept distinct from the free schedule. 

### `eventually_make_bounds`

 Numerical join. The two explicit hypotheses are precisely the geometry
outputs proved from the produced packing; every other Bounds field is derived
here from actual selector/scan outputs and the fixed setup majorant. 
