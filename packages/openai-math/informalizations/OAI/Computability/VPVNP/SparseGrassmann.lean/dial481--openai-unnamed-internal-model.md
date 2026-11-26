---
{
  "module": "OAI/Computability/VPVNP/SparseGrassmann.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/SparseGrassmann.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/SparseGrassmann.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Sparse walks from the Grassmann inequality

In Section 5.2 of *VP and VNP differ over every field*, conditioning on the
restriction of a random linear map to a common hyperplane leaves two independent
vertices in corresponding fibers. Two bijections from `I × E` onto the vertex
set describe the two fiber partitions, with `I` indexing the restrictions and
`E` indexing the possible extensions. We compare the energy of this conditional
coupling with a copy of the previous walk in every fiber and a symmetric
permutation walk joining corresponding extensions.


### `fiberWalk`

 Place one copy of the preceding walk in each source fiber. 

### `matchingWalk`

 Match a vertex to its partner in the target fiber, symmetrizing the direction. 

### `adjacentEnergy`

 The conditional adjacent-pair energy times the number of vertices. 

### `adjacentEnergy_le`

 Compare independent conditional endpoints through the source partner of the
target endpoint. The factor `γ` is paid only on the part of the energy within
a fiber. This gives the multiplicative coefficient used in the sparse recursion. 

### `sparseWalk`

 Average the fiber walk and the matching walk over the ordered adjacencies,
using their respective weights from the squared triangle inequality. 

### `sparseWalk_hasPoincareBound`

 The sparse recursion of Section 5.2. The sampling inequality is stated in
the same normalization as `HasPoincareBound`. Its coefficient `c` is `m - η`
when applied to the adjacent pairs of the binary Grassmannian. 

### `sparseWalk_support`

 A row of the new walk uses at most one old row and two matching edges per
ordered Grassmann adjacency. This count is independent of the fiber count. 
