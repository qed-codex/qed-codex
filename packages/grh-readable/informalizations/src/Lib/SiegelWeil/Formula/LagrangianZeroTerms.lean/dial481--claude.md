---
{
  "module": "src/Lib/SiegelWeil/Formula/LagrangianZeroTerms.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/SiegelWeil/Formula/LagrangianZeroTerms.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/SiegelWeil/Formula/LagrangianZeroTerms.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Lagrangians, zero terms of the Weil representation and vanishing of dominated functionals

Let `S` and `T` be hermitian spaces. The two unitary groups act by `New.SiegelWeil.splitWeil S T` on
the function space of `Hom(S, T)`. The file defines complete splittings of `S`, Lagrangians and the
zero term of a Lagrangian: the mean of `θ (ϱ z f)` over the maps `z : S → T` vanishing on it, adelic
modulo rational, where `ϱ z` is the Heisenberg translation by `z`. It computes the norm of the zero
term `P.lagrangian.zeroTerm T` of a splitting `P` under the parabolic, and bounds it along the
normalised torus of a second splitting. It then shows, by the Hecke maximum principle, that a
continuous invariant functional vanishes if it is dominated by the norms of the zero terms of the
vacuum and `rank T > rank S > 0`.

## Main definitions and results

* `New.SiegelWeil.CompleteSplitting S p`: splittings of `S` into `p` hyperbolic planes;
  `New.SiegelWeil.Lagrangian S`: Lagrangians. Every Lagrangian comes from a splitting
  (`New.SiegelWeil.Lagrangian.exists_completeSplitting`), and one is chosen for each
  (`New.SiegelWeil.Lagrangian.chosenSplitting`).
* `New.SiegelWeil.mixedValue`, `New.SiegelWeil.Lagrangian.zeroTerm`: the value `f[x]` in the model
  of a splitting, and the zero term `f[0]` of a Lagrangian, which depends on the Lagrangian only
  (`New.SiegelWeil.zeroTerm_lagrangian_eq_theta`).
* `New.SiegelWeil.theta_normalisedTorus_le`: if `rank T > rank S`, an integrable bound for theta,
  uniform along the torus `New.SiegelWeil.normalisedTorus`.
* `New.SiegelWeil.norm_zeroTerm_parabolic_mul`: an element `g` with `g k = k a` multiplies the norm
  of the zero term by `√|det a| ^ rank T`.
* `New.SiegelWeil.exists_zeroTerm_normalisedTorus_le`: an upper bound, along the normalised torus
  `New.SiegelWeil.normalisedTorus T P x`, for the zero term of a second splitting.
* `New.SiegelWeil.eq_zero_of_le_tsum_zeroTerm`: let `S` have even positive rank less than that of
  `T`, with summable zero terms. A continuous functional `ℓ` that is invariant under the group of
  `T` and is dominated, up to an additive constant, by the sum of the norms of the zero terms of the
  translated vacuum is zero.

Notions from other files:
* `New.pairWeil`: the representation `(g, h) ↦ a (det h) b (det g)⁻¹ ω (x ↦ h x g⁻¹)` of the product
  of the two adelic unitary groups on the function space of `Hom(S, T)`.
* `New.Space.Splitting.homSource`, `New.Space.Splitting.homSlice`: the splitting of `Hom(S, T)` over
  `Hom(S₁, T)` induced by a splitting of `S` over `S₁`, and the term `f ↦ f[x]` of its mixed model
  at an adelic matrix `x`.
* `New.Space.schrodingerOp`: the operator on `𝒮 V` attached to a function `Ψ` above a set of split
  places; the indicator `New.boxIndicator` gives the projection `New.Space.projOn` on the vacua
  there.

## Relation to the literature

Known; see `Lib.SiegelWeil.Formula.WeilRange` for sources.



## Splittings, Lagrangians and zero terms

A splitting `D : S.Splitting S₁ p` consists of dual isotropic frames `D.k`, `D.l` and an isometry
`D.i` from `S₁` to their complement; `θ _` on the space of rank zero turns a vector into a number.


### `CompleteSplitting`

 The type of splittings of `S` into `p` hyperbolic planes with zero-dimensional complement, that
is, of decompositions `S = l E ^ p ⊕ k E ^ p` with dual isotropic frames `l`, `k`. 

### `splitWeil`

 The Weil representation of the pair `(S, T)` on the function space of `Hom(S, T)`, twisted by
the character `upsilonU1 ^ (n / 2)` of `det h`, where `n` is the rank of `S` and `n / 2` is rounded
down. In `splitWeil S T (g, h)` the element `g` is in the group of `S` and `h` in that of `T`. For
split `S` this twist makes the group of `T` act on slices by substitution alone
(`New.SiegelWeil.mixedValue_splitWeil`). 

### `Lagrangian`

 The type of Lagrangians of `S`: subspaces `L` of `E ^ n` that are equal to their own orthogonal
complement for the form `x* J y` of `S`. 

### `exists_mulVec_add_mulVec_of_orthogonal`

 Let `D₁` be a splitting of `S` over `S₁`, with isotropic frame `k` and embedding `i` of `S₁`.
Every vector orthogonal to the columns of `k` has the form `k a + i w`. 

### `mixedValue`

 For a complete splitting `P` of `S` and an adelic matrix `x`, the continuous functional
`f ↦ f[x]`: the slice of `f` at `x`, which is a number, the value at `x` in the Schrödinger model
attached to `P`. 

### `CompleteSplitting.lagrangian`

 The Lagrangian `k E ^ p` spanned by the columns of the frame `k` of a complete splitting `P`. 

### `Lagrangian.exists_completeSplitting`

 Every Lagrangian `L` of `S` is the span of the isotropic frame `k` of a splitting `P` of `S`
into `r` hyperbolic planes, for some natural number `r`. 

### `Lagrangian.completeSplitting`

 A natural number `r` and a splitting of `S` into `r` hyperbolic planes whose isotropic frame `k`
spans the Lagrangian `L`, chosen once. 

### `Lagrangian.numPlanes`

 The number of hyperbolic planes in the splitting chosen for the Lagrangian `L`. 

### `Lagrangian.chosenSplitting`

 The complete splitting of `S` chosen for the Lagrangian `L`; its frame `k` spans `L`
(`New.SiegelWeil.Lagrangian.lagrangian_chosenSplitting`). 

### `Lagrangian.zeroTerm`

 The zero term along a Lagrangian `L`: the value at `0` in the Schrödinger model of the chosen
complete splitting `L.chosenSplitting`, whose frame `k` spans `L`. It sends `f` to the mean of
`θ (ϱ z f)` over the maps `z : S → T` that vanish on `L`, adelic modulo rational
(`New.Space.Splitting.zeroTerm_apply`). 

### `zeroTerm_lagrangian_eq_theta`

 For a complete splitting `P` of `S`, the zero term along its Lagrangian is the value `f[0]` in
the Schrödinger model of `P`, so it does not depend on the splitting chosen. Here `P.homSource T` is
the induced splitting of `Hom(S, T)`, and `θ` on the space of rank zero turns a vector into a
number. 

### `isometrySplitting`

 For a rational isometry `γ` of `S`, the splitting of `S` with no hyperbolic planes whose
complement is `S` itself, mapped in by `γ`. 

### `zeroTerm_isometrySplitting`

 For a rational isometry `γ` of `S`, the zero term on `Hom(S, T)` of the splitting without planes
given by `γ` is the Weil operator of `(γ⁻¹, 1)`, where `S.ratEmbed` embeds the rational points. 

### `zeroTerm_lagrangian_isometrySplitting_comp`

 Let `P` be a complete splitting of `S` with frame `k` and `γ` a rational isometry. The zero term
along the Lagrangian spanned by `γ k`, that of the splitting `P` moved by `γ`, is the zero term
along the Lagrangian of `P` taken after the Weil operator of `(γ⁻¹, 1)`. 

### `exists_isometry_orthogonal`

 For a complete splitting `P` of `S` and an isotropic frame `A` with a left inverse, some
rational isometry `γ` makes the columns of `γ P.k` orthogonal to those of `A`. 

### `mem_comap_iff_forall_dot_eq_zero`

 Let `D₁` split `S` over `S₁`, and let `L` be a Lagrangian of `S` that contains the columns of
`D₁.k`. The preimage of `L` under the embedding `D₁.i` is its own orthogonal complement in `S₁`. 

### `exists_lagrangian_equiv_containing`

 Let `D₁` be a Witt decomposition `S = (l E^r ⊕ k E^r) ⊥ S₁` with isotropic frame `D₁.k`. The
Lagrangians of `S₁` are in bijection with the Lagrangians of `S` that contain the columns of `D₁.k`.
The zero term of the image is the zero term in `S₁` composed with the zero term
`𝒮(Hom(S,T)) → 𝒮(Hom(S₁,T))` along the induced splitting `D₁.homSource T`. Here the zero term along
`L` sends `f` to the mean of `θ(ϱ z f)` over the maps `z` vanishing on `L`, adelic modulo
rational. 

### `mixedValue_splitWeil_levi`

 Let `P.levi (a, 1)` be the Levi element that acts on the frame `P.k` by `a`, and let `h` be in
the group of `T`. In the Schrödinger model of `P` the pair acts by
`f[x] ↦ χ (det a)⁻¹ √|det a| ^ rank T f[h⁻¹ x a]`, where `χ = AutChar.spaceChar 1 (rank T)` is
a unitary character of the ideles, `|·|` is `ideleAbs` and `h⁻¹.adeleMatrix` is the matrix of
`h⁻¹`. 

### `mixedValue_splitWeil`

 The group of `T` acts in the Schrödinger model by substitution:
`(splitWeil S T (1, h) f)[x] = f[h⁻¹ x]`, where `f[x] = mixedValue T P x f`. 

### `hasSum_mixedValue_theta_splitWeil`

 The theta function in the Schrödinger model of `P`: `θ (splitWeil S T (1, h) f)` is the sum of
the slices `f[h⁻¹ ξ]` over the rational matrices `ξ`, which `T.x⁻¹` puts in standard coordinates. 

### `normalisedTorus`

 For `x : p → ℕ`, the operator `2 ^ (-d * rank T * ∑ i, x i) • splitWeil S T (P.levi (δ, 1), 1)`,
where `d` is the number of infinite places and `δ = New.Core.dyadicDiag x` is diagonal with entries
`2 ^ x i` at the infinite places and `1` at the finite places. 

### `normalisedTorus_zero`

 For a complete splitting `P` of `S`, the normalised torus operator `normalisedTorus T P x` on
the function space of `Hom(S, T)` is the identity at `x = 0`. 

### `norm_mixedValue_normalisedTorus`

 The normalising factor of `normalisedTorus T P x` cancels `√|det δ| ^ rank T` for
`δ = New.Core.dyadicDiag x`: the value at `y` of the image of `f` has the norm of `f[y δ]`. 

### `theta_normalisedTorus_le`

 Let `P` be a complete splitting of `S` into `p` planes and let the rank of `T` exceed `2 p`.
There is a measurable function `N` on the group of `T`, with finite integral for `T.quotMeasure`
(the measure that computes integrals over the quotient by the rational points), such that the theta
functional `θ` satisfies `‖θ (splitWeil S T (1, h) (A x f))‖ ≤ N h * ‖f‖` for all `h`, `f` and
`x : p → ℕ`, where `A x = normalisedTorus T P x`. At `x = 0` this is the convergence of the theta
integral in the Siegel–Weil formula; the bound is uniform in the torus element.

Compare Weil's convergence criterion for the theta integral of a unitary dual pair; the hypothesis
here, that `T` has rank above `2 p`, is stronger than Weil's condition on the Witt index of `T`. 


## Size of the zero term under the parabolic and along the torus

The tool is the Iwasawa decomposition. `P.kAdelic` is the frame `k` in adelic coordinates,
`New.Core.dyadicDiag x` is the diagonal matrix with `2 ^ x i` at the infinite places and `1` at the
finite ones, and `New.Core.numInfPlaces E` is the number of infinite places.


### `norm_zeroTerm_parabolic_mul`

 Let `P` be a complete splitting of `S` with isotropic frame `k`. If `g` acts on the frame by
`a`, that is `g k = k a`, then a left factor `g` multiplies the norm of the zero term along the
Lagrangian of `P` by `√|det a| ^ card m`, where `card m` is the rank of `T`. 

### `_root_.New.Space.Splitting.exists_slice_omega_vacElem_of_isEmpty`

 Let `D` split `V` completely (`V₀` has rank zero). For every `g`, the slice `D.slice x` of
`ω(g) vac` is the vacuum of `V₀` times a nonzero constant `c`, the standard additive character at
`-xᴴ z x / 2` for a hermitian matrix `z`, and `‖vacuumFn (γᴴ x)‖ ^ 2` for an invertible matrix `γ`;
the last factor is a Gaussian times the indicator of a lattice. 

### `norm_zeroTerm_vacElem_pos`

 The zero term along the Lagrangian of a complete splitting `P` of `S` does not vanish on any
translate of the vacuum vector `vacElem` of `Hom(S, T)` by an element `g` of the group of `S`. 

### `exists_ideleAbs_le_of_isCompact`

 The idele norm is bounded on the ideles that lie in a compact set `C` of adeles. 

### `exists_zeroTerm_normalisedTorus_le`

 Let `P` and `P'` be complete splittings of `S` into `p` and `r` planes, with frames `k` and
`k'`. Let `Z` be an adelic `r × n` matrix with `Z k' = 1`, and let `K` be a compact set in the group
of `S`. Let `normalisedTorus T P x` be the normalised action of the Levi element `δ(x)` of `P`
(`δ = New.Core.dyadicDiag`). There is a constant `R` such that, for all `g ∈ K`, all `x`, `u` in
`ℕ ^ p` with `Z g k δ(x) = Z g k δ(u)` and all `f`, the zero term along the Lagrangian of `P'` of
`splitWeil S T (g, 1) (normalisedTorus T P x f)` has norm at most
`R * ‖f‖ * 2 ^ (d * (∑ u - ∑ x) * card m)`. Here `d` is the number of infinite places and `card m`
is the rank of `T`. `splitWeil` is the Weil representation of the pair `(S, T)` on test functions on
`Hom(S, T)`. The zero term along `L` sends `f` to the mean of `θ (ϱ z f)` over the maps `z : S → T`
vanishing on `L`, adelic modulo rational. 


## Vanishing of functionals dominated by vacuum zero terms

At a split place `w` and for `φ` fixed by the projection on the vacua at `w`, the Hecke transfer
`New.SiegelWeil.hecke_transfer_of_equivariant` writes `g ↦ λ * ℓ (splitWeil S T (g, 1) φ)`, for a
scalar `λ`, in norm as a weighted sum of translates. The total weight is less than `‖λ‖`, the sum of
the norms of the zero terms of the vacuum is a supersolution, and the maximum principle
`New.SiegelWeil.maximum_principle` applies.


### `New.SiegelWeil.prod_mul_prod_lt_prod_one_add_pow`

 For a real `x > 1` and positive `p`, `k`, write `q = x * x`. The product of
`∏ j < k, (1 + q ^ j * x ^ (2 * p))` and `∏ j < 2 * p, (1 + q ^ j * x ^ k)` is less than
`∏ j < 2 * p + k, (1 + q ^ j)`. The first product consists of the middle `k` factors of the last. 

### `New.SiegelWeil.transferWeight`

 The weight of the subspace `U` of `𝔽_w ^ n` in the Hecke operator at `w` that the Hecke transfer
at `-1` gives on the side of `S`, for `S` of rank `2 * p` and `T` of rank `N = 2 * p + k`. Here
`𝔽_w = ResField w` is the residue field, `w.q` is the norm of `w` and `υ.atUniformizer w` the value
of the splitting character at a uniformiser. For `x ≥ 0`, `qPochhammer q k (-x)` has norm
`∏ j < k, (1 + q ^ j * x)`, and `heckePolyCoeff y U = (-y) ^ dim U * q ^ (dim U choose 2)`. 

### `New.SiegelWeil.transferPoint`

 The point of the unitary group `G E s`, supported above the split place `w` (the inverse of the
representative `basicCosetRep U` of `U`, put at `w` by `ofSplitPlace`), by which the summand of the
subspace `U` of `𝔽_w ^ n` in the Hecke operator at `w` translates. 

### `New.SiegelWeil.norm_qPochhammer_mul_norm_eq_norm_sum`

 The Hecke transfer at `-1`. Let `S` have rank `2 * p` and `T` rank `2 * p + k`, let `f` be
fixed by the projection on the vacua at the split place `w` of norm `q = w.q`, and let `Λ` be a
functional invariant under the group of `T`. Then, in norm, `Λ (splitWeil S T (g, 1) f)` times
`qPochhammer q (card m) (-1) = ∏ l < card m, (1 + q ^ l)` is the sum, over the subspaces `U` of
`𝔽_w ^ n`, of the values of `Λ` at the translates by the points `transferPoint s hw U`, with the
weights `transferWeight p k (card m) U`. 

### `New.SiegelWeil.norm_qPochhammer_neg`

 For `x ≥ 0`, the norm of `qPochhammer q k (-x)` is `∏ j < k, (1 + q ^ j * x)`. 

### `New.SiegelWeil.norm_transferWeight`

 The norm of the weight of `U` for `N = 2 * p + k`: with `x = √q`, `q = w.q` the norm of `w`, it
is `∏ j < k, (1 + q ^ j * x ^ (2 * p))` times `(x ^ k) ^ dim U * q ^ (dim U choose 2)`. 

### `New.SiegelWeil.sum_norm_transferWeight_lt`

 If `card n = 2 * p`, `p` and `k` are positive and `N = 2 * p + k`, the total weight
`∑ U, ‖transferWeight p k N U‖` is less than `‖qPochhammer w.q N (-1)‖ = ∏ l < N, (1 + q ^ l)`,
where `q = w.q` is the norm of the place `w`. 

### `New.SiegelWeil.exists_zeroTerm_omega_schrodingerOp_eq_smul`

 Let `D` split `V` over a space `V₀` of rank zero, let `A` be a set of finite places disjoint
from its conjugate, `g` in the group of `V` and `f` in `𝒮 V`. As `Ψ` runs over the nonnegative
Schwartz–Bruhat functions above `A`, the zero terms of `V.ω g (V.schrodingerOp A Ψ f)` are
nonnegative real multiples of one vector `v`. Here `V.ω` is the Weil representation, and
`V.schrodingerOp A Ψ` is the combination of Heisenberg operators on `𝒮 V` whose counterpart in the
Schrödinger model is `Ψ`. 

### `New.SiegelWeil.exists_zeroTerm_transferPoint_eq`

 Let `w` be a split place (one that differs from its conjugate), `L` a Lagrangian of `S`, and `g`
in the group of `S`, which acts by the Weil representation `splitWeil S T (·, 1)`. For a subspace
`U` of `𝔽_w ^ n`, `transferPoint s hw U` is the element of the group of `S`, supported above `w`, by
which the summand of `U` in the Hecke operator at `w` translates. The zero terms along `L` of the
vacuum translated by `g * transferPoint s hw U`, multiplied by
`(υ.atUniformizer w ^ card m) ^ dim U`, are nonnegative real multiples of one complex number `v`.
Here the zero term is the mean of `θ (ϱ z f)` over maps `z : S → T` vanishing on `L`, adelic modulo
rational, and `υ.atUniformizer w` is the value of the splitting character at a uniformiser of
`w`. 

### `New.SiegelWeil.sum_norm_mul_norm_zeroTerm_le`

 For the zero term along a Lagrangian `L` of `S` and the vacuum vector `vacElem` translated by
`g`, all summands of the Hecke operator at a split place `w` (weights `transferWeight`, points
`transferPoint`, indexed by the subspaces `U` of `𝔽_w ^ n`) have the same phase: the sum of their
norms is at most the norm of their sum. 

### `New.SiegelWeil.eq_zero_of_le_tsum_zeroTerm`

 Let `S` have rank `2 * p > 0` and `T` rank greater than `2 * p`, and let `ℓ` be a continuous
functional on the function space of `Hom(S, T)` that is invariant under the group of `T` acting by
`ω(1, h)`, where `ω = splitWeil S T`. Suppose that for every `f` the zero terms along the
Lagrangians `L` of `S` are summable over `L`; the zero term sends `f` to the mean of `θ (ϱ z f)`
over the maps `z : S → T` vanishing on `L`, adelic modulo rational. Suppose also that for every `f`
the function `g ↦ ‖ℓ (ω(g, 1) f)‖ - ∑ L, ‖zero term along L of ω(g, 1) vacElem‖` on the group of `S`
is bounded above, with `vacElem` the vacuum vector; then `ℓ f = 0` for every `f`. 
