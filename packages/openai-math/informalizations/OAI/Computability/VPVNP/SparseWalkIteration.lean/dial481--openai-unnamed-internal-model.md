---
{
  "module": "OAI/Computability/VPVNP/SparseWalkIteration.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/SparseWalkIteration.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/SparseWalkIteration.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Iterating and rounding the sparse walk

The size `D` of the starting walk is a power of two. At each step the vertex
set consists of `m`-tuples of the preceding vertices. The row support grows by
at most a factor twice the number of Grassmann adjacencies, while the Poincaré
coefficient satisfies an affine recurrence with multiplier strictly below `m`.


### `SparseWalkBound`

 Uniform bounds for one symmetric stochastic matrix on every target in the class. 

### `uniform_sparseWalkBound`

 The starting graph is the uniform matrix on the full set. 

### `WordSpace`

 Binary words of length `k`, used as the vertex vector space at each stage. 

### `sparseCoefficient`

 The affine Poincaré recurrence in Section 5.2. 

### `sparseCoefficient_le`

 Solving the recurrence gives a prefactor independent of the starting size
and the iteration index. 

### `iterate_sparse_walk`

 Iterate the one-step construction on binary word spaces. The output is
reindexed by `Fin` so its size is available directly to the port construction. 
