---
{
  "module": "OAI/Computability/VPVNP/CubeExclusion.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CubeExclusion.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CubeExclusion.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Enlarging a class of targets by the real line

In Section 5.1 of *VP and VNP differ over every field*, uniform exclusion
passes to every larger cube by restriction to a face. In dimension at least
two the real line can then be included among the targets. Every triple on
the real line satisfies a closed polynomial identity on its distances, while
three corners of a Euclidean square violate that identity.


### `cubeDistances`

 Euclidean distances between the corners of the unit cube. 

### `withRealLine`

 Add the real line at the extra index `none`. 

### `line_triple_closure`

 On the line a triple has zero squared area. This is a closed condition
on ordinary distances, including after any choice of scale. 

### `realLine_cube_exclusion`

 The Euclidean square has a right triangle of side lengths `1`, `1`, `√2`. 

### `withRealLine_cube_exclusion`

 Marked arrays for the enlarged class are the union of the two classes
of arrays, so uniform exclusion in dimension at least two is preserved. 
