---
{
  "module": "src/Lib/Shimura/CongruenceRelation/KernelReduction.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Shimura/CongruenceRelation/KernelReduction.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Shimura/CongruenceRelation/KernelReduction.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Reduction of isogeny kernels: Cartier density, the tangent line and torsion sections

The file studies how kernels of isogenies of abelian schemes in a family `X : New.ThetaFamily D Z τ`
reduce from a valuation subring of `ℂ` to a field. The file records what goodness of the PEL data
gives at the kernel of a map to a field. It also finds the line of tangent vectors on which `𝓞 E`
acts through `x.baseHom`. From this line it gets a function that detects tangent vectors, and from
that function a parameter `t` whose powers are local equations for the torsion sections.

## Main definitions and results

* `New.Variety.cartier`: a function on a finite flat subgroup scheme (or coset) of a commutative
  group scheme that vanishes at all `K`-points is zero, for `K` an algebraically closed field of
  characteristic zero containing the base ring.
* `New.Variety.ker_factors_of_points`: over a valuation ring with fraction field `ℂ`, a closed
  condition that holds for the torsion complex points of the kernel of a finite flat homomorphism
  holds for all points of the kernel.
* `New.Variety.placeTorsion`: the points of `x.groupScheme` with values in a `k`-algebra `C` that
  are killed by the kernel of `x.baseHom`.
* `New.Variety.ker_factors_of_torsionPoint`: the torsion sections are dense in the kernel of an
  isogeny.
* `New.Variety.exists_isLieLine`: the line of tangent vectors on which `𝓞 E` acts through
  `x.baseHom`.
* `New.Variety.exists_isLocalEquation_pow_sectionCount`: at a local point `z` of the special fibre
  killed by a power of `β - b`, the power `t ^ N` of a parameter `t` is a local equation for a
  family of torsion sections, `N` of which pass through the closed point of `z`.
* `New.Variety.exists_param_pow_card_eq_zero`: the resulting parameter at a point killed by
  `ker x.baseHom`, and a nonzero torsion section that reduces to zero.

Notions from other files:
* `New.ThetaObject`: An object of the family X over a scheme T: a morphism x from T to the base of
  X; `x.groupScheme` is the pull-back of the abelian scheme along it.
* `New.ThetaObject.baseHom`: For an object x over Spec R, the ring homomorphism O_E → R induced by x
  and the structure morphism of the base of the family to Spec O_E.
* `New.AddObj`: A commutative group object.
* `New.specOver`: The spectrum of an R-algebra B, as a scheme over Spec R.
* `New.ValuativeArc`: A valuation ring O with fraction field ℂ, with its generic point Spec ℂ → Spec
  O.

## Relation to the literature

Known; see `Lib.Shimura.AbelianScheme.IsogenyFlatness`,
`Lib.Shimura.CongruenceRelation.HeckeNeighbours`, `Lib.Shimura.Deformation.TangentBound` and
`Lib.Shimura.ThetaModuli.UniversalFamily` for sources.



## Cartier's theorem on density of characteristic zero points

Over a subring `V` of an algebraically closed field `K` of characteristic `0`, the `K`-points of a
finite flat subgroup scheme of a fixed commutative group scheme are schematically dense in it.


### `point_snd_eq_zero_of_section`

 In characteristic `0`, a derivation of a finite `K`-algebra (given as a section `ρ` of
`R[ε] → R`) takes values in the kernel of every `K`-point `c`. 

### `cartier`

 **Cartier's theorem.** Let `V` embed in an algebraically closed field `K` of characteristic
`0`, let `S` be a finite flat `V`-algebra and `ι : Spec S ⟶ A` a monomorphism to a commutative
group scheme whose points are stable under `(x, y, z) ↦ x - y + z` (a subgroup or a coset).
Then every nonzero `s : S` is nonzero at some `V`-algebra map `S → K`. 

### `ker_factors_of_points`

 Let `V` be a valuation ring with fraction field `ℂ` (a `ValuativeArc`) and `ψ : A ⟶ B` a finite
flat homomorphism of commutative group schemes over `V`, with `B` separated. Let `r : A.left ⟶ Y`
be a morphism of schemes and `j : Z ⟶ Y` a closed immersion. If `r` maps every torsion `ℂ`-point of
the kernel of `ψ` into `Z`, then it maps every point `z : T ⟶ A` of the kernel into `Z`. 


## Goodness of the PEL data at the kernel of a map to a field

`New.Variety.ringChar_prime_and_exists_isCoprime_of_isGoodAt_ker` states what `New.PEL.IsGoodAt`
gives when the ideal is the kernel of a map `ρ` from `𝓞 E` to a field, in the form used by the
deformation arguments. `D.β` is an element with `star D.β = 1 - D.β`, and `D.level` is the level of
the PEL data `D`.


### `New.Variety.ringChar_prime_and_exists_isCoprime_of_isGoodAt_ker`

 Let `D` be PEL data over the CM field `E` with distinguished element `D.β` and level `D.level`,
and let `ρ : 𝓞 E → k` be a map to a field whose kernel `𝔭` is good for `D` in the sense of
`PEL.IsGoodAt`. Then (a) the characteristic `p` of `k` is a prime; (b) `𝔭 ≠ 0`, and there are
`c ≠ 0` in `𝔭` and `t ≡ 1` modulo `𝔭` with `t 𝔭 ⊆ (c)`; (c) for some integer `b`, `β - b` lies in
`𝔭`, the elements `β - b` and `star β - b` are coprime, and the ideal `(D.level)` together with
`𝔭 · (p, star β - b)` generates the unit ideal. 


## Torsion sections, the tangent line and local equations

This section studies how kernels of isogenies of the abelian schemes of a family
`X : New.ThetaFamily D Z τ` reduce. In the statements about torsion sections, `y` is an object over
a valuation subring `V` of `ℂ` with a full structure `e : y.FullLevelStructure`, which gives
sections `e.torsionPoint s` of `y.groupScheme` over `V`. These are injective and `𝓞 E`-linear in
`s : AdelicTorsion E D.Index`, and over `ℂ` every torsion point is one of them. In the statements
about reduction, the object `x` over the field `k` is the pull-back of `y` along `φ : V →+* k`, and
`w` in the docstrings, except that of `torsionReduction_eq_iff`, stands for the ideal
`ker x.baseHom` of `𝓞 E`. The lemmas on tangent vectors allow a local base ring `R` with a map to
`k`.

The idea: the tangent vectors at a point of the kernel of an element `d` of `𝓞 E` that is coprime to
`star β - b` and zero in `k` lie on one line, so a single function detects them. For
`d = (β - b) ^ (M + 1)` this function gives a local equation for the torsion sections through the
point.


### `placeTorsion`

 For an object `x` over a field `k` and a `k`-algebra `C`, the `𝓞 E`-module of `C`-points of
`x.groupScheme` killed by the kernel of `x.baseHom`. 

### `placeTorsionMap`

 The map from `placeTorsion x C` to `placeTorsion x C'` induced by a homomorphism `G : C → C'` of
`k`-algebras: a point `Spec C ⟶ x.groupScheme` is composed with `Spec G : Spec C' ⟶ Spec C`. 

### `ker_factors_of_torsionPoint`

 The torsion sections `e.torsionPoint s` of the object `y` over the valuation subring `V` of `ℂ`
(with full structure `e`) are dense in the kernel of an isogeny `ψ`: if `r` maps each of them that
lies in the kernel into the closed subscheme `j : W ⟶ Y.left`, then it maps every point `z` of the
kernel into it. 

### `IsLieLine`

 Let `x` be an object over `R` and `k` an `R`-algebra. A tangent vector at `0` is a point of
`x.groupScheme` over `k[ε]` that reduces to `0` over `k`. The map `L` is a line of tangent vectors
on which `𝓞 E` acts through `ρ`, and into which `star β - b` maps all tangent vectors. Here `β` is
`D.β` and `b` is an integer; in `exists_isLieLine`, `ρ` is `x.baseHom` followed by `R → k`, with
`ρ (D.β - b) = 0`. 

### `IsLieLine.apply_one_ne_zero`

 The generator `L 1` is not zero. 

### `IsLieLine.fstHom_comp`

 Each `L m` is a tangent vector at `0`. 

### `IsLieLine.smul_apply`

 The ring `𝓞 E` acts on the line through `ρ`. 

### `IsLieLine.scale_comp`

 The substitution `ε ↦ m ε` takes `L 1` to `L m`. 

### `IsLieLine.exists_smul_eq`

 The element `star β - b` maps every tangent vector at `0` into the line. 

### `exists_isLieLine`

 Let `x` be a theta object of the family `X` over a local ring `R`, that is, a point of the base
of `X`. Its group scheme `x.groupScheme` is the pulled-back abelian scheme with its `𝓞 E`-action,
and `k` is an `R`-algebra that is a field. Let `ρ : 𝓞 E → k` be the composite of `x.baseHom` with
`R → k`, and let `b` be an integer with `ρ (D.β - b) = 0`, where `D.β` is the element `β` of the PEL
datum `D`. Then there is an additive map `L` from `k` to the tangent vectors at `0` of
`x.groupScheme` over `k` (points over `k[ε]` reducing to `0`) that is a line on which `𝓞 E` acts
through `ρ` and into which `star β - b` maps all tangent vectors. 

### `IsLieLine.exists_detects_tangent`

 Let `x` be a theta object over a ring `R`, let `k` be an `R`-algebra that is a field, and let
`ρ : 𝓞 E → k` and an integer `b` be such that `L` is a line of tangent vectors at `0` of
`x.groupScheme` over `k` on which `𝓞 E` acts through `ρ` and into which `star D.β - b` maps all
tangent vectors. Let `d` in `𝓞 E` satisfy `ρ d = 0` and be coprime to `star D.β - b`, and let
`ι : Spec S ⟶ x.groupScheme` be the kernel of `d`: a monomorphism over `Spec R` that is killed by
`d` and through which every point killed by `d` factors. Then at each `k`-point `o` of `Spec S`
there is a function `T` in `S` such that every tangent vector at `o` (a `k[ε]`-point reducing to
`o`) along which `T` has zero derivative is itself zero. 

### `exists_detecting_tangent_vectors`

 Let `y` be an object over a local ring `R`, and let `ρ : 𝓞 E → k` be `y.baseHom` followed by
`R → k`. Let `ρ` send `β` to the integer `b`, with `β - b` coprime to `star β - b`. Let
`ι : Spec S → y.groupScheme` be the kernel of `(β - b) ^ (M + 1)`: a closed immersion killed by it,
through which every point that it kills factors. Let `o` be a `k`-point of `Spec S`. Some function
`T` on `Spec S` has nonzero derivative along every nonzero tangent vector at `o`. 

### `VanishesAlong`

 A point `p` of a group scheme `A` over `R`, with values in a ring `B`, vanishes along the ring
map `G : B →+* B'`: the point of `A` with values in `B'` induced by `G` is zero. 

### `vanishesAlong_iff`

 Vanishing along `G` may be tested on any morphism `a` over `R` given by `G`. 

### `sectionCount`

 For a full structure `e` on the object `y` over `V`, a family `c` of torsion vectors and a
point `p` of `y.groupScheme`, the number of indices `i` for which the torsion section
`e.torsionPoint (c i)` passes through `p`. 

### `IsLocalEquation`

 Let `e` be a full structure on the object `y` over `V` and `z` a point of `y.groupScheme` with
values in a ring `B`. The element `f` of `B` is a local equation at `z` for the closure of the
torsion sections `e.torsionPoint (c i)`, as seen by isogenies `ψ` out of `y.groupScheme` and ring
maps `G` out of `B`. 

### `IsLocalEquation.map_eq_zero`

 If `υ` maps `u` to `z` and the torsion of `ker ψ` into the family `c`, and `ψ u` vanishes
  along `G`, then `G f = 0`. 

### `IsLocalEquation.vanishesAlong`

 If `ψ` kills the sections `e.torsionPoint (c i)` and `G f = 0`, then `ψ z` vanishes along
  `G`. 

### `pow_card_dvd_of_sections`

 Let `O` be a domain and `θ j` distinct sections of a finite type `O`-algebra `S` through a point
`o`, and let `T` have nonzero derivative along every nonzero tangent vector at `o`. Let `χ` send the
elements not vanishing at `o` to units, and let `g` divide each `χ (θ j T - T)`. If `a` vanishes
along the `θ j`, `j ∈ s`, then `g ^ #s` divides `χ a`. 

### `exists_dvd_pow_card_of_sections`

 Let `θ j` be finitely many sections of an `O`-algebra `S`, `o` a `k`-point of `S` and `T` an
element of `S`. Let `χ` send the elements not vanishing at `o` to units, and let `χ (θ j T - T)`
divide `g` for each `θ j` through `o`. Some `F` vanishes along all `θ j`, and `χ F` divides
`g ^ N`, where `N` is the number of sections through `o`. 

### `map_eq_zero_of_vanishesAlong_of_sections`

 Density of the torsion sections, read on functions on `Spec S`. Let each section
`e.torsionPoint (κ i)` factor through the closed immersion `ι : Spec S ⟶ y.groupScheme` as the point
`θ i`, and let `υ` carry each torsion vector whose section the isogeny `ψ` kills into `κ`. If
`υ • u` is the point `z'` given by `γ : S → B`, `ψ u` vanishes along `G`, and `F` vanishes at every
`θ i`, then `G (γ F) = 0`. 

### `exists_spec_map_comp_eq_torsionPoint_of_smul_eq_zero`

 A torsion section of `y.groupScheme` that `d` kills factors through any
`ι : Spec S → y.groupScheme` through which every point killed by `d` factors: it is given by a
`V`-point `θ` of `Spec S`. 

### `vanishesAlong_of_map_pow_card_eq_zero`

 Let the sections `e.torsionPoint (κ i)` factor through the closed immersion `ι` as distinct
points `θ i` of `Spec S`, `S` finite over `V`, let `T` have nonzero derivative along each nonzero
tangent vector at the `k`-point `o`, and let `γ : S → B` give `z'`, invert the elements nonzero at
`o` and send `θ i T - T` to `t` for each `θ i` through `o`. If `ψ` kills each `e.torsionPoint (κ i)`
and `G` kills `t ^ N`, `N` the number of `θ i` through `o`, then `ψ (ι z')` vanishes along `G`. 

### `exists_isLocalEquation_pow_sectionCount`

 A local equation for the closure of torsion sections. Let `x` over `k` be the pull-back of `y`
(`ho`), let `β - b ∈ w = ker x.baseHom` be coprime to `star β - b`, and let `z` be a point of
`y.groupScheme` killed by `(β - b) ^ M` over a local `k`-algebra `B` with `k`-point `π`. Some
`t ∈ ker π` makes `t ^ N` a local equation at `z` for the sections of any injective family `c` of
`w`-torsion vectors, `N` the number of them through the closed point of `z`. 

### `torsionReduction`

 Reduction of torsion sections. Let `x` over `k` be the pull-back of `y` over `V` along `φ`
(`ho`), and let `e` be a full structure on `y`. A `w`-torsion vector `s`, for `w = ker x.baseHom`,
goes to the `w`-torsion `k`-point of `x` that corresponds to the section `e.torsionPoint s`. 

### `torsionReduction_eq_iff`

 The reduction of the torsion vector `s` is the point `w` exactly when the section
`e.torsionPoint s` is, read over `k` via `φ`, the point of `y.groupScheme` that
`ho.isGroupBaseChange.pointEquiv` matches with the `k`-point `w` of `x.groupScheme`. 

### `smul_mem_torsionBySet_of_comp_smul_eq_zero`

 Let `c` and `t` be elements of `𝓞 E` with `t w ⊆ (c)`, for `w = ker x.baseHom`. If the full
structure `e` sends the torsion vector `s` to a section that `c` kills, then `t • s` is
`w`-torsion. 

### `exists_param_pow_card_eq_zero`

 Let `x` over `k` be the reduction of `y` (`ho`) and `w = ker x.baseHom` good for `D` (`hw`).
Some nonzero `w`-torsion vector `s` has section `e.torsionPoint s` equal to `0` read over `k` via
`φ`; some additive map `ν` from `w`-torsion vectors to `w`-torsion `k`-points of `x` is such that,
for a `w`-torsion point `z` over a local `k`-algebra `B` with `k`-point `π`, some `t ∈ ker π` has
`t ^ N = 0`, `N` the size of the fibre of `ν` over the closed point `placeTorsionMap π z` of `z`; if
that point is `0`, `z` vanishes along every algebra map that kills `t`. 
