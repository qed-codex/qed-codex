---
{
  "module": "OAI/Computability/VPVNP/CompressorShrinkABSliceRecipe.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorShrinkABSliceRecipe.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorShrinkABSliceRecipe.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Whole-level calendar visits for the shrinking AB slice bank

Each fixed field count or rank pair contributes one catalog visit. The global
cursor ranges over assigned bundles. Register operands are computed from
that ordinal and the level's four sorted width/offset heads.


### `Inputs`

 Layout scalars read by the online planner. 

### `Inputs.rows`

 Recipe expression for the number of bundle rows visited in each whole-level AB scan. 

### `Inputs.oldStarts`

 Base-address expression of the old thick fields' starting offsets. 

### `Inputs.oldWidths`

 Base-address expression of the sorted old thick-field widths. 

### `Inputs.oldStride`

 Distance in words between consecutive bundle rows of the old width and start columns. 

### `Inputs.newStarts`

 Base-address expression of the starting offsets of the new AB pieces. 

### `Inputs.newWidths`

 Base-address expression of the new AB piece widths. 

### `Inputs.newStride`

 Distance in words between consecutive bundle rows of the AB width and start columns. 

### `Inputs.firstBank`

 Recipe expression for the address of the first bundle's intersection and
  endpoint-reference bank. 

### `Affine`

 Global-row address and stride of one local operand. All AB reads use
direct affine operands, so the worker prologue itself uses zero probes. 

### `constant`

 Represent a constant flat-row operand by its literal base and a zero bundle stride. 

### `bankField`

 An operand at a fixed offset inside each bundle's AB bank, with the full bank capacity as
its inter-bundle stride. 

### `arguments`

 Encode the local affine operands and fixed field cursor as flat-row prologue parameters,
with a base, stride and zero bias for each. 

### `flat`

 Compile a local AB worker into a visit that scans every bundle at one fixed local cursor. 

### `clearParams`

 The per-bundle base address from which the clearing worker zeros the endpoint counts. 

### `pairParams`

 Operands for computing a field-pair intersection, including the new field count, both
width/start column pairs, and the frame destination. 

### `refParams`

 The field counts, intersection frames, endpoint counts and reference arrays used to link
positive intersections into the two directories. 

### `Stage`

 One indexed whole-bundle scan that clears endpoint counts, computes an intersection frame
or appends its endpoint references. 

### `stage`

 Select the clear, pair or reference worker and build its whole-level visit at the specified
local index. 

### `phases`

 The AB execution order, clearing every endpoint count before computing all field-pair
frames and then linking their references. 

### `visits`

 The catalog visits implementing the complete AB schedule for the given input columns and
field counts. 

### `Describes`

 The recipe expressions evaluate to the actual row count, bank origin, and old and AB column
heads and strides. 

### `evaluated`

 The flat worker's concrete public words obtained by evaluating its affine parameter
expressions and fixed local index in the reference memory. 
