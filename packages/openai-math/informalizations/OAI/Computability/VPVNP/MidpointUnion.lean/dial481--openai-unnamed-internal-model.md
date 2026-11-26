---
{
  "module": "OAI/Computability/VPVNP/MidpointUnion.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/MidpointUnion.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/MidpointUnion.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Distances in the union of midpoint extensions

The finite stages in Corollary 2.5 preserve distances between parties
that have already appeared. The distance of two points in the union can
therefore be read at their first common stage. A single later stage suffices
to realize the entire distance matrix of a finite tuple.


### `unionDist`

 Read a distance at the first stage containing both arguments. 

### `unionDist_eq_stage`

 Each stage containing both points gives the distance in the union. 

### `unionPseudoMetric`

 The stage distances give a pseudometric on the union. The triangle
inequality can be checked in any stage containing the three points. 

### `unionDist_finite_stage`

 All distances of a finite configuration are read at one common stage,
including for an empty tuple. 
