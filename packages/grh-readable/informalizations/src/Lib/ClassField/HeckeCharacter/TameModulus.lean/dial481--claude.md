---
{
  "module": "src/Lib/ClassField/HeckeCharacter/TameModulus.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/ClassField/HeckeCharacter/TameModulus.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/ClassField/HeckeCharacter/TameModulus.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Characters on determinants, local values and characters tame for a modulus

This file evaluates characters of U(1)(𝔸), the norm-one ideles of the CM field E, on determinants of
elements of K₀ = `New.stdLevel E n`. Here `New.stdLevel E n` is the stabiliser of the standard
lattice in the finite adelic unitary group `New.Gf E n`. A character of weight `e` and residue
characters `ψ` (`New.AutChar.HasWeight`) takes at `det k`, for `k` in K₀, the product of the `ψ w`
at the determinants of the reductions of `k`. Local values are read through `New.atPlaces P`, the
map to the components at the places of a finite set `P`, and through `New.Exchange.localChar P ξ k`,
the character `ξ |·| ^ (k / 2)` of the product of the completions at `P`. For a modulus 𝔪
(`New.Modulus`, an ideal of O_E prime to its conjugate), the reduction K₀ → GL_n(O_E/𝔪) is onto, and
a character tame for 𝔪 is given on determinants of K₀ by a character of O_E/𝔪.

## Main definitions and results

* `New.Exchange.SplitTameChar.character_detFin_eq_of_mem_stdLevel`,
  `New.Exchange.upsilonU1_detFin_eq_one_of_mem_stdLevel`: on determinants of `stdLevel E n`, a tame
  character is its local character at the ramified places, and `New.WeilData.upsilonU1` is trivial.
* `New.Rows.exists_reductionGL_eq`, `New.Rows.liftMod`: reduction `New.Modulus.reductionGL` :
  K₀ → GL_n(O_E/𝔪) is onto, with lifts supported at the places dividing 𝔪 and their conjugates.
* `New.Modulus.charOfTamePart`: the character of O_E/𝔪 with given components at the residue fields.
* `New.Exchange.IsTameFor`, `New.Exchange.IsTameFor.apply_det`: ν is tame for 𝔪 with character χ;
  then ν(det k) = χ(det(k mod 𝔪)) for k in K₀.

Notions from other files:
* `New.AutChar`: The group of continuous circle-valued characters of U(1)(𝔸), the norm-one adeles of
  the CM field E, trivial on elements coming from E.
* `New.Gf`: The finite adelic unitary group G_f: matrices g in GL_n(𝔸_f) with gᴴg = 1; K₀ = G_f ∩
  GL_n(Ô) is the stabiliser of the standard lattice.
* `New.G.det`: The determinant, from the adelic unitary group of signs s (pairs of an archimedean
  and a finite part) to the adeles x of E with x x̄ = 1.
* `New.Exchange.SplitTameChar.semilocalChar`: The character t ↦ ν(t/t̄) of ∏_{w∈S} E_w, t read as an
  idele supported on S, extended by 0 to non-invertible elements.

## Relation to the literature

Known; see `Lib.ClassField.Global.CMSplittingCharacters` for sources.


 ## Characters of given weight on determinants of integral unitary points 

### `apply_det_eq_prod`

 Let `μ` have weight `e` and tame part `ψ` (`μ.HasWeight e ψ`, with `ψ u` a character of the
residue field at `u`), and let `ψ` be trivial outside the distinct places `w i`. Then for `k` in the
stabiliser `K₀ = stdLevel E n` of the standard lattice, `μ (det k) = ∏ i, ψ (w i) (det (k mod w
i))`, where `detFin s k` is the determinant of `k` as a norm-one adele. 

### `apply_det_eq_one`

 A character `μ` with trivial tame part (`μ.HasWeight e 1`) is trivial on the determinant
`detFin s k` of every `k` in the stabiliser `stdLevel E n` of the standard lattice. 

### `apply_det_eq_one_of_supportedOn`

 Let `μ` have weight `e` and tame part `ψ`, trivial at the places of `A` and their conjugates.
Then `μ` is trivial on `det k` for every integral point `k` supported on `A` and its conjugate. 


## Values of the local characters at determinants

* `New.Exchange.spaceChar_rankTwist`: in even rank the two twists by the splitting character cancel.


### `upsilonU1_detFin_eq_one_of_mem_stdLevel`

 Given Weil data on E, `upsilonU1` is the restriction of its splitting character υ to the
norm-one ideles, a character of U(1)(𝔸) trivial on E, with trivial tame part. It is trivial on
`detFin s k`, the determinant of (1, k) in G, for every `k` in the stabiliser `stdLevel E n` of the
standard lattice Ô^n. 

### `spaceChar_rankTwist`

 In even rank `n`, multiplying `ν` by `upsilonU1 ^ (n / 2)`, taking the base change and dividing
by `υ ^ n`, for the splitting character `υ`, gives the base change `ν.baseChange`, the character
t ↦ ν(t/t̄) of the ideles of E: the two twists by the splitting character cancel. 

### `localChar_det`

 The local character `localChar P ξ k` at the determinant of the components of `g` at `P` is
`ξ t * |t| ^ (k / 2)`, for the idele `t = detOn P g.val` that is `det g` at `P` and `1`
elsewhere. 

### `SplitTameChar.exists_atPlaces_eq`

 Every invertible matrix over the product of the completions at the ramified places
`𝔠.ramifiedPlaces` is the family of components at `𝔠.ramifiedPlaces` of an element of the finite
adelic unitary group supported on `𝔠.ramifiedPlaces` and its conjugate
(`supportedOn n 𝔠.ramifiedPlaces`). 

### `SplitTameChar.character_detFin_eq_of_mem_stdLevel`

 On the determinant of an integral finite point `k`, the character `𝔠.character` of the tame
character `𝔠` of weight `μ`, ramified at the finite set `𝔠.ramifiedPlaces` of split places, is the
local character `𝔠.semilocalChar` at the determinant of the components of `k` at
`𝔠.ramifiedPlaces`. 

 ## Reduction of K₀ modulo 𝔪 and characters tame for a modulus 

 ### Reduction modulo 𝔪 

### `Rows.exists_reductionGL_eq`

 Let `𝔪` be a modulus of the CM field `E`, that is, a nonzero ideal of O_E that no prime divides
together with its conjugate. Then every `g` in GL_n(O_E/𝔪) is the reduction modulo `𝔪` of some `k`
in K₀ = `stdLevel E n`, the stabiliser of Ô^n in the finite adelic unitary group `Gf`. Moreover `k`
can be chosen supported on the places dividing `𝔪` and their conjugates, meaning its component is 1
at every other place. 

### `Rows.liftMod`

 A chosen lift of g ∈ GL_n(O_E/𝔪) to K₀, with component 1 outside the places dividing 𝔪 and their
conjugates. 

### `Modulus.levelOfSubgroup`

 The level cut out by a subgroup H of GL_n(O_E/𝔪): the elements of K_0 (`New.stdLevel`) whose
reduction modulo 𝔪 lies in H, as a subgroup of G_f. 

### `Modulus.principalLevel_le_levelOfSubgroup`

 If `a ∈ 𝔪`, the principal level of `a` (the elements of `K₀` congruent to `1` modulo `a`) lies
in the level `𝔪.levelOfSubgroup H` of every subgroup `H`. 

### `instance : IsLevel (𝔪.levelOfSubgroup H)`

 `𝔪.levelOfSubgroup H` is a level: it lies in `K₀` and is open. 

### `Modulus.stdLevelIndex_levelOfSubgroup`

 Let `𝔪` be a modulus of the CM field `E` and `H` a subgroup of `GL_n(O_E/𝔪)`. Let
`𝔪.levelOfSubgroup H` be the preimage of `H` under reduction mod `𝔪` inside `K₀ = stdLevel`, the
stabiliser G_f ∩ GL_n(Ô) of the standard lattice. Then the index of `𝔪.levelOfSubgroup H` in `K₀`
equals the index of `H` in `GL_n(O_E/𝔪)`. 

### `Modulus.mem_principalLevel_iff`

 If 𝔪 = (a), an element of K₀ has principal level a exactly when it reduces to 1 modulo 𝔪. 

 ### Tame characters 

### `Modulus.charOfTamePart`

 The multiplicative character x ↦ ∏_{w∣𝔪} ψ_w(x mod w) of O_E/𝔪, for characters ψ_w of the
residue fields. 

### `Exchange.IsTameFor`

 ν is tame for 𝔪 with weight e and character χ: 𝔪 ≠ (1), ν has weight e and a tame part (ψ_w)
that is nontrivial exactly at the primes w dividing 𝔪, and χ = ∏_{w∣𝔪} ψ_w on O_E/𝔪. 

### `AutChar.HasWeight.apply_det_eq_charOfTamePart`

 Let `ν` be a character of `[U(1)]`, that is, an `AutChar E`, a character of U(1)(𝔸) trivial on
elements coming from E, that has weight `e` and tame part `ψ` (`HasWeight`), where `ψ` is a family
of residue-field characters ψ_w that are trivial for every finite place w not dividing the modulus
`𝔪`. Then for `k` in K₀ = `stdLevel E n`, the value of `ν` at the norm-one adele `detFin s k` is
`𝔪.charOfTamePart ψ` at the determinant of `k` mod `𝔪`. Here `𝔪.charOfTamePart ψ` is the character
x ↦ ∏_{w∣𝔪} ψ_w(x mod w) of O_E/𝔪. 

### `inv`

 If ν is tame for 𝔪 with weight e and character χ, then ν⁻¹ is so with -e and χ⁻¹. 

### `mul`

 Multiplying by a character of weight d with trivial tame part keeps ν tame with the same χ. 

### `apply_det`

 If ν is tame for 𝔪 with character χ, then ν(det k) = χ(det(k mod 𝔪)) for k in K₀. 


## The tame character on unit ideles and the idele of the uniformisers

Two facts on ideles for a tame character 𝔠 (`New.Exchange.SplitTameChar`) ramified at a finite set S
of split places.


### `SplitTameChar.invOnUnits_mul_finPart_div_star_eq_one`

 For a finite idele `u` that is a unit at every place, `χ(u_S)⁻¹ · ν(u/ū) / χ(ū_S)⁻¹ = 1`.
Here `χ` is `New.Exchange.SplitTameChar.semilocalChar`, `u_S = evalPlaces 𝔠.ramifiedPlaces u`
denotes the components of `u` at `S`, and `invOnUnits χ x` is `(χ x)⁻¹` when `x` is a unit at every
place of `S`. 

### `exists_idele_star_eq_uniformizer`

 There is a finite idele `c` with component `1` outside `S̄` (the conjugates of
`S = 𝔠.ramifiedPlaces`), whose conjugate has at `S` the chosen uniformisers `ϖ` (the uniformiser
`SemilocalField.ϖ` of the product `LocProd S` of the completions at `S`), and whose inverse has
absolute value `finIdeleAbs c⁻¹ = ∏_{w∈S} q_w`, with `q_w` the order of the residue field at `w`. 
