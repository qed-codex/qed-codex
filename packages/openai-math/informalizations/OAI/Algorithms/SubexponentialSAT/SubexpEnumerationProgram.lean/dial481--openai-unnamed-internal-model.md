---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SubexpEnumerationProgram.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SubexpEnumerationProgram.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SubexpEnumerationProgram.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Encoded interval enumeration by fixed finite control

A current label and a remaining count live on little-endian Boolean stacks.
The program invokes an actual body command once per label and advances using
verified finite-table increment/decrement routines.  Mathematical state
embeddings below occur only in execution proofs; no instruction evaluates an
arbitrary semantic function.


### `Ports`

 Fixed counter ports, independent of all runtime binary values. 

### `install`

 A proof-level frame embedding; executable code uses only its fixed port maps. 

### `ripple_local_trace`

 Actual complete carry/borrow trace, preserving the caller's flag bit. 

### `zero_local_trace`

 Actual scan/restore trace, including the final halt instruction. 

### `loopCmd`

 Fixed finite control; all growth is in stacks, never in this syntax. 

### `Visits`

 An observation of the actual body entries. Each constructor contains a
real body execution, and the controller transitions are the checked routines. 

### `BodyTotal`

 A callback specification consists of actual finite program executions.
It may change every unreserved register/stack, but preserves the two counters. 

### `enumerate_correct`

 Every input has an actual execution whose body-entry observations are
exactly the requested consecutive labels, with no omission or duplication. 

### `Visits.flag_fold`

 An external Boolean result flag folds the actual callback tests in visit
order. The controller never reads or changes this unreserved flag. 

### `Visits.flag_fold_of_invariant`

 Invariant-aware form for callbacks whose correctness needs a fixed
candidate word, a positive divisor, or other preserved caller data. 

### `Visits.output_fold`

 Prepending each computed row to an unreserved output stack records rows
in reverse visit order. Every row equation concerns an actual body execution. 

### `Visits.output_fold_of_invariant`

 The row-fold theorem with a preserved caller invariant, for fixed clause,
width, or lookup data needed to prove the actual row evaluator correct. 

### `enumerate_size`

 Exact static control size; none of the binary input values occurs here. 

### `program_trace`

 Every structured execution above is an execution of its actual finite
instruction table, including the terminal halt. 

### `skip_enumeration`

 A concrete body with no external correctness assumption: the generated
table traverses the whole encoded interval and ends with its successor. 

### `Visits.steps_le`

 An explicit instruction bound for a recorded traversal. `C` bounds actual
callback evaluations; `L` and `M` bound the current and remaining word widths. 

### `enumerate_bounded`

 A uniform bound with all growing encoded widths and the callback cost
visible. Leading zeroes are allowed in both counters. 
