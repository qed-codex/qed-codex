---
{
  "module": "OAI/Computability/VPVNP/EvaluatorSafetyTransfer.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/EvaluatorSafetyTransfer.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/EvaluatorSafetyTransfer.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Storage bounds for short branches and streamed queries

A short nondeterministic routine can increase a stack by at most its instruction
count. A deterministic long-running subroutine instead supplies the independent
peak bound along its actual run.


### `safe_of_allStops`

 Add a reserved continuation clock and a peak bound to a short all-path
execution. Only the routine's own instruction count is charged to its storage. 

### `Bounded.of_space_runs`

 A deterministic, space-bounded coordinate query satisfies the scheduler's
all-path contract even when the query time is exponential. 
