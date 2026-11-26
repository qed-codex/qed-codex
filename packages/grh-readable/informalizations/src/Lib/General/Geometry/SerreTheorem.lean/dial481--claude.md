---
{
  "module": "src/Lib/General/Geometry/SerreTheorem.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/General/Geometry/SerreTheorem.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/General/Geometry/SerreTheorem.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Absolute Frobenius, Serre's theorem on sections of powers, and projective embeddings

A line bundle (`New.LineBundle`) is an open cover `U i` with a cocycle `g i j`, and `L.picClass` is
its class in the additively written Picard group. `New.LineBundle.IsLinearSystem` says that the
transition functions behave like the affine coordinates `s j / s i` of a map to a projective space.
The file shows that the absolute `l ^ f`-Frobenius multiplies the class of a linear system by
`l ^ f`.

## Main definitions and results

* `New.Variety.absFrobenius f X`: the absolute `l ^ f`-Frobenius of a scheme `X` over a field of
  characteristic `l`. It acts on `B`-valued points through `x ↦ x ^ l ^ f` on `B`
  (`New.Variety.comp_absFrobenius`), commutes with all morphisms and fixes the underlying space.
* `New.Variety.eventually_span_coordSection`: let `N` be a projective embedding of an integral
  scheme over a field and `p` a base change to a noetherian ring. For large `m` the monomials of
  degree `m` in the coordinates span the sections of `(p^* N) ^ m`.
* The instance `New.isProper_pi`: the product in `Over S` of a finite family of proper schemes over
  `S` is proper over `S`.
* `New.Variety.HasProjEmbedding.of_isClosedImmersion_pi`: if finitely many `S`-schemes have
  projective embeddings over `S`, so does every closed subscheme of their fibre product.

Notions from other files:
* `New.LineBundle.pull`, `New.LineBundle.pow`: the pull-back of a line bundle along a morphism, and
  its `m`-th tensor power, whose charts are indexed by `m`-tuples of indices.
* `New.LineBundle.IsProjEmbedding`: a linear system on a proper scheme whose affine coordinates
  `g i j` separate the ring-valued points of each chart `U i` over the base.
* `New.Variety.coordSection`: the `j`-th coordinate `s j` of a linear system as a global section.
* `New.ThetaTori.formSpan R x m`: the values at a family `x` of the forms of degree `m` over `R`.

## Relation to the literature

Known result: a case of the surjectivity half of Serre's theorem on sections of powers of a
projective embedding.


 ## The absolute Frobenius and classes of linear systems 

### `natCast_eq_zero_of_over_charP`

 If `Spec B` maps to the spectrum of a field `k` of characteristic `l`, then `l = 0` in `B`. 

### `exists_absFrobenius`

 For a scheme `X` over a field `k` of prime characteristic `l`, there is an endomorphism of the
underlying scheme that acts on `B`-valued points through `x ↦ x ^ l ^ f` on `B`, for every ring
`B`. 

### `absFrobenius`

 For a scheme `X` over a field `k` of prime characteristic `l`, the absolute `l ^ f`-Frobenius of
the underlying scheme. It acts on `B`-valued points through `x ↦ x ^ l ^ f` on `B`
(`comp_absFrobenius`: `t ≫ absFrobenius f X = specMap (frobPow _ f) ≫ t`, where `frobPow` is that
map on `B` and `specMap` its map on spectra), and this determines it. 

### `picClass_pull_absFrobenius`

 Let `L` be a linear system (the data of a map to projective space) on a scheme `X` over a field
of characteristic `l`. The pull-back of `L` along the absolute `l ^ f`-Frobenius has class `l ^ f`
times that of `L` in the additively written Picard group. 

 ## Saturation and Serre's theorem on sections of powers 

### `mul_mem_formSpan_succ`

 Multiplying the value at `x` of a form of degree `m` by a member of the family `x` gives the
value of a form of degree `m + 1`. 

### `eventually_mem_formSpan_of_mul`

 Cancellation: let `k` be a noetherian ring, `F` a commutative `k`-algebra and `x` a finite
family in `F` with `x r = 1`. For all large `D`: if every `f * x j` is the value at `x` of a form of
degree `D + 1`, then `f` is the value at `x` of a form of degree `D`. 

### `eventually_mem_formSpan_of_mul_pow`

 Saturation: let `k` be a noetherian ring, `F` a commutative `k`-algebra and `x` a finite family
in `F` with `x r = 1`. For all large `D`: if for each `i` some `f * x i ^ N` is the value at
`x` of a form of degree `D + N`, then `f` is the value at `x` of a form of degree `D`. 

### `pow_transition_apply`

 The transition functions of the `m`-th power of `L` are products of `m` transition functions
of `L`. 

### `exists_mul_pow_mem_formSpan_of_isSection`

 Let `L` be a projective embedding (finitely many coordinates) of a scheme `X` over a ring `k`,
let `t` be a section of `L ^ m`, given as a value `t c` at `B`-valued points in each chart `c` (an
`m`-tuple of indices), regular and compatible with the transition functions (`IsSection`), and let
`ξ` be a `B`-valued point over `k` in the charts `i` and `j`, with affine coordinates
`x l = L.transition i l (ξ)`. Then for some `N`, the value of `t` at `ξ` in the chart `i` times
`x j ^ N` is the value at `x` of a form of degree `m + N`. 

### `eq_zero_of_apply_eq_zero_of_dominant`

 Let `ξ` be a quasi-compact scheme-theoretically dominant ring-valued point of `X` in the chart
`i` of a line bundle `L`. A global section of `L` whose value at `ξ` in this chart is zero is
zero. 

### `eventually_span_coordSection`

 A case of Serre's theorem, surjectivity half. Let `N` be a projective embedding (finitely many
coordinates) of an integral scheme `A` over a field `F`, and `p : A' ⟶ A` the base change along
`b : Spec k ⟶ Spec F`, with `k` noetherian. For all large `m`, the global sections of `(p^* N) ^ m`
are spanned over `k` by its coordinates `coordSection h`, where `h` is any proof that it is a linear
system. These coordinates are indexed by `m`-tuples of indices, each giving a monomial of degree `m`
in the coordinates of `p^* N`. 

 ## Finite products of proper schemes 

### `New.isProper_pi`

 A finite product of proper schemes over `S` is proper over `S`. 


## Projective embeddings of composites and products

The property `New.Variety.HasProjEmbedding` (proper, with a finite linear system that separates
points over the base) passes to composites.


### `instance {X S : Scheme} {s : X ⟶ S} {A : Over X} [hA : HasProjEmbedding A.hom] [hs : HasProjEmbedding (X`

 If `A` has a projective embedding over `X`, and `X` has one over `S`, then `A` has one over `S`,
given by the Segre product of the two linear systems. 

### `HasProjEmbedding.of_isClosedImmersion_pi`

 If an `S`-scheme `W` has a closed immersion over `S` into the fibre product of finitely many
`S`-schemes `A l`, each with a projective embedding over `S` (proper, with a finite linear system
that separates points), then `W` has a projective embedding over `S`. 
