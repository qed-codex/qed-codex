---
{
  "module": "src/Lib/Adelic/TraceFormula/Convergence.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Adelic/TraceFormula/Convergence.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Adelic/TraceFormula/Convergence.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Convergence of the geometric side

Let `k` be a function on the real points that decays against a high power of the norm, and let `φ`
be a test function on the finite points. The sums of `(k ⊗ φ)(x⁻¹ γ x)` over rational points `γ`
converge absolutely, with a bound by a power of the height of `x`. High in a cusp, short lattice
vectors span an isotropic subspace `A`, and the bound improves: for the `γ` that move `A`, the
points `x⁻¹ γ x` are large at infinity, and, if `k` is a cusp kernel, the terms of the `γ` that keep
`A` cancel along the unipotent radical. So the sum over the `γ` whose characteristic polynomial lies
in a given set is bounded uniformly in `x` and in the set, and the sum over the `γ` with irreducible
polynomial is bounded absolutely. These are known arguments for convergence in a simple trace
formula (cf. Flicker and Kazhdan).

Notions from other files:
* `New.Space E n s`: a hermitian form `J` over `E` with an adelic point. `G E s` is the unitary
  group `GInf E s × Gf E n`, and `V.ratEmbed` embeds the rational unitary group `U V.J` in it.
* `New.Space.height`: `V.height x` is the inverse of the first minimum, cut off at `1`, of the space
  `V.move x` whose point is moved by `x`.
* `New.IsCuspKernel B k`: `k` is a minimal idempotent kernel on the real points with decay of order
  `B`, an integrable moment and a compactly supported function that reproduces it.

## Main definitions and results

* `New.Space.exists_tsum_enorm_kernelTerm_le_height`: the bound by a power of the height.
* `New.Space.exists_norm_tsum_polyTerm_le`: the uniform bound for a set of polynomials.
* `New.Space.exists_tsum_enorm_irreducibleTerm_le`: the absolute bound for irreducible polynomials.


### `norm_tsum_le_of_tsum_enorm_le`

 If the sum of the moduli of the terms of a complex family is at most `T ≥ 0`, then so is the
modulus of the sum. 

### `add_le_of_thirteen_mul_cube_le`

 An order of decay of `13 n³` leaves `4 n³` to spare over the order `8 n² + 1` that the bound for
the kernel needs. 

### `kernelTerm`

 The term of the rational point `γ`, with the weight `a γ`, in the kernel of `k ⊗ φ` at the
pair of points `g, x`: the weight times the value of `k ⊗ φ` at `g⁻¹ γ x`. 

### `polyTerm`

 The value of `k ⊗ φ` at `x⁻¹ γ x` if the characteristic polynomial of `γ` lies in `S`, and
`0` otherwise. 

### `irreducibleTerm`

 The value of `k ⊗ φ` at `x⁻¹ γ x` if the characteristic polynomial of `γ` is irreducible, and
`0` otherwise. 

### `polyTerm_eq_kernelTerm_indicator`

 The term of a set `S` of polynomials is the term of the kernel whose weight is the indicator
of the rational points with characteristic polynomial in `S`. 

### `partialKernel`

 The part of the kernel of `k ⊗ φ` at `g, x` that comes from the rational points in `Z`. 

### `measurable_kernelTerm`

 For measurable `k` and a test function `φ`, each term of the kernel is measurable in the pair
of points. 

### `partialKernel_ratEmbed_mul`

 The partial kernel of the rational points in `Z` is left invariant in `g` under every rational
point `ν` with `ν Z = Z`. 

### `hasLevel_partialKernel`

 For a hermitian space `V` with a point, the partial kernel `V.partialKernel k φ Z g x` is the
part of the kernel of `k ⊗ φ` at `g, x` coming from the rational points in `Z ⊆ U V.J`; in each of
its terms, `g` enters only through left multiplication by `g⁻¹`. If `φ` on `Gf E n` satisfies
`φ (u⁻¹ * y) = φ y` for all `u ∈ J`, then as a function of `g` the partial kernel has level `J`,
i.e. it is right invariant under `J ⊆ G_f`. 

### `integral_mul_kernelTerm`

 A minimal idempotent kernel `k` on the real points satisfies `k * k = k`, so each term of the
kernel of `k ⊗ φ`, as a function of `g`, is fixed by right convolution with `k`. 

### `realConv_partialKernel`

 Let `k` be a minimal idempotent kernel on the real points (in particular continuous and
integrable, with `k * k = k`). If the sums of the moduli of the terms in a partial kernel (the sum
of the terms of the rational points in `Z`) are bounded in `g`, then the partial kernel, as a
function of `g`, is fixed by right convolution with `k`. 

### `CuspFrame.isIsotropicFrame`

 The matrices `A.isotropicCols` and `A.perpCols` of a cusp frame `A` of size `δ` for `V.move x`
(their columns are lattice vectors whose length bounds have product at most `δ`) span an isotropic
subspace and its orthogonal for the hermitian form `V.J`, which is the condition
`New.IsIsotropicFrame`. 

### `height_le_pow_mul_height`

 The height is positive, so multiplying it by `δ ^ card n` with `1 ≤ δ` does not decrease it. 

### `norm_mul_le_majorant`

 If `k` has decay of order `B`, that is, `‖k g‖ ‖g‖ ^ B ≤ C` for the product `‖g‖` of the
operator norms at the infinite places, then `|k ⊗ φ|` is at most `C` times the majorant
`|φ(y_f)| / ‖y_∞‖ ^ B` of exponent `B`. 

### `majorant_le_pow_mul`

 Let `‖y_∞‖` be the product of the operator norms of `y` at the infinite places. If
`A + j ≤ B` and `1 ≤ r ‖y_∞‖` unless `φ(y_f) = 0`, then the majorant
`|φ(y_f)| / ‖y_∞‖ ^ B` of exponent `B` is at most `r ^ j` times that of exponent `A`. 

### `exists_tsum_enorm_kernelTerm_le`

 The bound for the kernel, with the gain from rational points that are large at infinity. Let
`k` have decay of order `B ≥ 8 n² + 1 + j` against the product of the operator norms at the
infinite places (here `n` is short for `card n`), and let `r` times this product be at least `1`
at the points `g⁻¹ γ x` with `γ ∈ Z` at whose finite component `φ` does not vanish. Then the sum of
the moduli of the terms of `Z` in the kernel is at most a constant times `r ^ j` times a power of
the height of `x` (the inverse of the first minimum of the moved space, cut off at `1`). 

### `exists_tsum_enorm_kernelTerm_le_height`

 If `k` has decay of order `B > 8 (card n)²`, then the sum of the moduli of the terms of any
set `Z` of rational points in the kernel of `k ⊗ φ` at `g, x` is bounded by a power of the height of
`x`, uniformly in `Z` and `g`. In particular the kernel converges absolutely. 

### `summable_kernelTerm`

 If `k` has decay of order at least `13 (card n)³`, then the terms of the rational points in
`Z` in the kernel of `k ⊗ φ` are summable. 

### `summable_polyTerm`

 If `k` has decay of order at least `13 (card n)³`, then the values of `k ⊗ φ` at `x⁻¹ γ x`,
for the rational points `γ` with characteristic polynomial in `S`, are summable. 

### `exists_tsum_enorm_kernelTerm_le_of_notMem`

 Let `‖k(g)‖ ‖g‖^B` be bounded with `B ≥ 13 (card n)³`, where `‖g‖` is the product of the
operator norms. Let `A` be a cusp frame of size `δ` for `V.move x`, the space with its point moved
by `x`. This is a nonzero rational isotropic subspace such that it and its orthogonal are spanned by
lattice vectors whose length bounds have product at most `δ`. If no `γ ∈ Z` stabilises this
subspace, then `∑_{γ ∈ Z} ‖(k ⊗ φ)(x⁻¹ γ x)‖` is at most `C (δ ^ card n * height x) ^ (4 *
numInfPlaces * card n ^ 2)`. Here `C` does not depend on `x`, `δ`, `A` or `Z`, and `height x` is
`1 / min(1, first minimum of V.move x)`. 

### `exists_tsum_enorm_irreducibleTerm_le`

 If `k` has decay of order at least `13 (card n)³`, then the sum of the moduli of the values of
`k ⊗ φ` at `x⁻¹ γ x`, over the rational points `γ` with irreducible characteristic polynomial, is
bounded in `x`. 

### `exists_norm_partialKernel_spanStabilizer_le`

 Let `k` be a cusp kernel of order `B ≥ 13 (card n)³`: a minimal idempotent with `α ∗ k = k` for
some continuous compactly supported `α`, and with `‖g‖^(B+1) k` integrable and `‖g‖^B k` bounded,
where `‖g‖` is the product of the operator norms. Let `φ` be left invariant under the level `J`, an
open subgroup of `Gf E n`. Let `A` be a cusp frame of size `δ` for `V.move x`, the space with its
point moved by `x`. This is a nonzero rational isotropic subspace such that it and its orthogonal
are spanned by lattice vectors whose length bounds have product at most `δ`. Assume its radical is
covered: `N_A x ⊆ (Γ ∩ N_A) x Z_δ J`, with `Z_δ` the real `δ`-ball about `1`. Then the norm of the
sum of `(k ⊗ φ)(x⁻¹ γ x)` over the rational isometries `γ` that keep the subspace and have
characteristic polynomial in `S` is at most `C (δ ^ card n * height x) ^ (4 * numInfPlaces * card n
^ 2)`. Here `C` does not depend on `x`, `δ`, `A` or `S`, and `height x` is
`1 / min(1, first minimum of V.move x)`. 

### `exists_norm_tsum_polyTerm_le`

 If `k` is a cusp kernel (a minimal idempotent kernel with decay, an integrable moment and a
reproducing function of compact support) of order at least `13 (card n)³`, then the sums of
`k ⊗ φ` at `x⁻¹ γ x` over the rational points `γ` with characteristic polynomial in `S` are
bounded uniformly in the point `x` and in the set `S` of polynomials. 
