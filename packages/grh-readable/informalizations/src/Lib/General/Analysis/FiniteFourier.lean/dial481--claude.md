---
{
  "module": "src/Lib/General/Analysis/FiniteFourier.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/General/Analysis/FiniteFourier.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/General/Analysis/FiniteFourier.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Orthogonality, Fourier inversion and matrix Gauss sums over a finite ring

Finite Fourier analysis on matrices over a finite commutative ring `R`, for a primitive additive
character `ψ` (no multiple `ψ (r * ·)` with `r ≠ 0` is trivial).

* `New.exists_isPrimitive_apply_eq_of_surjective`, `New.exists_primitive_residue_addChar`: a
  character of a ring `F` for which the subring `O` is self-dual induces a primitive character of a
  suitable quotient ring of `O`.
* `New.sum_addChar_dotProduct`, `New.sum_addChar_trace_mul`: orthogonality; the sum of `ψ` along
  a nonzero linear form on vectors or on matrices is `0`.
* `New.Exchange.matrixFourier`, `New.Exchange.matrixFourier_matrixFourier`: the transform
  `ρ ↦ ∑ v, f v * ψ (tr (ρ v))`, not normalised, and its inversion formula.
* `New.exists_sum_smul_addChar_trace_eq`: every function on matrices is a linear combination of
  the characters `y ↦ ψ (tr (y u))`.
* `New.Exchange.exists_matrixFourier_eq_mul_inv_det`: the transform of a function with
  `S (g d) = χ (det g) S d`, for a multiplicative character `χ` (zero off the units) that is
  primitive, `New.Exchange.IsPrimitiveMulChar`, and the modulus of the Gauss sum of `χ ∘ det`.

## Relation to the literature

Known; see `Lib.Weil.TameGaussSum` for sources.


### `AddChar.map_sum_eq_prod`

 An additive character `ψ` sends a finite sum to the product of its values on the terms. 

### `exists_isPrimitive_apply_eq_of_surjective`

 Let `O` be a subring of `F`, `π : O → R` a surjective ring homomorphism (`hπ_surj`) with kernel
`{x | g * x ∈ O}` (`hπ_ker`), and `ψ` an additive character of `F` such that `ψ (t * ·)` is
trivial on `O` exactly when `t ∈ O` (`hψ`). Then `π x ↦ ψ (g * x)` is a well-defined primitive
character of `R`. 

### `exists_primitive_residue_addChar`

 `New.exists_isPrimitive_apply_eq_of_surjective` with its two conditions on `π` joined in
one hypothesis `hπ`: `π` is surjective, and its kernel is `{x | g * x ∈ O}`. Then `π x ↦ ψ (g * x)`
is a well-defined primitive character of `R`. 

 ### The Fourier transform on matrices 

### `Exchange.matrixFourier`

 The Fourier transform of a function `f` on `N × a` matrices, a function on `a × N` matrices:
`ρ ↦ ∑ v, f v * ψ (tr (ρ v))`, with no normalising factor. 

### `Exchange.IsPrimitiveMulChar`

 The multiplicative character `χ` of the finite ring `R` is primitive: for every `a ≠ 0` some
element `1 + c * a` has `χ`-value different from `0` (so it is a unit) and from `1`. That is,
for no nonzero `a` is `χ` trivial on the units congruent to `1` modulo `a`. 

### `sum_addChar_dotProduct`

 Orthogonality of characters along a linear form: for a primitive additive character `ψ` of `R`
and a vector `z` in `R^a`, the sum of `ψ (z ⬝ᵥ x)` over all `x` in `R^a` is the number of such `x`
if `z = 0` and `0` otherwise. 

### `sum_addChar_trace_mul`

 Orthogonality of characters on matrices: for a primitive additive character `ψ` of `R` and an
`a × N` matrix `ρ`, the sum of `ψ (tr (ρ v))` over all `N × a` matrices `v` is the number of such
matrices if `ρ = 0` and `0` otherwise. 

### `Exchange.matrixFourier_matrixFourier`

 Fourier inversion for matrices over a finite commutative ring R with a primitive additive
character ψ: applying the transform `New.Exchange.matrixFourier` twice to f gives y ↦ f(−y) times
the number of matrices. 

### `exists_sum_smul_addChar_trace_eq`

 For a primitive additive character ψ of a finite commutative ring R, every complex function
f on N × a matrices over R is a linear combination of the characters y ↦ ψ(tr(yu)), for u
ranging over the a × N matrices. 

### `Exchange.matrixFourier_eq_inv_det_mul`

 The first step towards the matrix Gauss sums. Let `R` be a finite commutative ring and `χ` a
primitive multiplicative character of `R` (`IsPrimitiveMulChar`: for no nonzero `a` is `χ` trivial
on the units congruent to `1` modulo `a`). Let `S` be a function on square matrices over `R` with
`S (g d) = χ (det g) S d` for all invertible `g`. Then the Fourier transform
`matrixFourier ψ S y = ∑ d, S d ψ (tr (y d))` equals `χ⁻¹ (det y)` times its value at `1`; in
particular it vanishes where `y` is not invertible. The additive character `ψ` may be any. 

### `Exchange.star_matrixFourier_det_mul`

 The second step towards the matrix Gauss sums. Let `ψ` be primitive, `χ` primitive in the sense
of `New.Exchange.IsPrimitiveMulChar`, and `S` a function on square matrices with
`S (g d) = χ (det g) S d` for all invertible `g`. Let `γ` be the Gauss sum of `χ ∘ det`, the
transform `New.Exchange.matrixFourier ψ (χ ∘ det)` at the matrix `1`. Then the complex conjugate of
`γ` times the transform of `S` at `1` is `S 1` times the number of matrices. The proof applies
Fourier inversion to `New.Exchange.matrixFourier_eq_inv_det_mul`. 

### `Exchange.matrixFourier_eq_and_star_mul_eq`

 Gauss sums of matrices over a finite ring, both steps in one statement. Let `ψ` be primitive,
`χ` primitive in the sense of `New.Exchange.IsPrimitiveMulChar`, and `S` a function on square
matrices with `S (g d) = χ (det g) S d` for all invertible `g`. Write `Ŝ` for its Fourier transform
`New.Exchange.matrixFourier ψ S`. Then (a) `Ŝ y = χ⁻¹ (det y) Ŝ 1` for every `y`, so `Ŝ` vanishes at
non-invertible `y` (`New.Exchange.matrixFourier_eq_inv_det_mul`). (b) `γ Ŝ 1` equals `S 1` times
the number of matrices, where `γ` is the complex conjugate of the transform of `χ ∘ det` at the
matrix `1` (`New.Exchange.star_matrixFourier_det_mul`). 

### `Exchange.exists_matrixFourier_eq_mul_inv_det`

 Gauss sums of square matrices over a finite ring `R`. Let `ψ` be primitive and `χ` primitive in
the sense of `New.Exchange.IsPrimitiveMulChar`, and let `n` be the cardinality of `a`. There is a
number `γ` with `|γ|² = #R ^ (n²)` such that every function `S` on `n × n` matrices with
`S (g u) = χ (det g) S u` for all invertible `g` has the Fourier transform `y ↦ γ χ⁻¹(det y) S 1`,
which is zero where `y` is not invertible.

The value of `|γ|²` comes from Fourier inversion
(`New.Exchange.star_matrixFourier_det_mul`), applied to `χ ∘ det`. 
