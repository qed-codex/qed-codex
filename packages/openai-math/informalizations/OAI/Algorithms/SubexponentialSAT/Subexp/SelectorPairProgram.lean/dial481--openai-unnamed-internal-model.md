---
{
  "module": "OAI/Algorithms/SubexponentialSAT/Subexp/SelectorPairProgram.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/Subexp/SelectorPairProgram.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/Subexp/SelectorPairProgram.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

+# Selecting and framing both read plans of a vertex pair

The two selector-map calls share a persistent table. Stack 6 initially holds
the left query records and stack 9 the right query records. Stack 11 is an
existing record accumulator. The result prepends one record whose payload is
`frame leftPlanBytes ++ frame rightPlanBytes`.


### `program_trace`

 Both selections, all moves, and both framing layers are actual fixed
instructions. No preparation operation is hidden in a callback contract. 

### `cost_bound`

 Polynomial in the actual table and two query encodings, including the
copies and both levels of output escaping. 

### `selected_pair_trace`

 The exact pair payload expected by the collision-score record iterator. 
