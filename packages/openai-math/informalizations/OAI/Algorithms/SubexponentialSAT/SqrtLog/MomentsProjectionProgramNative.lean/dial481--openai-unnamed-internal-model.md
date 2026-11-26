---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLog/MomentsProjectionProgramNative.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/MomentsProjectionProgramNative.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/MomentsProjectionProgramNative.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

### `scanMask_eval`

 The mask service preserves all tape fields outside work/key/newkey. 

### `emit_eval`

 Emit one framed record without touching the outer source or accumulated output. 

### `header_eval`

 Copy one unary field to the reversed output key, including its delimiter. 

### `rewriteKey_eval`

 The key rewriter reads the two unary fields and then scans precisely the mask. 

### `hit_eval`

 A successful record is prepended to the reversed accumulator. 

### `clean`

 All scratch tapes are empty at a record boundary. 

### `record_eval`

 One dictionary record is filtered by exact equality of its support mask. 

### `records_eval`

 The dictionary traversal is a genuine while loop, with one pass over each record. 

 A fixed finite program for exact-support projection of a raw sparse dictionary.
Coefficients are opaque framed payloads. No normalization or arithmetic is used. 

### `input`

 Serialized target-mask and dictionary input. 

### `serializedEval`

 Primitive instruction trace with explicit serialized input and output. 

### `primitive_serializedEval`

 The native program lowers to the primitive bit-machine with only its fixed
instruction-table overhead. The dictionary size already includes coefficient bits. 
