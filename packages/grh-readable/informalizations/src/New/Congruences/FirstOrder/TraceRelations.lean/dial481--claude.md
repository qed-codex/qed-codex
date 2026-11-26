---
{
  "module": "src/New/Congruences/FirstOrder/TraceRelations.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Congruences/FirstOrder/TraceRelations.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Congruences/FirstOrder/TraceRelations.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Constants, trace relations, lattices and local defects for Ribet's method

This file fixes the constants of Ribet's method: the bound `New.Selmer.oddClassBound` for the odd
classes, the local defect bound, the error term `New.Selmer.denominatorError` and the clearing
bound `New.Selmer.clearingBound`. It checks the trace relations and chooses block diagonal lattices
for representations with the trace of a twisted main summand plus `t` powers of the cyclotomic
character. It adds up the crystalline colengths of the summands and bounds the local defects.
Here `New.ellVal` is the valuation on `ℚ̄_ℓ` with `ellVal ℓ = 1`, with negative values replaced
by 0, and `New.inertiaAbove S` is the union of the inertia groups above `S`. The primes
`p₀ = D.levelPrime 0` and `p₁ = D.levelPrime 1` give the principal level.

## Main definitions and results

* `New.Selmer.exists_blockDiagonal_lattice`: let the trace form be non-degenerate on the span of the
  image of `R'`, let `R'` have the trace of the twisted main summand `ψ R` plus the characters
  `O(-e)`, `e < t`, and let the twisted lattice `ψ' R₀` span all matrices over `O`. Then `R'` has a
  lattice that is block diagonal with summands `ψ' R₀` and the characters.
* `New.Selmer.crystallineColength_le_sum_dualDefect`: at each place `v` above `ℓ` let the lattices
  of all `u x` and of `ρ` lie in the class `InClass (F v) (C v) (U v)`. Then the crystalline members
  have colength, among Ribet's cocycles modulo `ℓ ^ M`, at most the sum over `v` of the defects
  `dualDefect`.

Notions from other files:
* `New.CoeffRing`: rings of integers of finite Galois extensions of `ℚ_ℓ` inside `ℚ̄_ℓ`; their
  `normLength` is length over `O`, scaled so that `O/ℓ` has length 1.
* `New.Selmer.tateTwist`: the rank-one representation `O(-e)`, given by the power `e` of the inverse
  `New.Selmer.cyclotomicInv` of the cyclotomic character.
* `New.Selmer.crystallineColength`: the length of the cocycles of a summand that obey the linear
  relations among the `u x g - 1`, modulo those that obey the crystalline relations above `ℓ`.
* `New.Selmer.IsLiftSetting`: a descent pair `V` (`New.DescentPair`) has the places of the data and
  of the twist `ϑ`, an odd rank `card r ≤ D.r` and an odd difference of ranks `V.rankDiff ≤ D.t`.
  Its type polynomials `c i` are monic squarefree polynomials of degree `card r` over the residue
  fields at the chosen places above `p₀` and `p₁`, with conditions on their roots.
* `New.Lift.InClass F C U`: the local lattices `Y` such that `Bmax ⊗ Y` is spanned by the periods
  fixed both near `1` and along the filter `F`, the Hodge–Tate jumps lie in the sets `U`, and every
  polynomial `Q` with `C s Q` kills the inertial element `s` on the periods.

## Relation to the literature

The torsion cocycles that Ribet's method produces in the summands of a lift's Galois representation
need not reduce from crystalline ones. Local duality and a case analysis on ℓ bound their total
distance from the crystalline condition, over all summands and places above ℓ, by an explicit bound.
It is known that torsion crystalline classes can miss reductions of crystalline ones by a bounded
defect that vanishes for small weights. Related work: Sweeting, Bloch–Kato conjecture for
four-dimensional symplectic representations, 2025; Chang–Diamond, Extensions of rank one
(φ,Γ)-modules, 2011; T. Liu, Torsion p-adic Galois representations and a conjecture of Fontaine,
2007.


### `oddClassBound`

 A positive integer, at most `2 ^ (4 (N + t + 3) ^ 27) h_E` for the conductor `N` and the class
number `h_E`, whose valuation in large coefficient rings bounds, for each `0 < e < t`, the length of
the odd classes (`shaOdd`) in `(O/ℓ^ν)(-e)`, and for `e = 0` the length of the unramified
homomorphisms. 

### `oddClassBound_le`

 The chosen bound for the odd classes is at most `2 ^ (4 (N + t + 3) ^ 27)` times the class
number of `E`, where `N` is the conductor of the cyclotomic field that contains `E`. 

### `eventually_length_shaOdd_le`

 For every sufficiently large coefficient ring `O`, the valuation of `oddClassBound D` bounds
the length of the odd classes `shaOdd` in `(O/ℓ^ν)(-e)`, for all `e < t` and all `ν`. 

### `localDefectBound`

 The number `loc_ℓ = 4 f defect_ℓ`: a bound, per unit of rank, for the local defect above `ℓ`.
Here `f = D.f` is the number of infinite places of `E`, and `defect_ℓ = defectBound D ℓ` is an
explicit number that depends only on `D` and `ℓ`. 

### `denominatorError`

 The error term `e_ℓ`, with crude constants. Its four terms pay for the class group and the odd
classes, the places above `p₀ p₁` (the principal level `D.M`), the idempotent and the automorphisms,
and the congruences between the characters `O(-e)`. Here `D.f` is the number of infinite places of
`E`, `D.halfGap = D.r ^ 8`, and `D.chosenGroupOrder` is the product of the orders of
`GL (D.r * D.t)` over the residue fields at the chosen places above `p₀` and `p₁`. 

### `denominatorError_eq_natCast`

 The error term `denominatorError D ℓ` is the cast of a natural number, a combination of the
`ℓ`-adic valuations of `oddClassBound D` and `D.chosenGroupOrder`. 

### `clearingBound`

 The clearing bound `β_ℓ = loc_ℓ + (1 + 2 t) e'_ℓ + e_ℓ + v_ℓ(N)` per unit of rank of a main
summand at `ℓ`, where `N = D.chosenGroupOrder`. Here `loc_ℓ = localDefectBound D ℓ` bounds the local
defect, `e'_ℓ = twistError ℓ D` is the number `(4 f + 3) r v_ℓ(N) + 2 ^ (-ℓ)` allowed for the Selmer
length and for the ramification of a twist, and `e_ℓ` is the error term `denominatorError`. 

### `add_denominatorError_le_mul_clearingBound`

 Let `1 ≤ r' ≤ D.r` and `t' ≤ D.t`. Let `sel` and `ram` be at most the allowance
`e'_ℓ = twistError ℓ D`. Then `sel + 2 t' ram + r' loc_ℓ + e_ℓ + v_ℓ(N) ≤ r' β_ℓ`. Here
`N = D.chosenGroupOrder` is a product of orders of general linear groups over residue fields,
`loc_ℓ = localDefectBound D ℓ` bounds the local defect above `ℓ` per unit of rank,
`e_ℓ = denominatorError D ℓ` is an error term, and `β_ℓ = clearingBound D ℓ` is by definition
`loc_ℓ + (1 + 2 D.t) e'_ℓ + e_ℓ + v_ℓ(N)`. 

### `mul_padicValNat_add_le_add_denominatorError`

 The cost of `t' ≤ D.t` characters, an inequality between numbers. Let `v` be the `ℓ`-adic
valuation of `D.chosenGroupOrder`, let `h ≤ v` and put `sep = D.halfGap * h`. Let
`(k + nTest) sep ≤ halfGap ^ 22 h` and `nDetect ≤ 2 (k + nTest)`. Let `tame ≤ 2 ram + 8 D.f v` (the
cost of the tame places, and the ramification of the twist). Each character costs the valuation of
`oddClassBound D`, `tame`, and `2 nDetect sep`; a further `(k + 1) sep` is paid once. With `2 v`
this is at most `2 t' ram` plus the error term `denominatorError D ℓ`. 

### `ribetCocycles.apply_eq_zero`

 Ribet's cocycles vanish on the kernel of `u`: a cocycle `z` that obeys the linear relations
among the `u x g - 1` vanishes at every `g` with `u x g = 1` for all `x`. 

### `ribetCocycles.mem_selmerModule`

 Let `z` be a cocycle for `ρ` modulo `b` that obeys the linear relations among the `u x g - 1`
(`ribetCocycles`), where the `u x` are continuous and trivial on the inertia groups outside
`S`. Then `z` is continuous and unramified outside `S`, so it lies in the Selmer module for `S`
and for every set `L` of relations that it obeys. 

### `isTraceIdeal_withConjInv`

 Let every `u x` be conjugate self-dual with twist `t`. Let `w j` be new places with tame
generators `τ j` and elements `φ j` that fix the `ℓ ^ ν`-th roots of unity. Let `𝒥` be a trace
ideal. Then `𝒥` is also a trace ideal for the doubled families `withConjInv τ`, `withConjInv φ`,
which add the inverses of the conjugates; both copies of `j` use the variable `X j`. 

### `restrictToCoeffRing`

 A subalgebra over the integers of `ℚ̄_ℓ`, read as a subalgebra over a coefficient ring. 

### `IsTraceIdeal.of_isLatticeIn`

 Let `w j` be new places: `w j` is not above `ℓ`, `τ j` is a tame generator at `w j`, and `φ j`
fixes the `ℓ ^ ν`-th roots of unity. Let `u' x` be lattices over `O` in the conjugate self-dual
`u x`. Let the `S`-module `𝒥` be a trace ideal (`IsTraceIdeal`) for the `u x` over the integers of
`ℚ̄_ℓ`: it contains `ℓ ^ ν` times the traces and the traces of the relations that tie `τ j` to `φ j`
through `X j` and `H j`, and `S` contains the `X j` and the coefficients of the characteristic
polynomials. Let the polynomials `H' j` over `O` be equal to the `H j`. Then `𝒥` is a trace ideal
for the `u' x` over `O` and the doubled families `withConjInv τ`, `withConjInv φ`, which add the
inverses of the conjugates; both copies of `j` use `X j` and `H' j`. 

### `summandRep_some_apply`

 The summand `e` of `summandRep T`, the family of a main summand `T` and `t` characters, is the
`1 × 1` matrix of the power `e` of the inverse cyclotomic character `cyclotomicInv`. 

### `summandCoordIndexEquiv`

 The index set of a main summand and `t` characters, as a sum and as a family of summands. 

### `blockDiagonal'_summandRep`

 The block diagonal sum of a main summand `T` and the `t` characters `cyclotomicInv ^ e` is the
matrix with `T g` and a diagonal matrix on the diagonal, reindexed by `summandCoordIndexEquiv`. 

### `exists_blockDiagonal_lattice`

 Let the trace form be non-degenerate on the span of the image of `R'` (`IsTraceNondeg`). Let
`R'` have the trace of the twisted main summand `ψ R` plus the characters `O(-e)`, `e < t`, and let
the twisted lattice `ψ' R₀` span all matrices over `O`. Then `R'` has a lattice that is block
diagonal with summands `ψ' R₀` and the characters (`summandRep`), the summands being placed by
`ϵ`. 

### `exists_blockDiagonal_lattices`

 Let the representations `u x`, indexed by the type `Y`, have non-degenerate trace form
(`IsTraceNondeg`) and have lattices over `O`, and for `x ∈ 𝓧` let the trace of `u x` be that of the
twisted main summand `ψ (R x)` plus the characters `O(-e)`, `e < t`, where the twisted lattice
`ψ' x R₀ x` spans all matrices. Then there are lattices in all these representations that, for
`x ∈ 𝓧`, are block diagonal with the twisted lattice of the main summand and the characters. 

### `IsTwistedLattice.twistRep_apply_eq_of_eq_one`

 Let `R₀`, `ψ'`, `ζ'` be a model over `O` (`IsTwistedLattice`): `R₀` is a lattice in `R`, `ψ'`
and `ζ'` are `ψ` and `ζ` with values in `O`, and `γ` acts on the twisted lattice `ψ' R₀` by the
scalar `ζ'`. Then `ψ' R₀` agrees with `R₀` at every `g` with `ψ g = 1`. 

### `IsTwistedLattice.twistRep_eq_one_of_mem_inertiaAbove`

 Let `R₀`, `ψ'`, `ζ'` be a model over `O` (`IsTwistedLattice`): `R₀` is a lattice in `R`, `ψ'`
and `ζ'` are `ψ` and `ζ` with values in `O`, and the inertial element `γ` acts on the twisted
lattice `ψ' R₀` by the scalar `ζ'`. Let `ψ` come from the norm-one torus with modulus `Q`
(`IsFromU1`). Let `R` be a main summand (`IsMainSummandLike`): a conjugate self-dual representation
of twist `t` and empty level, with Hodge–Tate jumps `J` read through the isomorphism `ℂ ≃ ℚ̄_ℓ`
fixed by `PadicIso ℓ`; only that `R` is unramified outside `ℓ p₀ p₁` (`p₀ p₁ = D.M`) is used. Then
`ψ' R₀` is unramified outside `ℓ p₀ p₁`, `Q` and `Q̄`. 

### `length_ribetCocyclesVanishingOn_le`

 Let the `τ j` be tame generators at places `w j` off `ℓ`. Let `u x`, `x : Y`, be finitely many
continuous representations over `O`, unramified outside `ℓ p₀ p₁` (`p₀ p₁ = D.M`), `Q`, the `w j`
and their conjugates, and let `T` be unramified outside `ℓ p₀ p₁`, `Q` and `Q̄`. Consider the
cocycles in `T` modulo `ℓ ^ m` that obey the linear relations among the `u x g - 1`. Those that
vanish at `γ`, at the `τ j` and at the inverses of their conjugates have length at most
`crystallineColength T u m`, the length of all of them modulo those obeying the crystalline
relations above `ℓ`, plus the length of the Selmer cocycles `selmerCocycles T Q m γ`. 

### `hasTriangleCost_of_isCharacterCocycle`

 Let the places `w j` off `ℓ`, with tame generators `τ j`, elements `φ j` and monotone exponents
`0 < ty j < t`, form a triangle of primes for `g₀` up to `ℓ ^ sep`; `c` bounds `sep` times the
number of places and test points. Let the `u x` be continuous and unramified outside `ℓ p₀ p₁`
(`p₀ p₁ = D.M`), `Q`, the `w j` and their conjugates, and let `e < t`. Let `Z` consist of character
cocycles: cocycles in `O/ℓ^ν(-e)` that obey the relations among the `u x g - 1`, vanish at tame
generators `δ` of places `q` covering the remaining places prime to `ℓ` and at the inverses of their
conjugates, and, if they vanish at `γ`, have their value at `g₀` killed by every `χ g - 1`,
`χ = cyclotomicInv ^ e`. Here `γ` lies in inertia at a place not above `ℓ`. Then `HasTriangleCost`
holds along the `j` with `ty j = e`: for the members `Z₀` of `Z` that vanish on some set, agreement
at the earlier `τ i`, `φ i` and the inverses of their conjugates gives agreement at `τ j` up to
`ℓ ^ sep`, and the length of `Z / Z₀`, plus the length modulo `ℓ ^ sep`-torsion of any submodule of
`Z₀` that vanishes at the tame generators and agrees at the `φ j`, is at most the colength
`crystallineColength` of the crystalline members among Ribet's cocycles plus the length of `shaOdd`,
the cocycles unramified off `ℓ` that change sign under `conjGal`. Moreover a member of `Z` is zero
if it vanishes at the `τ j`, the inverses of their conjugates and on a set `s` that detects the
cocycles unramified outside `ℓ` (`IsDetectedBy`). 

### `isTameType_of_mem_placesAboveM`

 Let `V` be a descent pair of ranks `card r < card n`, with type polynomials `c i` over the
residue fields at its chosen places above `p₀` and `p₁`, forming a lift setting for the twist `ϑ`.
Let `t ≤ D.t`, and let `v` be a place above `ℓ` and above `D.levelPrime 0` or `D.levelPrime 1`. Then
`ℓ = D.levelPrime k` for some `k`. Fix any jumps `J`, any level `S` and an element `s` of inertia at
`v` (`IsWeilPair (toGp s) 0`). Consider the conjugate self-dual representations (`IsRepOfType`) with
these jumps and level on which inertia at the chosen places acts through the roots of
`scaledTypePoly V c i * (X - 1) ^ t`, where `scaledTypePoly` rescales the roots of `c i` by the
character of `V`. Let `O ⊆ ℚ̄_ℓ` be a coefficient ring (`CoeffRing ℓ`). The polynomials over `O`
whose images over `ℚ̄_ℓ` kill `s` on all these representations (`IsKilledBy`) satisfy `IsTameType`:
they include `X ^ e - 1`, with `e` the least common multiple of the `ℓ ^ i - 1` for `1 ≤ i ≤ D.r`,
and a monic polynomial over `ℤ_[ℓ]` of degree at most `(D.r + D.t) * D.r`. 

### `crystallineColength_le_sum_dualDefect`

 Ribet's cocycles above `ℓ`. At each place `v` above `ℓ`, let the restrictions of all `u x` and
of `ρ` lie in the class `InClass (F v) (C v) (U v)` of local lattices. This means three things.
Their periods are admissible along the filter `F v`. Their Hodge–Tate jumps lie in the sets `U v`.
Each inertial `s` is killed by every polynomial `Q` with `C v s Q`. Take the cocycles of `ρ` modulo
`ℓ ^ M` that obey the linear relations among the `u x g - 1`. Those that also obey the crystalline
relations above `ℓ` have colength at most the sum over `v` of the `dualDefect`. This defect is the
length of the crystalline cocycles of the Tate dual of `ρ`, modulo those orthogonal under cup
product to the class. 

### `hasJumps_localLattice_summandRep`

 Let `R` be a main summand (`IsMainSummandLike`), in particular conjugate self-dual with
Hodge–Tate jumps `J`, and let `T` agree on the decomposition group at `v` with a lattice `T₀` in
`R`. An element `g` of the absolute Galois group `Gp ℓ` of `ℚ_ℓ` gives an embedding
`coefficientEmbedding O g` of `O` and, through the chart `localChart` at `v`, a complex embedding
`σ` of `E`. At this embedding of `O` the summand `T` has the jumps `J σ`, and `O(-e)` has the single
jump `e`. 

### `sum_index_mul_defectBound_le`

 At each place `v` above `ℓ`, a summand costs the local degree (the index of the decomposition
group in the absolute Galois group of `ℚ_ℓ`) times its rank times the explicit number
`defectBound D ℓ`, divided by `D.t` for a character. For a main summand of rank `r' = card r ≥ 1`
and `t ≤ D.t` characters the total is at most `r' · localDefectBound D ℓ`. 

### `eventually_exists_inClass_sum_dualDefect_le`

 Let the descent pair `V`, with type polynomials `c i` at its chosen places, be a lift setting
for the twist `ϑ` (`IsLiftSetting`). Let `R` be a main summand of rank `r' = card r`, and let the
`ρ x` be representations of rank `card n` on which inertia at the chosen places acts through the
roots of `scaledTypePoly V c i * (X - 1) ^ t` (`IsRepOfType`). Over every sufficiently large
coefficient ring `O`, let the `u x` be lattices in the `ρ x`, and for one index `π` let `u π` be
block diagonal with summands `T` and the characters `O(-e)`, `e < t`, placed by `ϵ`, where `T`
agrees above `ℓ` with a lattice `T₀` in `R`. Then at each place `v` above `ℓ` there is a class
`InClass (F v) (C v) (U v)` of local lattices that contains the restrictions of all `u x` and of the
summands of `u π`. The defect `dualDefect` of a summand at `v` is the length of the crystalline
cocycles of its Tate dual modulo those orthogonal to the class; the defects of the `t + 1` summands
at all places above `ℓ`, scaled so that `O/ℓ` has length 1 (`normLength`), add up to at most
`r' · localDefectBound D ℓ`. 

### `pow_chosenGroupOrder_eq_one_of_mem_inertiaAbove`

 Let the descent pair `V` with type polynomials `c i` be a lift setting for `ϑ`, and let `R` be a
representation of a type on which inertia at the chosen places acts through the roots of the scaled
type polynomials times `(X - 1) ^ t`. Then each element `g` of inertia at a place above `p₀ p₁` and
prime to `ℓ` acts on `R` with order dividing `D.chosenGroupOrder`. 

### `exists_tame_relations`

 Let `V` with type polynomials `c i` form a lift setting (`IsLiftSetting`), and let `ψ` be an
auxiliary twist (`IsAuxTwist`): it comes from the norm-one torus with modulus `Q`, the places of `Q`
avoid the places `badPlaces D ℓ` that divide `ℓ p₀ p₁` or the level `D.N`, and the valuations of
`ψ - 1` at tame generators over `Q` add up to at most `ram`. Let the `u x` be representations of a
type with the scaled type polynomials, on which inertia above `Q` and `Q̄` satisfies
`(g - ψ g) (g - 1) = 0`, and let `u' x` and `ψ'` be models over `O`. Then there are finitely many
places `q j` prime to `ℓ`, covering `Q` and the places above `p₀ p₁` prime to `ℓ` up to conjugation,
with tame generators `δ j`. For each `δ` among the `δ j` and the inverses of their conjugates
(`withConjInv δ`) there is a polynomial `o` such that `o(δ) (δ - 1)` vanishes on every `u' x`, and
the valuations of the `o(1)` add up to at most `2 ram + 8 f v_ℓ(N)`, where `f = D.f` is the number
of infinite places of `E` and `N = D.chosenGroupOrder`. 
