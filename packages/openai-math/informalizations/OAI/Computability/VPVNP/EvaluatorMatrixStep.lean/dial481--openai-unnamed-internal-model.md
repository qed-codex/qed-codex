---
{
  "module": "OAI/Computability/VPVNP/EvaluatorMatrixStep.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/EvaluatorMatrixStep.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/EvaluatorMatrixStep.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Streaming one matrix-index path of the finite algebra evaluator

A linear step chooses its next basis index once, reads that single matrix
entry, and multiplies the running weight. The routines before and after the
choice are deterministic. The count formula allows their costs to depend on
the index and passes the exact remaining fuel to the next matrix step.


### `matrixStep`

 The first routine prepares the basis dimension. After the binary choice,
the second routine queries the chosen entry and updates both the current index
and the field product, keeping only the data for the next step. 

### `matrixStep_count`

 Count a machine step, with arbitrary subsequent computation. The per-index
postprocessing times need only admit a common bound. 

### `matrixStep_count_of_bound`

 A common step budget allows every branch to be charged its own actual
query time. The delays are independent of the choice of continuation. 

### `residueBranches`

 Convert the running field product to its prime-field residue. A failed
endpoint test sets the bound to zero. A successful endpoint test uses the
residue word as the bound and each legal choice accepts immediately. 

### `residueBranches_count`

 For the terminating routine the ordinary integer leaf count equals the
encoded residue, at every clock that covers its two routines and final halt. 
