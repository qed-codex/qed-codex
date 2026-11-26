---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/QueryPairEvaluation.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/QueryPairEvaluation.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/QueryPairEvaluation.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 The actual finite-difference callback uses the physical pair masks and
one semantic node accumulator. The reference support decoding below is used
only in the proof; the executed controller retains its four finite words. 

### `outer`

 The outer support represented by a finite ternary word. 

### `inner`

 The inner support consists precisely of the `some true` positions. 

### `visit`

 This is the additive semantic update performed after the complete tuple
product has been read out. The sign is computed from the actual two supports. 

### `fold_signed_sum`

 The verified native order visits each support pair once, uniformly for
J=0 and J>N. No byte-level representative of a ring element is selected. 

### `sum_pairs_transport`

 Reindex the actual finite-coordinate pair sum by the chosen free-variable
equivalence. The ambient assignment universe is not changed. 

### `framePorts`

 Physical words retained across each complete pair, in addition to the
source and ring masters. These include the current node cursor and address. 

### `Invariant`

 The semantic accumulator and compact off-controller words form the DFS
invariant. The four controller lengths are bounded by its separate geometry. 

### `Invariant.rebase`

 The semantic invariant is independent of both opaque bookkeeping words. 

### `cursor_popped_stacks`

 The callback's preliminary empty-depth pop changes registers only. 

### `cursor_shadow_bound`

 At a callback the two live masks have exactly the active dimension;
erasing only the unread depth/budget words gives the fixed compact cap. 

### `start_run`

 The actual paid pair start preserves the node sum and source witness,
resets851, and installs precisely the ambient images of the emitted masks. 

### `Invariant.query_frame`

 The full tuple provider restores its real query masters. The node word
and outer cursor words consequently retain their exact meaning. 

### `commit_run`

 The concrete signed commit restores the loop invariant at the SAME
compact cap. Its readout is additive and occurs after the complete tuple sum. 

### `pairValue`

 The complete attained-tuple value for the actual emitted free supports. 

### `signed_sum_free`

 The native finite-index sum is the exact free-coordinate sum consumed by
the source-target identity. Both masks retain their ambient-coordinate images. 

### `callback_run`

 One complete callback of the fixed program: actual mask expansion,
the complete attained-tuple DFS, and the actual signed dense commit. 

### `callback_cursor_run`

 The callback remains total when the untouched unary budget is arbitrary.
Only its proof-side shadow erases832/833; the actual run restores both words
and has exactly the same instruction count. 

### `run`

 The fixed native pair traversal computes its complete signed tuple sum.
Correctness, measured time, and every source-prefix stack bound refer to this
same run; no tuple evaluator, callback or byte-family service is a premise. 
