---
{
  "module": "OAI/Computability/VPVNP/CompressionBlock.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressionBlock.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressionBlock.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Executing one block of scheduled compression

The shrinking steps are composed in their chosen order. Each step retains
its execution tree for every branch of the preceding exact kernel. The final
refresh restores the initial degree. The procedure consumes the sum of the
scheduled lane lengths, divides the number of positions by their packing
product, and multiplies the leading energy coefficient by the quarter-bound
factor of Section 7.4.


### `Procedure.reindex`

 Change the presentation of equal indices without changing the exact procedure. 

### `ShrinkProcedures`

 One shrinking procedure per scheduled step, advancing to the next degree exponent with the
prescribed lane consumption, position divisor and shrinking energy multiplier. 

### `RefreshProcedure`

 The final block procedure restoring the initial degree exponent, consuming the final
exponent in lane coordinates and preserving the number of positions with the scheduled
refresh multiplier. 

### `shrinkPrefix`

 The first `j` shrinking procedures in the fixed block. 

### `assembleBlock`

 Run every shrinking procedure and then the refresh, keeping its exact
state execution for every possible term selection. 

### `assembleBlock_error_congr`

 When the constituent numerical bounds agree, the additive error of
the whole block agrees across coefficient rings and parameter assignments. 
