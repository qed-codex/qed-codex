---
{
  "module": "OAI/LinearAlgebra/MatrixExponent/Integral/Upper/PolynomialSectorFamily.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/MatrixExponent/Integral/Upper/PolynomialSectorFamily.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/MatrixExponent/Integral/Upper/PolynomialSectorFamily.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# The polynomial witness for the three-sector degeneration

Every coefficient has degree at most one.  Its constant coefficient is the
entire shared-first-input sector assembly.  At each nonzero parameter the
evaluated tensor is an actual restriction of the original polynomial tensor.
These explicit facts support interpolation without assuming that an arbitrary
tensor character preserves topological limits.


### `triplingPolynomialFamily`

 The same family as the diagonal degeneration, expressed in the complete
sector bases on the last two legs.  The first input is unchanged. 

### `triplingPolynomialFamily_coeff_zero`

 The constant coefficient retains all three branches, including their
vanishing cross-sector coefficients, in one shared first-input basis. 

### `triplingPolynomialFamily_degree_le`

 There is no growing or unspecified approximation degree: every coordinate
of this explicit family has degree at most one. 

### `triplingPolynomialFamily_eval_mem_restrictionOrbit`

 Every nonzero evaluation is an exact restriction of the original source
tensor. The sector reindexing is one fixed pair of local maps, with identity
on the common first input, after the diagonal maps. 
