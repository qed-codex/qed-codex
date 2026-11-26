---
{
  "module": "OAI/Computability/VPVNP/DegreeRefreshPass.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/DegreeRefreshPass.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/DegreeRefreshPass.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Degree refresh on dyadic compression states

A degree-`2^a` state spends `a` of its binary lane coordinates on the ports
of the expander. The next state has degree `2^a₀` and the remaining `g`
lane coordinates. Its positions, energy and largest width are related to
the old state by the estimates of Section 7.3 on each admitted branch.


### `splitSlots`

 Split the consumed port coordinates from the remaining lanes of the state. 

### `splitWidths`

 The original widths after the identical split of lane coordinates. 

### `DyadicRefreshChoice`

 Choices of local terms for the dyadic degree refresh, using the split slots and widths of
the current state. 

### `dyadicRefreshNext`

 The degree-restored state uses the port as part of its new base label. 

### `dyadicRefreshPass`

 The exact kernel over an arbitrary solution of the fixed parameter equations,
with every output of the kernel paired with its compression state. 

### `dyadicRefreshPass_place`

 Each old position stays at its own physical port. 

### `dyadicRefreshNext_positions`

 The degree refresh preserves the exact number of positions on every branch. 

### `dyadicRefreshNext_energy`

 Equation (7.3) with the energy and position count of the compression
state. The leading factor is `2^a₀ + 2 K'`, independent of the old degree
when the block is chosen by `exists_expander_parameters`. 

### `dyadicRefreshNext_width`

 The field bound of the degree refresh, stated on the full output state. 
