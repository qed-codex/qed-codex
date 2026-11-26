---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SubexpRecordScan.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SubexpRecordScan.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SubexpRecordScan.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Fixed-control selection of serialized coefficient records

The inner record body is `frame key ++ frame coefficient`. All execution
claims below are traces of fixed Boolean-register/stack instruction tables.


### `parseFrame`

 The existing frame parser relocated to two named ports. 

### `parseFrame_eval`

 Actual parser execution on arbitrary surrounding register/stack data. 

### `afterClear`

 The register/stack state after clearing a scratch port. 

### `rawSkip`

 Enter the existing raw-frame routines, rather than their tagged-list entry. 

### `selectPayload`

 Conditional payload selection keeps the entire frame and its boundary. 

### `compareKeys_eval`

 Actual bit-string comparison, with preserved surrounding ports and
bounded leftover lengths for the following cleanup loops. 

### `oneRecord`

 The entire inner-record selector is one fixed structured program.
Every call here is a fixed finite instruction table. 

### `oneRecordProgram`

 The actual compiled Boolean-stack machine; its control size is independent
of the encoded key and coefficient lengths. 

### `recordCost`

 The exact structured execution bound for one serialized inner record. 

### `oneRecord_eval`

 One record is consumed; the query is restored; all three scratch ports
are empty; and the complete coefficient frame is selected exactly on key
equality. The Boolean result remains in register 4. 

### `oneRecord_trace`

 Actual fixed-table traces, including the final halt instruction. 

### `recordCost_le_encoded_length`

 The measured bound is linear in actual encoded input lengths. 

### `oneRecord_fixedKey_trace`

 Matching the concrete exponent-key encoding is exactly matching exponent
indices, by the independently proved encoding injectivity. 

### `oneRecord_primitive_runs`

 The fixed-table trace also lowers to the actual primitive bit-machine
model, with the compiler's proved constant overhead. This is a component
configuration boundary, not a claim about a complete raw-input SAT solver. 
