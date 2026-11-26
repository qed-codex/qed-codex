---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/HashGreedyRound.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/HashGreedyRound.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/HashGreedyRound.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 Concrete streamed greedy rounds. The query seam below consists of actual
executions of the fixed attempt command; it must be instantiated by the native
exact-query implementation before an endpoint theorem can use these results. 

### `Boundary`

 Only the incumbent and two odometer ports vary across candidate boundaries.
The candidate/score ports are restored to the initial empty words. 

### `body_execution`

 Every actual candidate, including losing candidates, pays the attempt and
native comparison costs. No candidate family is allocated in the machine. 

### `body_spec`

 Instantiate the real finite iterator from the paid native attempt traces.
The only changing stored values are the incumbent and bounded odometer. 

### `body_refines`

 Determinism identifies every actual update trace with the measured native
one, including its restored scratch and the next odometer boundary. 

### `scan_minimum`

 The complete native scan returns an attained minimum, preserves every
fixed caller word, and resets the singleton counter for the next round. 

### `round_minimum`

 One complete fixed native round: paid seed, all candidate visits, native
comparison, one attained winner append, and charged outer flag restoration.
The mathematical range in the conclusion records the trace; it is not stored. 

### `chosenEntry`

 Proof-level name for the deterministic cached minimum. The finite machine
uses its binary counter and two entries, not this mathematical recursion. 

### `RowBoundary`

 The history and remaining unary count are the only words changed by outer
round control. All other retained parameters keep their literal contents. 

### `rounds_history`

 Actual unary-controlled iteration of complete native rounds, with literal
history serialization and exact caller-frame preservation. The query cost is
needed only at the bounded histories that this execution can reach. 

### `encodedHistory_iter_length_le`

 The physical serialized history grows only by the selected bounded row.
The exponentially many losing payloads never contribute to this retained word. 

### `chosen_contraction`

 Contraction averages over the original reference family. Extra decoded
binary candidates can repeat rows without changing the argument. 

### `iter_mass_zero`

 The deterministic rows serialized by the actual outer run have zero
violation mass at the supplied original square-root-log loop cap. 
