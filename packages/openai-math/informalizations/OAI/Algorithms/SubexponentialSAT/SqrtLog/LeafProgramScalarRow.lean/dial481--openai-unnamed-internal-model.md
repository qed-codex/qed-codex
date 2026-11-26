---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLog/LeafProgramScalarRow.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/LeafProgramScalarRow.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/LeafProgramScalarRow.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 Flat ring coefficients may scale sparse dictionaries directly. They need
not first be serialized as a singleton sparse dictionary. This interface is
used by the native weighted-clause interpreter. 

### `stored_scale_correct`

 Direct scalar scaling has precisely the truncated-multiplication meaning
used by the generic row fold. 

### `scalar_rowFold_source`

 The native left fold with flat scalar weights denotes the same source
polynomial as the generic weighted sparse-row evaluator. 
