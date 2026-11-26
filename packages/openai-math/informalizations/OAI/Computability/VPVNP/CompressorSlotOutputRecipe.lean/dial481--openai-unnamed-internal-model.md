---
{
  "module": "OAI/Computability/VPVNP/CompressorSlotOutputRecipe.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorSlotOutputRecipe.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorSlotOutputRecipe.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Planning the shrinking output columns

The base inverse, two actual incidence permutations, and width column are
allocated immediately after the sorted slot directory. Their native planner
rows are computed from the selected level's counts and heads. Only the width
worker also reads the head of the already materialized split-width input.


### `Phase`

 The four output passes following base matching, inverting base mates, expanding actual
mates in each direction, and collecting outgoing widths. 

### `arity`

 Number of public words required by each output worker, two for base inversion, five for
actual incidence, and eight for widths. 

### `limit`

 Exclusive output scan bound, counting base ports for the inverse scan and actual ports for
the other three passes. 

### `bank`

 Select the native parameter bank for the requested output phase, including the split-width
input head for the width scan. 

### `frame`

 Controller row containing the output worker tag, zero starting cursor, exclusive stop, and
public parameters. 

### `Columns`

 Native expressions for the additional addresses and the shared lane-slot count. 

### `Columns.count`

 Planner expression for the number of actual outgoing ports, the common length of the two
  mate columns and the width column. 

### `Columns.baseInverse`

 Planner expression for the start of the inverse base-matching column following the base
  displacement column. 

### `Columns.actualOut`

 Planner expression for the start of the actual forward mate column. 

### `Columns.actualIn`

 Planner expression for the start of the actual inverse mate column. 

### `Columns.width`

 Planner expression for the start of the actual outgoing-width column. 

### `Columns.finish`

 Planner expression for the first free address after the last output column. 

### `columns`

 Derive the output count and column boundaries from the current slot level's computed
dimensions and stop address. 

### `ColumnValues`

 Evaluating the planner expressions yields the word encodings of the actual port count, the
four output heads, and the final address. 

### `columnHeads`

 All six heads in the order used by the next level's incidence header. 

### `stop`

 Construct the cursor-stop expression for a base inverse, actual mate, or width scan. 

### `params`

 Construct the ordered parameter expressions for one output worker from the level inputs
and, for widths, the split table head. 

### `phase`

 Assemble one output worker recipe from its dispatch tag, zero starting cursor, computed
stop, and parameter expressions. 

### `padded`

 Extend the output worker's recipe to the scheduler's common parameter count with trailing
zero operands. 
