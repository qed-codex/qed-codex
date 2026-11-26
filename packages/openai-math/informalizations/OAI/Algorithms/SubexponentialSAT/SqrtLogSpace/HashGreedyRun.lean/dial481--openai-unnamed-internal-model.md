---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/HashGreedyRun.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/HashGreedyRun.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/HashGreedyRun.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 Concrete CNF scores instantiate the actual unary-controlled greedy run.
The only execution seam is the actual per-mark query. Initial-code distance
is used only for the final zero-mass and exact model-set consequences. 

### `rounds_eval`

 The complete native rounds retain exactly the deterministic CNF history.
No separate candidate evaluator or aggregate mass oracle is assumed. 

### `staged_boundary_attempt`

 Concrete per-boundary staged attempt, with a uniform cost over the actual
history-byte domain. Its frame reconstruction is shared by time and space proofs. 

### `exit_exact_models`

 The literal history returned by the native run accepts exactly the ambient
models. Its unmarked count is the exact CNF count, and positivity is SAT. This
is a semantic readback, not a claim that the final unmarked query has run. 
