---
{
  "module": "src/New/OneLift/ComparisonOperator/ProductsSpan.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/OneLift/ComparisonOperator/ProductsSpan.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/OneLift/ComparisonOperator/ProductsSpan.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Products span

For admissible data D (`New.Data`) and 1 ≤ j ≤ m, let 𝖥_i = `New.Data.choiceFn j i` be the functions
on the unitary group of W_j = `New.Data.spaceW j`, one for each choice i, and let θ° be the theta
kernel of (W_j, V°). A good form (`New.Data.goodForms`) is a form of principal level at the chosen
places in the image of the idempotent `New.Data.e₀`. We show that a good form y on W_j with
∫ y(g) 𝖥_i(g) θ°(g, ·) dg = 0 for all i is zero.

We write λ₁(g) for the first minimum `New.Space.firstMinimum` of the lattice at g, cut off at 1, |h|
for the largest operator norm `New.Rows.maxOpNorm` of a real point h, and m_u for the basic
holomorphic function `New.holMinorsPi` of a weight u, a quotient of products of minors. A peak
(`New.Rows.IsPeak`) of a bounded function is a point where its modulus exceeds half of the supremum.
Suppose y ≠ 0. The peaks of y are not deep in a cusp, and the proof has four steps.

1. The integral 𝖥^g of the carrier times a kernel on (S, W̃) times m_u₁ over the real group of S is
   a combination of the 𝖥_i (`New.Data.exists_sum_choiceFn_eq_integral`).
2. For every combination 𝖥 of the 𝖥_i, the integral of y 𝖥 m_u° over the real group at any point is
   zero (`New.Data.integral_mul_sum_choiceFn_eq_zero`).
3. At every peak g, 𝖥^g(g h) is close to 𝖥⁰(h), for one bounded function 𝖥⁰ with 𝖥⁰(1) ≠ 0
   (`New.Data.exists_choiceFn_approx`).
4. The mean over a circle of peaks makes 𝖥⁰(1) too small
   (`New.Data.norm_apply_one_le_of_forall_isPeak`).

Steps 1 and 3 do not involve y and come first in this file.

## Main definitions and results

* `New.Data.exists_datum_norm_modKernel_sub_polyMatrixCoeff_le` (sparse sums): for V, V' of ranks at
  most t and Q homogeneous of degree at most b^(3/2), if λ₁(g) λ₁(g') ≥ b^(−13), then for some datum
  Ψ the theta kernel `New.modKernel` at (g h, g' h') is close to the coefficient c_Q(h, h').
* `New.Data.exists_isPeak_carrierForm`: the carrier `New.Rows.carrierForm` has a peak g₁, and
  λ₁(g₁) ≥ (5 b √b)^(−1/2).
* `New.Data.exists_choiceFn_approx`: there is a bounded F₀ with F₀(1) ≠ 0 such that, when λ₁(g) ≥ (5
  b²⁴)^(−1/2), some combination F of the 𝖥_i satisfies |F(g h) − F₀(h)| ≤ 2 b^(−19 n_*) |F₀(1)|
  |h|^(6 n_*).
* `New.Data.thetaKernelPairing`: the pairing of a form on V°, given by its values at the classes,
  with the kernel θ°.
* `New.Data.eq_zero_of_integral_choiceFn_thetaKernelPairing`: products span.

Notions from other files:
* `New.Data.b`: The large scale b of the data, the weight at the b-places, as a real number.
* `New.Data.nStar`: The number n_* = 2ft³, where f is the number of infinite places of E and t = 5r.
* `New.Data.SecondFactorIndex`: The index set of V°: the r indices of W_j and t − 9m − 1 − r further
  ones.
* `New.Data.CarrierIndex`: The index set of the space S of signature (2m, m).
* `New.Data.conjHolomorphicWeight`, `New.Data.kernelWeight`: The weights u of the conjugate of y and
  u° of θ° on W_j. The 𝖥_i have the weight u − u°.

## Relation to the literature

For a finite family of choices with small integral data, a good form on U(W_j) orthogonal to all
products of the twist-free theta forms with theta kernels of the complementary block is zero. This
makes the map Θ° on good forms injective. It is a basis problem, the spanning of a space of forms by
theta series (Eichler, The basis problem for modular forms and the traces of the Hecke operators,
1973; Waldspurger, Engendrement par des séries thêta de certains espaces de formes modulaires,
1978/79; Böcherer, Siegel modular forms and theta series, 1989). It is known that stable-range theta
kernels reach all forms, that maxima of forms avoid the cusps, and that products span for GL(2).
Related work: J.-S. Li, Non-vanishing theorems for the cohomology of certain arithmetic quotients,
1992; Poor–Yuen, Linear dependence among Siegel modular forms, 2000; Khuri-Makdisi, Moduli
interpretation of Eisenstein series, 2012.



## Approximation by combinations of the 𝖥_i away from the cusps

Here S is the space of signature (2m, m), W̃ = W_j ⊕ (E^j)⁻ ⊕ E^(3m−j) is `New.Data.paddedSpace`,
W♭ = E^(6m+1), and P = `New.Data.paddedMinorProd j` is the fixed polynomial on (S, W̃).


### `negIndex_posRowIndex_injective_and_padSigns`

 Let `1 ≤ j ≤ m`, let `W_j` be the diagonal hermitian space of rank `r` with signs `D.signsW j`,
and pad it with `j` signs `-1` and `3 m - j` signs `1` to the space `W̃` with signs `padSigns j`.
The polynomial `paddedMinorProd j` is a product of minors whose rows are indices of `W̃`: one minor
has the `m` rows `negIndex j a`, and for each column height `h` one has the `2 m` rows
`posRowIndex j h a`, which start at the basis vector of number `h` of `W_j`. Each of these families
of rows is injective; the rows `negIndex j a` have sign `-1` and the rows `posRowIndex j h a` have
sign `1`. 

### `exists_datum_norm_modKernel_sub_polyMatrixCoeff_le`

 Sparse sums. The data `D` give the CM field `E` with its `f` infinite places `D.Φ`, a large real
scale `b = D.b`, the numbers `t = D.t` and `n_* = nStar D = 2 f t ^ 3`, and the modulus
`untwistedModulus 2 = ϖ²`. Let `V`, `V'` be hermitian spaces of ranks at most `t`, let the
characters `χ`, `χ'` of `U(1)` have weights `γ`, `e` at the infinite places and residue characters
`ψ`, `ψ'`, and let the polynomial `Q` be homogeneous of degree `d ≤ b ^ (3 / 2)`. Write `λ₁(g)` for
the first minimum, cut off at `1`, of the lattice of `V` moved by the adelic point `g`, `|h|` for
the operator norm `maxOpNorm h`, and `c_Q = polyMatrixCoeff s s' γ e Q` for the matrix coefficient
of the real Weil representation at the Fock vector of `Q`. If `λ₁(g) λ₁(g') ≥ b ^ (-13)`, then for
some function `Ψ` on matrices modulo `ϖ²` the theta kernel `modKernel` with data `Ψ`, `Q` at
`(g h, g' h')` differs from `c_Q(h, h')` by at most
`b ^ (-20 n_*) (|h| |h'|) ^ (6 n_*) |c_Q(1, 1)|`, for all real points `h`, `h'`. 

### `paddedMinorProd_mem_supported`

 Give a variable of `paddedMinorProd j` the sign `padSigns j` of its row times the sign `1 ⊕ᵥ -1`
of its column in `D.CarrierIndex`. Each of its variables has row and column of the same sign, so
`paddedMinorProd j` is a polynomial in the variables of sign `1`. 

### `maxOpNorm_sum_one_le`

 Extending a point of the group of `W_j` by the identity on the padding does not increase its
norm. 

### `polyMatrixCoeff_paddedMinorProd_ne_zero_and_bounded`

 Let `S` be the space of signature `(2 m, m)`, with index set `D.CarrierIndex` and signs
`1 ⊕ᵥ -1`, and let `W̃` be the space `W_j` (`1 ≤ j ≤ m`) padded to the signs `padSigns j`. Let
`P = paddedMinorProd j` be the fixed product of minors in the variables of `(S, W̃)`. For characters
of any weights `γ`, `e`, the matrix coefficient `polyMatrixCoeff` of the real Weil representation at
the Fock vector of `P` does not vanish at the identity, and it is bounded on the product of the real
unitary groups of `S` and `W̃`. 

### `exists_eval_smul_paddedMinorProd`

 The product of minors `paddedMinorProd j` is homogeneous of degree at most `b ^ (3 / 2)`, where
`b = D.b` is the large scale of the data. Its variables are indexed by an infinite place, a basis
vector of `W_j` (`D.RowIndex`) or of its padding (`PadIndex j`), and a basis vector of the space of
signature `(2 m, m)` (`D.CarrierIndex`). 

### `flatKernelWeight`

 The weight `u₁ = (-Δ'; 6 m + 1)` of the kernels on `(S, W♭)`, the same at every place. Here
`Δ' = reducedHalfGap` is `Δ / 2 - (t + 1) / 2`, where the gap `Δ = 2 r ^ 8` is the difference of the
weights of consecutive lifts, and `6 m + 1` is the rank of `W♭`. Here and below `(a; b)` has the
entry `a` at the signs `+1` and `b` at the signs `-1` of `S`. 

### `holomorphicWeight`

 The weight `(Δ'; μ₁⁺ + r + 2 m)` of the holomorphic factor in the coefficient of
`paddedMinorProd`. Here `Δ' = reducedHalfGap` is `Δ / 2 - (t + 1) / 2` for the gap `Δ`, and
`μ₁⁺ = #(DetIndex j w)` is the number of columns of the diagram `μ⁺` at the place `w`: the sum of
the column counts `colsPlus` of `untwistedDescentPair j`, plus `Δ'`. The weight is `u₂ + μ₁⁺`, where
`u₂ = (Δ' - μ₁⁺; r + 2 m)` is the weight for the standard character `υ ^ m`. The shift by `μ₁⁺` in
every entry arises because the character `carrierChar j` of the kernel has weight `m - μ₁⁺` instead
of `m`. 

### `antiholomorphicWeight`

 The weight `u₃ = (0; μ₁⁺ + n'' + 2 m)` of the antiholomorphic factor in the coefficient of
`paddedMinorProd`. Here `μ₁⁺ = #(DetIndex j w)` is the number of columns of the diagram `μ⁺` at the
place `w` (the sum of the column counts `colsPlus` of `untwistedDescentPair j`, plus
`reducedHalfGap`), and `n'' = #(FirstFactorIndex j) = r + 9 m + 1` is the rank of `W̃ ⊕ W♭`. 

### `polyMatrixCoeff_paddedMinorProd`

 Let `S` be the space of signature `(2 m, m)`, with signs `1 ⊕ᵥ -1`, and let `W̃` be the padded
space of rank `r + 3 m` with signs `padSigns j`. Let `c_P` be the matrix coefficient
`polyMatrixCoeff` of the Fock vector of the product of minors `P = paddedMinorProd j` on `(S, W̃)`;
the weight `γ` of the first character is arbitrary, and that of the second is `m - μ₁⁺`, where
`μ₁⁺ = #(DetIndex j w)` is the number of columns of the partition `μ⁺` of the `j`-th lift at the
place `w`. Then for every real point `h` of the group of `S`,
`c_P(h, 1) = c_P(1, 1) m₂(h) conj(m₃(h))`. Here `m₂`, `m₃` are the quotients of minors `holMinorsPi`
of the weights `holomorphicWeight j = (Δ'; μ₁⁺ + r + 2 m)` and
`antiholomorphicWeight j = (0; μ₁⁺ + r + 11 m + 1)`, with `Δ' = D.reducedHalfGap` and with the
entries at the signs `+1`, `-1` before and after the semicolon. 

### `flatKernelWeight_antiholomorphicWeight_bounds`

 Let `S` be the space of signature `(2 m, m)`, with index set `D.CarrierIndex` and signs
`1 ⊕ᵥ -1`. The weights `u₁ = flatKernelWeight D` and `u₃ = antiholomorphicWeight j` are integer
vectors on the indices of `S`, one for each infinite place. For every order `o` on the indices they
are `K`-dominant and have gap `300 n_*`, and `u₃` has entries of modulus at most `5 b`. Here
`b = D.b` is the large scale of the data and `n_* = nStar D = 2 f t ^ 3`, with `f` the number of
infinite places and `t = 5 r`. 

### `carrierChar_hasWeight_sub_card`

 The character `carrierChar j` of the kernels on `(S, W̃)` and `(S, W̃ ⊕ W♭)` has weight
`m - μ₁⁺`, with `μ₁⁺ = #(DetIndex j w)` at the place `w`, and trivial tame part. 

### `exists_isPeak_carrierForm`

 Let `S = signedSpace D.E (1 ⊕ᵥ -1)` be the space of signature `(2 m, m)`, and let
`φ° = carrierForm D.E D.m` be the carrier, the theta lift of the constant function `1` from the
negative definite space of rank `m` to `S`. Assume that `φ°` is automorphic of every level and
rapidly decreasing (`rapidOfLevel`), and holomorphic in the real variable of weight `(0; 3 m)` for
an order `o` with the signs `+1` first. Then `φ°` has a peak `g₁`, and the first minimum of the
lattice of `S` at `g₁`, cut off at `1`, is at least `(5 b √b) ^ (-1 / 2)`, where `b = D.b` is the
large scale of the data. 

### `paddedSpace`

 The space `W̃ = W_j ⊕ (E^j)⁻ ⊕ E^(3 m - j)`. 

### `firstMinimum_le_paddedSpace`

 For `g` in the group of `W_j = D.spaceW j`, the first minimum (cut off at `1`) of `W_j` moved by
`g` is at most that of the padded space `W̃ = paddedSpace j` moved by `G.sum (g, 1)`. So extending
`g` by `1` to `W̃` does not lower the first minimum. 

### `exists_sum_choiceFn_eq_integral`

 Step 1 of the proof that products span. Let `1 ≤ j ≤ m`, let `W_j` be the diagonal space with
signs `D.signsW j`, let `W̃ = paddedSpace j` be its sum with a definite space of each sign, and let
`S = signedSpace D.E (1 ⊕ᵥ -1)` be the space of signature `(2 m, m)`. Assume that the order `o` puts
the signs `+1` of `S` first, that the carrier `φ° = carrierForm D.E D.m` is automorphic of every
level and rapidly decreasing (`rapidOfLevel`), and that the quotient of minors
`m_u₁ = holMinorsPi _ u₁` is integrable on the real group of `S`, where `u₁ = flatKernelWeight D` is
the weight of the kernels on `S` and `W♭ = E^(6 m + 1)`. Let `g₁` be a point of the group of `S`,
let `Ψ` be a function on matrices modulo `ϖ²` (`untwistedModulus 2`, with `ϖ` the product of the
chosen places above the level primes), and let `θ[Ψ, P]` be the theta kernel `modKernel` of
`(S, W̃)` with datum `Ψ`, polynomial the product of minors `P = paddedMinorProd j`, and characters
`υ ^ m` and `carrierChar j` of `U(1)`, where `υ = upsilonU1` has weight `1`. Then, as a function of
the point `g` of the group of `W_j`, the integral of `φ°(g₁ h) θ[Ψ, P](g₁ h, (g, 1)) m_u₁(h)` over
the real points `h` is a linear combination of the functions `choiceFn j i`. These are the integrals
of `φ°` against theta kernels of `(S, W̃ ⊕ W♭)`, one for each choice `i` of an additive character
of the matrices modulo `ϖ²`, a class of `U(W♭)` at level `ϖ²` and rows of determinants. 

### `inv_pow_twenty_mul_pow_nStar`

 The identity `b ^ (-20 n_*) b ^ n_* = b ^ (-19 n_*)` for `n_* = nStar D`. 

### `inv_pow_le_firstMinimum_mul`

 Let `S = signedSpace D.E (1 ⊕ᵥ -1)`. Suppose the first minimum of `S` moved by `g₁` is at least
`(5 b √b) ^ (-1 / 2)`. Suppose that of `D.spaceW j` moved by `g` is at least
`(5 b ^ 24) ^ (-1 / 2)`. Then the first minimum of `S` moved by `g₁`, times that of `paddedSpace j`
moved by `G.sum (g, 1)`, is at least `b ^ (-13)`. Here `b = D.b` is the large scale of the data. 

### `card_carrierIndex_le_and_card_sum_padIndex_le`

 Let `S` be the space with index set `D.CarrierIndex` of `3 m` elements, and let `W̃` be the
padded space `W_j ⊕ (E^j)⁻ ⊕ E^(3 m - j)`: `j` signs `-1`, then `3 m - j` signs `1`. Both have rank
at most `t = 5 r`. The index set of `W̃` is `D.RowIndex ⊕ PadIndex j`: the `r` indices of `W_j` and
the `3 m` indices of the padding. 

### `integral_mul_polyMatrixCoeff_paddedMinorProd`

 Let `f` be holomorphic of weight `(0; 3 m)` on the real group of the space `S` of signature
`(2 m, m)`, for an order `o` with the signs `+1` first. Let `1 ≤ j ≤ m` and let `W̃` be the padded
space of rank `r + 3 m` with signs `padSigns j`. Let `c_P` be the matrix coefficient
`polyMatrixCoeff` of the Fock vector of the product of minors `P = paddedMinorProd j` on `(S, W̃)`;
the weight `γ` of the first character is arbitrary, and that of the second is `m - μ₁⁺`, with
`μ₁⁺ = #(DetIndex j w)` the number of columns of the partition `μ⁺` of the `j`-th lift at the place
`w`. Let `m₁`, `m₃` be the quotients of minors `holMinorsPi` of the weights
`u₁ = flatKernelWeight D`, that of the kernels on `S` and `E^(6 m + 1)`, and
`u₃ = antiholomorphicWeight j`, that of the antiholomorphic factor of `c_P(·, 1)`. If
`f c_P(·, 1) m₁` is integrable, its integral is `f(1) c_P(1, 1)` times the integral of
`|m₃| ^ 2`. 

### `exists_choiceFn_approx`

 There is a bounded function `F₀` on the real group of `W_j` with `F₀ 1 ≠ 0` such that, at every
adelic `g` off the cusps, in the sense that the lattice of `W_j` moved by `g` has first minimum at
least `(5 b ^ 24) ^ (-1 / 2)`, some combination `F` of the `choiceFn j i` has `|F (g h) - F₀ h| ≤ 2
b ^ (-19 n_*) |F₀ 1| |h| ^ (6 n_*)` for all real `h`. Here `|h| = maxOpNorm h`, `b = D.b` is the
large scale of the data, and `n_* = nStar D = 2 f t ^ 3`, with `f` the number of infinite places and
`t = 5 r`. 


## The proof that products span

The good form is called `F`. By the reproducing formula `New.Rows.reproducing_formula_modKernel`,
the vanishing pairings give a vanishing integral over the real group.


### `thetaKernelPairing`

 The pairing `⟨ζ, θ°(g, ·)⟩` of a form `ζ` on the definite space `V°` with the theta kernel `θ°`
of `(W_j, V°)`; it is conjugate-linear in `ζ`. The form is given by its values at the classes
`SecondFactorClasses` of `U(V°)` at principal level `ϖ²`, where `untwistedModulus 2` is the modulus
`ϖ²`. The values lie in the Weyl module, written in the basis `WeylIndexFamily`, of the diagrams
`μ⁻` with the column counts `colsMinus` of `untwistedDescentPair j`, the `j`-th descent pair at the
trivial twist. The term of a class `c` is the kernel `modKernelStdSpace` at `(g, c)` whose datum is
the indicator of the inclusion matrix of `W_j` in `V°` modulo `ϖ²` and whose polynomial is that of
the conjugate of `ζ c` in the variables of the negative basis vectors of `W_j` (`letterPoly`). 

### `isAdelicHol_star_goodForms`

 Let `1 ≤ j ≤ m`, let `W_j = D.spaceW j` be the diagonal hermitian space with signs `D.signsW j`,
and let `F` be a good form on `W_j`: an automorphic form whose real type is the discrete series of
doubled parameter `paramW`, fixed by the principal congruence subgroup at the chosen places above
the level primes, and in the image of the idempotent `e₀` of the group algebra of the finite groups
`GL_r` over their residue fields. Then for every adelic `g` the function `h ↦ conj F(g h)` on the
real group is holomorphic (`IsAdelicHol`). 

### `integral_mul_sum_choiceFn_eq_zero`

 Let `1 ≤ j ≤ m`, let `F` be a good form on `W_j = D.spaceW j`, and write `F_i = choiceFn j i`
for the functions on the adelic group of `W_j` attached to the choices `i`. Let `V°` be the definite
space with index set `D.SecondFactorIndex`. A form `ζ` on `V°` assigns to each class at level `ϖ²` a
vector of the Weyl module of the diagrams with column counts `colsMinus`, in the basis
`WeylIndexFamily`, and `thetaKernelPairing j ζ g` pairs it with the theta kernel of `(W_j, V°)` at
`g`. Assume that the integrals of `F F_i` against these pairings, over the adelic group modulo its
rational points (`quotMeasure`), vanish for all `i` and `ζ`, and that the quotient of minors
`m_u° = holMinorsPi _ u°` is integrable, where `u° = kernelWeight j` is the weight of that kernel on
`W_j`. Then the integral of `F(g h) (∑ c_i F_i(g h)) m_u°(h)` over the real points `h` is zero for
every adelic `g`. 

### `eq_zero_of_integral_choiceFn_thetaKernelPairing`

 Products span. For admissible data `D` and `1 ≤ j ≤ m`, let `W_j = D.spaceW j` be the diagonal
hermitian space with signs `D.signsW j` and let `V°` be the definite space with index set
`D.SecondFactorIndex`. Let `F` be a good form on `W_j`: a form of principal level at the chosen
places in the image of the idempotent `e₀` of the group algebra of the finite groups at these
places. If `∫ F(g) F_i(g) θ°(g, ·) dg = 0` for all `i`, then `F = 0`. Here the `F_i = choiceFn j i`
are integrals of the carrier `carrierForm` against theta kernels, one for each of the finitely many
choices `i` of kernel data; the integral is over the adelic group modulo its rational points
(`quotMeasure`); and `thetaKernelPairing j ζ g` is the pairing of the theta kernel `θ°(g, ·)` of
`(W_j, V°)` with a form `ζ` on `V°`. Such a form assigns to each class at level `ϖ²` a vector of the
Weyl module, in the basis `WeylIndexFamily` indexed by the infinite places `D.Φ`, of the diagrams
whose column counts `colsMinus` belong to the data `untwistedDescentPair j` of the `j`-th lift. 
