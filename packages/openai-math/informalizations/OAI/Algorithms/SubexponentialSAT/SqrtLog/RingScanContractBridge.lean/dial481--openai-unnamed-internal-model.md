---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLog/RingScanContractBridge.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/RingScanContractBridge.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/RingScanContractBridge.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 Whole-vector native multiplication after explicitly paid triple expansion. 

### `multiplicationBlocks`

 The required source format groups the triple stream by output coordinate,
then by the two operand indices. Producing it is a separate paid program. 

### `mulRun_contract_native`

 A fixed native instruction table computes the complete bilinear product
from a k-major triple stream. All contraction work is charged. The input
format does not claim that generating the stream or table is free. 
