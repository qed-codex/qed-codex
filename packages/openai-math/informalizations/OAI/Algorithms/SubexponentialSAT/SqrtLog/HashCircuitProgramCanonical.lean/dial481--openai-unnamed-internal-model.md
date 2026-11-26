---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLog/HashCircuitProgramCanonical.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/HashCircuitProgramCanonical.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/HashCircuitProgramCanonical.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 Direct native incidence evaluation from original unary CNF literal records.
This module composes the paid literal decoder with the paid dictionary lookup;
no preprocessing assumption converts literal numbers into variable keys. 

### `canonicalLiteral_runs`

 The input here is exactly `Encoding.literalCode`, not a new literal syntax. 
