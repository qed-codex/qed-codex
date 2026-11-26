---
{
  "module": "src/Lib/General/Geometry/SmoothnessCriterion.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/General/Geometry/SmoothnessCriterion.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/General/Geometry/SmoothnessCriterion.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Smoothness near an arc from an immersive generic family and a bound on the tangent space

A criterion for smoothness of a scheme `X` over a normal domain `R` near an arc `Spec V ⟶ X`, where
`V` is a valuation subring of `ℂ`.

* `New.Variety.exists_landsIn_smoothOfRelativeDimension`: the criterion.

Idea: by the tangent bound, `d` functions map `X` to affine `d`-space over `R`, unramified at the
closed point of the arc. The holomorphic family makes this map dominant, so it is étale there.

Notions from other files:
* `New.LandsIn`: The morphism t: Y → X lands in the open U, that is, t⁻¹U is all of Y.
* `New.IsHolomorphicImmersionAt`: A family of complex points is holomorphic at a parameter and
  constant to first order only in the direction 0.
* `New.specMap`: The morphism of spectra given by a ring homomorphism.
* `New.Variety.sqZeroReduction`: The morphism from Spec R to Spec (R ⊕ M) given by the projection
  of the trivial square-zero extension.
* `New.PointFn.ofSection`: The function on ring-valued points given by a section s over U: its value
  at t is t*s if t lands in U, and 0 otherwise.


### `New.Variety.exists_etale_away_of_faithful`

 Let `S` be a quotient of a standard étale algebra over a normal domain `A`, with a map to a
domain `V` in which `A` embeds. Then `S` is étale over `A` after inverting some `g` whose image in
`V` is a unit. 

### `New.Variety.span_tmul_differential`

 The differentials of elements of `B` span the relative cotangent space at a `k`-point. 

### `New.Variety.exists_span_differentials`

 If the relative cotangent space at a `k`-point has dimension at most `d`, the differentials
of `d` elements span it. 

### `New.Variety.isUnramifiedAt_of_span_differentials`

 Let `B` be of finite type over `A`. If the differentials of elements coming from `A` span the
cotangent space of `B` over `R` at a `k`-point, then `B` is unramified over `A` at that point. 

### `New.Variety.isIntegrallyClosed_mvPolynomial_fin`

 A polynomial ring in finitely many variables over a normal domain is normal. 

### `New.Variety.isStandardSmoothOfRelativeDimension_of_mvPolynomial`

 An algebra that is standard smooth of relative dimension `0` over the polynomial ring in `d`
variables over `R` is standard smooth of relative dimension `d` over `R`. 

### `New.Variety.exists_isStandardSmoothOfRelativeDimension_away`

 Let `A = R[X₁, …, X_d]` with `R` a normal domain, and let `S` be a quotient of a standard étale
`A`-algebra, with a map to a domain `V` in which `A` embeds. Then `S` is standard smooth of relative
dimension `d` over `R` after inverting some `g` whose image in `V` is a unit. 

### `New.Variety.specMap_comp_mono_eq_iff`

 Two points of `X` that factor through a monomorphism `j : Spec B ⟶ X` are equal if and only if
the ring maps on `B` agree. 

### `New.Variety.finrank_cotangent_le`

 Let `Spec B ⟶ X` be a monomorphism over `Spec R`, and `t` the `k`-point of `X` given by
`B → k`. Suppose that `finrank k M ≤ d` whenever a deformation of `t` over `k ⊕ M*`, constant in
`Spec R`, pulls back to the constant point along `l : M` only for `l = 0`. Then the relative
cotangent space of `B` at `t` has dimension at most `d`. 

### `New.Variety.inl_fst_eq_of_formallyUnramified`

 A ring map `θ` from a formally unramified `A`-algebra to `K ⊕ K` (square zero) whose
infinitesimal part vanishes on `A` has zero infinitesimal part. 

### `New.Variety.eq_zero_of_fderiv_ofSection_eq_zero`

 Let `φ` be a holomorphic immersion at `b`, let `W` be an affine open and `f` a function on it
such that `Γ(X, W)[1/f]` is formally unramified over `A`, and let `φ b` land in the locus where `f`
is invertible. If the functions coming from `A` are constant to first order on the family along
`v`, then `v = 0`. 

### `New.Variety.eq_zero_of_eventually_eval_eq_zero`

 Let `Q` be a polynomial over a ring embedded in `ℂ` by `u`, and `Z` a map that is strictly
differentiable with surjective derivative at `b`. If `Q(Z w) = 0` for `w` near `b`, then
`Q = 0`. 

### `New.Variety.eq_zero_of_eventually_ofSection_eq_zero`

 In an affine chart `W`, let `A = R[X₁, …, X_d]` act, let `u : R → ℂ` be injective, and let
the function coming from each `P` in `A` have the value `P(Z w)` at `φ w` for `w` near `b`, with
coefficients moved by `u`, where `Z` is analytic. Let `Γ(X, W)[1/f]` be formally unramified over
`A`, let `φ b` land in the locus of `W` where `f` is invertible, and let `φ` be a holomorphic
immersion at `b`. If the function of `Q` vanishes on the family near `b`, then `Q = 0`. 

### `New.Variety.ofSection_eq_zero_of_specializes`

 If a section over `U` vanishes at a complex point `x` in `U`, it vanishes at every complex
point in `U` to which `x` specialises. 

### `New.Variety.ofSection_eval₂Hom_eventuallyEq`

 Let `Spec ρ` be the structure map of an affine chart `W` of `X` over `Spec R`, and let the
points `φ w` lie in `W` near `b`, all over `u : R → ℂ`. Then a polynomial in functions `z i` on
`W` restricts on the family to the polynomial, with coefficients moved by `u`, in the values of
the `z i`. 

### `New.Variety.eq_zero_of_ofSection_eq_zero`

 In an affine chart `W` of `X` over `Spec R`, let `A = R[X₁, …, X_d]` act by `X i ↦ z i` and
let `Γ(X, W)[1/f]` be formally unramified over `A`. Let all `φ w` lie over an injective
`u : R → ℂ`, let `φ` be a holomorphic immersion at `b`, let `φ b` land in the locus where `f`
is invertible, and let `φ b` specialise to `φ w` for `w` near `b`. If `Q(z)` vanishes at `φ b`,
then `Q = 0`: it vanishes at the specialisations, so on the image of a submersion. 

### `New.Variety.exists_smooth_open_of_standardSmooth_away`

 Let `j : Spec B ⟶ X` be an open immersion over `Spec R` and `g : B` such that `B[1/g]` is
standard smooth of relative dimension `d` over `R`. If `β : B → V` maps `g` to a unit, then the
point given by `β` lands in an open set of `X` that is smooth of relative dimension `d` over
`Spec R`. 

### `New.Variety.exists_landsIn_smoothOfRelativeDimension`

 Let `s : X ⟶ Spec R` be locally of finite type, `R` a normal domain, `φ` a family of complex
points of `X` and `arc` a point with values in a valuation subring `V` of `ℂ`. Assume:
(a) `arc` extends `φ w₀`;
(b) all `φ w` lie over one embedding `emb : R → ℂ`;
(c) `φ w₀` specialises to `φ w` for `w` near `w₀`;
(d) `φ` has `d` parameters and is a holomorphic immersion at `w₀`, that is, it is holomorphic
there and constant to first order only in the direction `0`;
(e) `ϑ : V → k` is a local map to a field, so it gives a `k`-point `t` at the closed point of
`arc`;
(f) if `τ` is a deformation of `t` over the square-zero extension `k ⊕ M*`, constant in `Spec R`,
whose pull-back to `k[ε]` along `l : M` is constant only for `l = 0`, then `finrank k M ≤ d`.
Then `s` is smooth of relative dimension `d` on an open set through which `arc` factors. 
