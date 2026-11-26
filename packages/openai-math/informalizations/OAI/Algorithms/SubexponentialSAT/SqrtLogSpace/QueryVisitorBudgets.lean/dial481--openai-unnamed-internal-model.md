---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/QueryVisitorBudgets.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/QueryVisitorBudgets.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/QueryVisitorBudgets.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 Polynomial overhead and prefix space for the complete actual tuple
visitor. The number of heads and the proved maximum head-size exponent stay
explicit; the empty-head/empty-tuple term is retained. 

### `tailEnvelope`

 Actual final readout and tuple-accumulator addition. 

### `envelope`

 One uniform local coefficient covers both representative passes and the
final shared-U readout/addition, as well as their complete source prefix bound. 

### `head_coefficient_le`

 The actual source words, rather than their exponential integer values,
supply every remaining local head coefficient parameter. 

### `actual_bounds`

 Both measured quantities are the ones returned by the actual visitor
run theorem. Neither side grows with the number of emitted tuples. 

### `complete_polynomial`

 Uniform fixed constants cover complete visitor time and every source
prefix; the balanced-height exponent and r+1 empty term remain explicit. 
