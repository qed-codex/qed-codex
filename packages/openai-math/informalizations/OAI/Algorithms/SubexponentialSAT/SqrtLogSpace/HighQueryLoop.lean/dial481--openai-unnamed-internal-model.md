---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/HighQueryLoop.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/HighQueryLoop.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/HighQueryLoop.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 Concrete high-loop interfaces: the original ternary source count, exact
physical rank order, the fixed stream's durable frame, and its actual native
accumulator. The full loop still requires the actual stream semantics. 

### `residual_count_le`

 Each fixed-high query counts free assignments without pruning original
clause violations; its optional marked violation is part of the source test. 

### `rank_value_le`

 The rank function is the original source function in descending high-ID
order. Out-of-range proof indices contribute zero. 

### `rank_prefix_le`

 This is a mathematical prefix sum only. The machine retains a binary
accumulator and odometer, never this exponential range as a list. 

### `rank_prefix_succ`

 Appending the current residual count advances exactly one rank. 

### `stream_durable_frame`

 Every instruction and compiled prefix of the fixed stream leaves the
whole durable selector/high-counter interval unchanged. 

### `conditioned_durable_frame`

 The paid counter copy and real guard restoration preserve the live
accumulator, durable odometer, and both adder/counter scratch words. 

### `decoded_rank`

 The physical decoder at the beginning of this fixed stream sees exactly
the original descending high-coordinate rank, returned in ascending ambient
order. No arbitrary reindexing is supplied. 

### `add_rank`

 The genuine binary adder consumes a canonical residual answer, retaining
at most ambient n+1 bits even after exponentially many preceding branches. 

### `mass_boundary`

 Exact off-port frame plus the preceding numerical width proof restores a
fixed compact boundary after every real native addition. 

### `mass_prefix_at`

 The native adder's three local words have a fixed polynomial prefix cap.
Arbitrarily retained caller words enter only through the outside maximum. 

### `mass_prefix`

 The canonical public metadata selects the accumulator and residual word. 

### `branch_step_resources`

 This composes one actual fixed conditioned-stream execution with its paid
counter copy, guard restoration and native addition. The exact stream answer
is still an explicit per-run fact to be supplied by the stream proof. The
compact endpoint bound is independent of the transient prefix envelope. 

### `counter_length`

 A complete current high tuple has linear physical length, even when its
numeric value is exponentially large. 

### `advance_boundary`

 One real odometer step restores the same compact boundary. 

### `advance_resources`

 The actual high odometer has only two local stack words. Its complete
prefix bound is a maximum with retained storage; the number of high assignments
never enters this local space estimate. 
