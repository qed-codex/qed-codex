---
{
  "module": "src/Lib/Weil/TameGaussSum.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Weil/TameGaussSum.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Weil/TameGaussSum.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Tame local characters, integral frames and the local Gauss sum

`F` is a ring satisfying `New.SemilocalField`, modelled on a finite product of non-archimedean local
fields. Its integers are `O`, of volume one, and `ϖ` is a uniformiser. `New.invOnUnits χ` is `χ⁻¹`
on the units of `O` and zero elsewhere. `New.TameLocalChar χ` says that on `O`, `New.invOnUnits χ`
is a primitive character `η` of a finite ring `R` composed with a surjection `π` from `O` onto `R`
with kernel `ϖ O`. The file proves basic facts on such characters, introduces integral frames, and
shows that the Fourier transform of `New.invOnUnits χ` over `O` is γ·χ(ϖ t) when ϖ t is an integral
unit and zero otherwise, for some constant γ with ‖γ‖² = 1 / card R.

The quadratic Gauss sum that gives the product rule of the Weil representation at the finite places
is a different one; it is in `Lib.Weil.Construction.FiniteCocycle`.

## Main definitions and results

* `New.Exchange.IntegralFrame`: an integral basis in three blocks of columns `K, I, L` with its dual
  basis; `New.Exchange.IntegralFrame.blockRelations` lists the relations between the blocks.
* `New.Exchange.exists_local_gauss_sum`: the Fourier transform of the inverse of a tamely ramified
  character χ, cut off to the units, equal to γ·χ(ϖ t) when ϖ t is an integral unit and zero
  otherwise, for some γ with ‖γ‖² = 1 / card R.
* `New.Exchange.IntegralFrame.stdDatum`: the function x ↦ G(x (K I)) on integral matrices x, zero
  elsewhere.

Notions from other files:
* `New.SemilocalField`: Conditions met by a finite product of non-archimedean local fields: a
  locally compact ring with Haar measure, compact open subring O of volume one, a topologically
  nilpotent invertible ϖ in O, and `New.IsValuationPair O`.
* `New.HasIntegralConductor`: The additive character ψ is continuous and has conductor O: ψ is
  trivial on tO exactly when t lies in O.
* `New.IsIntegralUnit` x: x lies in O and has an inverse in O. `New.IsIntMatrix` O M: every entry of
  the matrix M lies in O.

## Relation to the literature

Known result: Gauss sums of a character of the determinant over matrix rings. Only one-dimensional
ramified characters are treated, and the exact value is not computed. For matrices over a finite
ring, the eigen-relation, the vanishing at singular index and the modulus are proved in another file
(`New.Exchange.exists_matrixFourier_eq_mul_inv_det`, used here). This file proves the scalar case
over the integers of a product of local fields, with the modulus. Source: T. Kondo, On Gaussian sums
attached to the general linear groups over finite fields, J. Math. Soc. Japan 15 (1963) 244–255; for
the scalar case over finite rings, E. Lamprecht, Math. Nachr. 9 (1953), see K. Conrad, Gauss and
Jacobi sums on finite fields and Z/mZ, §4; for the local scalar case, Tate's thesis §2.5.

See also `Lib.Weil.MixedModel.ZeroTerm`.


 ## First facts on tame local characters 

### `invOnUnits_uniformizer_mul_add`

 For a tame character χ and s in O, the function `invOnUnits χ` (χ⁻¹ on the units of O, zero
elsewhere) is unchanged by adding ϖ s: it is invariant under translation by ϖ O. 

### `norm_eq_one`

 A tame character χ has absolute value 1 at every unit t of O. 

### `isLocallyConstant_invOnUnits`

 For a tame character χ, the function `invOnUnits χ` (χ⁻¹ on the units of O, zero elsewhere) is
locally constant. 

 ## Integral frames and the local Gauss sum 

### `IntegralFrame`

 An integral invertible matrix over F cut into column blocks (K I L), with its integral inverse
cut into row blocks `dualK`, `dualI`, `dualL`; the blocks K and L have `p` columns, I has `n`. 

### `IntegralFrame.K`

 The first block of columns of the basis. 

### `IntegralFrame.L`

 The last block of columns of the basis. 

### `IntegralFrame.I`

 The middle block of columns of the basis. 

### `IntegralFrame.dualK`

 The block of rows of the dual basis that is dual to `K`. 

### `IntegralFrame.dualL`

 The block of rows of the dual basis that is dual to `L`. 

### `IntegralFrame.dualI`

 The block of rows of the dual basis that is dual to `I`. 

### `IntegralFrame.isIntMatrix_and_mul_eq_one`

 The matrix `P` with column blocks `K, I, L` and the matrix `Q` with row blocks
  `dualK, dualI, dualL` have entries in `O` and are inverse to each other. 

### `submatrix_id_mul`

 Selecting rows of `M` and then multiplying by `N` selects the same rows of `M * N`. 

### `div_invOnUnits`

 Dividing by `invOnUnits χ x` multiplies by `χ x` if `x` is a unit of `O`; otherwise it is a
division by zero, which gives zero. 

### `exists_local_gauss_sum`

 The local Gauss sum. Let `F` be semilocal, with Haar measure giving `O` volume one. Let `χ` be
tame, that is, `χ⁻¹` on the units of `O` is the pullback of a primitive character of the finite
residue ring `R = O / ϖ`, and let `ψ` be a continuous additive character of conductor `O`, so that
`ψ` is trivial on `t O` exactly when `t ∈ O`. Then there is `γ` such that (a)
`‖γ‖ ^ 2 = (card R)⁻¹`, and (b) for every `t`, the integral over `O` of the product of
`invOnUnits χ x` (which is `χ⁻¹` on the units and `0` elsewhere) and `ψ (t x)` equals `γ χ(ϖ t)`
if `ϖ t` is a unit of `O`, and `0` otherwise. 

### `IntegralFrame.BlockRelations`

 The six blocks of an integral frame have entries in `O`, and each block of the dual basis
is a left inverse of its own block of the basis and vanishes on the other two. 

### `IntegralFrame.BlockRelations.isIntMatrix_dualL`

 The block `dualL` has entries in `O`. 

### `IntegralFrame.BlockRelations.isIntMatrix_dualI`

 The block `dualI` has entries in `O`. 

### `IntegralFrame.BlockRelations.isIntMatrix_K`

 The block `K` has entries in `O`. 

### `IntegralFrame.BlockRelations.isIntMatrix_L`

 The block `L` has entries in `O`. 

### `IntegralFrame.BlockRelations.isIntMatrix_dualK`

 The block `dualK` has entries in `O`. 

### `IntegralFrame.BlockRelations.isIntMatrix_I`

 The block `I` has entries in `O`. 

### `IntegralFrame.BlockRelations.dualK_mul_K`

 `dualK` is a left inverse of `K`. 

### `IntegralFrame.BlockRelations.dualI_mul_K`

 The rows of `dualI` vanish on the columns of `K`. 

### `IntegralFrame.BlockRelations.dualL_mul_K`

 The rows of `dualL` vanish on the columns of `K`. 

### `IntegralFrame.BlockRelations.dualK_mul_I`

 The rows of `dualK` vanish on the columns of `I`. 

### `IntegralFrame.BlockRelations.dualI_mul_I`

 `dualI` is a left inverse of `I`. 

### `IntegralFrame.BlockRelations.dualL_mul_I`

 The rows of `dualL` vanish on the columns of `I`. 

### `IntegralFrame.BlockRelations.dualK_mul_L`

 The rows of `dualK` vanish on the columns of `L`. 

### `IntegralFrame.BlockRelations.dualI_mul_L`

 The rows of `dualI` vanish on the columns of `L`. 

### `IntegralFrame.BlockRelations.dualL_mul_L`

 `dualL` is a left inverse of `L`. 

### `IntegralFrame.blockRelations`

 The relations `New.Exchange.IntegralFrame.BlockRelations` hold in every integral frame: its six
blocks have entries in `O`, and each block of the dual basis is a left inverse of its own block
of the basis and vanishes on the other two. They are read off block by block from
`A.isIntMatrix_and_mul_eq_one`. 

### `IntegralFrame.stdDatum`

 For an integral frame A with blocks K, I, L and a function G on `a × (p ⊕ n)` matrices, the
function of an `a × m` matrix x equal to G(x·(K I)) if x has entries in O and 0 otherwise. 


## Multiplicativity of the character cut off to units

`New.invOnUnits_mul`: `New.invOnUnits χ` is multiplicative on `O`, since a product in `O` is a unit
exactly when both factors are.


### `New.invOnUnits_mul`

 For x and y in O, `invOnUnits χ (x y) = invOnUnits χ x * invOnUnits χ y`. 
