---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLog/LeafProgramNodeSemantics.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/LeafProgramNodeSemantics.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/LeafProgramNodeSemantics.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 Public source-specific facts for the native node/count join. The target,
its degree, and its exact constant count all refer to the same polynomial. 

### `model_target_origin`

 Actual original-ID layout rows give the required source origin, and the
integer lifts give the required prime-subfield residues automatically. 

### `liftedHashes_width`

 The sparse source width bound survives coefficient lifting verbatim. 

### `model_target_degree`

 This degree bound is attached to the same code-derived source polynomial
whose constant coefficient is identified by model_target_origin. 

### `model_count_bound`

 The generic count reader's ambient bound follows from summing only free
assignments. The multiplicity m is the outer query allowance. 

### `actual_dense_hasJets`

 Concrete native outputCodes, rather than an arbitrary list decoder,
provide the reconstruction jets once the node bucket theorem is applied. 
