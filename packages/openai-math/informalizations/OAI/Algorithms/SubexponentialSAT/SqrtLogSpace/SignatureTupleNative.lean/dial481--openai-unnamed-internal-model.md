---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/SignatureTupleNative.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/SignatureTupleNative.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/SignatureTupleNative.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Concrete adapters for the attained-signature tuple controller

The cursor primitives are fixed in `SignatureTupleProgram`. This module
installs the actual head loader and predecessor predicate on the shared leaf
ABI, and relates their physical state to the attained-prefix traversal.


### `initializeLevelsCommand`

 Copy the runtime palette size and initial physical head address into two
persistent controller tapes. The active flag is set even for zero heads, so
the empty tuple reaches the callback exactly once. 

### `rescanStacks`

 The scratch bank is disjoint from the retained ring tables and metadata.
Only the five named persistent source fields are mapped outside340..363. 

### `initializeFreshCommand`

 A real one-bit latch initializer, charged on every predicate call. It
also covers the first call after the loader has cleared its scratch bank. 

### `advanceCandidateCommand`

 A completed duplicate step clears its saved key before the next predicate.
Thus every scan boundary has an empty output key tape. 

### `resetPredecessorCommand`

 On return to a parent, only the predecessor zero word is reset. The saved
candidate and remaining counter are restored and then advanced exactly once. 

### `probeWith`

 The candidate predicate runs only when the complete remaining word is
nonzero. Its one-bit result is copied from the actual latch, not from a key. 

### `descendWith`

 A child starts after one emitted representative is recorded and its
parent's bounded cursor is suspended. All current head arrays are cleared. 

### `resumeParentWith`

 The parent cursor is restored without rerunning its preceding candidate
scans. Only its polynomial-size matrix is reconstructed before the advance. 

### `setupWith`

 Clear every tuple controller tape once at entry. The fixed list has twelve
ports, independent of the input, assignment count, and number of signatures. 

### `assembleRoutines`

 Finite-command assembly used by the concrete loader/predicate adapters.
The exact callback is instantiated by the query evaluator. These arguments
are syntactic programs; this constructor is not the final correctness theorem. 

### `remaining_word_after_advance`

 Decrement retains the full `h+1`-bit remaining word, including leading
zeros. This matches the suspended-frame encoding after every candidate. 

### `initializeLevels_stack_bound`

 The initial head-controller copies and flag operations have polynomial
space at every source prefix, including all persistent caller stacks. 

### `rescan_avoids_tuple`

 Every tuple control tape outside the four current predicate fields is
outside the local rescan's port image. 

### `rescan_lifted_stack_bound`

 The preserved caller frame is charged once when transferring the local
predicate's uniform bound to all896 physical source stacks. 

### `candidateMachine`

 The complete predecessor predicate, on the fixed shared leaf ABI. The
program computes its candidate key before rescanning earlier assignments. 

### `candidate_run`

 The actual complete predicate retains its exact key and freshness result,
with time and all physical source-stack prefixes bounded on one lifted run.
The caller's persistent data are included through `frameBound`. 

### `candidateOutput_control`

 Saved cursor frames, representative frames, depth, remaining assignments,
and the physical head address survive the actual predicate call unchanged. 

### `candidate_eval`

 Calling from a concrete caller requires only its explicit local data
projection, rather than a supplied successful evaluation. 

### `probe_candidate_eval`

 Every nonempty generator probe includes its full-word availability test,
latch initialization, actual complete predecessor scan, and latch readback. 

### `probe_exhausted_eval`

 Exhaustion never runs the candidate scanner. In particular the binary
fuel word can be zero even when it retains leading zero cells. 

### `CandidateReady`

 Exact physical data needed by the rescan. The predicate itself supplies
its evaluation; these are byte descriptions of its input tapes. The latch
may initially contain any word because `probeWith` initializes it. 

### `CandidateReady.probe_projection`

 Preparing a candidate changes only the latch word. The whole fixed local
input projection is then the one used in the proved native rescan theorem. 

### `advanceState_outside`

 No physical tape outside the two counters and their decrement scratch is
changed by advancement. The increment scratch is restored as well. 

### `CursorWords`

 The numeric candidate may reach2^h only at exhaustion. Its retained word
has at mosth+1 bits, and every candidate sent to the scanner has exactlyh. 

### `AncestorStorage`

 These are actual retained controller words at an attained prefix. The
prefix is proof data, while the run stores only the two framed bit stacks. 

### `CursorStorage`

 The same fixed controller state is related to scan, leaf, and halted
semantic cursors. Matrix/cache and accumulator facts are supplied separately
by their concrete program invariants. 

### `ScanStorage.tuple_bound`

 Every tuple-control tape at a scan boundary has a uniform polynomial
word bound. In particular no number of completed probes is added to it. 
