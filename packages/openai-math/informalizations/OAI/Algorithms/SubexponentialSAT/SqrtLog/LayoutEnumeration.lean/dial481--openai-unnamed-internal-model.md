---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLog/LayoutEnumeration.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/LayoutEnumeration.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/LayoutEnumeration.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 Bridges for an explicit runtime enumeration of raw integer rows.
The enumeration need not agree with the semantic `Fintype.equivFin` order. 

### `data_rationalRowSpan`

 A certificate against the raw joint-indexed matrix suffices for any
runtime-selected constraints on the semantic universal layout. 
