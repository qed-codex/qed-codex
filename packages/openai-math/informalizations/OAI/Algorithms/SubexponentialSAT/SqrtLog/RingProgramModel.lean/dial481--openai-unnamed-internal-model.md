---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLog/RingProgramModel.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/RingProgramModel.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/RingProgramModel.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 Concrete ternary coefficient input and the executable represented arithmetic
for the supplied-polynomial unramified ring model. 

### `ternaryLiteral`

 A ternary residue has a constant-size literal encoding. 

### `liftCoefficientsRun`

 Materialized coefficient words for the lower coefficients of the monic
polynomial. The leading coefficient is implicit. 

### `modelProgram`

 An entirely executable program for the actual supplied ternary polynomial.
Its table and coefficient words can be retained across all later operations. 

### `modelProgramRun`

 Explicit preparation retains both coefficient words and the generated table. 

### `modelRing_decode`

 The decoder is exactly reconstruction from the model's coefficient basis. 

### `modelRing_decodeCount`

 A canonical coefficient-zero word reads as its exact natural value. 
