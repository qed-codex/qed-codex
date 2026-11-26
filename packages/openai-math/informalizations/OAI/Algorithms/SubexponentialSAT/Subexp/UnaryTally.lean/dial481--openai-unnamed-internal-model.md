---
{
  "module": "OAI/Algorithms/SubexponentialSAT/Subexp/UnaryTally.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/Subexp/UnaryTally.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/Subexp/UnaryTally.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# A fixed bit program tallying padded collision leaves

Each successful leaf pushes one false bit. The resulting unary stack is the
exact common numerator used for conditional expectation. This file proves the
actual instruction trace from a prepared Boolean leaf list.


### `tally_trace`

 Exact instruction trace, including the final halt. 

### `pairNumerator_runsIn`

 Padded completion leaves are tallied by this fixed program into the exact
unary numerator expected by UnaryCompare. 
