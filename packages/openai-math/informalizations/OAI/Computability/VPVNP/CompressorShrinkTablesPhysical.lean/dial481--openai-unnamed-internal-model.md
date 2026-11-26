---
{
  "module": "OAI/Computability/VPVNP/CompressorShrinkTablesPhysical.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorShrinkTablesPhysical.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorShrinkTablesPhysical.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 # Allocated tables for the AB, surviving-width and ordered-slot passes

At a live shrinking level the selected rows end in table zero. The interval
records and widths fit in the following two tables, and the native slot passes
end in table three. The calendar reads their starting addresses from the same
published header as the prefix. Scalar bounds hold uniformly on the selected
states once the input length reaches the word-capacity threshold.


### `TableSpace`

 The address bounds used by all three workers and by the preceding hidden-map frame. 

### `table_space`

 Specialize the compiled block endpoints to the three separately allocated tables. 

### `TableArithmetic`

 Uniform arithmetic capacity for the surviving and AB workers. The address
argument of `fields` is discharged by `table_space` after allocating the level. 

### `withAB_physical`

 The post-hidden memory drives the actual three-table workers. The AB operand
readbacks refer to that memory and therefore also describe its source trace. 
