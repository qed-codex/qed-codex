---
{
  "module": "OAI/Computability/VPVNP/SparseGrassmannFamily.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/SparseGrassmannFamily.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/SparseGrassmannFamily.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# The rounded sparse Grassmann family

Section 5.2 of *VP and VNP differ over every field* constructs a common graph
for an entire class of targets from their strict Grassmann inequality. Its
order is `D ^ (m ^ j)`, its power-of-two degree is at most `4 Cj D`, and its
Poincaré coefficient grows as `O(α ^ j)` for `α < m`. The degree constant may
depend on `j`, while the coefficient prefactor is independent of both `D` and `j`.


### `exists_readPlane_laws`

 The same linear map is sampled for every plane. On complementary pairs its
two readings are independent, and on adjacent pairs their extensions are
conditionally independent given the restriction to the intersection. 

### `exists_sparse_rounded_family`

 Sparse regular multigraphs of order `D^(m^j)` for every starting order
`D=2^d≥2`. The choices of the matrices and of their power-of-two degrees are
simultaneous for all the targets satisfying the strict Grassmann inequality. 
