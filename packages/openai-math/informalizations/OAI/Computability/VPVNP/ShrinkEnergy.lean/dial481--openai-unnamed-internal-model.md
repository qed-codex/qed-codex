---
{
  "module": "OAI/Computability/VPVNP/ShrinkEnergy.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/ShrinkEnergy.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/ShrinkEnergy.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Energy of the surviving wires in a shrinking step

Section 7.2 of *VP and VNP differ over every field* applies the six-party
identity separately at each motif, then chooses one layout for the entire
list of terms. The chosen layout retains at most half the total supply
energy. Subdivision into the graph's integral slots incurs the multiplicative
mass loss and a rounding error of at most one quarter per slot.


### `groupEnergy`

 Energy in one of the two surviving supply groups, at actual mass `p*q`. 

### `chosenLayout`

 One deterministic choice of layout for the whole list. Equal costs retain
BC, BN, CN and DM (`false` in `SurvivingSlots`). 

### `slotWidth`

 Actual widths on the subdivided genuine arc IDs. 

### `group_sum_le`

 Scaling the relative masses of Lemma 6.2 by `p` also scales the
additive energy allowance per motif by `1/p`. 

### `parallel_energy_le`

 Summed rounding cost after choosing a layout, including every parallel slot. 

### `shrinking_step_le`

 Substitute each six-party identity, choose the smaller layout, and
regularize the surviving widths. The displayed errors account separately
for splitting the thick bundle, selecting a motif term, and rounding slots. 

### `roundingConstant`

 A common quadratic error coefficient for all position counts, widths and
term lists at the fixed old and new degrees. `Q` is the number of AB pieces. 

### `equalArcMass`

 Uniform mass of a single arc on a degree-`d` graph on `V`. 

### `packed_energy_le`

 Equation (7.2) for an actual packed graph. Each motif uses one selected
supply term. The chosen layout is shared by every motif. The error coefficient
depends only on the degrees, number of color bits, relative masses, subdivision
and fixed conversion constants. 
