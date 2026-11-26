---
{
  "module": "OAI/Computability/VPVNP/SpectralSectorDistance.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/SpectralSectorDistance.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/SpectralSectorDistance.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Euclidean coordinates on a spectral sector

The pullback seminorm from Section 4.1 has a quadratic square on the coordinate
plane. Its three coefficients are determined by the two unit axis lengths and
the length of the chord between their endpoints. The calculation includes
boundary points and degenerate sectors.


### `sectorPoint_dist_sq`

 The sector of two rays or segments with a linear equal-parameter distance
has exactly the Euclidean squared distances determined by its three side lengths. 
