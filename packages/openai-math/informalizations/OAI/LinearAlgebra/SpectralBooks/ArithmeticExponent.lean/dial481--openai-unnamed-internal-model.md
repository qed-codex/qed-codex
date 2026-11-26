---
{
  "module": "OAI/LinearAlgebra/SpectralBooks/ArithmeticExponent.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/SpectralBooks/ArithmeticExponent.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/SpectralBooks/ArithmeticExponent.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 # Rectangular arithmetic exponents over a field

The wire order is (12,23,31), so the product has dimensions
`(n31 × n12) × (n12 × n23)`. Correctness means polynomial identity over
the ground field, including when that field is finite.


### `FormalAdmissibleExponent`

 Admissible exponents for the rounded rectangular formats, with positive slack. 

### `formalOmega`

 The arithmetic exponent in base size `N` at three prescribed wire weights. 

### `formalAdmissibleExponent_naive`

 The entrywise algorithm gives an admissible exponent in every weighted format. 

### `formalOmega_admissible`

 Positive slack allows the infimum itself as an admissible exponent. 

### `FormalAdmissibleExponent.rank_growth`

 A formal arithmetic cost bound also controls ordinary rank in each rounded format. 

### `matrix_load_le_log_tensorRank`

 Each logarithmic site load is a lower bound on the ordinary log-rank. 

### `FormalAdmissibleExponent.load_le`

 Every formal rectangular arithmetic exponent dominates each local dimension exponent. 

### `radicalTest_sInf_of_matrix_rank_growth`

 Take the infimum over all polynomial growth bounds supplied by a circuit model.
The rank may be measured over a common extension of its field of constants. 

### `formalOmega_radicalTest_of_rank_bound`

 The finite ordinary-rank inequality gives the rectangular arithmetic exponent inequality. 

### `formalOmega_square_lower_bound_of_rank_bound`

 The square exponent consequence of the finite ordinary-rank inequality. 
