---
{
  "module": "OAI/Computability/VPVNP/Evaluator.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/Evaluator.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/Evaluator.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Counting a monomial in a finite algebra

The evaluator of Section 8.2 processes base-`Q` digits most significant first
using the linear maps for Frobenius and multiplication by a label. Once a
basis of the coefficient algebra containing `1` is given, an index path
through their matrices contributes a product of entries in the slice field.
The final prime-field coordinate of this product determines the number of
accepting branches.

`finiteAlgebra_pathCount` proves equation (8.2) for these branches, and
`digitProgram_length_le` bounds the number of linear steps. The construction
of a slice and the algorithms for querying individual matrix entries are
separate parts of Theorem 8.1 and Appendix D.


### `digitSteps`

 The linear steps for one digit position. The `i`th digit is `d i`. 

### `digitProgram`

 The linear program for the low `width` base-`#K` digits of every exponent.
The recursive call on the quotients processes the more significant digits first. 

### `digitSteps_eval`

 A single digit raises the previous accumulator to the field cardinality and
then multiplies by the label monomial of this digit. 

### `digitProgram_eval`

 For exponents given by `width` input bits, `width` base-`#K` digits suffice.
Starting the linear program at the unit returns the entire label monomial. 

### `digitSteps_length`

 Number of linear steps, including the Frobenius step, for one digit. 

### `digitProgram_length_le`

 The linear program executes at most one Frobenius and `t * (#K - 1)` label
multiplications per input bit. 

### `IndexPath`

 One index guess for each matrix factor, with a unique path when there are no factors. 

### `pathWeight`

 Product of entries along an index path. Ending at a different index contributes zero. 

### `AcceptingBranches`

 Distinguish all index paths and all admissible final choices, including paths of equal weight. 

### `card_acceptingBranches_cast`

 The integer path count, reduced modulo the prime, equals the prime-field coordinate of the
matrix product entry. The coordinate is applied once to the product of entries on each path. 

### `transitionMatrices`

 At a step from index `i` to `j`, read row `j`, column `i` of the
matrix of the linear map. Transposing puts these entries in path order. 

### `transitionMatrices_unit_entry`

 The matrix product entry from the basis element `1` to itself gives its
coordinate after the chronological sequence of linear maps. 

### `primeFunctional`

 The first coordinate over the slice field, followed by a prime-field
coordinate. This is the functional of Theorem 8.1. 

### `finiteAlgebra_pathCount`

 Equation (8.2). For every vector of exponents fitting in `width` bits,
the integer number of accepting branches reduces to the prime-field
functional of the entire monomial. 
