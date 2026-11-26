---
{
  "module": "src/New/UpperBound/Seesaw/SeesawIdentity.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/Seesaw/SeesawIdentity.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/Seesaw/SeesawIdentity.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# The seesaw identity and the top of the chain

On the definite space `Y_m`, the integral of a matrix coefficient of a form on `X_m` against a form
on `Y_m` is a multiple of the inner product with the restricted form. To prove the seesaw identity,
we pair `Θ_ξ 𝒫 φ` with a form on `Y_m` and move the Bessel period up the lower chain, one lift at a
time. Each outer integral is a real integral times a weighted sum over the classes `Ω_j`. What
remains is the upper chain for the tensor `φ_ξ`, a multiple of which is the glued tensor of a chain
datum.

Notions from other files:
* `D.spaceY j`, `D.FormY j`: the space `Y_j` of the lower chain and the forms on its unitary group.
* `liftY ϑ j`, `lowerChainUpTo ϑ j`: the theta lift from `Y_j` to `Y_(j+1)` with twist `ϑ`,
  normalised by the index of its level, and the composite of the first `j` lifts.
* `D.poincareAt g t`: the Poincaré map `𝒫` from forms on `X_0` to forms on `Y_0`.
* `Grading`, `unfoldStage`: a grading of a space, with its Bessel group `R`, and the function `𝒲`
  that is left after some steps of unfolding.
* `cutPoints ϑ j`, `cutSum`: the classes `Ω_j` of the finite variables and the weighted sum over
  them.

In the notation of the comments the subscript `ξ` of `Θ_ξ`, `J_ξ` and `φ_ξ` stands for the twist
`ϑ`: `Θ_ξ = lowerChainUpTo ϑ`, `J_ξ(Y_j) = levelY ϑ j`. A `ξ` by itself is the tuple of real parts
of the outer variables. The lattice stabiliser `stdLevel` is written `J°`, and the index
`stdLevelIndex J` is `[J° : J]`. A tame character `ϑ` is an automorphic character of `U(1)` of
weight `0` with a finite set `ϑ.Q` of places (its modulus) outside which its tame part is trivial;
it is a twist if the tame part is nontrivial at every place of `ϑ.Q`. The chosen places, those
dividing `D.piM`, are fixed by the data `D` and do not depend on `ϑ`.

## Relation to the literature

For ramified source forms φ and every twist, the restricted definite chain of lifts of φ, with data
of controlled support and denominators, is a non-zero constant, free of φ and the twist, times the
indefinite chain of lifts of the Poincaré series of φ. The transfer of a Bessel or Fourier–Jacobi
period under one theta lift is known, locally and globally. Related work: B. Wang, Global theta
lifting and periods associated to nilpotent orbits, 2025; Gomez–Zhu, Local theta lifting of
generalized Whittaker models, 2014; Gan–Ichino, The Gross–Prasad conjecture and local theta
correspondence, 2016.

Each period in the seesaw unfolding is a constant times a finite sum over cosets of a small level,
weighted by reciprocals of stabiliser indices that divide powers of the norm of the twist's
conductor. So the coefficients of the definite chain get no new denominators away from the
conductor. Related work: Gross, Algebraic modular forms, 1999; Hsieh–Namikawa, Bessel periods and
non-vanishing of Yoshida lifts modulo a prime, 2015; X. Zhang, Non-vanishing mod p of theta lifts
for (O(2n+1), Mp(4n)), 2022.


 ## Restriction to the definite space `Y_m` at the top of the chain 

### `restrictToFormY`

 The restriction from the forms `D.FormX M` on `X_m` to the forms `D.FormY M` of the lower chain
on `Y_m`: it is `D.restrictToY`, read in automorphic forms. The index `m` is written as any number
`M` equal to it. 

### `lowerChain_eq_of_lowerChainUpTo_eq`

 If the image `lowerChainUpTo ϑ M f` of a form `f` on `Y_0` under the composite of the lifts with
twist `ϑ` is the restriction `restrictToFormY hM ψ` to `Y_m` of a form `ψ` on `X_m`, where `M = m`,
then `lowerChain ϑ f = restrictToYOfEq hM ψ`. Here `lowerChain` and `restrictToYOfEq` are the same
two maps with values in algebraic forms in place of automorphic forms. 

### `exists_integral_eq_mul_inner_restrictToFormY`

 Let `M = m`, the number of lifts. For every linear form `t` on the values of forms on `X_m`
there is a constant `C` as follows. Let `x` be a form on `Y_m`, `ψ` one on `X_m` and `F` a function
on `G_m = U(Y_m)`, whose signs at infinity are `D.signsY M`. The last grading `D.lastGrading hM`
identifies `Y_m` with the standard definite space on `D.InitIndex M`, the `n_m - 1` basis indices of
`X_m` other than the last, and `inclX` is the resulting map of unitary groups. Suppose that at the
image of `k` under `inclX` the value of `F` is the coefficient `t (ψ (diag (k, 1)))`. Then the
integral of `F` times the conjugate of `x` over `[G_m]` is `C` times `⟨x, res ψ⟩`, where `res` is
`restrictToFormY`. 

 ### Iterated unfolding 

### `ConjFormY`

 Forms on `Y_j` of the conjugate type; they are paired with the forms of the lower chain. 

### `transposedLiftY`

 The transposed lift, or descent, from `Y_{j+1}` to `Y_j`, times the index `[J° : J_ξ(Y_j)]`
that normalises the lift `liftY ϑ j`. 

### `transposedLiftY_apply`

 The descent as a theta integral. Let `ϑ` be a tame character, let `j < m`, and let `z` be a
conjugate form on `Y_(j+1)`. The descent of `z` at `g` is the index of the level `levelY ϑ j` in the
lattice stabiliser `stdLevel` of `Y_j`, times the integral over `h ∈ [G_(j+1)]` of `z h` times
`θ (ω (g, h) (datumY ϑ j))`. Here `datumY ϑ j` is the Schwartz function on `Hom(Y_j, Y_(j+1))` that
defines the lift, `θ` is the theta functional, `G_j = U(Y_j)`, and `ω` is the Weil representation of
`G_j × G_(j+1)` whose character on a space of rank `n` is `rankTwist` of `D.chainChar ϑ (j + 1)`:
this character of `U(1)`, formed from `ϑ ^ (j + 1)`, times `υ ^ ⌊n / 2⌋`, with `υ` the fixed
character `upsilonU1`. 

### `integral_mul_liftY`

 Lift and descent are transposes of each other. Let `ϑ` be a tame character, which twists both
maps, let `j < m`, and let `f` be a form on `Y_j` and `z` a conjugate form on `Y_(j+1)`. Then the
integral over `[G_(j+1)]` of `z` times the lift `liftY ϑ j f` is the integral over `[G_j]` of the
descent `transposedLiftY ϑ j z` times `f`. Here `G_j` is the unitary group of `Y_j`. 

### `twistedPairWeil_datumY_of_mem_levelY`

 Let `ϑ` be a tame character and `u` an element of its level `levelY ϑ j`: an integral finite
adelic point of `G_j = U(Y_j)` that reduces to `1` at the chosen places and at the places of the
modulus `ϑ.Q`. Let `datumY ϑ j` be the Schwartz function on `Hom(Y_j, Y_(j+1))` that defines the
lift from `Y_j` to `Y_(j+1)`. In the Weil representation of `G_j × G_(j+1)` for this lift, with
characters given by `rankTwist` of `D.chainChar ϑ (j + 1)`, the pair of the point `(1, u)` of `G_j`,
with archimedean part `1` and finite part `u`, and the identity of `G_(j+1)` fixes this datum. 

### `hasLevel_transposedLiftY`

 Let `ϑ` be a tame character, `j < m` and `z` a conjugate form on `Y_(j+1)`. The descent
`transposedLiftY ϑ j z` is fixed by right translation by the level `levelY ϑ j` (`HasLevel`),
because the datum of the lift is. 

### `isRapid_conjFormY`

 For `j < m` every conjugate form on `Y_(j+1)` is rapidly decreasing. 

### `unfoldedPeriod`

 The integral `Ξ_{k+1}` of the product `𝒲_{k+1} z` over `R_{k+1}(F) \ G_{k+1}(𝔸)`, where
`𝒲_{k+1} = unfoldStage ϑ t φ ξ y k hk Y` is the function on `G_{k+1}` left by the first `k + 1`
steps of unfolding for the source form `φ`, the linear form `t` and the outer variables
`g_i = (ξ i, y i)`, and `R_{k+1}(F) = Y.ratBessel` consists of the rational points of the Bessel
group of `Y`. 

### `integrable_unfoldStage_mul`

 The integral `Ξ_{k+1}` converges absolutely. Let `k ≤ 2 ϱ + 1`, let `ϑ` be a tame character,
`φ` a form on `X_0`, `t` a linear form on its values and `(ξ i, y i)` the archimedean and finite
parts of points `g_i` of `U(Y_i)`, at which the earlier stages are evaluated. These define the
function `unfoldStage` on `G_{k+1} = U(Y_{k+1})` that is left after `k + 1` steps of unfolding. For
a grading `Y` of `Y_{k+1}`, whose Bessel group has rational points `R_{k+1}(F) = Y.ratBessel`, and a
conjugate form `z` on `Y_{k+1}`, its product with `z` is integrable over
`R_{k+1}(F) \ G_{k+1}(𝔸)`. 

### `integral_unfoldStageOn_mul_transposedLiftY`

 The recursion of the iterated unfolding, for the tame character `ϑ`, the source form `φ` on
`X_0`, the linear form `t` on its values and the outer variables `g_i = (ξ i, y i)`, points of
`U(Y_i)` split into archimedean and finite part. Let `k ≤ 2 ϱ + 1`, where `m = 2 ϱ + 2` is the
number of lifts, let `Y` be a grading of `Y_{k+1}`, and let `z` be a conjugate form on `Y_{k+1}`.
The function `unfoldStageOn` on the Bessel group `R_k` of the standard grading `D.gradingY k` is the
Bessel function of `φ` for `k = 0`, and for `k > 0` the function left by `k` steps of unfolding,
translated by `g_k`. Integrate it at `r ∈ [R_k]` times the descent of `z` at `r g_k`. The result is
the index of `levelY ϑ k` in the lattice stabiliser times `Ξ_{k+1}` (`unfoldedPeriod`): the integral
of `z` times the function left by `k + 1` steps over the quotient of `U(Y_{k+1})` by the rational
Bessel group of `Y`. 

### `sum_quotient_chosenLevel_eq_sum_cutPoints`

 Let `ϑ` be a tame character and `J = levelY ϑ 0` its level on `Y_0`, a subgroup of
`J_M = D.chosenLevel`. Let `f` be a function on the finite adelic unitary group of `Y_0` that is
fixed by right translation by `J`. Then the sum of `f` over representatives of `J_M / J` is its sum
over representatives of `Ω_0 = cutPoints ϑ 0`, the classes modulo `J` of the elements of `J_M`. 

### `integral_mul_liftY_poincareAt`

 Let `ϑ` be a tame character, `t` a linear form on the values of forms on `X_0`, `g` an
archimedean point of `U(Y_0)` and `𝒫 φ = D.poincareAt g t φ` the Poincaré series of `φ` on `Y_0`.
Let `Y` be a grading of `Y_1` with a string of `2 ϱ` vectors. The integral of a conjugate form `z`
on `Y_1` times the first lift `liftY ϑ 0 (𝒫 φ)` is `[J° : J_M]` times the sum of the periods `Ξ_1`
over the classes `c` in `Ω_0 = cutPoints ϑ 0`. Here `J°` is the lattice stabiliser `stdLevel`,
`J_M = D.chosenLevel` is its subgroup of elements that reduce to `1` at the chosen places, and `Ω_0`
consists of the classes modulo `levelY ϑ 0` of the elements of `J_M`. The period `Ξ_1`
(`unfoldedPeriod`) is the integral, over the quotient of `U(Y_1)` by the rational Bessel group of
`Y`, of `z` times the function left by one step of unfolding of `φ` at the outer variable
`(g, c.out)` of index `0`; the others are `1`. 

### `exists_integral_mul_lowerChainUpTo_eq_cutSum`

 The outer integrals of the seesaw, one at a time. Let `t` be a linear form on the values of
forms on `X_0`, `g` an archimedean point of `U(Y_0)`, `k ≤ 2 ϱ + 1`, `Y` a grading of `Y_{k+1}`
with a string of `s = 2 ϱ + 1 - (k + 1)` vectors, and `a` a function of tuples `ξ` of archimedean
points of the groups `U(Y_i)`. There is a number `c` as follows, for every tame character `ϑ`,
ramified source form `φ` on `X_0`, conjugate form `z` on `Y_{k+1}` and function `S` of the classes
modulo `levelY ϑ i` of tuples `y` of finite points. Suppose that `unfoldedPeriod` at step `k`, the
integral of `z` times the function on `U(Y_{k+1})` left by `k + 1` steps of unfolding of `φ` at
`(ξ, y)`, is `a ξ` times `S` at the classes of `y` whenever `y 0 ∈ D.chosenLevel` and `y m = 1`,
where `m = 2 ϱ + 2`. Then the pairing of `z` with the image of the Poincaré series
`D.poincareAt g t φ` under the first `k + 1` lifts is `c` times `cutSum`: the sum of `S` over
`Ω_0 × ⋯ × Ω_k`, where `Ω_j = cutPoints ϑ j`, each term divided by the multiplicities
`cutMultiplicity` of its classes. 

 ### The tensor `φ_ξ` and the seesaw identity 

### `evaluatedTensor`

 The tensor product of the evaluated data (`evaluatedDatum`) of all double lifts, translated by
representatives of the classes `c j` of the outer variables of the lower chain. 

### `evaluatedTensor_mk`

 At the classes of a tuple `y` of points of `G_f`, `evaluatedTensor ϑ` is the pure tensor
`pure (evaluatedDatum ϑ y) (D.ϱ + 1)`, built from the first `D.ϱ + 1` evaluated data. 

### `seesawDatum`

 The tensor `φ_ξ` of finite data for the upper chain: the weighted sum `cutSum` over the cuts of
the lower chain of the evaluated translates `evaluatedTensor` of its data. 

### `isInvariant_seesawDatum`

 The tensor `φ_ξ = seesawDatum ϑ` of finite data for the chain of lifts `X_0 → ⋯ → X_m`, where
`ϑ` is a tame character and `m = 2 ϱ + 2`, is jointly invariant for `ϑ` (`IsInvariant`): it is fixed
by every tuple `b` with `b j` in the level `D.levelX j` of `X_j` and `b m = 1`. 

### `exists_lowerChainUpTo_poincareAt_eq`

 Fix an archimedean point `g` of `U(Y_0)` and a linear form `t`, and let `m = 2 ϱ + 2`. There is
a number `c₀` such that, for every tame character `ϑ` and every ramified source form `φ` on `X_0`,
the `m` lifts along `Y_0, …, Y_m` take the Poincaré series `D.poincareAt g t φ` to `c₀` times the
restriction to `Y_m` of the image of `φ` under the chain of lifts `X_0 → ⋯ → X_m` with twist `ϑ` and
tensor of finite data `seesawDatum ϑ`. 

### `exists_isAdmissibleCombination_seesawDatum`

 The tensor `φ_ξ = seesawDatum ϑ` of data for the upper chain is a combination of translated
vacuum data, with bounds. There is one number `C` as follows for every tame character `ϑ`. Let `ϑ.Q`
be its modulus, a finite set of finite places, and `q = ϑ.normQ` the product of their norms. Let
`m = 2 ϱ + 2` be the number of lifts and `B = D.residueMatrixCount = D.M ^ (D.f * D.n D.m ^ 2)`,
with `D.M` the principal level and `D.n D.m` the rank of `X_m`. An element `x` of `Translations` is
a tuple of finite adelic matrices, one for each lift, and `D.gluedVacuum x` is the tensor of the
integral vacuum data translated by `x`. Then `φ_ξ` is a finite sum `∑ r x • C • D.gluedVacuum x`,
with coefficients `r x`, over `x` in `admissibleTranslations q`. Each `B ^ (2 m) * r x` is integral
at the primes not dividing `q`. If `ϑ.Q = ∅`, then `∑ ‖σ (r x)‖ ≤ B ^ (2 ϱ + 2)` for every
automorphism `σ` of `ℂ`. 

### `seesaw_identity`

 **Seesaw identity**. Let `D` be admissible data, with field `E = D.E`, number of lifts
`m = D.m`, and hermitian spaces `X_j` (upper chain) and `Y_j` over `E`. Let `t` be a linear form on
the values of forms on `X_0` and `g` an archimedean point of `U(Y_0)`. Then there is a number
`c ≠ 0` such that every twist `ϑ` has a chain datum `Ψ` with
`lowerChain ϑ (𝒫 φ) = c • compositeLift ϑ Ψ φ` for all ramified source forms `φ` on `X_0`, where
`𝒫 = D.poincareAt g t` is the Poincaré map from forms on `X_0` to forms on `Y_0`. The datum
`Ψ` is a finitely supported function on `D.Translations`, the tuples of finite adelic matrices, one
for each lift of the upper chain; its glued tensor is the sum of `Ψ x` times the vacuum data
translated by `x`, and `compositeLift ϑ Ψ` is the upper chain from `X_0` to `X_m` with this tensor
as data, restricted to `Y_m`. That `Ψ` is a chain datum (`IsChainDatum`) means that its support is
admissible and supported at the level, its values are integral away from the modulus of `ϑ` and
bounded if this is empty, and its glued tensor is invariant under the levels of the `X_j`. 
