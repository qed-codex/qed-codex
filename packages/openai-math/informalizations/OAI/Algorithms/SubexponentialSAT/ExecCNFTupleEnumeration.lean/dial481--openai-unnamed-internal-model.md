---
{
  "module": "OAI/Algorithms/SubexponentialSAT/ExecCNFTupleEnumeration.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/ExecCNFTupleEnumeration.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/ExecCNFTupleEnumeration.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Actual overflow-controlled enumeration of framed binary tuples

The callback is fixed executable code. Every iteration invokes it and then
invokes the concrete framed odometer, including the final overflow increment.
The number and widths of records are never part of finite control.


### `Visits`

 The log contains the payload rank at every actual callback invocation. 

### `BodySpec`

 The only callback premise is a measured execution of actual fixed code,
preserving the tuple and scratch ports while maintaining its data invariant. 

### `loop_exists`

 Every remaining payload rank is visited exactly once. The induction is on
the semantic remaining count; that number does not occur in executable code. 

### `enumerate_correct`

 From zero payloads, the actual callback log is exactly all ranks below
2^B. It includes the callback and overflow increment at the final rank. 

### `enumerate_size`

 Fixed syntax size: only the chosen callback contributes variable code. 

### `program_runs`

 The finite-table compiler adds exactly the final halt to the full trace. 

### `word_eq_of_length_value`

 Equal-width little-endian words are determined by their unsigned values. 

### `tuple_eq_of_shape_value`

 Fixed component widths and payload rank uniquely identify the tuple. 

### `Visits.hit`

 Every logged rank is attached to an actual callback trace at a tuple of
the prescribed shape; this includes candidates that the callback rejects. 

### `Visits.covers`

 Completeness for all tuples of this shape, hence also for the increasing
in-range tuples retained by the executable guard. 

### `masked_tuple_count_le`

 A core-selector mask followed by r clause indices is one mixed-width
tuple. The bound applies also to m=0, m=1, and r=0. 

### `program_primitive`

 Whole enumeration compiles to primitive tape steps with a constant that
depends only on the fixed callback and fixed port assignment. 

### `fixedBits`

 A mathematical witness used for coverage: exactly w little-endian bits.
The executable enumerator does not call this function or decode a rank. 

### `Visits.covers_indices`

 Every in-range index list and every k-bit selector mask appears in the
actual callback log. An increasing-index guard therefore loses no valid set. 

### `zero_tuple_value`

 The separately implemented zero-tuple constructor satisfies the initial
rank condition even when either dimension is zero. 

### `advanceResult_register_frame`

 Latches outside the three odometer registers survive its entire call. 

### `Visits.stack_fold`

 The persistent witness stack is exactly the fold of actual callback
updates. Incrementing the tuple does not modify that stack. 

### `Visits.stack_fold_of_invariant`

 Invariant-aware witness folding, for callbacks that need a fixed input
formula or a previously saved valid witness in their correctness statement. 

### `masked_program_runs`

 The candidate-loop bound after substituting the core-mask/index shape.
All padded or rejected candidates and the terminal increment remain charged. 

### `Visits.hit_of_invariant`

 Invariants needed by semantic callback correctness are retained at the
actual occurrence, rather than erased when extracting a rank witness. 

### `BodySpec.preserves`

 Determinism transfers the invariant in the callback's existential contract
to the actual callback execution recorded by the iterator. 

### `Visits.hit_with_bodySpec`

 The invariant at every actual rank hit follows from the same BodySpec used
for the runtime theorem; no separate universal callback-correctness axiom is needed. 

### `Visits.covers_with_bodySpec`

 Complete tuple coverage with the input/output invariants needed by the
concrete guard, lookup, and sunflower-checker proofs. 
