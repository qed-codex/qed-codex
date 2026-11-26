---
{
  "module": "src/Lib/SiegelWeil/Formula/StrongApproximation.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/SiegelWeil/Formula/StrongApproximation.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/SiegelWeil/Formula/StrongApproximation.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Strong approximation and constancy of automorphic functions in equal rank

This file proves that an automorphic function on a unitary group with a hyperbolic plane is constant
under level and torus hypotheses. This is the step that makes the period of a theta lift between
spaces of equal rank a constant. Strong approximation gives invariance under two opposite unipotent
radicals, Witt's theorem reaches the rational points of the Levi factor, and weak approximation
with the Iwasawa decomposition gives all points. `New.Exchange.IsAutFunction W D` says that `D` is
continuous on the adelic unitary group of `W` and left invariant under rational points, and
`H : W.Splitting W₀ Unit` splits off a hyperbolic plane.

## Main definitions and results

* `New.Exchange.IsAutFunction.apply_eq_apply_one`: an automorphic function on a unitary group with a
  hyperbolic plane is constant if it is right invariant under `Gf.supportedOn n S` for a nonempty
  set `S` of finite places, has level `stdLevel` away from `S`, and satisfies a hypothesis on the
  torus of the plane.
* `New.Exchange.exists_torus_mul_rational_fixes`: if `D` is left invariant under the radical
  elements of every splitting of a hyperbolic plane off `W` with complement `W₀`, then for each set
  `R` of finite places and each rational point `γ` of `W₀` it is left invariant under the components
  on `R ∪ R̄` (`closurePart R`) of a Levi element with `W₀`-block `γ`.

Notions from other files:
* `New.Space`: a hermitian space with a point, given by a matrix J over E and x in GL_n(𝔸) with xᴴJx
  equal to diag(s) at the infinite places and 1 at the finite places.
* `New.Space.Splitting.levi`: The homomorphism GL_p(𝔸) × G(V₀) → G(V) sending (m, g₀) to the element
  with k ↦ km, ι ↦ ιg₀, l ↦ l m*⁻¹.
* `New.Space.Splitting.radicalElement`: `P.radicalElement 0 b`, written `n(b)`, is the unipotent
  element with k ↦ k and l ↦ l − k(½ȷ⁻¹(b + b*)), where ȷ is the purely imaginary element of
  `WeilData E`.

## Relation to the literature

A weak substitute for strong approximation for special unitary groups. Only the constancy of a
continuous function `D` on the adelic points of the full unitary group is proved, under three
hypotheses. First, `D` is left invariant under the rational points. Second, for a nonempty set `S`
of finite places, `D` is right invariant under the points supported on `S` and the complex
conjugates of its places, and under the integral finite adelic points that are trivial on `S`.
Third, for a splitting of a hyperbolic plane: if `D` is left invariant under the unipotent radical
of the parabolic subgroup fixing the isotropic line, then the values of `D` on the Levi subgroup
`GL₁ × G(W₀)`, with `W₀` the complement of the plane, do not depend on the `GL₁` component.

Source: M. Kneser, Starke Approximation in algebraischen Gruppen I, J. reine angew. Math. 218
(1965); G. Shimura, Arithmetic of unitary groups, Ann. of Math. 79 (1964); survey A. Rapinchuk, MSRI
Publ. 61 (2013).


### `New.Exchange.exists_torus_mul_quasiReflection_fixes`

 Let `D` be left invariant under the radical elements `H'.radicalElement c z` of every splitting
`H'` of a hyperbolic plane off `W` with complement `W₀`, and let `R` be a set of finite places. For
each quasi-reflection `ρ` of `W₀`, given by a vector `v` and a unit `σ` with `σ + σ̄ = ⟨v, v⟩`,
there is a torus element `a` such that `D` is left invariant under the components on `R ∪ R̄`
(`closurePart R`) of the Levi element `H.levi (a, ρ)`. 

### `New.Exchange.exists_torus_mul_rational_fixes`

 Let `D` be left invariant under the radical elements of every splitting of a hyperbolic plane
off `W` with complement `W₀`. Then for each set `R` of finite places and each rational point `γ` of
`W₀` it is left invariant under the components on `R ∪ R̄` (`closurePart R`) of a Levi element with
`W₀`-block `γ`. 

### `New.Exchange.IsAutFunction.apply_eq_apply_one`

 Let `H` split a hyperbolic plane off `W` with complement `W₀`, and let `D` be continuous on the
adelic unitary group of `W` and left invariant under rational points (`IsAutFunction`). Let `S` be a
nonempty set of finite places, and let `D` be right invariant (`HasLevel`) under the points
supported on `S ∪ S̄` (`Gf.supportedOn n S`) and under the integral points (`stdLevel E n`) that are
trivial on `S` (`Gf.trivialOn n S`). If invariance under the radical of `H` makes `D` on the Levi
group independent of the torus, then `D` is constant.

A weak substitute for strong approximation for special unitary groups (Kneser, Platonov): only the
constancy of `D` is concluded, for isotropic `W` and under the hypothesis on the torus. The
approximation inputs of the proof are additive strong approximation in unipotent radicals and weak
approximation in unitary groups. 
