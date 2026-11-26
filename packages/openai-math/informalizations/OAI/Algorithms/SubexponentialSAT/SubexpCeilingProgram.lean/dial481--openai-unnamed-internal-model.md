---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SubexpCeilingProgram.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SubexpCeilingProgram.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SubexpCeilingProgram.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# The actual binary program for the packed dimension

Binary long division yields quotient and remainder. A finite zero test and
conditional increment then produce the ceiling. The input-dependent values are
stack words throughout; the control table is fixed.


### `packed_dimension`

 With the actual schedule words, the same finite program computes `D(n)`.
The positive-divisor premise is discharged by the previously checked guard. 

### `lifted_output`

 Fixed port maps preserve unrelated caller data. 
