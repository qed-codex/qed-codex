---
{
  "module": "OAI/Computability/VPVNP/LiveEvaluatorReindexSkeleton.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LiveEvaluatorReindexSkeleton.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LiveEvaluatorReindexSkeleton.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Writing the zero-exponent evaluator input on the live tape

The runtime suffix consists of three unary width fields and one exponent
field, with a zero terminator after each field. The exponent payload symbols
start at zero and are overwritten by the subsequent coordinate scatter.


### `skeletonBit`

 Characterization of the zero-exponent runtime input by absolute address.
The exponent field begins at an odd offset, so its tags have odd addresses. 

### `runtime_zero_at`

 Every generated symbol is the corresponding byte of the actual serialized
evaluator input for the zero exponent vector. 

### `setupOps`

 Public words give the unary width, total number of exponent bits, first
destination symbol address, and total length of the runtime suffix. 

### `skeletonStage`

 Every active path uses eight local control instructions after setup to
select the tape symbol, one write, and one last-cursor test. 

### `execute_active_word`

 An active call is deterministic and emits exactly one symbol write.
The last cell hands off to the next stage in that same call. 

### `events`

 Report for one runtime position: local control ticks, one external write,
and the local cursor test. 

### `skeletonStage_call`

 With the actual evaluator dimensions, the native stage writes the actual
serialized input bit, encoded as a nonblank two-tape symbol. 

### `skeletonStage_sweep`

 The complete runtime preparation uses one deterministic call per symbol.
The four terminating zeros guarantee a nonempty sweep even if either
dimension vanishes. Every address outside the prepared interval is preserved. 
