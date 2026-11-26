---
{
  "module": "OAI/Computability/VPVNP/CubeFilling.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CubeFilling.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CubeFilling.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Filling a Euclidean cube from its corners

The spectral wire argument uses the rigidity of flat quadrilaterals to fill an isometric
copy of the cube from its vertex configuration. We recursively interpolate
the two opposite faces. The induction keeps track of an entire family of
parallel faces, so that the diagonal distances needed for each application
of rectangle rigidity are known as well.


### `cubeSquaredDistance`

 Squared Euclidean distance between two points in the unit cube. 

### `cubeCorner`

 The corner with ones in the indicated coordinate positions. 

### `fillCube`

 The filling by successive CAT(0) segment interpolations, starting on
opposite faces and ending at the first coordinate. 

### `InterpolationTree`

 A finite prescription for extending a set of marked parties by fractional
points. The tree depends only on the labels and fractions, so the same
prescription can be used in each subsequent metric realization. 

### `InterpolationTree.eval`

 Evaluate a finite prescription in a CAT(0) space. 

### `cubeInterpolation`

 Interpolation instructions for a specified point of the cube, using only
the original corner labels. 

### `fillCube_dist_sq`

 If the corner squared distances are scaled Hamming distances, the full
cube has Euclidean squared distances with the same scale. 

### `fillCube_segment`

 Straight line segments in the filled cube coincide with the corresponding
CAT(0) segments. In particular its image is geodesically convex. 

### `isCompact_range_fillCube`

 The filled cube is compact. 

### `fillCube_nearest`

 For any ambient point, a closest point in the cube satisfies the
CAT(0) projection inequality against every other point in the cube. 
