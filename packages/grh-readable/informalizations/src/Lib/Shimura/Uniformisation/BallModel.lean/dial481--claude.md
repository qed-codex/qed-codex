---
{
  "module": "src/Lib/Shimura/Uniformisation/BallModel.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Shimura/Uniformisation/BallModel.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Shimura/Uniformisation/BallModel.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Period signatures, analytic families of theta tori and the ball chart of moduli points

Φ v denotes the embedding E → ℂ that the CM type chooses at the infinite place v, and v₀ is the base
infinite place fixed by `New.CMBase`. Theta tori that vary analytically with a parameter b in a
domain of ℂⁿ⁻¹, all uniformised by one fixed space V, form analytic families. Near each b₀, their
theta coordinates become analytic after a common factor c(b) ≠ 0. For a fixed frame, the positive
lines form a ball, and the moduli points with this frame are the points of a single analytic family
over that ball.

## Main definitions and results

* `New.ThetaTori.PeriodMap.isSignedFrameFor`: the sign condition on the matrix of a polarised period
  map.
* `New.Variety.AnalyticFamily`: a family of theta tori, with periods Q_b analytic in b and with
  B(Q_b ·, ·) independent of b.
* `New.Variety.AnalyticFamily.exists_analytic_thetaCoord`: near b₀, after a common factor c(b) ≠ 0,
  the theta coordinates are analytic in (b, z).
* `New.Variety.positiveBall`, `New.Variety.exists_ball_chart`: the positive lines, in coordinates
  ℂ × ℂ^(n−1); the set is star-convex, hence connected.
* `New.Variety.ballPeriod`: an explicit period map (E ⊗ ℝ)ⁿ → `New.Variety.BallFibre`, affine in the
  point.
* `New.Variety.exists_analyticFamily_positiveBall`: the ball carries an analytic family
  `New.Variety.AnalyticFamily` with these periods and the reflections `New.Variety.formReflection`.
* `New.Variety.IsBallFamily`, `New.Variety.exists_isBallFamily`: the points with the frame of a
  given point o are the points `New.Variety.AnalyticFamily.ballPoint` of one analytic family. An
  isomorphism z in GL_n(E) from a translate o·(g, α) to o acts on the parameters near 0 by a linear
  map K, and its local term, a complex polynomial p (`New.Variety.localTerm`), satisfies
  p(t) = p(0)·det(1 − tK) for all t in ℂ.

Notions from other files:
* `New.Variety.IsSignedFrameFor` g ℓ β: the adelic matrix `g` is a frame for the matrix `β` over E,
  the matrix `β.map (Φ w)` is positive definite for every infinite place `w ≠ v₀`, and
  `β.map (Φ v₀) * ℓ` is positive definite.
* `New.Variety.IsPeriodMap` ℓ Q: Q carries iℓ at v₀ and i at the other places to multiplication by
  i.
* `New.Variety.BallBase`: The complex vector space ℂ^(n−1), which contains the parameter domains of
  the families of periods.
* `New.Variety.RealVectors`: The space (E ⊗ ℝ)ⁿ, written as n-tuples of elements of the product of
  copies of ℂ over the infinite places of E.
* `New.Variety.BallFibre`: The complex space (ℂ × ℂ^(n−1)) × ∏_{v ≠ v₀} ℂⁿ, the common target of the
  period maps of a family.

## Relation to the literature

Known; see `Lib.Shimura.Uniformisation.AppellHumbert` for sources.



## The signature of the hermitian matrix of a polarised period map

The matrix `β` over `E` of a polarised period map (`New.ThetaTori.PeriodMap`) for the frame `g` and
the complex matrix `ℓ` satisfies the sign condition `New.Variety.IsSignedFrameFor g ℓ`.


### `New.ThetaTori.PeriodMap.isSignedFrameFor`

 The matrix `β` of a polarised period map for `(g, ℓ)` has `g` as a frame (`gᴴ β g` is a
scalar matrix, a unit of `Ẑ`), `Φ v β` is positive definite for every infinite place `v ≠ v₀`,
and `Φ v₀ β * ℓ` is positive definite (hermitian in particular). 


## Analytic families of theta tori and analytic theta coordinates

A theta torus (`New.ThetaTori.ThetaTorus`) has a period map Q onto V, a form B and lattices
`New.ThetaTori.PeriodMap.latticeOver` S. Its theta functions for the lattice over S = `D.lagrangian`
are the multiples of one function, chosen for each b with no regularity in b, and
`New.ThetaTori.PeriodMap.thetaCoord` lists its normalised translates by t ∈ T. The factor c(b)
replaces the chosen function by a Poincaré series (`New.IsAppellHumbert.poincareSeries`), which does
depend analytically on b.


### `AnalyticFamily`

 A family of theta tori with fixed frame g over a parameter domain U = `domain` in ℂ^(n−1). The
periods are analytic, and their differential is injective modulo ℂ-linear maps. The matrix β and the
forms B(Q·, ·) are constant, and Re B is positive definite. 

### `AnalyticFamily.domain`

 The parameter domain, an open subset of ℂⁿ⁻¹. 

### `AnalyticFamily.isConnected`

 The domain is non-empty and connected. 

### `AnalyticFamily.frame`

 The adelic frame g, the same for all members of the family. 

### `AnalyticFamily.reflection`

 The reflection J_b attached to the parameter b. 

### `AnalyticFamily.torus`

 The theta torus of the point (g, J_b), with period map Q_b onto the fixed space
  V = `New.Variety.BallFibre`. 

### `AnalyticFamily.analyticAt`

 For each vector w, the period b ↦ Q_b w is analytic at every point of the domain. 

### `AnalyticFamily.eq_zero_of_linear`

 On the domain, the derivative of Q in the direction v is complex linear for the complex
  structure given by Q_b only if v = 0. 

### `AnalyticFamily.form_const`

 The matrix β over E and the complex linear forms B(Q_b w, ·) on V do not depend on b. 

### `AnalyticFamily.re_pos`

 For every b, the real part of B(u, u) is positive for u ≠ 0. 

### `eventually_isUnit_of_analyticAt_of_apply_ne_zero`

 Let `c b • φ b` be a family of functions whose value at `(b, z)` is analytic in `(b, z)` at
`(b₀, w)` and nonzero there. Then `c b` is a unit for all `b` near `b₀`. 

### `AnalyticFamily.exists_analytic_thetaCoord`

 Let f be an analytic family of theta tori, b₀ in its domain, and θ_t(b, ·) (t ∈ T) the theta
coordinates of the member b, functions on V. There is a function c of b such that
(a) for each t, the function (b, z) ↦ c(b)·θ_t(b, z) is analytic at every point (b₀, z);
(b) c(b) ≠ 0 for b near b₀.
The factor is the same for all t and z, so the projective point (θ_t(b, z))_t is unchanged. 


## The ball chart of moduli points with a given frame

A point `New.Variety.ModuliPoint` is a triple (x, ℓ, P): an adelic frame x, a line in ℂⁿ, recorded
as the reflection ℓ that fixes it, and vectors P_i in (E ⊗ ℝ)ⁿ. For fixed x the frame determines a
form β, and the lines that occur are those positive for H = Φ_{v₀}(β); they form a ball in ℂ^(n−1).


### `ballPeriod`

 For a continuous linear isomorphism e : ℂⁿ ≃ ℂ × ℂ^(n−1) and a complex matrix H, the map,
ℂ-linear in q = (q₁, q') and ℝ-linear in w, with value ((e⁻¹q)ᵀHw₀, q₁y₂ − y₁q', (q₁w_v)_{v≠v₀}),
where w₀ = w_{v₀} and (y₁, y₂) = e(w̄₀). 

### `positiveBall`

 The set of b in ℂ^(n−1) such that x = e⁻¹(1, b) in ℂⁿ is positive for H, that is, Re ∑ x_i
H_ij conj(x_j) > 0. 

### `formReflection`

 The matrix of w ↦ 2(uᴴHw)/(uᴴHu)·u − w; if uᴴHu ≠ 0 it fixes u and is −1 on the w with
uᴴHw = 0. 

### `exists_eq_formReflection`

 If H is Hermitian, J is a reflection (J = u wᵀ − 1 for vectors u, w with w ⬝ᵥ u = 2) and HJ is
positive definite, then J is the reflection for the form H in a vector u with uᴴHu > 0. 

### `re_form_lt_of_mem_positiveBall`

 Write `H(a, c) = star a ⬝ᵥ H *ᵥ c`. Let `H` be Hermitian, negative definite on the
hyperplane `(e (star y)).1 = 0` and positive at `star x`, `x = e.symm (1, b)`. Then
`re H(y, y) < 2 re (s * H(star x, y))` for `y ≠ 0`, where `s = (e (star y)).1`. 

### `ballFormAt`

 The form at the infinite place v from which `exists_form_along_ballPeriod` builds its form: the
map (w, p) ↦ 2π Im Φ_v(ξ) · F_v(w, p), ℝ-linear in w ∈ (E ⊗ ℝ)ⁿ and ℂ-linear in p ∈ `BallFibre`,
where F_{v₀}(w, p) = (e(w̄_{v₀}))₁ p₁₁ − (e⁻¹(p₁ − p₁₁ (1, 0)))ᵀ H w_{v₀}, p₁ ∈ ℂ × ℂ^(n−1) being
the first component of p and p₁₁ its first coordinate, and F_v(w, p) = w̄_vᵀ Φ_v(β) p₂(v) for v ≠
v₀. 

### `ballFormAt_ballPeriod`

 The value of `ballFormAt e H β v` at w = y on the periods P_b z = `ballPeriod E e H (1, b) z`:
2π Im Φ_v(ξ) times, at v = v₀, s_y H(x, z) + s_z H(x, y) − H(z̄, y), where y and z stand for
y_{v₀} and z_{v₀}, x = e⁻¹(1, b), s_y = (e(ȳ_{v₀}))₁ and H(a, c) = aᵀ H c; and times
ȳ_vᵀ Φ_v(β) z_v at v ≠ v₀. 

### `exists_form_along_ballPeriod`

 Riemann relations along the periods. Assume `IsSignedFrameFor g ℓ β`: `g` is a frame for `β`,
`β` is positive definite at every place `w ≠ v₀`, and `Φ v₀ β * ℓ` is positive definite. Let
H = Φ_{v₀}(β) be negative definite on the y ≠ 0 with `(e (star y)).1 = 0`. Write
P_b = `ballPeriod E e H (1, b)` for the period map at b ∈ ℂ^(n−1). Then some A(w, p), ℝ-linear in
w ∈ (E ⊗ ℝ)ⁿ and ℂ-linear in p ∈ `BallFibre E D.Index`, has: (a) Re A(w, P_b w) > 0 for b in
`positiveBall e H`, w ≠ 0; (b) A(y, P_b z) − A(z, P_b y) = 2πi · `polarisationForm D β` y z, which
equals 2πi ∑_v 2 Re(Φ_v(ξ) z̄_vᵀ Φ_v(β) y_v), for all b; (c) A(c y, P_b z) = A(y, P_b (c̄ z)) for c
in E acting through the CM embedding. 

### `_root_.Set.Nonempty.exists_retraction`

 A nonempty set `S` is the range of a map `r` that fixes every point of `S`. 

### `injective_of_re_pos`

 A real linear map `P` from (E ⊗ ℝ)ⁿ to the fibre `New.Variety.BallFibre` is injective if a form
`A` has Re A(w, P w) > 0 for every w ≠ 0. 

### `re_comp_symm_apply_self_pos`

 If a form `A` has Re A(w, P w) > 0 for every w ≠ 0 and the real isomorphism `Q` agrees with
`P`, then the form B = A ∘ Q⁻¹ on the fibre has Re B(u, u) > 0 for every u ≠ 0. 

### `hasFDerivAt_ballPeriod`

 The period b ↦ `ballPeriod E e H (1, b) w` is affine in b; its derivative is v ↦
`ballPeriod E e H (0, v) w`. 

### `finrank_realVectors_eq_finrank_ballFibre`

 The real vector spaces (E ⊗ ℝ)ⁿ and `New.Variety.BallFibre E D.Index` have the same
dimension. 

### `isPeriodMap_formReflection_of_apply_eq_ballPeriod`

 Let x = e⁻¹(1, b) have xᵀHx̄ ≠ 0, and let the real isomorphism `Q` agree with
`New.Variety.ballPeriod` at (1, b). Then `Q` is a period map (`New.Variety.IsPeriodMap`) for the
reflection `New.Variety.formReflection` for H in x̄. 

### `exists_analyticFamily_positiveBall`

 Let `positiveBall e H` (the b with x = e⁻¹(1, b) satisfying Re ∑ x_i H_ij x̄_j > 0) be
connected. Let H = β.map (Φ v₀) be negative on the y ≠ 0 with (e ȳ).1 = 0, and let g be a frame for
β with β.map (Φ w) positive definite for every infinite place w ≠ v₀ and H * ℓ positive definite
(`IsSignedFrameFor g ℓ β`). Then some analytic family has domain `positiveBall e H` and frame g, and
at each b its reflection is `formReflection H u` for u = conj e⁻¹(1, b), and the period map of its
torus is `ballPeriod E e H (1, b)`: ℂ-linear in q, ℝ-linear in w, with value ((e⁻¹q)ᵀHw₀,
q₁y₂ − y₁q', (q₁w_v)_{v≠v₀}), where (y₁, y₂) = e(w̄₀). 

### `exists_ball_chart`

 If H is hermitian and a = ūᵀHu > 0, there are linear coordinates e : ℂⁿ ≅ ℂ × ℂ^(n−1) with
a·e(y)₁ = yᵀHu and e(ū) = (1, 0). In these coordinates the b for which x = e⁻¹(1, b) has Re xᵀHx̄ >
0 form a set star-convex at 0. 

### `exists_charpoly_roots_eq_erase`

 An endomorphism Y of K × Kⁿ that preserves both factors and acts by ν on the first is ν ⊕ N, and
the characteristic roots of N are those of Y with one copy of ν removed. 

### `AnalyticFamily.ballPoint`

 The point of an analytic family f at p = (b, z): it has the frame of f, the reflection of the
member b, and the vectors Q_b⁻¹(z_i) + P_i, where Q_b is the period map of the member b. 

### `AnalyticFamily.heckeTranslate`

 The Hecke translate of an analytic family by a similitude γ: it has the frame gγ, the same
domain, reflections and period maps, and the matrix β and each form B are multiplied by the positive
rational c with γᴴ(c·1)γ a unit of Ẑ, that is, by the inverse of the rational similitude factor of
γ. 

### `AnalyticFamily.exists_ballPoint_eq`

 Let `f` be an analytic family whose frame `f.frame` has the sign condition for the matrix `β`
and some complex matrix `ℓ` (only `β` is used afterwards) (`hβ`), let `H = Φ_{v₀}(β)` be negative
definite on the vectors `y ≠ 0` with `(e (star y)).fst = 0` (`hneg`), let the domain of `f` be
`positiveBall e H` (`hU`), and let its reflection at `b` be the reflection for `H` in
`star (e.symm (1, b))` (`hℓ`). Then every moduli point `a` with frame `f.frame` is the point
`f.ballPoint 0 p` for some `p` whose first coordinate lies in the domain. 

### `fibreEnd`

 The action on the fibre (ℂ × ℂ^(n−1)) × ∏_{v ≠ v₀} ℂⁿ = `New.Variety.BallFibre` that matches a •
z on periods, for z in GL_n(E) with eigenvalue μ at v₀, the block `N` of its entrywise conjugate in
the ball chart and a in E: multiplication by Φ_{v₀}(a)μ, by the conjugate of Φ_{v₀}(a) times `N`,
and by Φ_v(a)Φ_v(z) at each place v ≠ v₀. 

### `ballEnd`

 The linear map on the coordinates (b, (z_i)_i) of points near the base point of a ball family
that an isomorphism z with eigenvalue μ and block `N` induces: (μ̄)⁻¹N on b, and
`New.Variety.fibreEnd` at α i on z_i. 

### `det_one_sub_smul_ballEnd`

 The map 1 − t·`ballEnd μ N z α` is block diagonal, so its determinant is the product of the
factors 1 − tλ over the eigenvalues λ of its blocks: (μ̄)⁻¹ times the roots of `N`; and for each i,
Φ_{v₀}(α i)μ, the conjugate of Φ_{v₀}(α i) times the roots of `N`, and Φ_v(α i) times the roots of
the characteristic polynomial of z at each place v ≠ v₀. 

### `eval_localTerm_eq_mul_det`

 Let μ be the j-th root (`New.Variety.numberedRoots`) under Φ_{v₀} of the separable
characteristic polynomial P of z, let every root r of P under Φ_{v₀} have r·r̄ = μ·μ̄, and let the
roots of `N` be those of P under the conjugate of Φ_{v₀} with one copy of μ̄ removed. Then the
polynomial p = `New.Variety.localTerm` α P j satisfies p(t) = p(0)·det(1 − t·`ballEnd μ N z α`). 

### `IsBallFamily`

 An analytic family f around the point o, with A p = `f.ballPoint o.markedPoint p` its point at p
with the vectors of o: A 0 = o, f meets every point with the frame of o, and an isomorphism from a
translate of o to o acts linearly on the parameters near 0, with a determinant formula for its local
term. 

### `IsBallFamily.zero_mem`

 The domain of the family contains the parameter `0`. 

### `IsBallFamily.ballPoint_zero`

 At `0` the family passes through `o`. 

### `IsBallFamily.exists_ballPoint_eq`

 Each point with the frame of `o` is the point of `f` at some p with p.1 ∈ f.domain and vectors
  0. 

### `IsBallFamily.exists_linear_isLevelIso`

 If z : o·(g, α) ≅ o at level `levelGU D.Index D.level` has separable characteristic polynomial
  and the reflection of o is `markedReflection z j`, some linear map K has z : A(q)·(g, α) ≅ A(Kq)
  for q near 0, where A(q) = `f.ballPoint o.markedPoint q`, and p(t) = p(0)·det(1 − tK) for
  p = `localTerm α z.val.charpoly j`. 

### `exists_isBallFamily`

 Every moduli point `o` (a finite adelic frame, a reflection `J` and marked vectors) has a ball
family: an analytic family of theta tori `f` whose point at parameter 0, with the marked vectors of
`o`, is `o`. The family passes through every moduli point having the same frame as `o`, and an
isomorphism from a translate of `o` to `o` acts linearly on its parameters near 0
(`New.Variety.IsBallFamily`). 
