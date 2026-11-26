---
{
  "module": "src/New/UpperBound/Divisibility/ChainValuation.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/Divisibility/ChainValuation.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/Divisibility/ChainValuation.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# p-adic gauge bounds for chains of theta lifts and restrictions to `Y_m`

This file proves that the value of a chain of theta lifts is a sum over classes. It deduces a
general p-adic gauge bound for the chain. It then gives gauge and norm bounds for the restriction
`New.Data.restrictToY` to `Y_m`, and describes the values of source forms. `New.weylGauge` is the
gauge of a vector at a finite point `g`: a maximum of p-adic absolute values read through the
embedding ι of `[PadicPlace p]`. `New.GaugeLe d c φ` says that `φ g` has gauge at most `c` at
`g * d` for all `g`.

## Main definitions and results

* `New.Data.chainCombination_eq_sum`: take a chain that is jointly invariant for the kernels
  `D.liftKernel ϑ`. Its value at `g D.m` is a sum over tuples of classes for the levels
  `D.levelX j`, `j < D.m`, and over the tuples x in the support of Ψ. The terms are the kernel
  products times Ψ x.
* `New.Data.IsWeakChainDatum.gaugeLe_chain`: let `Ψ` be a weak chain datum for the twist `ϑ`, and
  let the places of `ϑ` have norm prime to `p`. Suppose every datum of the chain, changed by an
  operator `t j` that commutes with the levels, multiplies gauges by at most `p ^ r j` from the base
  point `d j` to `d (j + 1)`. Then the `Ψ`-combination of the chains sends a source form of gauge at
  most 1 at `d 0` to a form of gauge at most `p ^ ∑ r j` at `d D.m`.

Throughout, `D : Data P` fixes a CM field `E = D.E`, primes `p₀`, `p₁`, `N = D.N`, an integer
`π = D.piN` of `E` with `π π̄ = N`, and a length `m = D.m`. The type `D.X j` indexes a basis of a
definite hermitian space `X_j` over `E`, and `Gf D.E (D.X j)` is the group of finite adelic points
of its unitary group. Forms on `X_j` (`D.FormX j`) are algebraic automorphic forms on this group.
The level of `X_j` is `D.levelX j`, the elements of the integral subgroup `D.chosenLevel` whose last
row is `(0, …, 0, 1)` modulo `π`. Source forms are the forms on `X_0` fixed by `D.levelX 0`.

Notions from other files:
* `New.Data.Twist`: A twist: a tame character (`New.Data.TameChar`) whose tame part is non-trivial
  at every place of its set Q.
* `New.Data.Translations`: Tuples (x_j) of finite adelic matrices with rows X_{j+1} and columns X_j,
  the translations that define the data of a chain.
* `New.IsJointlyInvariant`: the tensor ∑_x L_x ⊗ Φ_{x,m−1} ⊗ ⋯ ⊗ Φ_{x,0} is unchanged by the joint
  action of the levels K_j, j < m.
* `New.Data.translateDatum`: The j-th datum of the tuple x: the normalised vacuum of Hom(X_j,
  X_{j+1}) translated by the finite Heisenberg operator of x_j.
* `New.Data.piNPlaces`: the set of primes dividing `π`, where `π π̄ = N`.



## Standard data at p and the chain value as a sum over classes

Ψ is a finitely supported function on tuples x of translations, and `New.Data.IsWeakChainDatum`
records where these are integral, that the coefficients Ψ x are integral away from the twist, and
that the combination is jointly invariant under the levels.


### `natCast_notMem_and_star_notMem_piNPlaces_of_ne`

 A place of E above a prime p ≠ N does not lie above N, and its conjugate does not divide π. 

### `mem_integralAfter_of_mem_admissibleTranslations`

 Let x be an admissible tuple of translations for q (the `x_j` become integral at the places
prime to q after multiplication by the image of `New.Data.piMBar`), and S a set of places such that
at each w in S, q is not in w, and δ is `New.Data.piMBar` or the conjugate of w is not chosen. Then
x_j lies in `integralAfter δ S`. 

### `projOn_translateDatum`

 Let S be a set of finite places, and let x_j be integral at the places of `Set.conjClosure S`,
those in S and their conjugates. Then the datum of x at j, the integral vacuum of the space
Hom(X_j, X_{j+1}) (`homX j`) translated by x_j, is fixed by `projOn (homX j) S`. This operator is
the mean, over integral vectors y, of the Heisenberg translations by the part of y at S and the
conjugate places. 

### `exists_supported_translateDatum_eq`

 If `x` lies in `D.admissibleTranslations q`, then some `x'` in `D.admissibleTranslations q` that
vanishes at all places prime to `D.M * q` (where `D.M = p₀ p₁`) has the same data:
`D.translateDatum x = D.translateDatum x'`. 

### `chainCombination_eq_sum`

 **A chain of lifts is a plain sum.** Let `D.liftKernel ϑ j` be the theta kernel from forms on
`X_j` to forms on `X_{j+1}` for the twist `ϑ`, and let the tensor `∑ x, Ψ x • ⊗ⱼ Φ x j` of data be
jointly invariant under the levels `D.levelX j`, `j < D.m`. Let `φ` be a source form, a form on
`X_0` fixed by its level. The form `chainCombination ϑ Ψ Φ D.m φ` is the sum over `x` of `Ψ x` times
the result of `D.m` successive lifts of `φ` with data `Φ x`. Its value at `g D.m` is the sum, over
tuples `c` of classes for these levels and over `x` in the support of `Ψ`, of `Ψ x` times
`kernelProduct`: the kernels at the points `classPoints c g`, applied in turn to the value of `φ` at
the first point. 

### `IsWeakChainDatum.translateDatum_mem_standardData`

 Let `Ψ` be a weak chain datum for the twist `ϑ`; only the support condition is used: each tuple
`x` in the support of `Ψ` is integral, up to the factor `star D.piM`, at the places prime to
`ϑ.normQ * N`. For a prime `p ≠ N` coprime to `ϑ.normQ`, the datum of `x` at `j` lies in
`New.Parameters.standardData` (the span of the translates of the integral vacuum by points that `δ`
makes integral above `p`) for `δ = D.piMBar`, and for every `δ` if `p` does not divide
`D.M = p₀ p₁`. 


## Valuation bound for chains with data changed by commuting operators

`New.Kernel.raises` collects the data whose kernel multiplies gauges by at most a constant.


### `gaugeLe_chainCombination`

 Let the tensor of data `∑ x, Ψ x • ⊗ⱼ Φ x j` be jointly invariant: it is unchanged when `Φ x j`
is moved by `(D.liftKernel ϑ j).ω (a j, a (j + 1))`, for `a j` in the level `D.levelX j` and
`a j = 1` for `j ≥ m = D.m`. Let the `Ψ x` be integral at `p`, and let the kernel of each `Φ x j`
send vectors of gauge `c` at `g * d j` to vectors of gauge at most `p ^ r j * c` at `g' * d (j + 1)`
(`raises`). Then the `Ψ`-combination of the chains of `m` lifts sends a source form of gauge at most
`1` at `d 0` to a form of gauge at most `p ^ ∑ j < m, r j` at `d m`. 

### `IsWeakChainDatum.gaugeLe_chain`

 Let `Ψ` be a weak chain datum for the twist `ϑ`: the tensor `∑ x, Ψ x • ⊗ⱼ D.translateDatum x j`
is invariant under the joint action of the levels `D.levelX j`, `j < m = D.m`, and the `Ψ x` are
integral at the primes that do not divide `ϑ.normQ`, such as `p` (`hQ`). Let `t j` be linear
operators on the finite part of `D.homX j`, and let `d j` be base points. Suppose that (a) the `t j`
commute with the action of `D.levelX j × D.levelX (j + 1)` on the data `D.translateDatum x j`, `x`
in the support of `Ψ`; (b) the theta kernel of each `t j (D.translateDatum x j)` sends vectors of
gauge at most `c` at `g * d j` to vectors of gauge at most `p ^ r j * c` at `g' * d (j + 1)`
(`raises`); (c) the source form `φ` has gauge at most `1` at `d 0`. Then the `Ψ`-combination of the
chains of `m` lifts with data `t j (D.translateDatum x j)` sends `φ` to a form of gauge at most
`p ^ ∑ j < m, r j` at `d m`. 

 ## Gauge and norm bounds for the restriction of forms 

### `GaugeLe.restrictToY_of_diag`

 Let `φ : D.FormX D.m` be an algebraic automorphic form on the unitary group of the hermitian
space `X_m`, and `D.restrictToY φ` its restriction to the subspace `Y_m` orthogonal to the last
basis vector. For each infinite place `τ : D.Φ` of `E`, let `w = inducedPlace τ` be the place above
`p` that `ιₚ ∘ τ` induces; the map `adeleExtension (weightEmbedding ιₚ τ)` reads an adele in `ℂ_[p]`
through its component at the conjugate place `w̄`. Suppose that this component of `d` is
`diag (1, …, 1, N)` if `w̄` lies in `D.piNPlaces`, the primes dividing `π = D.piN` (where
`π π̄ = N`), and `1` otherwise. Then `GaugeLe d c φ` implies the bound `c` for the restriction, with
base point `1`. 

### `GaugeLe.restrictToY`

 For `p ≠ N`, a form that has gauge at most `c` at every point has a restriction to `Y_m` with
the same bound. 

### `weylNormSq_restrictToY_le`

 For every embedding `σ` of `ℂ`, the squared norm of `σ` of the value at `h` of the restriction
of `φ` to `Y_m` is at most `exp (x ^ 70) N ^ (-∑ τ, n_τ)` times that of `σ` of the value of `φ` at
`D.borderU h = diag (h, 1)`. Here `weylNormSq` is the squared norm for the Gram matrix of the Weyl
module, `x = D.x` is the large integer `D.natX` that sets the scale of the data `D`, and
`n_τ = D.branchExponent τ` is the sum of the entries of the weight on `X_m` at `τ` minus that of the
weight on `Y_m`. 

 ## Values of source forms 

### `weylGauge_le_one_iff_mem_span`

 The weight on the hermitian space `X₀` has `D.columnCount τ h` columns of height `h` in its
Young diagram at the infinite place `τ`, and last entry `D.lastEntry 0 = 0`. Let `ζ` be a vector of
its Weyl module, `toPoly` of `ιₚ ∘ ζ` its polynomial, and `z_τ` the first column of variables at
`τ`, indexed by the basis of `X₀`. Then `ζ` has gauge at most `1` at `g` if and only if this
polynomial, after the substitution `rowSubst` of `g z_τ` for `z_τ`, is a combination of the
`∏_τ (a_τ! / α_τ!) z_τ ^ α_τ` with `|α_τ| = a_τ` and coefficients in the unit ball `valRingCp p` of
`ℂ_[p]`. Here `g` is read at the place induced by `ιₚ` and the complex embedding `New.Φ τ` chosen at
`τ`, and `a_τ`, the length of the one row of the weight at `τ`, is `D.a` at the places in
`D.aPlaces` and `0` at the others. 
