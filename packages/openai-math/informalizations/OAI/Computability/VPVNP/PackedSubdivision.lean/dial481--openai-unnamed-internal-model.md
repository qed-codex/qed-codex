---
{
  "module": "OAI/Computability/VPVNP/PackedSubdivision.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PackedSubdivision.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PackedSubdivision.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Masses and subdivision counts of an actual packed graph

The color bits and old slot label give exactly `K = 2^c*d` old positions
per packed site. Section 7.2 consequently computes the new arc mass from
the old arc mass and the two degrees alone.


### `card_positions`

 The number of old positions per packed site is the number of choices
of color word times the number of choices of the old slot label. 

### `equalArcMass_packed`

 Actual masses satisfy `p' = pKd/d'`. 

### `packed_degree_budget`

 The exact packed role counts and the actual floor choice fit inside
the output degree, so the regularization's common deficit exists. 
