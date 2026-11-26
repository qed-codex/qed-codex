---
{
  "module": "OAI/Computability/VPVNP/RankQueryStackEngineSpace.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RankQueryStackEngineSpace.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RankQueryStackEngineSpace.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 # Polynomial stack space with expensive scalar-entry calls

The descriptor can invoke another complete matrix or coefficient computation.
Its time may be exponential while its space stays polynomial. The execution
below links its bounded run directly. The other Schur actions have polynomial
instruction budgets and reuse the same workspace between transitions.


### `DescribeBounded`

 Scalar reads in the descriptor have independent time and space bounds.
The caller's suspended frames are present throughout the subcall. 

### `boundedSpace`

 The descriptor subcall and the short local transitions share the same tapes. 

### `boundedStepTime`

 Maximum one-step time allowance covering descriptor evaluation and the other engine
transitions. 

### `eval_run_bounded`

 Simulate the full Schur recursion with an exponential-time, polynomial-space
descriptor while preserving both bounds across each linked action. 

### `eval_root_bounded`

 The physical root call returns the requested coefficient with a cap independent
of the time spent inside scalar-entry queries. 
