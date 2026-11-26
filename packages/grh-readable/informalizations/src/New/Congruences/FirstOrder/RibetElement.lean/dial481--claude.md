---
{
  "module": "src/New/Congruences/FirstOrder/RibetElement.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Congruences/FirstOrder/RibetElement.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Congruences/FirstOrder/RibetElement.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Ribet's element for conjugate self-dual representations

This file chooses the coefficient ring: polynomials over the integers of `ℚ̄_ℓ`, and models of the
representations, are defined over every large coefficient ring. It bounds the valuation at the lift
and counts the cocycles of the main summand at the lift by its loss and its Selmer group. It then
constructs Ribet's element for a finite family of conjugate self-dual `ℓ`-adic representations of
the Galois group of `E`, some of which have the trace of a twisted main summand plus `t` powers of
the cyclotomic character.

## Main definitions and results

* `New.Selmer.exists_length_le_loss_add_crystallineSelmerLength`: with divisible coefficients, the
  cocycles of the main summand at the lift are counted by its loss, free of the level, and its
  Selmer group.
* `New.Selmer.ribet_columns`: Ribet's element and the bound on its coefficient of `∏ X j`.

Letters: the new places are `w j`, with tame generators `τ j`, Frobenius elements `φ j` and tied
relations `τ j - 1 - X j * (φ j - 1) * H j (φ j)`. The primes `p₀ = D.levelPrime 0`
and `p₁ = D.levelPrime 1` give the principal level; `g₀` is the element of the Galois group that
separates the characters.

Notions from other files:
* `New.CoeffRing`: rings of integers of finite Galois extensions of `ℚ_ℓ` inside `ℚ̄_ℓ`; their
  `normLength` is length over `O`, scaled so that `O/ℓ` has length 1.
* `New.Selmer.IsLiftSetting`: a descent pair `V` (`New.DescentPair`) has the places of the data and
  of the twist `ϑ`, an odd rank `card r ≤ D.r` and an odd difference of ranks `V.rankDiff ≤ D.t`.
  Its type polynomials `c i` are monic squarefree polynomials of degree `card r` over the residue
  fields at the chosen places above `p₀` and `p₁`, with conditions on their roots.
* `New.Lift.InClass F C U`: the local lattices `Y` such that `Bmax ⊗ Y` is spanned by the periods
  fixed both near `1` and along the filter `F`, the Hodge–Tate jumps lie in the sets `U`, and every
  polynomial `Q` with `C s Q` kills the inertial element `s` on the periods.
* `New.Selmer.IsPrimeTriangle`: a linearly ordered tame generator family `w j` with monotone
  exponents `ty j`. An even class of exponent `ty j` that kills the earlier `τ i`, and the earlier
  `φ i` of the same exponent, has its value at `τ j` killed by `ℓ ^ h`. Finitely many test points
  and `g₀` detect the cocycles unramified off `ℓ`, and `g₀` separates the characters up to `ℓ ^ h`.
* `New.Selmer.IsTameGeneratorFamily`: `w j` is not above `ℓ`, `τ j` is the chosen tame generator at
  a place over `w j`, and `φ j` fixes the `ℓ ^ ν`-th roots of unity.
* `New.Selmer.clearingBound` (in `New.Congruences.FirstOrder.TraceRelations`): the clearing bound
  `β_ℓ` per unit of rank of a main summand at `ℓ`.
* `New.Selmer.denominatorError` (in `New.Congruences.FirstOrder.TraceRelations`): the error term
  `e_ℓ`, with crude constants.

## Relation to the literature

Ribet's method in any rank, with congruent summands and tied primes, gives a Hecke element,
polynomial in the tie parameters, that kills all determinants det (1 - u g) modulo the ties. On
lifts it has no term properly dividing the product of all parameters, and the coefficient of that
product has bounded valuation; the orders of the even classes do not enter. Fitting-ideal forms of
Ribet's method are known for distinct summands in any rank and for congruent characters in rank 2.
Related work: Dasgupta–Kakde–Silliman–Wang, The residually indistinguishable case of Ribet's method
for GL2, 2023; Bellaïche–Chenevier, Families of Galois representations and Selmer groups, 2009;
Urban, Selmer groups and the Eisenstein–Klingen ideal, 2001.


### `eventually_exists_map_eq`

 A polynomial over the integers of `ℚ̄_ℓ` is defined over every large coefficient ring. 

### `eventually_exists_map_eq_and_eval_one`

 Finitely many polynomials over the integers of `ℚ̄_ℓ` with value `1` at `1` come from such
polynomials over every large coefficient ring. 

### `IsTameGeneratorFamily.dvd_eval_cyclotomicInv_sub_one`

 Let `τ j` be tame generators at the places `w j` with auxiliary elements `φ j` fixing the
`ℓ ^ ν`-th roots of unity (`IsTameGeneratorFamily ν w τ φ`), and let `H(1) = 1`. The elements `φ j`
and the inverses of their conjugates (`withConjInv φ k`) act on the character `O(-e)` by scalars
that are `1` modulo `ℓ ^ ν`. Hence the values of `H` at these scalars are also `1` modulo
`ℓ ^ ν`. 

### `ellVal_add_le_of_addVal_le`

 The valuation at the lift. Let `v` be the `ℓ`-adic valuation of `chosenGroupOrder` and put
`sep = halfGap h`. Let `t' ≤ D.t`, `h ≤ v`, `(k + nTest) sep ≤ halfGap ^ 22 h` and
`nDetect ≤ 2 (k + nTest)`; in the application `k` counts the new places, `nTest` the test points
together with `g₀`, and `nDetect` these elements together with two tame generators for each new
place. Let the valuation of `d` in `O` be at most the sum of the losses `lossT` of the main summand
and `lossχ e` of the `t'` characters, the Selmer length `selT`, the lengths `odd e` of the odd
classes, `t'` times the cost `tame` of the tame places, and `2 t' nDetect + k + 1` times the
valuation of `ℓ ^ sep`. Let each `odd e` be at most the valuation in `O` of the positive integer
`oddClassBound D`. After scaling by `normLength`, which gives `O/ℓ` length 1, let the losses add up
to at most `loc`, `selT ≤ sel` and `tame ≤ 2 ram + 8 D.f v`. Then `ellVal d + 2 v ≤ sel + 2 t'
ram + loc + denominatorError D ℓ`. 

### `eventually_exists_twistedLattice_and_block_lattices`

 Models over a large coefficient ring. Fix an isomorphism `ℂ ≃ ℚ̄_ℓ` (`PadicIso ℓ`); `intQpBar ℓ`
is the ring of integers of `ℚ̄_ℓ`. Let the `u x` be conjugate self-dual, and for `x ∈ 𝓧` let `u x`
have the trace of the twisted main summand `ψ (R x)` plus the characters `O(-e)`, `e < t`. Let each
`x ∈ 𝓧` have, over all large `O`, a model `R₀`, `ψ'`, `ζ'` with a property `Good x O R₀ ψ'`; here
`IsTwistedLattice` says that `R₀` is a lattice in `R x`, that `ψ'` and `ζ'` are `ψ` and `ζ x` with
values in `O`, and that the inertial element `γ x` acts on `ψ' R₀` by the scalar `ζ'`, with `ζ' - 1`
a unit. Then over every large `O` there are such models `R₀ x`, `ψ' x`, `ζ' x`, whose twisted
lattices span all matrices, and lattices `u' x` in all `u x` that are block diagonal for `x ∈ 𝓧`:
the twisted lattice, then the characters. 

### `IsLatticeIn.det_one_sub`

 The determinant `det (1 - R g)` can be computed on a lattice `R₀` in `R`, where `1 - R₀ g` is
the combination of the `R₀ g' - 1` with the single coefficient `-1` at `g`. 

### `exists_length_le_loss_add_crystallineSelmerLength`

 The losses at the lift, with divisible coefficients. Let the `w j` form a tame generator family:
`w j` is not above `ℓ`, `τ j` is the chosen tame generator at a place over `w j`, and `φ j` fixes
the `ℓ ^ ν`-th roots of unity. Over the coefficient ring `O`, let the classes
`InClass (F v) (C v) (U v)` of local lattices at the places `v` above `ℓ` contain the restrictions
of all `u x` and of the summands `summandRep T i`, which are `T` for `i = none` and `O(-e)` for
`i = some e`. Let the defects `dualDefect` of these summands have normalised sum at most
`card r * localDefectBound D ℓ`, an explicit bound (`eventually_exists_inClass_sum_dualDefect_le`).
Let the `u x` be continuous and unramified off `ℓ p₀ p₁`, `Q`, the places `w j` and their
conjugates, and `T` off `ℓ p₀ p₁`, `Q` and `Q̄`. Let `selT = crystallineSelmerLength T Q γ`, the
length of the Selmer group of `T` in `Frac(O) / O` of cocycles zero at `γ`, have normalised value at
most `sel < ∞`. Then the cocycles of `T` in `Frac(O) / O` that obey the relations among the
`u x g - 1` and vanish at the `τ j`, the inverses of their conjugates and `γ` have length at most a
number `b₀ = lossT + selT`, where the loss `lossT` (in the proof, the sum of the defects of `T`
above `ℓ`) and the colengths modulo `ℓ ^ ν` (`crystallineColength`) of the characters `O(-e)`,
`e < t`, have normalised sum at most `card r * localDefectBound D ℓ`. 

### `ribet_columns`

 Ribet's element for conjugate self-dual representations, with `t' = V.rankDiff`, the difference
`card n - card r` of the ranks of the descent pair `V`, and `r' = card r`. Let `V` with type
polynomials `c i` over the residue fields at its chosen places above `p₀`, `p₁` form a lift setting
for `ϑ` (`IsLiftSetting`), and let `ψ` be an auxiliary twist of modulus `Q` with ramification at
most `ram` (`IsAuxTwist`). Write `v = ellVal`, `N = D.chosenGroupOrder` and `halfGap = D.r ^ 8`. Let
the places `w j`, with tame generators `τ j`, elements `φ j` and exponents `0 < ty j < t'`, form a
triangle of primes for `g₀` (`IsPrimeTriangle`) up to `ℓ ^ (halfGap h)` with bound `halfGap ^ 22 h`,
where `h ≤ v(N)`. Let `u x`, `x : Y`, be finitely many conjugate self-dual representations with
Hodge–Tate jumps `J'` and level `Q`, the `w j` and their conjugates, on which inertia at the chosen
places acts through the roots of the rescaled polynomials `scaledTypePoly V c i` and `1`
(`IsRepOfType`), and inertia above `Q` and `Q̄` satisfies `(g - ψ g) (g - 1) = 0`. For `x ∈ 𝓧` let
`u x` have the trace of `ψ (R x)` plus the characters `O(-e)`, `e < t'`. Here `R x` is a main
summand, and `ψ (R x)` has a lattice on which `γ x` acts by the scalar `ζ x`. Let `S` be an algebra
of families, indexed by `Y`, of polynomials in variables `X j`, and let the `S`-module `𝒥` contain
`ℓ ^ ν` times the traces and the traces of the relations `τ j - 1 - X j (φ j - 1) H j (φ j)`
(`IsTraceIdeal`), with `H j (1) = 1`. At one `π ∈ 𝓧` let the Selmer group of `ψ (R π)` with
divisible coefficients have length at most `sel < ∞`. Then the determinants `det (1 - u x g)` lie in
`S` and vanish on `𝓧`, and there is one `f ∈ S`, the Ribet element, that multiplies each of them
into `𝒥`, has on `𝓧` no monomial properly dividing `∏ X j`, and whose coefficient `d` of `∏ X j` at
`π` satisfies `v(d) + 2 v(N) ≤ sel + 2 t' ram + r' loc + e_ℓ`, with the explicit bounds
`loc = localDefectBound D ℓ` and `e_ℓ = denominatorError D ℓ`. 
