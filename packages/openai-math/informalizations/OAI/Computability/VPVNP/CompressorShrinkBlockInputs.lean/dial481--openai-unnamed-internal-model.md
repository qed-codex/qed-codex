---
{
  "module": "OAI/Computability/VPVNP/CompressorShrinkBlockInputs.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorShrinkBlockInputs.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorShrinkBlockInputs.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Connecting the shrinking passes to the fixed block

A single persistent arena starts with the two greedy directories. The
ranked AB and CD inputs determine the fused motif worker's term addresses.
The stored terms determine the score, selected placement, arc roles and
child directory. All later slot visitors read the same common layout bit.


### `a`

 The input degree exponent of this shrinking substep in the block schedule. 

### `b`

 The degree exponent of the output level produced by this shrinking substep. 

### `newSites`

 Expression for the packed output site count, multiplying the base-vertex count by the tag
count and residual lane count. 

### `slotTemplate`

 The fixed tag, degree, color and subdivision parameters used to build the ordered output
slots of this shrinking substep. 

### `termVisits`

 The physical motif table has a grid index, a repetition count and eight
supply coordinates for the two layouts. 

### `selectedInputs`

 The level sizes, term-record addresses, selector width and placement operands needed to
score and materialize a selected shrinking term. 

### `slotInputs`

 Role offsets, subdivision counts, cyclic successor and the append/sort
workspace occupy disjoint intervals of the slot arena. 

### `beforeSlices`

 The deterministic header and greedy visits, followed by bundle preparation, term choice and
selected placement before the slice scans. 

### `slots`

 Generate the ordered output-slot visits using this substep's template, selected layout bit,
slot arena and split index. 
