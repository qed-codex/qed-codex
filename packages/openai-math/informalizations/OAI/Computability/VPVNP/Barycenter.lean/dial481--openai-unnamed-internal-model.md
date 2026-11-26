---
{
  "module": "OAI/Computability/VPVNP/Barycenter.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/Barycenter.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/Barycenter.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Barycenters in the spectral wire geometry

Section 5.3 of *VP and VNP differ over every field* smooths a configuration by
taking barycenters along the rows of a stochastic matrix. In a complete space
satisfying the CAT(0) inequality (4.2), every finite probability distribution
admits a barycenter with the squared-distance variance bound used in that step.


### `HasCATZeroSegments`

 The squared-distance form (4.2) of the CAT(0) geodesic inequality. The
point at fraction `t` along `xy` satisfies the bound for every test point. 

### `weightedSquaredDistance`

 The mean squared distance to a finite distribution of points. 

### `exists_barycenter_variance`

 Existence and the variance inequality from Section 5.3. At every test
point the energy exceeds its minimum by at least the squared displacement. 

### `existsUnique_barycenter_variance`

 In a metric space the barycenter satisfying the variance bound is unique. 
