---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/SparseCodeProgram.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/SparseCodeProgram.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/SparseCodeProgram.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Sparse rows from the candidates actually selected by the search

The construction below consumes the selected shifts and local matrix explicitly. Its
proofs need their checked Walsh and distance properties, not identity with the old
materialized search's selected candidates. The finite list of final rows is polynomial
size and can be retained; lists of all candidates and all test words cannot.


### `candidates_exist`

 Positive parameter values ensure that a checked graph and local code exist.
The actual streaming search must use completeness to select such candidates. 

### `selectedMatrix_encoding_length_le`

 Dense serialization of the final selected code is polynomial even without
compressing sparse rows. This concerns only the retained result, not the search. 

### `rejectedRank`

 A proof-only predicate on the odometer rank. The native callback computes
this predicate by conversion and the arithmetic checks; it is never an oracle. 

### `local_stream_body`

 Every width-two local-word candidate, including the invalid digits, has an
actual bounded callback execution. Only the persistent OR latch changes. 

### `graph_stream_body`

 The binary graph domain is checked in the same bounded-memory scan; padded
high-bit candidates are charged and physically discarded. 

### `RejectionFrame`

 The iterator may alter its counter and scratch; one Boolean is the only
additional retained result. All other caller stacks have an exact frame. 

### `RejectionBody`

 Intermediate contract for an actual, fixed rejection body. The concrete
local and graph bodies below instantiate this by their native arithmetic traces. 

### `rejection_scan_runs`

 Full actual stream correctness and cost, including every padded candidate,
all losing checks, the terminal increment, initialization, and halt. 

### `local_rejection_body`

 The local-code iterator contract is discharged by the concrete byte-level
checker for every current tuple and every retained caller frame. 

### `graph_rejection_body`

 The Walsh iterator likewise uses the actual graph arithmetic on every
valid character, and physically clears every invalid padded word. 

### `rejection_visits_space`

 The complete stream has a uniform prefix bound independent of its number
of iterations. Each body invocation uses only its polynomial local budget. 

### `no_rejectedRank_iff`

 Exhaustive rank rejection is equivalent to rejecting an actual field
word. This includes dimension zero and all invalid padded bit patterns. 

### `rejection_scan_runs_space`

 Time and space hold on the same complete source trace. The uniform storage
bound contains no exponential iteration count. 

### `local_stream_runs`

 An actual local-code scan decides the full distance property, with time
and all-prefix source space on the same trace, for any supplied matrix. 

### `graph_stream_runs`

 The actual Walsh scan similarly decides Good for every supplied graph,
including failed candidates and the zero-dimensional character space. 

### `localScanPorts`

 The runtime dimension is preserved; every other port here is temporary. 

### `coreSpace`

 The core workspace is polynomial in the initial retained data and one
candidate's arithmetic budget, independently of how many words are checked. 

### `local_checker_runs`

 Complete actual local-matrix checker: it initializes its word counter,
checks every word, computes the Boolean acceptance bit, then clears temporary
state. Time and the uniform source-prefix space bound describe the same run. 

### `graph_checker_runs`

 Complete actual graph-matrix checker: it initializes its word counter,
checks every word, computes the Boolean acceptance bit, then clears temporary
state. Time and the uniform source-prefix space bound describe the same run. 

### `MatrixState`

 The outer search retains only its current tuple, first witness, and a
constant number of linear-size conversion buffers above the checker's ports. 

### `lift_checker_resources`

 A complete checker call keeps its local every-prefix space proof after
embedding; the eight persistent outer-search stacks are counted separately. 

### `matrixCandidate`

 The branch accepts only properly encoded matrices; the actual checker
then decides its algebraic property by its inner complete word scan. 

### `matrix_candidate_invalid`

 Invalid matrix digits are rejected by actual finite control and all of
conversion's retained buffers are cleared. 

### `matrix_candidate_valid`

 This composition lemma charges conversion and replacement locally, while
using the separately proved complete checker's space bound for its long scan.
The next two theorems instantiate this interface with the actual checkers. 

### `local_matrix_candidate_runs`

 Every current outer-counter tuple is processed by the actual local matrix
command, including invalid scalar digits and losing code candidates. 

### `graph_matrix_candidate_runs`

 The graph search likewise processes every current two-bit matrix tuple;
the only accepted physical matrix satisfies the actual Walsh checks. 

### `candidateSpace_le`

 The streamed checker's retained workspace is a fixed linear polynomial
in its input words, dimensions, and one arithmetic callback budget. 

### `candidateBudget_le`

 New staging, validation, and complete inner checking add only a fixed
linear factor to the explicit original arithmetic and word-scan budget. 
