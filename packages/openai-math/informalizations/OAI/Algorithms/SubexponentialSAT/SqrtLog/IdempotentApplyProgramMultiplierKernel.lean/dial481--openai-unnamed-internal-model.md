---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLog/IdempotentApplyProgramMultiplierKernel.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/IdempotentApplyProgramMultiplierKernel.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/IdempotentApplyProgramMultiplierKernel.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 Source component: IdempotentApplyProgramMultiplierArithmetic. 

 Native construction of the cubic multiplier before its U shift. 

### `Runs`

 A bounded native transition, with all Boolean registers allowed to change. 

### `arithmetic_runs`

 All inputs are ordinary stored data. No arithmetic callback premise is used. 

 Source component: IdempotentApplyProgramMultiplier. 

 Concrete preparation of the stored multiplier used by native Horner evaluation. 

### `eval_sequence_append`

 Sequence composition accounts for the zero-cost final skip explicitly. 

### `prepareMultiplier_eval`

 Actual native execution from H and cached constants to the computed multiplier.
All low tapes and all high tapes other than output86 and U-key94 are preserved. 

 Source component: IdempotentApplyProgramMultiplierSemantics. 

 The multiplier produced by the native preparation is U H(H-1)(H-2). 

### `prepared_denote`

 Cached one and minus-one are checked by their represented ring meanings;
no premise supplies the desired multiplier or its denotation. 
