---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLog/IdempotentApplyProgramExecution.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/IdempotentApplyProgramExecution.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/IdempotentApplyProgramExecution.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 Native high-register services for the quadratic and Horner steps. 

### `scalarReady`

 Workspace condition for the native scalar reader, expressed only in high memory. 

### `mul_hash_eval`

 Copy the persistent hash into the operand port, then invoke the real sparse product. 

### `add_constant_eval`

 The constant term is read from the real reversed coefficient stream. 

### `eval_seq_assoc`

 Reassociation does not insert instructions or alter the measured cost. 

 Complete native evaluation of one degree-two coefficient digit. 

 The native Horner accumulator update, including every move and cleanup. 

 Measured descending Horner loop over the actual computed coefficient tape. 

### `applyLoop_eval`

 Tape reversal, native Horner evaluation and final scratch reclamation. 
