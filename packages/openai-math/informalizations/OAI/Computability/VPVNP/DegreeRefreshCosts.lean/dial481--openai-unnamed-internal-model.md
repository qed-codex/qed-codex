---
{
  "module": "OAI/Computability/VPVNP/DegreeRefreshCosts.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/DegreeRefreshCosts.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/DegreeRefreshCosts.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Cost of each admitted expander-motif term

Apply the fixed block of Theorem 6.1 with unit mass on each internal tie
and mass `D / d₀` on each expander arc. A payload is admitted by its weighted
norm. Its wire carries both that payload and the common list of selectors.
The same padded widths are used in the actual slots for the energy bound and
the maximum-width bound.


### `RefreshBlock`

 Fixed motif block converting refresh tie wires into the specified supply on the port graph. 

### `termWidths_energy`

 Convert the executable admission condition on the outer payload into the
normalized termwise energy inequality needed in the refresh. 

### `term_repetitions_le`

 A surviving motif entry uses one scalar parameter per block repetition.
This number is bounded linearly in the maximum old width for a fixed port count. 

### `admitted_actual_energy`

 Equation (7.3) for each admitted collection of expander payloads,
with the selector bits included on every internal supply arc. 

### `admitted_actual_width`

 For every admitted collection of block choices the same bound on field
lengths works at all the actual slots, independently of the old graph and lanes. 

### `expander_branch_energy_le`

 Equation (7.3) for every branch of `expanderRefreshStep`. In the block
chosen by `exists_expander_parameters`, the coefficient `K'` equals
`2 * γ * d₀ / dH + 1`, so the leading coefficient is uniform over port counts. 

### `expander_branch_width_le`

 All external, internal and padding widths in an admitted branch of
`expanderRefreshStep` obey the same linear bound in the largest old field. 
