---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLog/LayoutSignatureBound.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/LayoutSignatureBound.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/LayoutSignatureBound.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 Exact integer signature ranges for Boolean assignments. 

### `boolSignature`

 Boolean assignments are embedded in the integers before signatures are
computed. No precision-dependent modulus enters this definition. 

### `card_range_boolSignature_le`

 The number of attained integer labels has the usual height/rank bound,
independently of the characteristic and prime-power precision used later. 
