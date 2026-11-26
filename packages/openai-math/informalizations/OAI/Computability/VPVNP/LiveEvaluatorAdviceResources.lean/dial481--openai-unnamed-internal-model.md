---
{
  "module": "OAI/Computability/VPVNP/LiveEvaluatorAdviceResources.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LiveEvaluatorAdviceResources.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LiveEvaluatorAdviceResources.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Cost of the four linked advice preparation stages

The packed length occupies one row. The actual advice prefix occupies the
rounded-up number of rows and reads a five-word operand frame per call. The
ordinal table uses one row per ordinal. A single initializer publishes the
frames. These bounds charge the native probe logs and the live linker's
dispatch and transfer at each call.


### `prefixCalls`

 The number of calls budgeted to pack the evaluator prefix, including the terminating call
for zero rows. 

### `orderCalls`

 The number of calls budgeted to pack the ordinal rows at the specified bit width, including
the empty-table case. 

### `setupCost`

 The combined probe charge for packing the length, prefix, and ordinal rows and publishing
the four midpoint frames. 

### `prefixCalls_le`

 Ceiling rounding and one reset per row add at most a word of padding
and one extra bit call per occupied bit. 

### `pack_run_bounds`

 The worker clock bound holds even when the caller supplies more fuel.
Successful partial or complete executions consume one report per choice list. 

### `setupReports`

 Reports in the same order as the midpoint branch of the native live
program. Each entry contains the memory from which its operand frame is read. 

### `linkedSetupResources`

 The full four-stage bounds from the native packing runs, the initializer's
actual report, the five cached prefix operands and all dispatch/transfer
events. In the 21-stage live program the largest dispatch clock is 130. 
