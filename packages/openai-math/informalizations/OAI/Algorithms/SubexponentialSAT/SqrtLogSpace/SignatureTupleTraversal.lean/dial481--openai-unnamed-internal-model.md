---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/SignatureTupleTraversal.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/SignatureTupleTraversal.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/SignatureTupleTraversal.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Cursor semantics for the attained-signature tuple controller

The cursor stores an attained prefix and one numeric candidate. Suspended
ancestors are first occurrences, so the tree branches over attained keys only.
The traces and finite sums below are mathematical specifications; the actual
controller retains neither a trace nor a family of assignments or tuples.


### `Cursor`

 The finite prefix specifies the suspended candidate frames,
in root-to-current order. Exhaustion is represented by `candidate = N depth`. 

### `Event`

 Every probe, including a losing one, every exhausted generator, and every
leaf callback has its own event. None of these domains is stored at runtime. 

### `Step`

 These are exactly the four controller branches, including advancement
only after a child has returned. Root exhaustion alone halts the cursor. 

### `Trace`

 A proof-level weighted trace. Taking indicator weights states exact
visit counts; taking natural costs charges actual source evaluations. 

### `subtreeTotal`

 Weighted subtree size. The recursive sum is over first occurrences only;
the separate candidate sum charges every successful and losing probe. 

### `subtree_trace`

 A complete subtree starts at its first candidate and returns to the
parent's next candidate. This includes the terminal exhaustion test. 

### `levelTotal`

 The exact charge of the invocation domain at one depth. 

### `eventTotal`

 Sum over every internal attained prefix and every complete attained tuple.
Each candidate and exhaustion appears once per internal invocation. 

### `complete_trace`

 Every candidate, exhausted generator and leaf in the attained-prefix
domain is visited exactly once: this holds for arbitrary additive weights. 

### `Iterations`

 Weighted native iterations before the final loop-guard test. This is a
proof relation over actual evaluations, not an executable trace container. 

### `Trace.nativeIterations`

 Transfer the complete semantic path to actual controller iterations.
The same evaluations carry both the time charge and the callback accumulator.
Concrete routines must prove the local `hstep` clause. 

### `native_complete`

 One actual controller traversal realizes the full weighted event sum.
The bound includes its final guard test; setup and compilation are charged by
`SignatureTupleProgram.program_trace` when this traversal is embedded. 

### `eventTotal_le`

 The exact invocation-domain bound, before any uniform polynomial
estimate. Full tuple callbacks are charged on the same event sum. 

### `costWeight`

 Per-candidate comparison charge; the index is a binary counter value,
not a retained word length. The rescan uses precisely its predecessors. 

### `eventTotal_cost_le`

 The stronger runtime scale needs only one square of each head's raw
assignment count, multiplied by the attained-key product. 

### `callbackWeight`

 Only leaves alter the mathematical callback accumulator. 

### `eventTotal_pair`

 Cost and exact callback value share the same weighted traversal. 

### `native_complete_bounded`

 A concrete controller satisfying the local cursor invariant runs every
attained tuple callback once, with the squared-head cost on that same run.
This is the native integration lemma; its local clauses must be discharged
by the actual probe, frame, loader and callback commands. 

### `representativeWords`

 Exactly one bounded binary assignment word per retained ancestor. 

### `representativeFrames`

 The deepest ancestor is first on physical representative stack 837. 

### `representativeFrames_pop`

 Popping an ancestor restores precisely the previous dependent prefix. 

### `cursorFrame`

 The frame order is the actual save-cursor command's order: remaining
first, then candidate. Both values use fixed polynomial word lengths. 

### `retainedFrames_length_le`

 Both persistent frame banks together use polynomially many actual bits,
including framing delimiters for empty heads. 

### `representativeKernelEquiv`

 Reloading or changing the faithful physical encoding of a full key does
not change its first-occurrence candidate. The equivalence fixes every index. 

### `duplicateScan_kernel`

 The actual predecessor latch depends only on full-key equality. Only
the comparisons that are really visited occur in this premise. 

### `actual_fresh_iff_model`

 The byte-key rescan's actual fresh bit is exactly the first-occurrence
predicate of the stable mathematical full signature. 

### `rangeLabelEquiv`

 The finset subtype used by head grouping and the set-range subtype used
by first occurrences have the same actual label, with no added restriction. 

### `representativeLabelEquiv`

 A bounded assignment enumerator reindexes attained labels without
requiring its chosen representative to satisfy a correction restriction. 

### `sum_representative_labels`

 This is exactly the attained-label sum appearing in the restricted
grouping theorem. Full raw head rescans remain inside each callback value. 

### `retainFrames_state`

 The actual record-then-save commands install precisely the dependent
child prefix in both persistent banks and empty their consumed words. 

### `returnFrames_state`

 Dropping the just-finished representative and restoring the two saved
cursor words gives exactly `Fin.init`, before the paid parent increment. 
