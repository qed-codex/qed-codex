---
{
  "module": "src/Lib/Shimura/TraceFormula/DefiniteTrace.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Shimura/TraceFormula/DefiniteTrace.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Shimura/TraceFormula/DefiniteTrace.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Trace formula for algebraic forms, finiteness of signed frame classes, the definite side

This file gives a trace formula for a Hecke operator on a finite-dimensional space of algebraic
forms, computed from class representatives with weights. It also shows that only finitely many
double cosets GL_n(E) x (GU ∩ V), with V an open subgroup, contain a signed frame. These results
serve the definite side of the comparison of traces. There the trace of a regular Hecke element on
forms supported on definite frames is written as a sum over orbits of triples.

## Main definitions and results

* `New.trace_eq_weighted_sum`: the trace of the twisted Hecke operator `T` on a finite-dimensional
  space of algebraic forms, from representatives `r i` with weights `w i`.
* `New.Variety.finite_isSignedFrame_classes`: for an open subgroup V, only finitely many double
  cosets GL_n(E) x (GU ∩ V) contain a signed frame.
* `New.Variety.definiteForms`: the forms with values in a representation `ξ` of `GL n E` that
  are left `GL n E`-equivariant, vanish off the definite frames and are right invariant under the
  level.
* `New.Variety.definiteForms.rep`: the action of the Hecke algebra `New.Variety.heckeAlgebra` on it.
* `New.Variety.finite_definiteForms`, `New.Variety.finite_support_countTerm_definite`,
  `New.Variety.trace_definiteForms_eq_finsum_countTerm`: finite dimension, finite support and the
  trace formula.

Notions from other files:
* `New.levelSpace π K`: The vectors fixed by the subgroup `K` under the representation `π`; here
  `π` is `New.rightRegular`, the action of `G` on functions `G → W` by right translation.
* `New.Variety.GU`: The unitary similitudes: the `g ∈ GL_n(𝔸f E)` with `c • gᴴ g = ε • 1` for some
  rational `c > 0` and unit `ε` of `Ẑ`, that is, the frames of the forms `c • 1`.
* `New.Variety.levelGU`: the principal level K(𝔑), the similitudes in `GL_n(Ô E)` that are congruent
  to `1` modulo `𝔑`.
* `New.Variety.IsRegularHecke`: a(x⁻¹y⁻¹xK) ≠ 0 forces the characteristic polynomial of `y` to
  be separable.
* `New.Variety.IsNeat`: The level 𝔑 is neat: 𝔑 ≠ 0 and, whenever `x` is a signed frame with `ℓ` for
  some form (`New.Variety.IsSignedFrame`), every y in GL_n(E) with x⁻¹yx in `levelGU n 𝔑` that fixes
  ℓ under `New.Variety.ratConj` equals 1.

## Relation to the literature

Known; see `Lib.Shimura.TraceFormula.MarkedDefiniteSums` and
`Lib.Shimura.Uniformisation.AppellHumbert` for sources.



## Trace of a Hecke operator from weighted class representatives

The identity of a space `M` of equivariant forms is written as a weighted sum of maps that factor
through `W` by evaluation at representatives `r i`; the trace then moves over to `W`.


### `New.pi_sum_apply_mem_coindV_inf_levelSpace`

 Let `S g` be finite sets of elements of `Γ` with `γ ∈ S g ↔ g⁻¹ * (e γ * r) ∈ K`, empty for
`g ∈ D`. Then for every `v ∈ W` the function `g ↦ ∑ γ ∈ S g, ρ γ v` is equivariant along `e`
(it lies in `ρ.coindV e`), vanishes on `D` and is right `K`-invariant. 

### `New.trace_mul_comp_proj_comp_eq_finsum_cosetFn`

 The trace of one term of the trace formula `New.trace_eq_weighted_sum`. Let `J : W → M` be
linear with `ι (J v) g = ∑ γ ∈ S g, ρ γ v`, where `γ ∈ S g ↔ g⁻¹ * (e γ * r) ∈ K`; let `σ` be an
automorphism of `G` preserving `K`, and let `T` send `F` to the right translate of `s ∘ F ∘ σ⁻¹` by
the group ring element `a`. Then the trace of `T ∘ J ∘ (F ↦ F r) ∘ ι` on `M` is `∑ᶠ γ, cosetFn K a
(r⁻¹ * σ (e γ) * σ r) * trace (s * ρ γ)`. Here `cosetFn K a x` is the sum of the coefficients `a g`
over the `g` with `g K = x K`. 

### `New.trace_eq_weighted_sum`

 Let `ι` identify `M` with the `F : G → W` with `F (e γ * g) = ρ γ (F g)`, zero on `D` and right
`K`-invariant; `T` sends `F` to the right translate of `s ∘ F ∘ σ⁻¹` by `a`, and `σ` preserves `K`.
For points `r i` of `G` and weights `w i` such that `S i g = {γ | e γ * r i ∈ g K}` is empty on `D`
and `∑ i, w i * #(S i g) = 1` off `D`, `M` is finite-dimensional and `tr T` is the sum over `i` of
`w i * ∑ᶠ γ, cosetFn K a ((r i)⁻¹ * σ (e γ) * σ (r i)) * tr (s * ρ γ)`; `cosetFn` = `∑ a_g [gK]`. 


## Finiteness of double cosets carrying signed frames

An element `x` is a frame for a rational matrix β (`New.Variety.IsFrameFor`) if xᴴ β x is a unit of
Ẑ times the identity. `New.Variety.IsSignedFrame x ℓ` asks for such a β that is positive definite at
all infinite places other than the base place v₀ given by `CMBase E`, and such that β ℓ is positive
definite at v₀.


### `New.Variety.exists_star_mul_mul_mem_unitary`

 An invertible self-adjoint complex matrix `B` is congruent to a unitary one: for
`a = √|B⁻¹|`, built by the continuous functional calculus, the matrix `aᴴ B a` is unitary. 

### `New.Variety.exists_isCompact_gram_mkAdelicGL_mem`

 There is a compact set `B` of adelic matrices such that every frame `x` for an invertible
rational form `J` (that is, `xᴴ J x` is a unit of `Ẑ` times `1`) can be completed by archimedean
components `a` to an adelic matrix `g = (a, x)` whose Gram matrix `gᴴ J g` lies in `B`. 

### `New.Variety.doubleCoset_mk_eq_of_isFrameFor`

 If `r` and `y` are frames for the same rational form `β` and lie in one coset of `V`, then
`r` and `Y y`, for `Y` in `GL_n(E)`, lie in one double coset `GL_n(E) r (GU E n ⊓ V)`. 

### `New.Variety.finite_isSignedFrame_classes`

 Let `V` be an open subgroup of `GL_n(𝔸f E)`. The elements `x` that are signed frames for some
complex matrix `ℓ` (`New.Variety.IsSignedFrame`: `x` is a frame for some form `β` over `E` with
positivity conditions) lie in finitely many double cosets `GL_n(E) x (GU E n ⊓ V)`. Here `GU E n` is
the unitary similitudes `g` with `gᴴ g` a scalar finite idele of `ℚ`, and `GL_n(E)` acts on the left
through its diagonal embedding `toFinGL`. 


## Definite forms, their Hecke action and their trace

Conventions: `New.Variety.IsSignedFrame x 1` says that `x` is a frame for a rational form that is
positive definite at every infinite place (a definite frame).


### `definiteForms`

 Forms on the definite frames: the functions `φ` from `GL n` of the finite adeles to `W`
such that `φ (y x) = ξ y (φ x)` for `y` in `GL n E`; `φ x = 0` unless
`New.Variety.IsSignedFrame x 1` holds, that is, unless `x` is a frame for a totally positive
definite rational form (the submodule `pi S ⊥` asks for vanishing on `S`); and `φ (x k) = φ x`
for `k` in the principal level `levelGU n 𝔑`. 

### `definiteForms.rep`

 The action of the Hecke algebra of level `𝔑` on definite forms by right translation. Its
elements `a` are supported on `GUPlus E n`, and their coset function is left
`levelGU n 𝔑`-invariant. 

### `DefiniteClass`

 The definite classes: the double cosets `GL n E \ GL n (𝔸f E) / K`, with `K = levelGU n 𝔑`,
whose chosen representative is a definite frame. 

### `finite_definiteClass`

 At a neat level `𝔑` there are only finitely many definite classes. 

### `frame`

 The chosen representative `x_j` of the definite class `j`. 

### `isSignedFrame_frame`

 The representative of a definite class is a definite frame. 

### `coset`

 The coset `y x_j K`. 

### `coset_eq_mk_iff`

 The coset `y x_j K` is `g K` if and only if `g⁻¹ y x_j` lies in `K = levelGU n 𝔑`. 

### `eq_and_eq_of_coset_eq`

 At a neat level the coset `y x_j K` determines the class `j` and the rational matrix `y`. 

### `isSignedFrame_one_iff`

 The definite frames are the elements of the cosets `y x_j K`. 

### `orbit`

 The orbit under `GL n E` of the marked triple `(x_j K, y⁻¹, μ)`. A triple is a coset of
`levelGU n 𝔑`, an element of `GL n E` and an index in `n`; `γ` sends `(x K, z, μ)` to
`(γ x K, γ z γ⁻¹, μ)`. 

### `orbit_injective`

 At a neat level distinct triples `(j, y, μ)` give distinct orbits `orbit (j, y, μ)`. 

### `countTerm_orbit`

 The definite term of the orbit of `(x_j K, y⁻¹, μ)`: the coefficient of `a` at `x_j⁻¹ y x_j K`
times the weight `w` at the characteristic polynomial of `y⁻¹` and `μ`. 

### `support_countTerm_subset_range_orbit`

 An orbit with a nonzero definite term is the orbit of some `(x_j K, y⁻¹, μ)`. 

### `finite_support_countTerm_definite`

 At a neat level only finitely many orbits of triples have a nonzero definite term
`countTerm False a w` (the flag `False` selects the orbits whose frame is definite). 

### `finite_definiteForms_and_trace_eq_finsum_definiteClass`

 Let `ξ` be a representation of `GL_n(E)` on a finite-dimensional complex space `W`, and let the
level `𝔑` be neat (`hN`). The definite forms are the functions `φ : GL_n(𝔸f E) → W` with
`φ(yx) = ξ(y) φ(x)` for `y ∈ GL_n(E)`, which vanish off definite frames and are right-invariant
under `K = levelGU n 𝔑`. This space is finite-dimensional, and the trace on it of a Hecke element
`a` acting by right translation equals `∑_j ∑_{y ∈ GL_n(E)} f_a(x_j⁻¹ y x_j) · tr ξ(y)`. In this sum
`j` runs over the definite classes in `GL_n(E) \ GL_n(𝔸f E) / K` with chosen representatives
`x_j = j.frame`, and `f_a = heckeCosetFn a` is the function `∑ a_g 1_{gK}` for `a = ∑ a_g [g]`. 

### `finite_definiteForms`

 At a neat level the space of definite forms with values in `ξ` is finite-dimensional. 

### `trace_definiteForms_eq_finsum_definiteClass`

 At a neat level the trace of a Hecke element `a` on the definite forms is the sum, over the
definite classes `j` and the rational matrices `y`, of `heckeCosetFn a` (the function `∑ a_g [gK]`
of `a` on cosets) at `x_j⁻¹ y x_j`, where `x_j = j.frame` is the frame of `j`, times `tr (ξ y)`. 

### `trace_definiteForms_eq_finsum_countTerm`

 The trace formula on the definite side. Let `W` be finite-dimensional, `𝔑` neat and `a` a
regular Hecke element. Suppose `tr ξ(y⁻¹) = ∑ i, w P i` whenever the characteristic polynomial `P`
of `y` is separable. Then the trace of `a` on definite forms is the sum, over all orbits of triples,
of the definite terms `countTerm False a w` (the flag `False` selects definite frames). On the orbit
of `(x_j K, y⁻¹, μ)` this term is `heckeCosetFn a (x_j⁻¹ y x_j) * w (y⁻¹).charpoly μ`
(`countTerm_orbit`). 
