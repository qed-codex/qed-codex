---
{
  "module": "OAI/Computability/VPVNP/ShiftedResidue.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/ShiftedResidue.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/ShiftedResidue.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

Note from QED Codex: the notes below name results of Kirill Khoruzhii. [Lemmata entry (CC BY 4.0)](https://github.com/ZIB-IOL/lemmata/blob/a2dd430f283febd755a6ee6932d0b0fdabfb330c/docs/crossing-decomposition/index.md)


# Shifted fermionic residues

Appendix B, equation (B.1), of *VP and VNP differ over every field* extracts a
different coefficient for every shift. Khoruzhii's `weighted_matrix_residue`
computes the constant coefficient. Here the extra factor `T² - 1` clears every
matched pole. On a finite window of Laurent exponents the two resulting
Wick expansions agree, so the even coefficients of the original commutator
all equal its constant coefficient. Widening the mode cutoff permits any
integer shift. We use Khoruzhii's integer-valued doubled energies throughout.


### `coeff_T_two_sub_one_mul`

 Multiplication by the Laurent binomial gives the difference of consecutive
coefficients of the same parity. 

### `even_coeff_eq_zero_coeff`

 If the Laurent binomial clears the coefficients in a symmetric window, all
even coefficients of the original polynomial in that window equal its constant term. 

### `wickCoeff_list_sum`

 Extracting a Laurent coefficient commutes with the sum over Wick matchings. 

### `weighted_matrix_locality_of_terms`

 When the multiplier cancels every pole at a specified coefficient, the signed
commutator vanishes at that coefficient. The two products use opposite normal orders. 

### `shifted_weighted_matrix_residue`

 The residue of the two ordered fermion fields at every even Laurent exponent in
the cutoff window. Exponent `2 * j` corresponds to the bivariate coefficient with
paper shift `s = -j-1`. 

### `matrix_vacuum_exchange`

 Transposing the two operator-source labels gives the sign from reflecting
the variable difference and exchanging the two fermionic blocks. 

### `invert_multiplier`

 Inverting the Laurent variable reflects the pole-clearing multiplier. 

### `reflected_term`

 For equal external energy, the Laurent powers of the two fields in a matrix-product
entry add to minus the sum of the two source energies. Swapping the source whose Laurent
variable is recorded reflects the index about `-1`. 

### `forward_matrix_reflect`

 Switching the field that carries the Laurent variable reflects the selected
coefficient and interchanges the two ordered products. 

### `commutator_reflect`

 The Laurent coefficient of the signed commutator at `2j` in orientation `(A,B)`
is the coefficient at `2(-j - 1)` in the opposite orientation, up to the explicit sign. 

### `shifted_weighted_matrix_residue_all`

 The shifted coefficient identity in both orientations of the input blocks. A single
cutoff suffices for exponent `2 * j` and its reflected exponent `2 * (-j - 1)`. 
