---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLog/HeadIdentifierProgramLowMask.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/HeadIdentifierProgramLowMask.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/HeadIdentifierProgramLowMask.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 Explicit order conversion between the reverse high-incidence mask and the
forward low-variable mask consumed by head-identifier selection. 

### `program_runsIn`

 Consumes a reverse original-order high mask and emits the forward low
mask. Original coordinate j now carries exactly the complement of high[j]. 
