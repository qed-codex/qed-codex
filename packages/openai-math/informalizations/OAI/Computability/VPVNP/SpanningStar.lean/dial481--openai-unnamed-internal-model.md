---
{
  "module": "OAI/Computability/VPVNP/SpanningStar.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/SpanningStar.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/SpanningStar.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 # Diameter of a spectral configuration on all parties

A star joining a central party to every party restricts to the all-parties
diagonal. The loop at the central party has spectral wire distance zero.


### `starNetwork_restricts_diagonal`

 At each party keep the basis vectors whose incident wire labels are all
the output coordinate. Along a spanning star these restrictions impose the
all-parties diagonal. 

### `one_le_sum_wireDistance`

 The total wire distance along the spanning star is at least one. 

### `nontrivial_parties`

 A nonempty party set admitting a spectral point has at least two parties.
For a singleton, the star sum would vanish. 

### `inv_card_sub_one_le_wire_diameter`

 The sharp normalization bound for the diameter of any configuration whose
labels cover all parties. 
