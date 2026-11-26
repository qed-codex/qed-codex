---
{
  "module": "OAI/Computability/VPVNP/BalancedLayoutThreshold.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/BalancedLayoutThreshold.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/BalancedLayoutThreshold.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# A common strict threshold for balanced cube layouts

Theorem 4.2 compares a single star witness with every balanced cut. The
extension places all subset centroids simultaneously. Its terminal wire lengths
and its bridge length can therefore be computed in one filled cube. Finiteness
of the cuts makes the strict savings uniform before the tensor is chosen.


### `balancedCut_uniformGap`

 Choose one positive saving below the unit-cube star length for every
balanced split of the same dimension, including at the dimension threshold. 

### `centroid_wire_costs`

 The bridge and the sum of terminal distances in a spectral realization of
the two filled side centroids. The boolean side convention agrees with the
two-center circuit factorization. 

### `exists_cubeCentroid_layout_threshold`

 Extend the marked cube to one spectrum with two centers for each cut, then
choose a threshold strictly between all balanced layouts and the star bound.
The same margin can be used to select the tensor witness in (4.4). 
