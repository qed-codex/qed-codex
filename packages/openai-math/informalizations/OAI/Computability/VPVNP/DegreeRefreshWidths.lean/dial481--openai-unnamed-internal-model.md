---
{
  "module": "OAI/Computability/VPVNP/DegreeRefreshWidths.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/DegreeRefreshWidths.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/DegreeRefreshWidths.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Widths on the refreshed slots

Each port has one concatenated external field, one field per internal expander
arc, and zero bits on every padding arc. This module charges the resulting
actual slots in the paper's normalization and derives the bound (7.3) from
the internal motif's bound with masses divided by the old arc mass.


### `newWidths`

 Widths of the external, internal and padding slots, respectively. 

### `internalEnergy`

 Energy of the expander slots in a single block. 

### `internalEnergy_of_motif`

 The internal motif inequality uses demand mass one and supply mass
`D / d₀`. Multiplying by the reciprocal old arc mass restores the actual
energies used in the network. 

### `newWidths_energy_le`

 The network estimate (7.3) for the actual refreshed widths, including
the zero-width padding slots. `B` indexes blocks of `D` ports. The leading
coefficient is independent of `D` whenever the chosen motif coefficient is. 

### `newWidths_max_le`

 For fixed degrees and motif coefficients, every new slot has width
bounded by a constant times one plus the maximum old width. The same bound
applies to the concatenated fields read by the external segment ties. 

### `bundleWidths`

 Present the actual old width profile in the source order of each bundle. 

### `refreshedCoordinates`

 Group actual refreshed slots by their block and port, followed by their
outgoing slot number. 

### `actualWidths`

 The profile assigned to the actual slots of the new lifted topology. 

### `actualWidths_energy_le`

 Equation (7.3) in the original and refreshed actual-arc coordinates. The
two half-wire ties use the old graph's residual-lane shift and its port shift,
so all widths may vary with the lane. 
