---
{
  "module": "OAI/Computability/VPVNP/CompressorShrinkTermRecipe.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorShrinkTermRecipe.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorShrinkTermRecipe.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Online row planners for the shrinking motif gather and selection

Both phases visit one row per CD occurrence. The packed AB width and offset
rectangles precede the dense pair array, followed by the selected term rows.
The sorted CD widths occupy the second half of the sorted-width rectangle.
The planner obtains its shape scalars and allocation heads from level expressions.


### `Inputs`

 Dynamic scalars and addresses read by the two planners. 

### `Inputs.vertices`

 Expression for the number of input base vertices at the selected shrinking level. 

### `Inputs.degree`

 Expression for the input degree used to count bundles and old port slots. 

### `Inputs.lanes`

 Expression for the number of input lanes per base vertex before shrinking. 

### `Inputs.residualLanes`

 Expression for the residual lane count used to enumerate packed bundles. 

### `Inputs.sortedWidth`

 Base-address expression for the two sorted thick and CD width rectangles. 

### `Inputs.sortedStride`

 The row stride expression shared by the per-bundle sorted-width rectangles. 

### `Inputs.abStart`

 The starting address expression for the balanced AB pieces, ahead of the dense pair and
  term tables. 

### `ranks`

 Number of CD motif ranks per bundle, computed from the input degree and the shrinking color
count. 

### `bundles`

 The runtime bundle count obtained from base vertices, tags, residual lanes and input
degree. 

### `oldSlots`

 The runtime count of old directed slots over all base vertices and input lanes. 

### `count`

 Total number of dense term visits, one for every bundle and motif rank. 

### `cdStart`

 The head of the sorted CD widths, following the entire thick-width rectangle. 

### `dense`

 Head of the dense two-word AB/CD demand pairs, following the AB width and offset
rectangles. 

### `term`

 Head of the selected term records, immediately after all dense demand pairs. 

### `stopAddress`

 Exclusive end of the selected term table at the supplied record stride. 

### `gatherOperands`

 The rank counts, sorted stride and AB, CD and dense output heads used by the paired demand
gather. 

### `termHeads`

 The selector's dense demand base and stride of two, followed by the selected term base and
record stride. 

### `gatherPhase`

 A planner phase launching the paired demand gather from zero over the full dense motif
count. 

### `termPhase`

 A planner phase launching the fused motif term selector with the computed addresses and
fixed supply ordering. 

### `N`

 Number of base vertices in the input state used by the term recipe's address formulas. 

### `B`

 The concrete number of packed bundles in this input state for the given degree and residual
lane exponents. 

### `M`

 The concrete number of dense motif rows, equal to the bundle count times the number of
ranks per bundle. 

### `originalSlots`

 Number of original directed input ports across the base vertices and all uncompressed
packing lanes. 

### `count_card`

 The chosen physical interval indexes every motif exactly once. 

### `four_count`

 Exact cardinality before taking any word reduction. 

### `Describes`

 The input fields describe the current dyadic state and the already packed
source rectangle. The AB width rectangle starts at the supplied allocator cursor. 

### `Installed`

 Read back the physical row emitted by the compiled planner. Fields above
the worker arity contain the zero padding of the shared dispatcher frame. 
