---
{
  "module": "OAI/Computability/VPVNP/LinearNormalizationDimension.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LinearNormalizationDimension.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LinearNormalizationDimension.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Number of variables in an integral polynomial normalization

In a polynomial ring over a field, an injective integral normalization has
as many coordinates as the ambient polynomial ring has variables.


### `isIntegral_range`

 Integrality of an algebra homomorphism makes each target element integral
over its image subalgebra. 

### `isIntegral_iff_range`

 Integrality over the image characterizes an integral homomorphism. 

### `numVars_eq_of_integral_injective`

 The image of the source variables is a transcendence basis of the target,
so the two polynomial rings have the same number of variables. 
