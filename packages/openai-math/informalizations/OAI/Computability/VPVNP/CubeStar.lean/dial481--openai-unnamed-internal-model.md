---
{
  "module": "OAI/Computability/VPVNP/CubeStar.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CubeStar.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CubeStar.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# The star estimate for cube corners in a CAT(0) space

Section 4.3 of *VP and VNP differ over every field* compares the total distance
from an ambient center to the basis vertices with the wire lengths of a
balanced cut. The nearest point in the filled cube reduces the lower bound to
the Euclidean star estimate, and the cut centroids also belong to that cube.


### `cubeVector`

 The Euclidean vector with the coordinates of a point in the unit cube. 

### `fillCube_dist`

 The filling scales Euclidean distances by the same factor as its corners. 

### `cube_star_lower`

 The star estimate (4.4) in the ambient metric. Its center may lie anywhere
in the CAT(0) space containing the cube. 

### `cubeCentroidCoordinates`

 Unit-cube coordinates of the centroid of the basis vertices in a side of the cut. 

### `filledSubsetCentroid`

 The side centroid realized in the CAT(0) target by filling the marked cube. 

### `basis_dist_filledSubsetCentroid`

 The distance from an individual basis terminal to a side centroid. 

### `filledSubsetCentroid_star_length`

 Total distance of one side's terminal wires in a scaled CAT(0) cube. 

### `disjoint_filledSubsetCentroids_dist`

 Distance between the centroids of disjoint sides of a scaled CAT(0) cube. 

### `filled_balancedLayout_strict`

 In a positively scaled cube of dimension at least `18 * C²`, a balanced
two-centroid layout costs strictly less than a star with any ambient center. 
