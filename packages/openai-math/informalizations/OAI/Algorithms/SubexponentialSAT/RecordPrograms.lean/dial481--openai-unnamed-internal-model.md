---
{
  "module": "OAI/Algorithms/SubexponentialSAT/RecordPrograms.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/RecordPrograms.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/RecordPrograms.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 A reusable actual iterator over the project's framed-record representation.
The callback is a fixed structured program, whose executions are measured in the
same semantics as the parser and iterator. It is never an atomic semantic oracle.


### `CallbackContract`

 The contract describes measured executions of the fixed callback code.
Only the actual parser and callback execute; the predicate and budget are specs. 

### `reader_eval`

 The callback receives the reversed payload, with every auxiliary port framed. 

### `afterTag`

 State just after the outer list marker has been read. 

### `loop_run`

 Measured loop execution, including the final failed loop guard. 

### `iterate_run`

 One fixed iterator handles all record counts and payload lengths. The
bound sums genuine callback executions and parser/guard instructions. 

### `CallbackContractWith`

 A callback contract that additionally records its change to auxiliary data. 

### `Visits`

 The ordered auxiliary effects of all callbacks actually visited before
the first successful match, or until the list ends. 

### `iterate_run_with`

 The effect-sensitive form is useful for map/filter/fold builders. 

### `program`

 A finite instruction table for the iterator and its fixed callback. 

### `program_budget_le_input`

 Linear callbacks give a polynomial bound in the actual serialized input,
with all payload bits and record delimiters included. 

### `Visits.fold_of_false`

 When every callback continues, its auxiliary-state relation folds over
the whole input list in order. This supports exact filter/map output proofs. 

### `CallbackContractOn`

 A typed callback only needs to execute on payloads satisfying its schema. 
