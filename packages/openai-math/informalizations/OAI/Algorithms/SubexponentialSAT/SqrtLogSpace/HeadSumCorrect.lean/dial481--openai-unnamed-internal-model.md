---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/HeadSumCorrect.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/HeadSumCorrect.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/HeadSumCorrect.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 Semantic correctness of the concrete head accumulator. Native dictionary
witnesses are retained only for the current partial sum, and their meaning is
proved using the actual finite-ring normalization program. 

### `accumulate_decode`

 Every actual addition-and-reset execution puts the sum of the two decoded
arrays on853. This also covers an empty or zero-valued assignment product. 

### `normalized_partial_sum`

 The mathematical partial-sum invariant advances by the actual decoded
addition, without choosing a synthetic implementation of an assignment. 

### `initial_stacks`

 The first semantic loop state is produced by the paid cleanup and seed.
The head accumulator is the actual empty dictionary, and only the named
counter words are installed in addition to the reclaimed workspace. 

### `initial_word_bound`

 The paid initial state restores the compact boundary used between all
assignments. The transient source-prefix envelope is not fed into this bound. 

### `advance_word_bound`

 Candidate increment and fuel decrement restore the same compact boundary,
including the final overflow word that is never passed to the evaluator. 

### `chosen_free_head`

 The existing native ID selector covers every free coordinate in the
chosen head, including coordinates with no incidences. 

### `freeOrder_eq_headOrder`

 The reviewed source order equivalence names the same positions as the
actual head-size word and ID stream; it introduces no executable reindexing. 

### `counter_sum_eq_head`

 Reindex the semantic head sum along the already proved source order.
Only the finite mathematical sum is transported; the machine still uses its
single bounded-width bit counter. 

### `candidate_correction_iff`

 The concrete correction gate tests the selected original coordinates of
the typed head, using the same order as its assignment counter. 

### `prepared_head_update`

 The paid ambient overlay realizes exactly the candidate substitution used
by restricted grouping, while retaining the fixed-high assignment. 

### `gate_source_iff`

 The actual full key and correction words admit exactly the intended
original-coordinate signature fiber. Every raw matrix row is retained. 
