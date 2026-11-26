---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/QueryStreamSpaceBudgets.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/QueryStreamSpaceBudgets.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/QueryStreamSpaceBudgets.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 Fixed polynomial space for the actual complete conditioned query.
Retained words and local arithmetic work are counted independently of the
number of support pairs, attained signatures, head assignments or nodes. 

### `finishEnvelope`

 The actual node readout, ordered append, cleanup and next-index work. 

### `recoveryEnvelope`

 The actual reconstruction bound includes all arithmetic temporaries and
whole count-word readback. Its exponent is fixed before the query. 

### `envelope`

 A sum dominates the actual nested prefix maxima; it never multiplies
space by the number of executed candidates or callbacks. 

### `complete_polynomial`

 Constants and degree are fixed before all input and source dimensions.
The bound contains only the actual scalar and word caps; neither assembled
runtime nor attained counts occur. 

### `all_stack_bits_polynomial`

 The fixed 896-tape source bank is counted in full, including retained
caller words; the compiler can consume this bound for every source prefix. 
