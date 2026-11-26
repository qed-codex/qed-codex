---
{
  "module": "src/Lib/Shimura/AbelianScheme/Pairings.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Shimura/AbelianScheme/Pairings.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Shimura/AbelianScheme/Pairings.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Pairings of line bundle classes on abelian schemes and their fpqc descent

This file studies classes of line bundles on commutative group schemes and abelian schemes. Line
bundles are cocycles (`New.LineBundle`), and `New.Pic` is written additively. For a class `c` and
points `x`, `y`, the pairing `New.Pic.pairing c x y` is the class (x + y)^*c − x^*c − y^*c + 0^*c.
The file proves rules for the pairing, a quasi-finiteness criterion, and stability of abelian
schemes under base change. It also treats the descent of identities between pairings along an fpqc
cover.

## Main definitions and results

* `New.Variety.locallyQuasiFinite_of_pull_picClass`: a map that pulls a class back to a nonzero
  multiple of an embedding class is locally quasi-finite.
* `New.Pic.ParallelogramLaw.pairing_nsmul_left`, `New.Variety.pairing_comm`,
  `New.Variety.pairing_comp`: rules for the pairing.
* `New.Variety.pull_nsmul_eq_sq_smul`: over a local ring, multiplication by `m` pulls `c` back to
  `m² c` if `c` satisfies the parallelogram law.

Notions from other files:
* `New.Pic.atPoint`: For c in Pic A and a T-point x of A, the pull-back x^*c in Pic T.
* `New.Pic.ParallelogramLaw`: (x + y)^*c + (x − y)^*c + 2·0^*c = 2(x^*c + y^*c) for all points.
* `New.IsAbelianScheme`: a commutative group scheme A over S is abelian if it is smooth and proper
  over S and multiplication by every m ≠ 0 is surjective.
* `New.LineBundle.IsProjEmbedding L s`: `L` embeds `X` in projective space over `S`: it is a linear
  system, `s` is proper, and points of one chart with the same coordinates and the same image in `S`
  are equal.

## Relation to the literature

Known; see `Lib.Shimura.AbelianScheme.IsogenyFlatness` for sources.


 ## Quasi-finiteness, rules for the pairing, and multiplication by m 

### `Variety.locallyQuasiFinite_of_pull_picClass`

 Let N be a linear system separating the points of A, proper over S, and let B be separated
over S. An S-morphism f : A → B with f^*c = m[N] for some c in Pic B and m ≠ 0 is locally
quasi-finite. 

 ### The pairing of a class that satisfies the parallelogram law 

### `Pic.ParallelogramLaw.pairing_add_add_pairing_sub`

 If `c` satisfies the parallelogram law, its pairing `⟨·, ·⟩` (`New.Pic.pairing`) satisfies
`⟨x + y, z⟩ + ⟨x - y, z⟩ = 2 ⟨x, z⟩` for `T`-points `x`, `y`, `z` of `A`. 

### `Pic.ParallelogramLaw.pairing_nsmul_left`

 If c in Pic A satisfies the parallelogram law on a commutative group scheme A over S, then ⟨mx,
y⟩ = m⟨x, y⟩ in Pic T for T-points x, y and natural m, where ⟨x,
y⟩ = (x+y)^*c − x^*c − y^*c + 0^*c. 

### `Pic.ParallelogramLaw.nsmul_pairing_eq_pairing_nsmul`

 If `c` satisfies the parallelogram law, the pairing of `m • c` at `(x, y)` is the pairing of `c`
at `(m • x, y)`. 

 ### Base change and products 

### `isGroupBaseChange_counit`

 Let `A` be a commutative group scheme over `S` with an action of the ring `O` (`ModuleObj O A`).
The pull-back of `A` along `b : S' → S`, with the counit as projection, is a base change in the
sense of `New.IsGroupBaseChange`: the square is a pullback, and composing with the counit is
`O`-linear on points. 

### `pairing_comm`

 The pairing `⟨x, y⟩ = (x + y)^*c − x^*c − y^*c + 0^*c` of a class `c` in `Pic A` is symmetric
in the `T`-points `x`, `y` of `A`. 

### `pairing_comp`

 Pairing after pulling `c` back along a homomorphism `f : B → A` is pairing at the images under
`f`. 

### `instance [IsProper A.hom] [IsProper B.hom] : IsProper (A ⊗ B).hom`

 The product over `S` of two proper schemes over `S` is proper over `S`. 

### `noncomputable instance [i : IsAbelianScheme B] : IsAbelianScheme (pullback b B)`

 The base change of an abelian scheme along `b : S' → S` is an abelian scheme over `S'`. 

 ### Group schemes over a local ring 

### `atPoint_toUnit_comp_eq_zero`

 Over a local ring, a class pulls back to zero along a point that comes from a section. 

### `pull_nsmul_eq_sq_smul`

 Let `A` be a commutative group scheme over a local ring and `c` a class in `Pic A` that
satisfies the parallelogram law `New.Pic.ParallelogramLaw`. Then the pull-back of `c` under
multiplication by a natural number `m` is `m² c`. 


## Descent of pairing identities along an fpqc cover

A' is a base change to S of an abelian variety over a field, and f : A → A₁ is flat, surjective and
quasi-compact over S.

* `New.Variety.eq_pull_zero_section`: a class on A₁ × A' that is trivial on A × A' is pulled back
  from A₁ × 0.
* `New.Variety.pairing_eq_of_fpqc_cover`: an identity between two pairings that holds for points
  factoring through f holds for all points.

The idea: global functions on a base change of A' are constant along A'
(`New.Variety.hasConstFunctions_of_isPullback`), so a frame normalised along the zero section
descends.


### `New.Variety.lift_left_comp_whiskerRight_left`

 Let `f : A → A₁` be a morphism over `S`. For `T`-points `x` of `A` and `a` of `A'`, the point
`(x, a)` of `A × A'` maps to `(f x, a)` under `f × 1` (as morphisms of underlying schemes). 

### `New.Variety.exists_eq_lift_of_comp_whiskerRight_eq`

 Let `f : A → A₁` be a morphism over `S`. Two `Y`-points of `A × A'` with the same image under
`f × 1` lie over one point `s` of `S` and have the form `(x, z)` and `(y, z)` with `f x = f y`. 

### `New.Variety.exists_apply_lift_eq_mul_of_isFrame`

 Let A' be the base change of an integral abelian variety over a field (`hp`), and let `u` be a
frame of the pull-back of `L` along `f × 1`. For points `x`, `y` of `A` with `f x = f y`, the
values of `u` at `(x, a)` and `(y, a)` differ by a factor that does not depend on `a`. 

### `New.Variety.eq_pull_zero_section`

 Let A' be the base change along q : S → Spec k of an integral abelian variety A₀ over a field k
(`hp`), and let f : A → A₁ be flat, surjective and quasi-compact over S. A class in Pic(A₁ × A')
that is trivial on A × A' equals its pull-back along (x, a) ↦ (x, 0). 

### `New.Variety.pairing_eq_of_fpqc_cover`

 Let A' be the base change of an integral abelian variety over a field (`hp`), let f : A → A₁ be
flat, surjective and quasi-compact, let a, a' be morphisms from A₁, and let b, b' be homomorphisms
on A'. If ⟨a(x), b(y)⟩_c = ⟨a'(x), b'(y)⟩_c' for all points x of A₁
factoring through f and y of A', it holds for all x. 
