---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLog/HashInputProgramOrigin.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/HashInputProgramOrigin.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/HashInputProgramOrigin.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 Exact original-clause provenance for a raw tuple, including repetitions.
The integer lift is taken BEFORE the tuple terms are added; its reduction, not
its value in the thickened ring, equals the combined ternary selector row. 

### `rawRow_reduction`

 This is the selector-origin theorem for the actual raw tuple expansion.
It handles repeated IDs and coefficients zero without a deduplication premise. 

### `clausePayload_codes`

 Original literal byte order is retained, including repeated literals. 
