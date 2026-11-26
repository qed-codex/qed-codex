---
{
  "module": "OAI/Computability/VPVNP/LinearNormalizationLine.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LinearNormalizationLine.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LinearNormalizationLine.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Highest coefficient on an affine line

Substitute `hᵢ + vᵢT` in a polynomial of total degree `d`. The resulting
polynomial in `T` has degree at most `d`, and its coefficient of `Tᵈ` is the
degree-`d` homogeneous component evaluated at the direction `v`.


### `line`

 Restriction to the affine line through `h` with direction `v`. 

### `natDegree_line_le`

 Restriction to an affine line cannot increase the total degree. 

### `coeff_line_totalDegree`

 Only the top homogeneous component contributes to the coefficient of the
highest possible power of the line parameter. 
