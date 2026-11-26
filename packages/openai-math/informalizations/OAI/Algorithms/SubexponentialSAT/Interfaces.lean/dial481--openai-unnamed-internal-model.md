---
{
  "module": "OAI/Algorithms/SubexponentialSAT/Interfaces.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/Interfaces.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/Interfaces.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Finite reduction and leaf-search interfaces

These lemmas connect a finite OR reduction with executable Boolean leaf tests.
`scan` records the number of calls to its supplied leaf test.  This is **not**
a count of bit operations or Turing-machine transitions.  A machine realization
of the leaf test, the reduction, and this search is a separate obligation.

No declaration here asserts the existence of the manuscript's fast counter.


### `scan`

 Search in order and stop at the first accepting leaf. The second component
counts calls to `test`, not the implementation cost of those calls. 

### `scan_accepts_iff`

 The short-circuit search has the ordinary finite-OR semantics. 

### `scan_calls_le_length`

 The call count is bounded by the number of explicitly supplied leaves. 

### `scan_reject_calls`

 A rejecting search tests every leaf. This also covers an empty leaf list. 

### `finite_or_reduction_correct`

 The finite OR reduction need preserve only existence, not disjointness or
the number of witnesses. Every displayed hypothesis is a semantic proof
obligation; this theorem supplies no reduction algorithm or fast leaf test. 

### `scanCounts`

 Deciding a finite list from its supplied nonnegative integer counts. 

### `scanNonzero`

 The main algorithm can test a lifted ring value for zero directly, without
first decoding the represented integer count. 

### `sat_reduction_correct`

 Correctness glue for Section 6.1. `hcover` is furnished by sparsification;
`hcount` must be furnished by an actual leaf counter. They do not require
disjoint leaves, and duplicate leaves do not affect acceptance. 

### `exhaustive_reduction_correct`

 Concrete exhaustive leaf testing is sufficient for the correctness bridge.
This theorem makes no fast-running-time claim. 

### `sat_residue_reduction_correct`

 The exact interface used by the manuscript's final `H(0) ≠ 0` test.
`hzero` must come from the prime-power count theorem and count bound; it is
not an assumption that an arbitrary residue-field count suffices. 
