---
{
  "module": "OAI/Computability/VPVNP/CompressionPowers.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressionPowers.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressionPowers.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Repeating an exact compressor block

Theorem 7.1 of *VP and VNP differ over every field* repeats the same block
along every branch of its tensor expansion. For the energy estimate (7.4),
adding a fixed multiple of the squared position count to the energy makes
this quantity contract by a factor of four at each block.


### `repeatExecution`

 Execute the same block `T` times, consuming `T*k` lanes and retaining
`g` unused lanes. Each continuation receives its own selected output state. 

### `repeat_positions`

 Every final branch has the exact position count after `T` blocks. 

### `potentialWeight`

 Coefficient of the squared position count in the contracting quantity. 

### `potential_step`

 A single block contracts the energy plus the squared-position correction. 

### `repeat_scaled_potential`

 The scaled contracting quantity along the actual branch-dependent execution. 

### `repeat_totalWidth_le`

 Equation (7.4), with the coefficient of the initial position count given
explicitly. The first inequality controls all final shared wire fields. 

### `repeat_contract`

 The history attached to the repeated execution gives the exact finite
sum of its expanded kernel paths for every assignment of initial factors. 

### `repeatWithLanes`

 For an input with at least `T*k` lanes, keep exactly the unused suffix.
This is the lane-count convention in Theorem 7.1. 

### `repeatWithLanes_bounds`

 Position count and final wire bound for every term, starting with any
number of lanes that suffices for the chosen repetition count. 
