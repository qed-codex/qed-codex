---
{
  "module": "OAI/Computability/VPVNP/GraphRounding.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/GraphRounding.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/GraphRounding.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Rounding a symmetric stochastic matrix to a regular multigraph

At the end of Section 5.2 of *VP and VNP differ over every field*, arc
multiplicities are rounded up from half the desired degree times each
transition probability. The missing arcs are loops. The normalized walk
of the resulting multigraph preserves at least half of every edge energy.


### `rowSupport`

 Entries charged one unit of possible rounding error in a row. 

### `ceilingArcs`

 The integral arc multiplicities before loops are added. 

### `ceilingArcs_row_le`

 The loss from rounding up is at most the number of nonzero entries. 

### `roundedArcs`

 Padded arc multiplicities. A loop counts as one outgoing arc. 

### `roundedArcs_symm`

 Rounding and adding loops preserve symmetry. 

### `roundedArcs_row_sum`

 Every row has total degree exactly `h` when its support has size at most `h / 2`. 

### `normalizeArcs`

 The transition matrix associated to a regular graph's integral arc counts. 

### `normalizeArcs_row_sum`

 Uniformly choosing one of the `h` outgoing arcs gives a stochastic row. 

### `roundedArcs_entry_ge`

 Entrywise lower bound on the normalized rounded transition matrix. 

### `walkEnergy_le_twice_of_half_le`

 Entrywise domination of half of the original walk preserves half of every edge energy. 

### `hasPoincareBound_of_half_le`

 The entrywise energy comparison gives a factor of two in the Poincaré bound. 

### `roundedArcs_hasPoincareBound`

 Rounding a walk with Poincaré bound `γ` costs at most a factor of two. 

### `exists_regular_rounding`

 Simultaneous realization for every metric target of a sparse symmetric stochastic matrix.
The regular degree is a power of two between twice and four times the support bound. 
