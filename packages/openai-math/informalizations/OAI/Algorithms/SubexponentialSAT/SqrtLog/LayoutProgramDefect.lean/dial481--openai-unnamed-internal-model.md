---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLog/LayoutProgramDefect.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/LayoutProgramDefect.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/LayoutProgramDefect.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 Physical clearing-defect entries from the actual signed numerator pair.
A diagonal entry is D−(P−N), an off-diagonal entry is −(P−N). The numerator
and cached denominator remain intact; the result is a fresh signed pair.
The diagonal flag is a runtime bit, supplied by the type equality scan. 

### `result_mass_le`

 Noncanonical numerator components are bounded separately. The physical
transform only adds the denominator to that total on diagonal entries. 
