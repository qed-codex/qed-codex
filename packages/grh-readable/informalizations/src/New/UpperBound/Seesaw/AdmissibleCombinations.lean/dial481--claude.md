---
{
  "module": "src/New/UpperBound/Seesaw/AdmissibleCombinations.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/Seesaw/AdmissibleCombinations.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/Seesaw/AdmissibleCombinations.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Graded lattices, integrality away from q and admissible combinations of translates

This file provides tools for the computations at the finite places of the seesaw. A grading
(`New.Grading`) presents a hermitian space `V` as `X` plus a string of `s` basis vectors, and
`New.gradedLatticeBasis` is an explicit basis of a lattice in it, unimodular when `N = π π̄`.
Integrality lemmas handle numbers integral away from `q` and `l`-adic units.
`New.Seesaw.IsAdmissibleCombination v A n d p B z` says that `z = ∑ r(x) v(x)` with `r` finitely
supported in `A`, denominator `d` away from `n`, and size `B` when `p` holds. Moved vacua
(translates of the vacuum vector of the Weil representation, moved by a finite unitary element) and
the values of the operators `V.schrodingerOp` attached to functions modulo `𝔪` are such
combinations of translates.

## Main definitions and results

* `New.Seesaw.integralAway`, `New.Seesaw.IsAdmissibleCoeffs`: complex numbers integral away from
  `n`, and finite families of coefficients with bounded denominator and, on demand, bounded size.
* `New.Seesaw.weightedTranslations`, `New.Seesaw.translations`: finite adelic vectors with given
  denominators away from `q`. They index the translates that may occur in a combination.
* `New.Seesaw.isUnimodular_gradedLatticeBasis_gram`: if `N = π π̄`, the Gram matrix of
  `New.gradedLatticeBasis` is hermitian and invertible over every subring.
* `New.Seesaw.exists_conjTranspose_mul_gradedGram_mul_eq_signMatrix`: for `N > 0` the form is
  congruent over `ℂ` to a diagonal of signs, `(s + 1) / 2` of them negative.
* `New.Seesaw.IsAdmissibleCombination.bind`: substitution; denominators and sizes multiply. The
  rules for scalars, bilinear maps and pure tensors follow from it.
* `New.Seesaw.isAdmissibleCombination_weil_vacElem`,
  `New.Seesaw.isAdmissibleCombination_schrodingerOp`: moved vacua and the values of
  `V.schrodingerOp` are admissible combinations of translates.

Notions from other files:
* `New.Space`: a hermitian space with a point, given by a matrix J over E and x in GL_n(𝔸) with
  xᴴJx equal to the diagonal matrix of its signs at the infinite places and 1 at the finite places.
* `New.gradedGram e N`: the Gram matrix of X plus a string of length s: the identity on X; string
  vectors a, b with a + b = s − 1 pair to 1, or to −N if a = b.
* `New.finMultiplier`: for g in the finite adelic unitary group `New.Gf`,
  Δ_f(g) = υ(det u)|det u|^(−1/2), with υ the splitting character of the Weil data and u a chosen
  invertible matrix with uÔⁿ = Ôⁿ ∩ g⁻¹Ôⁿ.
* `New.AutChar.HasWeight`: μ has weight e and tame part ψ: almost all residue characters ψ_w are
  trivial, and μ(u) = ∏_v u_v^{e(v)} · ∏_w ψ_w(u mod w) whenever u has integral finite part.

## Relation to the literature

See `New.UpperBound.Seesaw.SeesawIdentity` for related work. See
`Lib.ClassField.Global.CMSplittingCharacters` for sources.



## Lattices of graded spaces and admissible coefficients

* `New.Seesaw.IsSplitSquarefree`: `N = π π̄`, where `π` is a uniformiser at the places of `P` and a
  unit elsewhere, and no place of `P` has its conjugate in `P`.

Valuations `v` are multiplicative: `v x ≤ 1` means integral, and `exp (-1)` is the value at a
uniformiser.


### `gradedLatticeBasis`

 A basis matrix (the basis vectors are its columns), for `X = X' ⊕ Unit` and a string of `s`
vectors, indexed by `ι` through `e`; write `π̄ = star π` and `ā = star a`. For odd `s`: the vectors
of `X'` are unchanged, the last vector `y` of `X` is replaced by `y / π̄ + u z / (π π̄)` with `z`
the middle vector of the string, and each string vector is multiplied by `u`. For even `s`:
diagonal, `1` on `X`, `u a⁻¹` on the first half of the string and `u ā` on the second half. 

### `Grading.SpansLattice`

 Let `Y` present the hermitian space `V` as `X' ⊕ Unit` plus a string of `s` vectors. The
condition says that the finite frame `V.xFin` spans the same `Ô`-lattice as the basis
`New.gradedLatticeBasis Y.indexEquiv a π u`: the two differ by some `k` in `GL(Ô)`. 

### `integralAway`

 The subring of complex numbers whose image under every ring homomorphism `ℂ → ℂ_l` is
integral (has norm at most `1`), for every prime `l` coprime to `n`. 

### `IsAdmissibleCoeffs`

 The conditions on finitely supported coefficients `r`: the support lies in `A`, each `d * r x`
is integral away from `n` (`New.Seesaw.integralAway`) and, if `p` holds, `∑ ‖σ (r x)‖ ≤ B` for
all automorphisms `σ` of `ℂ`. 

### `IsAdmissibleCoeffs.support_subset`

 The points with a nonzero coefficient lie in `A`. 

### `IsAdmissibleCoeffs.integral`

 Every coefficient, multiplied by `d`, is integral away from `n`. 

### `IsAdmissibleCoeffs.sum_norm_le`

 If `p` holds, then for every field automorphism `σ` of `ℂ` the sum of the absolute values of
  the `σ`-conjugates of the coefficients is at most `B`. 

### `weightedTranslations`

 The group of finite adelic vectors `x` such that `d i * x i` is integral at every place `w` not
dividing `q`, for every index `i`. There is no condition at the places dividing `q`. 

### `translations`

 The group of finite adelic vectors `x` indexed by `ι` such that `d * x i` is integral at every
place `w` not dividing `q`, for every index `i`. 

### `IsSplitSquarefree`

 The element `N` of `E` factors as `π π̄` for the finite idele `π`, which is a uniformiser at the
places of `P` and a unit at all other places, and no place of `P` has its conjugate in `P`. 

### `IsSplitSquarefree.algebraMap_eq_mul_star`

 In the finite adeles `N = π π̄`. 

### `IsSplitSquarefree.v_apply`

 The idele `π` is a uniformiser at the places of `P` and a unit at the others. 

### `IsSplitSquarefree.star_notMem`

 No place of `P` has its conjugate in `P`. 


## A unimodular lattice basis and the signature of the graded Gram matrix

`New.gradedGram e N` is the Gram matrix of `X ⊕ Unit` (identity) plus a string of length `s`
(antidiagonal, with `-N` in the middle if `s` is odd), and `New.gradedLatticeBasis` is a basis of
a lattice in this space.


### `gluedGram`

 A form on `X ⊕ Unit` plus a string of `s` vectors, by blocks: identity on `X`; string vectors
paired antidiagonally to `1`, with `-p` in the middle; for odd `s` the vector of `Unit` has norm
`q` and pairs to `-1` with the middle vector (for even `s` it is a unit vector orthogonal to the
string). 

### `eq_rev_iff_of_odd`

 For odd `s`, the reversal `c ↦ s - 1 - c` of `Fin s` fixes exactly the middle index. 

### `ne_rev_of_not_odd`

 For even `s`, the reversal `c ↦ s - 1 - c` of `Fin s` has no fixed point. 

### `map_gluedGram`

 A ring homomorphism carries `gluedGram p q` to the form with parameters `(f p, f q)`. 

### `gluedGram_mul_eq_one`

 The matrices `gluedGram p 0` and `gluedGram 0 p` multiply to `1`. 

### `map_gradedGram`

 A ring homomorphism carries the graded Gram matrix with parameter `r` to the one with `f r`. 

### `isHermitian_map_gradedGram_natCast`

 The image of the graded Gram matrix `New.gradedGram e N`, with `N` a natural number, under a
ring homomorphism `f` into a star ring is hermitian. 

### `gram_gradedLatticeBasis_eq_gluedGram`

 Let `e` index `X ⊕ Unit` and a string of `s` vectors by `ι`. Let `J = New.gradedGram e N` be the
form that is the identity on `X ⊕ Unit` and pairs string vectors `b` and `s - 1 - b` to `1`, or to
`-N` if they are equal, carried from `S` to the star ring `R` by `f`; write `π̄ = star π` and
`ā = star a`. The columns of `B = New.gradedLatticeBasis e a π u` are the basis vectors, changed as
follows. For odd `s`, the string vectors are multiplied by `u` and the vector `y` of `Unit` becomes
`y / π̄ + u z / (π π̄)`, with `z` the middle string vector. For even `s`, the first half of the
string is multiplied by `u a⁻¹` and the second half by `u ā`. If `N = π π̄` in `R`, then `Bᴴ J B`
is `gluedGram N 0`, reindexed by `e`. It agrees with `J` except that, for odd `s`, the vector of
`Unit` has norm `0` and pairs to `-1` with the middle vector. 

### `isUnimodular_gradedLatticeBasis_gram`

 Let `e` index `X ⊕ Unit` and a string of `s` vectors by `ι`. Let `J = New.gradedGram e N` be the
form that is the identity on `X ⊕ Unit` and pairs string vectors `b` and `s - 1 - b` to `1`, or to
`-N` if they are equal, carried from `S` to the star ring `R` by `f`. For units `a`, `π` and a
unitary `u` of `R`, the columns of `B = New.gradedLatticeBasis e a π u` are the basis vectors,
changed as follows. For odd `s`, the string vectors are multiplied by `u` and the vector `y` of
`Unit` becomes `y / π̄ + u z / (π π̄)`, with `z` the middle string vector. For even `s`, the first
half of the string is multiplied by `u a⁻¹` and the second half by `u ā`. If `N = π π̄` in `R`,
then `Bᴴ J B` is unimodular over every subring `O` of `R`: it is hermitian and lies in `GL(O)`. 

### `stringSign`

 The signs on a string of `s` vectors: `-1` at the first `⌊(s + 1) / 2⌋` indices and `1` at
the others. 

### `stringFrame`

 A complex frame for a string of `s` vectors `e_b`, with `σ = stringSign s`. Column `b` is
`(σ b • e_b + e_{s - 1 - b}) / √2`. At the middle index `b = s - 1 - b` these two terms cancel,
as `σ b = -1`, and `e_b / √N` is added. 

### `gram_stringFrame_eq_signMatrix`

 On a string of `s` vectors `e_b`, take the form that pairs `e_b` and `e_{s - 1 - b}` to `1`, or
to `-N` if they are equal, with `N` a positive integer. Let `σ = stringSign s` be `-1` at the first
`⌊(s + 1) / 2⌋` indices and `1` at the others. The frame `stringFrame s N` has column `b` equal to
`(σ b • e_b + e_{s - 1 - b}) / √2`, or to `e_b / √N` if `b = s - 1 - b`. Its Gram matrix is the
diagonal matrix `New.signMatrix σ` of the signs `σ b`. 

### `conjTranspose_stringFrame_one_mul_self`

 For `N = 1` the frame `stringFrame s N` is unitary. 

### `exists_conjTranspose_mul_gradedGram_mul_eq_signMatrix`

 Let `e` index `X ⊕ Unit` and a string of `s` vectors by `ι`, and let `N` be a positive integer.
Let `J` be the image under `φ` of `New.gradedGram e N`, the form that is the identity on `X ⊕ Unit`
and pairs string vectors `b` and `s - 1 - b` to `1`, or to `-N` if they are equal. If exactly
`⌊(s + 1) / 2⌋` of the signs `ε i` are `-1`, then `yᴴ J y = diag(ε)` (`New.signMatrix ε`) for some
complex matrix `y`, which is unitary if `N = 1`. 

 ## Integrality away from q and above a prime l 

### `Seesaw.div_mem_integralAway`

 For natural numbers `c`, `d`, `q` and `k`: if `c` divides `d * q ^ k`, then the complex number
`d / c` lies in `integralAway q`. 

### `Seesaw.localLevel_le_integralAbove_of_coprime`

 If `l` is coprime to `q`, a finite adelic unitary point that is integral at all places not
dividing `q` is integral at the places above `l`. 

### `Parameters.norm_finMultiplier_eq_one`

 Let `E` be a CM field with Weil data, of which only the splitting character `υ` (a Hecke
character of `E`) is used. For `g` in the finite adelic unitary group `New.Gf E n` of matrices
indexed by `n`, the multiplier `New.finMultiplier g` is `υ(det u) |det u|^(-1/2)`, where `u` is a
chosen invertible finite adelic matrix with `u Ôⁿ = Ôⁿ ∩ g⁻¹ Ôⁿ`. If `g` and `g⁻¹` are integral at
the places above the prime `l`, its image under every ring homomorphism `ι : ℂ → ℂ_l` has norm
`1`. 

### `AutChar.HasWeight.norm_apply_detFin_eq_one`

 Let the automorphic character `a` of the norm-one adeles have weight `e` (its exponents at the
infinite places) and tame part `ψ` (its characters of the residue fields), and let the finite adelic
unitary point `g` be integral above `l`. Then the value of `a` at `New.detFin s g`, the determinant
of `(1, g)` in the unitary group of signature `s`, has norm `1` under every ring homomorphism
`ι : ℂ → ℂ_l`. 


## Admissible combinations of vectors and their calculus

* `New.Seesaw.IsAdmissibleCombination.normUnit_smul`: clearing the denominator by rescaling.


### `New.Seesaw.IsAdmissibleCombination`

 The statement that `z = ∑ r x • v x` for some finitely supported `r` with support in `A`,
denominator `d` away from `n` and, if `p` holds, size at most `B`
(`New.Seesaw.IsAdmissibleCoeffs`). 

### `of_sum`

 A finite sum `∑ i ∈ s, c i • v i` is an admissible combination over `s`, with denominator `d`
away from `n` and size `B` under `p`, if each `d * c i` is integral at the primes coprime to `n`
and, if `p` holds, `∑ i ∈ s, ‖σ (c i)‖ ≤ B` for all automorphisms `σ` of `ℂ`. 

### `smul_single`

 A single term `c • v x` with `x ∈ A` is an admissible combination of size `1` if `d · c` is
integral away from `n` and, under `p`, all conjugates `σ c` have absolute value at most `1`. 

### `single`

 Each vector `v x` with `x ∈ A` is an admissible combination of size `1`, for any
denominator `d`. 

### `bind`

 Substitution. Fix a natural number `n` and a proposition `p`. A vector is an admissible
combination of the `v x`, `x ∈ A`, with denominator `d` and size `B` if it is a finite sum
`∑ r x • v x` over points of `A` in which each `d * r x` is integral at the primes coprime to `n`
and, if `p` holds, `∑ ‖σ (r x)‖ ≤ B` for all automorphisms `σ` of `ℂ`. Let `z` be such a
combination, and let each `v x`, `x ∈ A`, be an admissible combination of the `v' y`, `y ∈ A'`, with
denominator `d'` and size `B'`. Then `z` is an admissible combination of the `v' y`, `y ∈ A'`, with
any denominator `e` divisible by `d d'` and any size `C` that is at least `B |B'|` if `p` holds. 

### `bind_one`

 Substitution without loss: if each `v x`, `x ∈ A`, is an admissible combination of the `v' y`,
`y ∈ A'`, with denominator `1` and size `1`, then an admissible combination of the `v x` is one of
the `v' y`, with the same denominator and size. 

### `map`

 A linear map `L` sends an admissible combination of the `v x` to one of the `L (v x)`, with the
same coefficients. 

### `smul`

 Admissible combinations are stable under a scalar `c` that is integral away from `n` and, if
`p` holds, has all conjugates `σ c` of absolute value at most `1`. 

### `smul_of_eq_zero_or_isOfFinOrder`

 Admissible combinations are stable under a scalar that is `0` or a root of unity. 

### `of_eq_isOfFinOrder_smul`

 If each `v x`, `x ∈ A`, is a root of unity times some `v' y`, `y ∈ A'`, then an admissible
combination of the `v x` is one of the `v' y`, with the same denominator and size. 

### `map_bilinear`

 Fix a natural number `n` and a proposition `p`. A vector is an admissible combination of the
`v x`, `x ∈ A`, with denominator `d` and size `B` if it is a finite sum `∑ r x • v x` over points of
`A` in which each `d * r x` is integral at the primes coprime to `n` and, if `p` holds,
`∑ ‖σ (r x)‖ ≤ B` for all automorphisms `σ` of `ℂ`. Let `z` be such a combination, and let `z'` be
one of the `v' y`, `y ∈ A'`, with denominator `d'` and size `B'`. For a bilinear map `b`, the value
`b z z'` is an admissible combination of the `b (v x) (v' y)`, `(x, y) ∈ A × A'`, with denominator
`d d'` and size `B |B'|`. 

### `smul_mem`

 Let `z` be an admissible combination of the `v x`, `x ∈ A`, with denominator `d` away from `n`,
and let `l` be a prime coprime to `n`. Then `d z` lies in every module `M` that contains these `v x`
over `New.embValRing`, the ring of complex numbers whose image under the chosen homomorphism
`ιₚ : ℂ → ℂ_l` is integral. 

### `normUnit_smul`

 Let `d ≠ 0` and let `z` be an admissible combination of the `C • v x`, `x ∈ A`, with denominator
`d` and size `B`. Then `a • z`, multiplied by `normUnit (a * C / d)` (which is `d / (a C)`, or `1`
if `a C = 0`), is an admissible combination of the `v x`, `x ∈ A`, with denominator `1` and size
`d B`. 

### `New.Seesaw.IsAdmissibleCombination.pure`

 Fix a natural number `n` and a proposition `p`. A vector is an admissible combination of vectors
`w x`, over a set of indices `x`, with denominator `d` and size `B` if it is a finite sum
`∑ r x • w x` over that set in which each `d * r x` is integral at the primes coprime to `n` and, if
`p` holds, `∑ ‖σ (r x)‖ ≤ B` for all automorphisms `σ` of `ℂ`. Let each `f i`, `i < m`, be such a
combination of the vectors `v i (s, t)` with `s ∈ A (2 i)` and `t ∈ A (2 i + 1)`. Then the pure
tensor `f (m - 1) ⊗ ⋯ ⊗ f 0` is an admissible combination, over the families `y` with all
`y j ∈ A j`, of the pure tensors of the `v i (y (2 i), y (2 i + 1))`, with denominator `d ^ m` and
size `|B| ^ m`. 


## Moved vacua as admissible combinations

A translate of the vacuum moved by a finite unitary element is a multiple of a sum, over lattice
classes, of translates of the vacuum times roots of unity.


### `New.Seesaw.isAdmissibleCombination_weil_vacElem`

 Let `E` be a CM field with Weil data, `V` a hermitian space over `E` with coordinates `n` and
signs `s`, and `ω` its Weil representation. Let `g` be a finite adelic unitary matrix, and factor as
`c * C` its multiplier `finMultiplier g = υ(det u) |det u|^(-1/2)`, with `υ` the splitting character
of the Weil data and `u Ôⁿ = Ôⁿ ∩ g⁻¹ Ôⁿ`. Translate the vacuum `vacElem` by `x`, with the
Heisenberg operator `finHeisenbergOp x`, and apply `ω (1, g)`. The result is a finite sum
`∑ r y • C • finHeisenbergOp y vacElem` over `y` in `A`, for any set `A` that contains all
`g (x + z)` with `z` in the lattice `Ôⁿ`. If `d c / ‖finMultiplier g‖ ^ 2` is integral at the primes
coprime to `q`, so is each `d * r y`. The proposition `p` is arbitrary: if under `p` all conjugates
`σ c` have absolute value at most `1`, then under `p` all `∑ ‖σ (r y)‖ ≤ 1`. 


## Values of `schrodingerOp` as admissible combinations

By finite Fourier inversion, the operator attached to a function modulo `𝔪` sends a vector to an
admissible combination of translates.


### `card_residueRing_pi_dvd`

 Let `𝔪` be a modulus of `E` (a nonzero ideal of `𝓞 E` prime to its conjugate) that divides
`g q`, for `g` in `𝓞 E` and a natural number `q`. Then the number of vectors over `𝓞 E / 𝔪` divides
a power of `q` times `N(g) ^ card n`, where `N(g)` is the absolute norm of the ideal `(g)`. 

### `star_idem_smul_mem_translations`

 Let `𝔪` be a modulus of the CM field `E`, with `𝔪.places` the primes dividing it,
`𝔪.reduction : Ô → 𝓞 E / 𝔪` the reduction of integral finite adeles and `𝔪.generator` a chosen
finite idele generating its kernel. Divide a vector `z` of integral finite adeles by `𝔪.generator`,
set the components outside `𝔪.places` to `0` (multiplication by the idempotent `idem 𝔪.places`), and
apply complex conjugation `star`. If `d q ≡ 0` modulo `𝔪`, the result times `star d` is integral at
all places not dividing `q`. 

### `isAdmissibleCombination_schrodingerOp_of_reduction`

 Let `E` be a CM field with Weil data (the choices that fix the Weil representation), `V` a
hermitian space over `E` with coordinates `n` and signs `s`, and `𝒮 V` the space of its Weil
representation, on which a finite adelic vector `y` acts by the Heisenberg operator
`finHeisenbergOp y`. Let the modulus `𝔪` divide `g q` and `d q`. Let `v` be the image of `u` under
`projOn 𝔪.places`, the mean of the `finHeisenbergOp y` over the integral `y` supported at the primes
dividing `𝔪` and their conjugates. Let `Ψ` be a function on vectors modulo `𝔪` with values integral
away from `q`, read on finite adelic vectors by `liftFn`. The operator `V.schrodingerOp` attached to
it sends `u` to a finite sum `∑ r y • finHeisenbergOp y v` over vectors `y` with `star d • y`
integral away from `q`. Each `N(g) ^ card n * r y` is integral away from `q`, with `N(g)` the
absolute norm of `(g)`. If under the proposition `p` all `∑ ‖σ (Ψ x)‖ ≤ B`, for the automorphisms
`σ` of `ℂ`, then under `p` all `∑ ‖σ (r y)‖ ≤ B`. 

### `isAdmissibleCombination_schrodingerOp`

 The case `d = g` of `isAdmissibleCombination_schrodingerOp_of_reduction`. Let `V` be a hermitian
space over the CM field `E`, `u` a vector of its Weil representation `𝒮 V`, and `𝔪` a modulus that
divides `g q`. Let `v` be the mean `projOn 𝔪.places u` of the Heisenberg translates
`finHeisenbergOp y u` over the integral `y` supported at the primes dividing `𝔪` and their
conjugates. Let `Ψ` be a function on vectors modulo `𝔪` with values integral away from `q`. The
operator `V.schrodingerOp` attached to `Ψ` sends `u` to a finite sum `∑ r y • finHeisenbergOp y v`
over vectors `y` with `star g • y` integral away from `q`, and each `N(g) ^ card n * r y` is
integral away from `q`, with `N(g)` the absolute norm of `(g)`. If under the proposition `p` all
`∑ ‖σ (Ψ x)‖ ≤ B`, for the automorphisms `σ` of `ℂ`, then under `p` all `∑ ‖σ (r y)‖ ≤ B`. 
