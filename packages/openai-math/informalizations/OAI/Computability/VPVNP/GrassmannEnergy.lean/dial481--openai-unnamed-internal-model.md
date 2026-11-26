---
{
  "module": "OAI/Computability/VPVNP/GrassmannEnergy.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/GrassmannEnergy.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/GrassmannEnergy.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Averaging the quadrilateral inequality on the binary Grassmannian

The quantities in Lemma 5.3 are uniform means over ordered pairs of a fixed
sum dimension. Transitivity identifies these means with averages of a single
quadrilateral translated by the general linear group. In the saturated case
each translate has zero quadrilateral deficit.


### `average_translate`

 Any seed pair of a given type gives the uniform pair mean under random
linear changes of coordinates. 

### `deficit`

 The difference between the side and diagonal sums of a quadrilateral. 

### `QuadrilateralBound`

 Squared CAT(0) distance arrays, and limits of those arrays, obey this inequality. 

### `IsSquare.eq_of_mean_eq_add`

 When the pair means saturate subadditivity, each such quadrilateral
saturates the inequality pointwise. 

### `HasType.eq_of_zero`

 Type zero consists of the diagonal of the Grassmannian. 

### `mean_add_le`

 Grassmannian pair means are subadditive up to the maximum type. 

### `mean_eq_mul_one`

 Saturation between adjacent and complementary pairs forces saturation at
every intermediate type. 

### `energy`

 Section 5.1's `Bᵣ` for a map of the Grassmannian into a metric space. 
