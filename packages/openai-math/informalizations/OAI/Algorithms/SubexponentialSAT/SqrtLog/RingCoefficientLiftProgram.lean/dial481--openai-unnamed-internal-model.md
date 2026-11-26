---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLog/RingCoefficientLiftProgram.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/RingCoefficientLiftProgram.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/RingCoefficientLiftProgram.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 A fixed scanner widens consecutive two-bit coefficients using a runtime
width tape. The original width is preserved, and all bit movement is paid. 

### `padded`

 The word list is a specification value; the machine scans its flat tape. 

 Exact byte bridge from canonical F3 coefficients to the supplied-polynomial
ring model. The program itself has no degree or width parameter. 

 Search-to-table ABI. The search has 22 registers and 28 stacks. In particular,
stack24 may contain unread candidates and is outside this adapter's ports. 

### `searchCommand_eval`

 The polynomial input appears on21, source13 is consumed, and all other
stacks (including the runtime width12, degree14, counts22 and candidates24)
are preserved. The exact result is the ring model's coefficient code. 

### `searchProgram_primitive`

 The corresponding single-bit primitive machine has a fixed overhead,
independent of both the runtime degree and the runtime coefficient width. 
