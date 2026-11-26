---
{
  "module": "OAI/Computability/VPVNP/Expanders.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/Expanders.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/Expanders.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Expanders from uniform exclusion of a Euclidean cube

Theorem 5.1 of *VP and VNP differ over every field*. The strict Grassmann
inequality supplies a sparse family with growth exponent below the plane
dimension. Choose the iteration count first, then the starting size, so the
resulting port graph admits both smoothing and an integral port matching.
Cloud replacement and the loopless double give fixed degree and Poincaré
bound at arbitrarily large power-of-two orders.


### `expanders_of_cube_exclusion`

 Theorem 5.1. The vertex sets are `Fin (2 ^ o)` and the integral arc
multiplicities describe connected loopless symmetric `2 ^ e`-regular
multigraphs. The degree and the Poincaré constant precede the order bound
and work for every space in the original class. 
