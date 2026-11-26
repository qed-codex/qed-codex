---
{
  "module": "OAI/Computability/VPVNP/LiveEvaluatorInputStages.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LiveEvaluatorInputStages.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LiveEvaluatorInputStages.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Native preparation of the midpoint evaluator input

The four stages write the control, copy the true advice prefix, generate
the zero-exponent runtime field, and install the permuted exponent payloads.
Their executions share ordinary external memory. The source banks are
preserved throughout preparation, and the final bank contains exactly the
tape machine's initial configuration on the advice and true exponents.


### `Layout`

 Public-word addresses and capacities for the two writes preceding the
scatter. Only the occupied prefix of the advised stream is copied. 

### `costBound`

 Cost of all four midpoint stages before linked stage dispatch. 

### `Runs`

 Actual terminated RAM calls for the four phases, in their execution order. 

### `run`

 Given the physical packed advice bank and the incoming and order-advice
buffers, the four fixed native stages produce the actual evaluator input. 

### `Runs.forces`

 Every accepting execution of these four stages uses the indicated empty
branch streams. In particular the preparation cannot multiply path counts. 
