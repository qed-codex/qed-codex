---
{
  "module": "src/Lib/ClassField/HeckeCharacter/SplitTameCharacters.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/ClassField/HeckeCharacter/SplitTameCharacters.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/ClassField/HeckeCharacter/SplitTameCharacters.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Splitting character on U(1), characters tamely ramified at split places, theta integrals

The subject is continuous characters of U(1)(𝔸), the norm-one adeles of a CM field E, with their
weights and tame parts (`New.AutChar.HasWeight`). Write x̄ for complex conjugation, w̄ for the place
conjugate to w, and υ for the splitting character of the Weil data (`New.WeilData`). The file first
computes the base change x ↦ μ(x / x̄) on local units. It then introduces characters tamely ramified
exactly at a set of split places, and defines the theta integral of a datum for an arbitrary pair
of characters.

## Main definitions and results

* `New.AutChar.HasWeight.baseChange_finPart_locIdele`: if μ has tame part ψ, w̄ ≠ w and ψ is trivial
  at w̄, the base change x ↦ μ(x / x̄) is given on local units at w by ψ_w.
* `New.AutChar.HasWeight.baseChange_finPart_locIdele_eq_one`: if w̄ = w and ψ_w is trivial, the
  base change is trivial on E_w^×.
* `New.WeilData.upsilonU1_hasWeight`, `New.WeilData.baseChange_upsilonU1`: on U(1), υ has weight 1
  and trivial tame part, and its base change is υ².
* `New.Exchange.SplitTameChar`: a character of positive weight, tamely ramified exactly on a
  nonempty set S of split places. `New.Exchange.SplitTameChar.semilocalChar` is its character at S.
* `New.Exchange.SplitTameChar.tameLocalChar`: the character at S is tame in the sense of
  `New.TameLocalChar`.
* `New.Exchange.thetaIntegral`: the integral over [U(T)] of the theta kernel of the dual pair
  (U(S), U(T)), for arbitrary characters a and b of U(1)(𝔸).

Notions from other files:
* `New.AutChar`: The group of continuous circle-valued characters of U(1)(𝔸), the norm-one adeles of
  the CM field E, trivial on elements coming from E.
* `New.divStar`: The map x ↦ x / x̄ from ideles to norm-one adeles.

## Relation to the literature

The results of this file are known; see `Lib.ClassField.Global.CMSplittingCharacters` and
`Lib.Weil.MixedModel.ZeroTerm` for sources.



## Base change at local units and the splitting character on U(1)

`New.locIdele` places any element of E_w^× at w in the ideles, with 1 at all other places.


 ### Base change at local units 

### `AutChar.HasWeight.exists_baseChange_finPart_locIdele`

 Let `μ` be an automorphic character of `U(1)(𝔸)` for the CM field `E`, of weight `e` with tame
part `ψ` (residue characters `ψ_w` with `μ u = ∏_v u_v^{e(v)} · ∏_w ψ_w(u mod w)` for `u` with
integral finite part), and suppose `ψ` is trivial at the conjugate place `w̄` (`star w`). Let
`x ∈ E_w^×` be viewed as an idele at `w`, with `x` a local unit if `w` is split (`w̄ ≠ w`). Then
`x/x̄` has integral finite part, and the finite part of the base change `y ↦ μ(y/ȳ)` evaluated at
the finite idele `x` equals `ψ_w` of the finite part of `x/x̄` reduced mod `w`. 

### `AutChar.HasWeight.baseChange_finPart_locIdele`

 Let μ have weight e and tame part ψ, and let w be a finite place with w̄ ≠ w and ψ_{w̄}
trivial. Then the base change y ↦ μ(y/ȳ), at a local unit x placed at w, equals ψ_w(x mod
w). 

### `AutChar.HasWeight.baseChange_finPart_locIdele_eq_one`

 Let μ be a continuous circle-valued character of U(1)(𝔸), the norm-one adeles of the CM field E,
trivial on elements of E. Suppose μ has weight e and tame part ψ, i.e. μ(u) = ∏_v u_v^{e(v)} · ∏_w
ψ_w(u mod w) when u has integral finite part. If w is a finite place with w̄ = w and ψ_w trivial,
then the base change y ↦ μ(y/ȳ) is trivial on E_w^×, viewed as finite ideles supported at w. 

 ### The splitting character on U(1) 

### `upsilonU1_hasWeight`

 The restriction to U(1)(𝔸) of the splitting character υ of the Weil data has weight 1 at
every infinite place and trivial tame part. 

### `hasWeight_upsilonU1_zpow`

 For every integer z, υ^z on U(1)(𝔸) has weight z at every infinite place and trivial tame
part. 

### `hasWeight_upsilonU1_pow`

 For every natural number n, υ^n on U(1)(𝔸) has weight n at every infinite place and trivial tame
part. 

### `_root_.New.AutChar.HasWeight.mul_upsilonU1_pow`

 If μ has weight e and tame part ψ, then μ·υ^n has weight n + e and tame part ψ. 

### `_root_.New.AutChar.HasWeight.hasWeight_rankTwist`

 If μ has weight e and tame part ψ, and n is a finite type with #n elements, then the character
μ·υ^⌊#n/2⌋ (`New.rankTwist μ n`) has weight e + ⌊#n/2⌋ at every infinite place and tame part ψ. 

### `baseChange_upsilonU1`

 The base change x ↦ υ(x/x̄) of the restriction of the splitting character υ to U(1)(𝔸)
equals the Hecke character υ². 


## Characters tamely ramified at split places, local data and theta integrals

The theta integral is defined for an arbitrary pair of characters of U(1)(𝔸). For a character
tamely ramified at split places, its character at the ramified places is shown to be tame.


### `SplitTameChar`

 A character ν (`character`) of [U(1)] of weight e, with e(v) > 0 for every v, and with tame part
ψ (`tamePart`) non-trivial exactly on a non-empty finite set S (`ramifiedPlaces`) of places disjoint
from its conjugate. 

### `SplitTameChar.character`

 The character of the norm-one adeles. 

### `SplitTameChar.tamePart`

 The tame part of `character`: a character of the residue field at each finite place. 

### `SplitTameChar.hasWeight`

 `character` has weight `e` and tame part `tamePart`. 

### `SplitTameChar.ramifiedPlaces`

 The set of ramified places. 

### `SplitTameChar.nonempty`

 At least one place is ramified. 

### `SplitTameChar.star_notMem`

 The conjugate of a place of `ramifiedPlaces` is not in `ramifiedPlaces`; in particular these
  places are split. 

### `SplitTameChar.ne_one_iff`

 The residue character `tamePart w` is non-trivial exactly when `w` is in `ramifiedPlaces`. 

### `SplitTameChar.weight_pos`

 Every component of the weight `e` is positive. 

 ### Reading the components at a set of places 

### `ReadsAt`

 π reads the components at A: A is disjoint from its conjugate, π is continuous with a
continuous additive section σ, σ(πx) being the A-part of x, and π(x) ∈ O iff x is integral
at A. 

### `ReadsAt.disjoint_star`

 No place of `A` has its conjugate in `A`. 

### `ReadsAt.mem_iff`

 `π x` lies in the subring `SemilocalField.O` exactly when `x` is integral at the places of
  `A`. 

### `ReadsAt.exists_section`

 `π` is continuous and has a continuous additive section `σ`, with `σ (π x)` the part of `x` at
  the places of `A`. 

### `localChar`

 The multiplicative character of ∏_{w∈P} E_w that is t ↦ ξ(t)|t|^{k/2} on invertible
elements, t read as an idele, and 0 on the others. 

### `ReadsAt.star`

 If `π` reads the components at `A`, then `π` composed with complex conjugation reads the
components at the conjugate places `star ⁻¹' A`. 

### `SplitTameChar.readsAt`

 The projection to the ramified places of `𝔠` reads the components there. 

### `residueAt`

 The ring map from the integers of ∏_{w∈P} E_w to the residue field at the place i of P. 

### `namedVector`

 The vector of 𝒮(Hom(S,T)) obtained from the vacuum by applying the operator
`New.Space.schrodingerOp`, for the places A, of the function y ↦ Ψ(π y) on finite adelic matrices,
π acting entrywise. The argument of type `ReadsAt A π` only records that `π` reads the components
at `A`. 

### `localDatum`

 The datum in 𝒮(Hom(S,T)) with real part v, the function Ψ of the components at the places A read
through π, and the vacuum elsewhere. 

### `thetaIntegral`

 The function g ↦ ∫ θ^{S,T}_{a,b}(f)(g,h) dh on U(S) = G E s, for f in 𝒮(Hom(S,T)). Here h runs
over U(T) = G E s', and dh is the measure `T.quotMeasure` on [U(T)]. It is the integral of the theta
kernel `New.pairTheta` over [U(T)], for arbitrary characters a and b of U(1)(𝔸). 

 ### Units at the places of P 

### `residueAt_eq_zero`

 The residue at `i` of an integral `u` is zero exactly when the component `u i` has valuation
below `1`. 

### `isIntegralUnit_iff_v_eq_one`

 An element of ∏_{w∈P} E_w is an integral unit exactly when each component has valuation 1. 

### `semilocalChar`

 The character t ↦ ν(t/t̄) of ∏_{w∈S} E_w, t read as an idele supported on S, extended by 0
to non-invertible elements. 

 ### The character at the ramified places through its residue characters 

### `localChar_apply_of_isUnit`

 On a unit u of the ring of integers at S, the character `New.Exchange.localChar` of the base
change of ν is, for every k, the product over S of the residue characters ψ_w at the residues of
u. 

### `character_apply_of_integral`

 On a norm-one adele u with integral finite part, ν(u) is the weight factor ∏_v u_v^{μ(v)} times
the character `New.Exchange.SplitTameChar.semilocalChar` at the components of u at S. 

### `tameLocalChar`

 The tameness data (`New.TameLocalChar`) of t ↦ ν(t/t̄)|t|^{k/2} on ∏_{w∈S} E_w: the product of
the residue fields at S, with the character ∏ψ_w⁻¹ on it. 
