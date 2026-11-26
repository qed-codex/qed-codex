---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/CodeCandidateProgram.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/CodeCandidateProgram.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/CodeCandidateProgram.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 Fixed-table conversion of one odometer tuple to one arithmetic candidate.
The input contains only the current candidate. The output is reversed scalar
frames, directly suitable for the existing word and matrix callbacks. 

### `zeroTupleProgram`

 Construct the zero candidate from a runtime unary dimension word.
The instruction table is independent of the dimension. 

### `initialize_trace`

 Empty dimensions produce the one-bit empty tuple, not an absent witness. 

### `initialize_call`

 The dimension is consumed from one caller port; all other caller tapes
survive the concrete constructor call. 

### `convert`

 `ternary = false` is the graph alphabet; `true` is the local-code alphabet.
Register 4 reports an unused digit. No candidate family is ever constructed. 

### `convert_trace`

 Complete execution, including initialization, every rejected digit and halt. 

### `convert_prefix_space`

 The bound covers both stacks at every concrete source prefix. This uses
only the linear cost of one candidate conversion, never the search duration. 

### `convert_call`

 Concrete port relocation, preserving the entire off-port caller frame. 

### `firstSuccessStep`

 Retain the first successful current candidate. The callback is actual
fixed native code; it includes all range and mathematical candidate checks. 

### `firstSuccessStep_skip`

 Later candidates still pay the branch, but never overwrite the witness. 

### `firstSuccessStep_accept`

 The successful case pays for copying the entire candidate into the saved
witness port. The temporary copy stack is empty again at return. 

### `firstSuccess`

 Recover the witness flag from its physical stack on every invocation.
The saved tuple is nonempty even for the unique zero-dimensional candidate. 

### `firstSuccess_fresh_accept`

 A fresh selection invokes the real checker after the physical empty-stack
peek. This lemma exposes the success case to the outer iterator invariant. 

### `firstSuccess_update`

 Every real callback invocation performs exactly the first-success saved
word update. This connects native execution to the odometer's rank log. 

### `search_retains_selected`

 Once a native callback has saved a witness, every subsequent callback
and odometer increment preserves those exact bytes. 

### `search_reaches_success`

 A covered successful candidate forces a nonempty native result. This
uses the actual occurrence and its remaining execution, without choosing an
abstract matrix or materializing a family of candidates. 

### `search_runs`

 Full fixed-control scan, with each failed matrix, post-success branch and
final odometer reset charged. The invariant is a concrete checker contract. 

### `firstSuccess_fresh_space`

 Selection composes the checker's uniform prefix bound with only a local
linear-time copy. The checker may run for exponentially many steps. 

### `firstSuccess_saved_space`

 Later visits retain the first witness with constant time and bounded
space, even though the odometer still traverses the remaining ranks. 

### `ScanPorts`

 Fixed caller ports: dimension, consumed copy, current tuple, copy scratch,
and one-bit rejection latch. The embedding is chosen before any input. 

### `prepareScan_eval`

 Preparing one streaming scan restores the dimension copy and scratch;
only the counter and the one-bit rejection latch are initialized. 

### `finishScan`

 Read the actual rejection bit, negate it into the acceptance register,
and clear the current counter with all cleanup charged. 

### `scanPreparedStacks`

 State assertion for preparation, not a free input-construction operation. 

### `scanWrapper_resources`

 The native setup, complete core scan, actual Boolean readout and cleanup
form one measured run. Its storage uses the core's prefix bound, never the
core's possibly exponential running time. 

### `searchInitializePorts`

 Outer-search ports are dimension, consumed copy, current tuple, and copy
scratch. No saved-witness sentinel is seeded by this initializer. 

### `prepareSearch_eval`

 Runtime preparation retains one bounded-width tuple, including the
one-bit terminator when the matrix has zero entries. All other stacks survive. 

### `prepareSearch_space`

 Every preparation prefix is bounded by retained input plus linear local
work; no exponential search budget enters this space estimate. 

### `search_resources`

 Complete actual first-success traversal with both resources on its trace.
The callback contract is discharged by the concrete candidate checker; its
uniform prefix bound, rather than its running time, controls loop storage. 

### `firstSuccess_matrix_sound`

 Selection soundness refers to the physical retained matrix, not to an
arbitrary successful element of an abstract family. A preexisting witness is
unchanged; a fresh witness comes from the actual checker's acceptance bit. 

### `firstSuccess_frame`

 Every callback boundary retains the same polynomial word bound. Only the
matrix being tested and the saved candidate may change; all caller words and
the counter survive selection exactly. 
