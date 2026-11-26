---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SubexpScanPrimitives.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SubexpScanPrimitives.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SubexpScanPrimitives.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 Concrete stack operations used by the serialized coefficient scanner. 

### `takeWord`

 Copy the runtime width, consume exactly that many source bits, and restore
their order in the destination. The control table does not contain the width. 

### `zeroFillProgram`

 Push four zero bits for each item of the runtime counter. 
