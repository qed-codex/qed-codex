---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/NativeLeafPreparation.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/NativeLeafPreparation.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/NativeLeafPreparation.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 Actual physical preparation of the streamed greedy selector. The final
suffix clears the argmin bank, preserves the serialized code history, and
constructs the single retained zero candidate using the runtime depth word. 

### `afterCode`

 This runs after actual serialization, while the saved modulus and round
words are still intact. It neither repeats parameter arithmetic nor searches. 

### `finishedWords`

 Complete physical store after the final preparation suffix. 

### `afterCode_eval`

 The final suffix has one actual execution, exact full-store readback,
a fixed local polynomial cost, and an all-port bound on that same trace. 

### `finished_parameters`

 The concrete final preparation changes no formula, count, or saved
parameter word; it preserves the history produced by the actual serializer. 

### `Ready`

 Physical entry condition for the streamed selector. Every field records
an actual stack word; none supplies an evaluator, trace, or resource oracle. 

### `finished_ready`

 This exact store implication is used with the actual suffix execution,
so no readiness field is left as an implementation assumption. 

### `afterCanonical`

 Actual code searches and row serialization followed by paid selector
initialization. The code matrices are produced by the searches themselves. 

### `afterCanonical_eval`

 Code construction and initialization expose their actual intermediate
metadata state for the fixed numerical envelopes, never an assumed layout. 

### `command`

 The executable preparation is fixed before its input. Numeric parameters
occur only in the correctness and resource statements. 

### `command_eval`

 From the actually loaded nonterminal formula, the native preparation
produces the selector's physical entry state and its attained initial code.
The same execution carries the time and every-prefix all-stack bounds.
The retained bound is independent of the exponential search runtime. 
