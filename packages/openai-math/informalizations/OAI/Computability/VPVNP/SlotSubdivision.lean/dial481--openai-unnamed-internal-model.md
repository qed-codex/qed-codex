---
{
  "module": "OAI/Computability/VPVNP/SlotSubdivision.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/SlotSubdivision.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/SlotSubdivision.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# The subdivision counts in degree regularization

In §7.2 of *VP and VNP differ over every field*, an old wire has mass
`p` and a new slot has mass `p * K * d / d'`. Thus the floor count depends
only on the degrees, the packing ratio and the supply type's relative mass.
The same degree threshold works for every position count and every term.


### `count`

 Number of regularized slots for one surviving supply edge. 

### `count_fraction`

 For the paper's rational supply masses, ordinary natural division computes
the subdivisions used in the local circuit descriptions. 

### `eventually_represented`

 For every sufficiently large output degree, the floored counts are positive
and represent at least `1-δ` of each type's old mass. In particular the same
threshold works when output degrees are restricted to powers of two. 

### `degree_budget`

 The sum of the floored subdivisions fits inside the available output degree.
Each of the four types has `d * Q` incidences at each site, and the relative
masses of one surviving group sum to `4/3`. 
