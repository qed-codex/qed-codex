---
{
  "module": "OAI/Computability/VPVNP/GrassmannFourPoint.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/GrassmannFourPoint.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/GrassmannFourPoint.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Four-point inequalities for Grassmannian distance arrays

The proof of Lemma 5.3 uses the squared quadrilateral inequality and its
equality case even for limits of scaled configurations in different CAT(0)
spaces. The midpoint comparison yields a closed system of inequalities on
the array alone. A nonnegative square in the quadrilateral deficit gives the
equality case directly for every array in this closed set.


### `midpointUpper`

 The squared-distance upper bound from the midpoint of `ac` to `b`. 

### `catZeroArrays`

 Closed four-point conditions inherited from CAT(0) squared distances. 

### `scaledDistSq_mem_catZeroArrays`

 Scaling squared distances by any nonnegative factor preserves the closed
four-point conditions. Only the midpoint case of the segment inequality is needed. 

### `QuadBounds`

 The four-point properties used by the averaging and rigidity arguments
on the binary Grassmannian. At equality both pairs of opposite sides agree. 
