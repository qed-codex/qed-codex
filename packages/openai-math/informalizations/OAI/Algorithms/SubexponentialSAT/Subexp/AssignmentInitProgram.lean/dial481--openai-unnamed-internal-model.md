---
{
  "module": "OAI/Algorithms/SubexponentialSAT/Subexp/AssignmentInitProgram.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/Subexp/AssignmentInitProgram.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/Subexp/AssignmentInitProgram.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Physical initialization of the sequential assignment memory

The input contains the already generated alphabet and incidence records.
This fixed routine duplicates the runtime tables, creates the initial packed
assignment by actual repeated copying, and clears all temporary ports. The
production of the input records is a separate frontend stage.

