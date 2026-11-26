---
{
  "module": "src/Lib/Weil/Construction/FourierInversion.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Weil/Construction/FourierInversion.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Weil/Construction/FourierInversion.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Fourier inversion for theta functions

Let `δ` be integral with `δ δ̄` a nonzero natural number and let `r` be the number of elements of
`InfinitePlace E × n`, that is, the number of infinite places times the rank.

* `New.Space.exists_entireTheta_eq_of_isThetaFunction`: a theta function for `δ̄ 𝔞₀ⁿ` is the theta
  function of a vector `φ` of the finite part `V.finitePart` (a subspace containing the vacuum and
  stable under the translations `V.ϱ (finVec _)`).
* `New.Space.fourier_inversion`: if the theta function of `φ` is one for `δ̄ 𝔞₀ⁿ` and `y` runs over
  `δ⁻¹ 𝔞₀ⁿ⧸𝔞₀ⁿ`, the signed sums of translates of `ρ(-y) φ` over `𝔞₀ⁿ⧸δ̄ 𝔞₀ⁿ` are multiples
  `c_y vac` of the vacuum, and `∑ c_y ρ(y) vac = (δ δ̄) ^ r φ`, with `ρ` the finite translation.
* `New.Space.norm_mul_vacElem_le_one_of_eq_sum`: if the values of `φ` at the vectors `finVec x` are
  integral at a prime, then so are those of such a multiple `c_y vac`.

Here `φ` lies in `𝒮 V`. In the first two results the space `V` is standard (`V.IsStd`: all signs are
`+1` and the point is the identity); the third holds for every space. The theta functions of these
sums are theta functions for `𝔞₀ⁿ`, and orthogonality of the characters of `δ⁻¹ 𝔞₀ⁿ⧸𝔞₀ⁿ` inverts the
summation.

Notions from other files:
* `idealLattice E n` is the lattice `𝔞₀ⁿ` in `Eⁿ` of the vectors with integral finite image
  `finiteImage`, and `Ô E` is the ring of integral finite adeles.
* `ratShift γ` is the translation `T_γ` of functions on `ℂ^(InfinitePlace E × n)`, `ratPhase γ γ'`
  the commutator of `T_γ` and `T_γ'`, and `signedShift γ` the translation `T_γ` times the
  semicharacter at `γ`.
* `IsThetaFunction Y F` says that `F` is entire and fixed by the signed translations along `Y`.
* `entireTheta φ` is the theta function of a vector `φ` of `𝒮 V`. The vector `V.vacElem` is the
  vacuum, `V.ϱ` the translation by adelic vectors and `V.finHeisenbergOp` the signed finite
  translation.

## Relation to the literature

Known result: theta functions for a sublattice are spanned by translates of the theta function of a
principal polarization. The proof is by Fourier inversion on a finite abelian group. Source:
Mumford, Tata lectures on theta I.


### `IsRepresentativeSystem`

 The elements `y i` of `K` represent each class of `K` modulo `H` exactly once. 

### `IsRepresentativeSystem.mem`

 The elements lie in `K`. 

### `IsRepresentativeSystem.existsUnique`

 Each element of `K` is congruent modulo `H` to exactly one of them. 

### `mk_eq_mk_iff_sub_mem`

 Two elements of `K` have the same class modulo `H ⊓ K` exactly if their difference lies
in `H`. 

### `out`

 Chosen representatives of the quotient of `K` by `H ⊓ K` are a system of representatives. 

### `exists_mem_iff_eq`

 Exactly one of the representatives lies in `H`. 

### `card_eq_relIndex`

 A system of representatives of `K` modulo `H` has `[K : H ⊓ K]` elements. 

### `sum_add_left`

 If `f` is constant on the classes of `K` modulo `H`, its sum over the representatives is
unchanged by translation by an element of `K`. 

### `sum_character`

 Orthogonality: for `ψ` multiplicative and trivial on `H`, the sum of `ψ` over representatives
of `K` modulo `H` is their number if `ψ` is trivial on `K`, and `0` otherwise. 

### `exists_of_relIndex_ne_zero`

 If `[K : H ⊓ K]` is finite, `K` has a finite system of representatives modulo `H`. 

### `relIndex_map_nsmul_toAddSubgroup`

 The index of `N L` in a free `ℤ`-module `L` of finite rank `r` is `N ^ r`. 

### `ratPhase_swap`

 The commutator `exp (2 π i {y, γ})`, with `{·,·}` the Riemann form `ratRiemannForm`, is
`exp (2 π i {-γ, y})`, as the Riemann form is alternating. 

### `IsThetaFunction.ratShift`

 A translate `T_y F = ratShift y F` of a theta function for `Y` is one too if `T_y` commutes with
the translations along `Y`, that is, if the commutator `ratPhase γ y` is `1` for `γ ∈ Y`. 

### `IsThetaFunction.sum_signedShift`

 Let `F` be a theta function for `Y` and let `γ j` represent the classes of `𝔞₀ⁿ` modulo `Y`.
Then the sum of the signed translates of `F` by the `-γ j` is a theta function for `𝔞₀ⁿ`. 

### `star_smul_idealLattice_le`

 For an integral `δ` the lattice `δ̄ 𝔞₀ⁿ` lies in `𝔞₀ⁿ`. 

### `idealLattice_le_inv_smul`

 For a nonzero integral `δ` the lattice `𝔞₀ⁿ` lies in `δ⁻¹ 𝔞₀ⁿ`. 

### `relIndex_star_smul_inv_smul`

 For `δ δ̄ = N` and `δ ≠ 0`, the index of `δ̄ 𝔞₀ⁿ` in `δ⁻¹ 𝔞₀ⁿ` is that of `N 𝔞₀ⁿ` in `𝔞₀ⁿ`,
where `𝔞₀ⁿ = idealLattice E n`: multiplication by `δ` carries one pair to the other. 

### `relIndex_map_nsmul_idealLattice`

 The index of `N 𝔞₀ⁿ` in the lattice `𝔞₀ⁿ = idealLattice E n` is `N ^ (2 r)`, with `r` the number
of elements of `InfinitePlace E × n`: the real image `realLattice E n` of `𝔞₀ⁿ` is a lattice of
rank `2 r`. 

### `relIndex_mul_relIndex_idealLattice`

 For `δ` integral with `δ δ̄ = N ≠ 0`, the orders of `𝔞₀ⁿ⧸δ̄ 𝔞₀ⁿ` and `δ⁻¹ 𝔞₀ⁿ⧸𝔞₀ⁿ` have the
product `N ^ (2 r)`, with `r` the number of elements of `InfinitePlace E × n`. 

### `exists_isRepresentativeSystem_inv_smul`

 For `δ` integral with `δ δ̄ = N ≠ 0`, the group `δ⁻¹ 𝔞₀ⁿ⧸𝔞₀ⁿ`, where `𝔞₀ⁿ = idealLattice E n`,
has a finite system of representatives. 

### `exists_isRepresentativeSystem_star_smul`

 For `δ` integral with `δ δ̄ = N ≠ 0`, the group `𝔞₀ⁿ⧸δ̄ 𝔞₀ⁿ`, where `𝔞₀ⁿ = idealLattice E n`,
has a finite system of representatives. 

### `sum_ratPhase_inv_smul`

 Let `δ ≠ 0` and `𝔞₀ⁿ = idealLattice E n`. For `x` in `𝔞₀ⁿ`, the sum of the commutators
`ratPhase x y = exp (2 π i {x, y})` over representatives `y` of `δ⁻¹ 𝔞₀ⁿ` modulo `𝔞₀ⁿ` is their
number if `x` lies in `δ̄ 𝔞₀ⁿ`, and `0` otherwise. 

### `sum_ratPhase_star_smul`

 Let `δ ≠ 0` and `𝔞₀ⁿ = idealLattice E n`. For `x` in `δ⁻¹ 𝔞₀ⁿ`, the sum of the commutators
`ratPhase γ x = exp (2 π i {γ, x})` over representatives `γ` of `𝔞₀ⁿ` modulo `δ̄ 𝔞₀ⁿ` is their
number if `x` lies in `𝔞₀ⁿ`, and `0` otherwise. 

### `card_representatives_inv_smul_eq_card_star_smul`

 For `δ ≠ 0` and `𝔞₀ⁿ = idealLattice E n`, there are as many classes of `δ⁻¹ 𝔞₀ⁿ` modulo `𝔞₀ⁿ`
as of `𝔞₀ⁿ` modulo `δ̄ 𝔞₀ⁿ`, as the commutator pairing makes them dual to each other. 

### `card_representatives_idealLattice`

 For `δ` integral with `δ δ̄ = N ≠ 0` and `𝔞₀ⁿ = idealLattice E n`, the representatives `y` of
`δ⁻¹ 𝔞₀ⁿ⧸𝔞₀ⁿ` and `γ` of `𝔞₀ⁿ⧸δ̄ 𝔞₀ⁿ` both number `N ^ r`, with `r` the number of elements of
`InfinitePlace E × n`. 

### `IsThetaFunction.sum_ratShift_sum_signedShift`

 Let `F` be a theta function (entire, fixed by the signed translations) for `δ̄ 𝔞₀ⁿ`, `δ ≠ 0`,
with `𝔞₀ⁿ = idealLattice E n`, and let `y`, `γ` run over representatives of `δ⁻¹ 𝔞₀ⁿ⧸𝔞₀ⁿ` and
`𝔞₀ⁿ⧸δ̄ 𝔞₀ⁿ`. With `T_y = ratShift y` the translation and `S_γ = signedShift γ` the signed
translation, `∑_y T_(-y) ∑_γ S_(-γ) T_y F` is `F` times the number of the `y`. 

### `Space.exists_smul_entireTheta_vacElem_eq`

 Fourier inversion for theta functions in a standard space `V` (all signs are `+1`, the point is
the identity). Let `δ` be integral with `δ δ̄ = N ≠ 0` and `F` a theta function for `δ̄ 𝔞₀ⁿ`, where
`𝔞₀ⁿ = idealLattice E n`: `F` is entire and fixed by the signed translations `signedShift` along
`δ̄ 𝔞₀ⁿ`. Let `y`, `γ` represent `δ⁻¹ 𝔞₀ⁿ⧸𝔞₀ⁿ` and `𝔞₀ⁿ⧸δ̄ 𝔞₀ⁿ`. With `T_y = ratShift y`, the sum
of the `signedShift (-γ) (T_y F)` is a multiple `c_y ϑ` of the theta function `ϑ` of the vacuum, and
`∑ c_y T_(-y) ϑ = N ^ r F`, with `r` the number of elements of `InfinitePlace E × n`. 

### `Space.fourier_inversion`

 Fourier inversion in a standard space `V` (all signs are `+1`, the point is the identity). Let
`δ` be integral with `δ δ̄ = N ≠ 0` and let the theta function `entireTheta φ` of a vector `φ` of
`𝒮 V` be entire and fixed by the signed translations along `δ̄ 𝔞₀ⁿ`, where `𝔞₀ⁿ = idealLattice E n`.
Let `y` run over `δ⁻¹ 𝔞₀ⁿ⧸𝔞₀ⁿ` and `γ` over `𝔞₀ⁿ⧸δ̄ 𝔞₀ⁿ`. Then the sum of the signed translates, by
`V.finHeisenbergOp`, of `ρ(-y) φ` by the `γ` is a multiple `c_y vac` of the vacuum, and
`∑ c_y ρ(y) vac = N ^ r φ`. Here `ρ(y)` is the translation `V.ϱ` by the adelic vector
`finVec (finiteImage y)`, with finite part `y` (as `finiteImage` divides by the finite idele `α`
and `finVec` multiplies by it) and infinite part zero, and `r` is the number of elements of
`InfinitePlace E × n`.

This is used instead of the upper bound in Frobenius's formula for the dimension of a space of
classical theta functions (the Pfaffian of the Riemann form), for the lattice `δ̄ 𝔞₀ⁿ` and theta
functions of the form `entireTheta φ` only. 

### `Space.exists_entireTheta_eq_of_isThetaFunction`

 Let `δ` be integral with `δ δ̄ = N ≠ 0` and let `V` be a standard space (all signs are `+1` and
the point is the identity). Every theta function `F` for the lattice
`δ̄ 𝔞₀ⁿ = star δ • idealLattice E n`, that is, every entire function fixed by the signed
translations along it, is the theta function `entireTheta φ` of a vector `φ` of the finite part
`V.finitePart` (a subspace containing the vacuum and stable under the translations `V.ϱ (finVec _)`)
of `𝒮 V`. 

### `Space.exists_fourier_coefficients`

 Let `V` be a standard space (all signs are `+1` and the point is the identity), let `δ` be
integral with `δ δ̄ = N ≠ 0`, and let the theta function `entireTheta φ` of `φ` be one for `δ̄ 𝔞₀ⁿ`
(fixed by the signed translations along it), where `𝔞₀ⁿ = idealLattice E n`. There are finite
families of `y` with `δ y ∈ 𝔞₀ⁿ` and, indexed by `N ^ r` elements, of `γ ∈ 𝔞₀ⁿ`, and numbers
`c_y`, such that `c_y vac` is the signed sum of the translates of `ρ(-y) φ` by the `γ`, and
`∑ c_y ρ(y) vac = N ^ r φ`. Here `r` is the number of elements of `InfinitePlace E × n`, `vac` the
vacuum `V.vacElem`, `ρ(y)` the translation `V.ϱ` by the vector `finVec (finiteImage y)` with
infinite part zero, and `V.finHeisenbergOp` the signed translation. 

### `Space.exists_sum_finHeisenbergOp_apply_eq`

 Let `E` be a CM field with Weil data, `V : Space E n ε` a hermitian space, `φ` a vector of
`𝒮 V`, and `a j`, `b`, `x` finite adelic vectors. Write `ρ(b) φ = V.ϱ (finVec b) φ` for the
translate of `φ` by `finVec b`, the adelic vector with finite part `α b` and infinite part zero,
where `α` is the finite idele of the Weil data. The value at `finVec x` of the sum over `j` of the
operators `V.finHeisenbergOp (a j)` (scalar-twisted translates) applied to `ρ(b) φ` equals a sum
over `j` of values of `φ` at some vectors `finVec (z j)`, each multiplied by the value at some `w j`
of the finite-adelic character `selfDualAddChar`. 

### `Space.norm_mul_vacElem_le_one_of_eq_sum`

 Let the values of a vector `φ` of `𝒮 V` at the points `finVec x` with infinite part zero be
integral at `p`, that is, of norm at most `1` under the embedding `ιₚ : ℂ → ℂ_[p]` given by the
instance `PadicPlace p`. If a multiple `c • vac` of the vacuum `V.vacElem` is a sum of signed
translates `V.finHeisenbergOp (a j)` of the translate `V.ϱ (finVec b) φ`, then the values of
`c • vac` at these points are integral too. 
