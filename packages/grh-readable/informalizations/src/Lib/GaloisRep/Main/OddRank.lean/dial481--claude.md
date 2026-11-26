---
{
  "module": "src/Lib/GaloisRep/Main/OddRank.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/GaloisRep/Main/OddRank.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/GaloisRep/Main/OddRank.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Attached Galois representations in odd rank and their descent along weak base change

This file proves that eigenforms on the definite space `New.stdSpace` of odd rank over stably
unramified CM fields have attached Galois representations. It first proves a descent result along
a step of weak base change. The general odd-rank case is then reduced to the split case of
`Lib.GaloisRep.Main.SplitCase` by quadratic base changes, whose representations are glued on open
subgroups of the Galois group.

## Main definitions and results

* `New.IsWeakBaseChange.hasHeckePolyAt_of_decompGroup_le`: along a step of weak base change from f
  to f', at a split place off S and its conjugate whose decomposition group lies in the open
  subgroup N of the step, the Hecke polynomial of f passes to f'.
* `New.IsWeakBaseChange.attached_comp_stepKerInclusion`: a representation r' attached to f',
  restricted to N (`New.QZChar.stepKer`), is attached to the polynomials of f.
* `New.IsWeakBaseChange.descendsAt`: the local conditions on r' pass to every representation
  attached to f (`New.GaloisRep.DescendsAt`).
* `New.GaloisRep.sphericalCompat_of_odd`: the statement `New.GaloisRep.SphericalCompat` (an
  eigenform has an attached Galois representation, and every attached representation is compatible
  at a spherical place w) for the definite space `New.stdSpace` of odd rank over a stably unramified
  CM field (`New.HasPrimitiveRoot5040`). The split case is applied to base changes of f along
  quadratic steps. The representations obtained on open subgroups are glued
  (`New.GaloisRep.exists_attached_of_open_subgroups`), and the local properties at w descend from
  one step (`New.IsWeakBaseChange.isCompatibleAt_of_attached`).

Notions from other files:
* `New.IsWeakBaseChange` μ Z f f': the set Z is finite and, for u above w ∉ Z ∪ Z̄, sphericity
  passes from f to f' at `New.IsStepUnramifiedAt` places, and Hecke polynomials pass from f to f' at
  `New.IsMatched` places.
* `New.IsEigenform`: f ≠ 0, and almost all places w of prime norm are split and f has the Hecke
  polynomial P w at w.
* `New.GaloisRep.Attached` P r i: r is continuous with non-degenerate trace form, i (by default the
  identity) is an open map to Gal(Ω/E), and at most Frobenius elements the characteristic
  polynomials of r are ℓ-adically close to those given by P.

## Relation to the literature

Galois representations attached to forms on definite unitary groups. The form proved
is for the standard definite unitary group of odd rank over a stably unramified CM field
(`New.HasPrimitiveRoot5040`). At a place whose local compact group fixes the form,
each attached ℓ-adic representation is unramified or crystalline with the Hodge–Tate jumps of the
weight, and each Hecke polynomial there kills geometric Frobenius. Here "attached" asks, beyond
continuity and a non-degenerate trace form, only that Hecke polynomials are ℓ-adically close to
characteristic polynomials at most Frobenius elements. The construction uses ℓ-adic limits, and
quadratic base changes whose representations are glued on open subgroups of the Galois group.
Source: Chenevier, Harris, Construction of automorphic Galois
representations II, Camb. J. Math. 1 (2013), Thm 3.2.3; with Labesse, Changement de base CM et
séries discrètes (2011), Cor. 5.3, and Barnet-Lamb, Gee, Geraghty, Taylor, Potential automorphy and
change of weight (2014), Thm 2.1.1.



## Descent along a step of weak base change

A continuous character χ of Gal(Ω/E) with values in ℚ/ℤ gives the field L = `New.QZChar.stepField` χ
cut out by g ↦ χ g + χ (gᶜ), the idele character `New.QZChar.ideleChar` χ, and the open subgroup
N = `New.QZChar.stepKer` χ = Gal(Ω/L) ∩ ker χ of Gal(Ω/E).

Places of Ω are valuation subrings A (`New.IsPlaceOver`, decomposition group `New.decompGroup`).


### `QZChar.stepKer`

 The subgroup Gal(Ω/L) ∩ ker χ of Gal(Ω/E), where L = `New.QZChar.stepField` χ: the elements
killed by χ and by its symmetrisation. 

### `QZChar.stepKerInclusion`

 The inclusion of Gal(Ω/L) ∩ ker χ in Gal(Ω/L), where L = `New.QZChar.stepField` χ. 

### `GaloisRep.DescendsAt`

 The local conditions at the valuation subring A of Ω pass from the representation r' of
Gal(Ω/L), where L = `New.QZChar.stepField` χ, to the representation r of Gal(Ω/E). 

### `GaloisRep.DescendsAt.isFiniteTypeAt`

 If r' is of finite type at A, so is r. 

### `GaloisRep.DescendsAt.hasJumpsAt`

 If r' has the jumps of the weight κ pulled back to L, in rank m, then r has those of κ. 

### `GaloisRep.DescendsAt.polyKillsAt`

 For s in Gal(Ω/L) ∩ ker χ, a polynomial that kills the image of s in Gal(Ω/L) for r' kills s
  for r. 

### `IsPlaceOver.isMatched_of_decompGroup_le`

 If the decomposition group of a place `A` of the closure above `w` is killed by `χ` and by its
symmetrisation, so that it fixes the field of the step, then `w` is matched: `ideleChar χ` is
trivial on the local ideles at `w`, and `w` splits completely in the field of the step. 

### `IsWeakBaseChange.hasHeckePolyAt_of_decompGroup_le`

 Let `f'` be a weak base change of `f` to the field `stepField χ`, off `S` and its conjugate.
Let the place `A` of `Ω` lie over a split place `w` of `E` outside these sets, with
decomposition group killed by `χ` and by its symmetrisation. If `f` has the Hecke polynomial `Q`
at `w`, then every place `u` of `stepField χ` above `w` has the norm of `w` and is split, and `f'`
has the Hecke polynomial `Q` at `u`. 

### `HasHeckePolyAt.unique`

 A nonzero function has at most one Hecke polynomial at a split place. 

### `IsWeakBaseChange.attached_comp_stepKerInclusion`

 Let `χ` be a continuous `ℚ/ℤ`-valued character of Gal(Ω/E), and let `L = New.QZChar.stepField χ`
be the fixed field of the kernel of `g ↦ χ g + χ (gᶜ)`. Let `f` and `f'` be eigenforms on the
unitary groups over `E` and `L` with systems of polynomials `P` and `P'`, let `f'` be a weak base
change of `f` off `S` relative to the idele character of `χ`, and let `r'` be attached to `P'`. Then
the restriction of `r'` to the subgroup Gal(Ω/L) ∩ ker χ of Gal(Ω/E) is attached to `P` along the
inclusion of this subgroup in Gal(Ω/E). 

### `IsWeakBaseChange.descendsAt`

 Let `χ` be a continuous `ℚ/ℤ`-valued character of `Gal(Ω/E)`, and let
`L = New.QZChar.stepField χ` be the field cut out by `g ↦ χ g + χ (gᶜ)`. Let `f'` on `L` be a weak
base change of `f` off the finite set `S` of places of `E`, relative to the idele character
`exp(2πi χ ∘ Art)`, with both eigenforms for the systems `P'` and `P`. If `r'` is attached to `P'`
and `r` to `P`, then the local conditions at every valuation subring `A` of `Ω` pass from `r'` to
`r` (`New.GaloisRep.DescendsAt`). 

### `IsWeakBaseChange.isCompatibleAt_of_attached`

 Let `f'` be a weak base change of `f` to `stepField χ`, both eigenforms, with `r'` and `r`
attached to their systems of polynomials. Let `A` lie over `w ∉ S ∪ S̄` and let `u` be a place of
`stepField χ` above `w`. If `χ` and its symmetrisation kill inertia at `A`, and also decomposition
when `w` is split, then compatibility of `r'` with `f'` at `u` (`New.GaloisRep.IsCompatibleAt`:
good, with the jumps of the weight in rank `a`, and at a split place each Hecke polynomial kills
geometric Frobenius) gives that of `r` with `f` at `w`. 

 ## The general odd-rank case 

### `New.GaloisRep.exists_weak_baseChange`

 Let `μ` be the character of a step `E' / E` (`New.IsStep`: a CM extension of prime degree with
an idele character), with `E'` stably unramified (`New.HasPrimitiveRoot5040`), and `f` a nonzero
form of weight `κ` over `E`. Some eigenform `F` over `E'`, of the pulled back weight, is a weak
base change of `f` with empty exceptional set (`New.IsWeakBaseChange`). 

### `New.GaloisRep.isStepUnramifiedAt_of_decompGroup_le`

 Let the step given by `χ` be an extension of prime degree with idele character
(`New.IsStep`). If the decomposition group of `A` is killed by the symmetrisation of `χ`, so fixes
the field of the step, and `χ` kills inertia, then the step is unramified at the place below `A`
(`New.IsStepUnramifiedAt`: the extension and the character are unramified at each place above). 

### `New.GaloisRep.exists_attached_of_open_subgroups`

 Let `ρ₀` on a normal subgroup `N₀` of `Gal(Ω/E)` and the `ρ T` on open normal subgroups `N T`
be attached to the same system `P` along the inclusions (`New.GaloisRep.Attached`: the
representation is continuous with non-degenerate trace form, the inclusion is open, and the
characteristic polynomials are `ℓ`-adically close to those of `P` at most Frobenius elements). Let
`I` be a set such that every subgroup containing `I` meets every coset of `N₀`, and such that each
conjugate of an element of `I` lies in every `N T` and is killed by `ρ T`. If every arithmetic
Frobenius element at a place `A` of `Ω` over a place `y` of prime norm lies in some `N T`, then a
representation of `Gal(Ω/E)` is attached to `P`. 

### `New.GaloisRep.sphericalCompat_of_odd`

 Let `a` be odd, `E` a CM field containing a primitive 5040th root of unity, and `w` any finite
place. Then eigenforms of any weight on the standard definite unitary group of rank `a` satisfy
`New.GaloisRep.SphericalCompat` at `w`: each has an attached representation. If the form is
spherical at `w`, every representation attached to its Hecke polynomials satisfies the local
conditions `IsCompatibleAt` at the places of `Ω` over `w`: it is good there, has the jumps of the
weight, and at a split `w` the Hecke polynomial kills geometric Frobenius elements. 
