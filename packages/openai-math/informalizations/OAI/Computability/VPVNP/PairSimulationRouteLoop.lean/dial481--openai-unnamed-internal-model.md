---
{
  "module": "OAI/Computability/VPVNP/PairSimulationRouteLoop.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSimulationRouteLoop.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSimulationRouteLoop.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Native counted traversal of cursor routing fields

The field scheduler uses the same three labels for a successor scan, a
phase scan, and the scan of steps within a phase. The body may itself
traverse an inner loop. The traversal theorem counts every test, increment
and body instruction.


### `instruction`

 The loop resets the index, tests it against the exclusive bound and
advances it after the body. The constant-one register is an input. 

### `Linked`

 All three loop-control instructions occur in the enclosing machine. 

### `run_exact`

 Run the fixed loop on a body with an exact per-index instruction count.
The invariant may refer to registers, private memory and the processed prefix. 
