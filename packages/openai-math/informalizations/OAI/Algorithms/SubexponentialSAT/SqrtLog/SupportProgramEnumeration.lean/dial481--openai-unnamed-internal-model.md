---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLog/SupportProgramEnumeration.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/SupportProgramEnumeration.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/SupportProgramEnumeration.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 Pruned enumeration of bounded-weight Boolean masks. Every recursive call
extends an admissible prefix; there is no enumeration of all binary words. 

### `masks`

 Enumerate the length-n masks with strictly fewer than J set bits. 

### `calls`

 Count of recursive calls in the explicit pruned recursive specification. 

### `calls_le`

 The enumeration tree has only polynomially many nodes per emitted mask. 
