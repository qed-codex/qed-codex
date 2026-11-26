---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/NativeEntrySpace.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/NativeEntrySpace.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/NativeEntrySpace.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 Every-prefix space composition for the actual canonical frontend and
fixed-cutoff dispatcher. The large evaluation is a concrete subsequent run;
this module only composes its existing bound with the paid entry instructions. 

### `frontend_bounded`

 Obtain the frontend state, its binary dimension, and its source prefix
bound from the actual canonical-input evaluation theorem. 

### `entry_large_bounded_eval`

 The fixed-cutoff scan has polynomial local space and the same bound is
retained on every prefix of the following actual large-input evaluation. 

### `entry_bounded_trace_space`

 The terminal halt and the selected Boolean output metadata preserve the
same entry bound. The primitive compiler can consume this exact source trace. 
