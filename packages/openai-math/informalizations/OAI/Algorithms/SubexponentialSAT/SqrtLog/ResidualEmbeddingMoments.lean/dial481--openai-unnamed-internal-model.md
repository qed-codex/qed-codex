---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLog/ResidualEmbeddingMoments.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/ResidualEmbeddingMoments.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/ResidualEmbeddingMoments.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 Ambient support enumeration may include supports meeting fixed high
coordinates. Their coefficients are zero, so the output equals the residual
moment computation without any additional Boolean assignments. 

### `sum_jetCoeff`

 Only the image supports contribute, even if the residual polynomial being
extracted depends on the requested ambient support through its weights. 

### `localBoolWeight_map`

 Actual Boolean head weights agree on the embedded supports. Values of the
ambient head assignment outside the image cannot affect this product. 

### `run_finite_output`

 The native ambient run can use any larger support list with exactly the
required image supports. Extra supports have zero extracted coefficient.
Both computations use the identical head-assignment lists. 
