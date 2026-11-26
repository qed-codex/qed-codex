---
{
  "module": "OAI/Computability/VPVNP/GrassmannInequality.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/GrassmannInequality.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/GrassmannInequality.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# The strict Grassmann inequality

Lemma 5.3 of *VP and VNP differ over every field* gives a strict, uniform
improvement over the bound by the Grassmann plane dimension `m` when all
target spaces exclude a Euclidean cube of some dimension less than `m`.
The proof here identifies the extremal distances on all pairs of type
`r < m`, exhibits the cube on the coordinate planes, and uses compactness
of normalized finite distance arrays to obtain the uniform gap.


### `value_eq_type_of_saturated`

 At a saturated normalized array every ordered pair of type `r < m`
has squared distance exactly `r`. 

### `cube_of_saturated`

 The equality case of Lemma 5.3 gives the marked Euclidean cube, with
Hamming distance as its squared distance. 

### `strict_grassmann_bound`

 Lemma 5.3. The improvement over the factor `m` is uniform in both the
target space and the configuration of its Grassmannian points. 
