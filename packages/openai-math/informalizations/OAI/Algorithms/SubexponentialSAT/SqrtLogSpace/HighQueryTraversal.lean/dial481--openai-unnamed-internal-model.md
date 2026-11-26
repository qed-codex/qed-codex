---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/HighQueryTraversal.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/HighQueryTraversal.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/HighQueryTraversal.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 The actual fixed high-counter loop. The induction index and prefix sum
are proof data only; executable syntax retains one bounded-width odometer and
one binary accumulator. The concrete per-rank stream proof is supplied by the
downstream count integration, not by a runtime callback. 

### `while_step_space`

 Prefix composition for a tested loop, before specializing its fixed body. 

### `while_done_space`

 The final false guard does not allocate stack words. 

### `overflow_counter`

 At overflow the fixed-width physical odometer returns its unique zero
tuple, including the empty tuple when the high set is empty. 

### `loop_run`

 Direct induction over the remaining numerical ranks executes the fixed
branch and the real odometer, including the final overflow. Every boundary
returns the same B; intermediate prefixes use a separate uniform maximum.
The branch premise names the fixed actual command and remains explicit only
in this compositional support theorem. 

### `high_loop_run`

 The real initializer, all high ranks, final overflow, false guard and
compiler halt are paid in one run. An empty high set still executes one
branch. The endpoint word bound is B, independently of the visit count. 
