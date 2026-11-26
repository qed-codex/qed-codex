---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLog/RingScanBridge.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/RingScanBridge.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/RingScanBridge.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 Exact byte interfaces between the semantic ring callbacks and fixed native
flat-stack scanners. Materializing the input vectors/triples is a separate,
explicitly charged caller operation. 

### `addRun_native`

 The flat input/output of the native scanner is precisely the semantic
coefficient-vector add callback, including exact canonical result words. 

### `coordinateMulRun_native`

 Each physical streamed coordinate is exactly the original right-fold
coefficient callback. The canonical-zero hypothesis is discharged by the
prepared scalar-cache construction. 

### `addVectorProgram_primitive`

 Primitive-machine refinement of the same physical vector-add execution. 
