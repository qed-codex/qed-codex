---
{
  "module": "OAI/Computability/VPVNP/RefreshMonomialWitness.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RefreshMonomialWitness.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RefreshMonomialWitness.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Scalar witnesses on the dyadic refresh pass

Splitting the old lane into port and remaining lane coordinates reindexes the
arguments of the two diagonal ties and the motif matrix entry at each port.
The accepting entry contributes its list of template labels to the pass.


### `dyadicRefreshKernelWitness`

 Each refresh site checks its two diagonal ties and reads the selected
motif entry on its actual half-wire arguments. 

### `dyadicRefreshKernelWitness_degree_le`

 The exponents contributed at a physical port are bounded by the number
of internal ties times the largest old wire width. 
