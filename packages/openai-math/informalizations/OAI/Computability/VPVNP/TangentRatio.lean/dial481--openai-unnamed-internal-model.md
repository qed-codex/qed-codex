---
{
  "module": "OAI/Computability/VPVNP/TangentRatio.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/TangentRatio.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/TangentRatio.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 # The radial slope and its equality case

The proof of Lemma 4.1 of *VP and VNP differ over every field* compares
the endpoint distance with the right limit of the equal-parameter ratios.
Equality forces the original segments to have the same equal-parameter
distances as their tangent rays.


### `radialRatio_tendsto`

 The radial ratios converge from the right at zero to their infimum. 

### `radialSlope_eq_endpoint`

 The distance between endpoints attains the radial slope exactly when the
equal-parameter distance between the two original segments grows linearly. 
