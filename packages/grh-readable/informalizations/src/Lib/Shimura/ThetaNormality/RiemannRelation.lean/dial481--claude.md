---
{
  "module": "src/Lib/Shimura/ThetaNormality/RiemannRelation.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Shimura/ThetaNormality/RiemannRelation.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Shimura/ThetaNormality/RiemannRelation.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Riemann's theta relation and the reduction of theta functions at a valuation

Theta functions `θ_s = x.thetaCoord s` (`s ∈ D.dualTorsion`) of a theta torus
`x : New.ThetaTori.ThetaTorus` and their reduction at a valuation `v` of `ℂ`.

* `New.ThetaTori.ThetaTorus.isCutOutAt_reduction`: under good reduction, the ideal of the reductions
  of all theta vectors `(θ_s z)_s` has the expected ranks and is cut out by the level points.
* `New.ThetaTori.ThetaTorus.riemann_relation`: Riemann's theta relation of degree `D.paddedNorm` in
  one variable.
* `New.ThetaTori.ThetaTorus.exists_forall_valuation_thetaCoord_zero_le`: each `s` is `u + (s - u)`
  with theta constants of largest valuation.
* `New.ThetaTori.ThetaTorus.IsRiemannTuple`, `New.paddingTuple`: the systems of coefficients
  used in Riemann's relation.

Conventions: `x.torsionLift s` is a chosen lift of the torsion class `s`, `x.latticeOver S` the
lattice over a group `S` of classes, `x.intAction a` multiplication by `a ∈ 𝓞 E`, `x.multiplier` the
multiplier χ of the `θ_s`, and e(t) = exp(2πi t); `IsIntegralCoords w p` says that `p` are integral
homogeneous coordinates of a complex vector `w`, one of them a unit.

Notions from other files:
* `New.ThetaTori.ThetaTorus`: a polarised period map to `V`, with reflection matrix `ℓ`, such that
  multiplication by `star a` is adjoint to multiplication by `a ∈ 𝓞 E` for the form
  `x.automorphyForm`. In suitable coordinates `a` acts on `V` diagonally, through the complex
  embeddings of `E`.
* `New.ThetaTori.PeriodMap.thetaCoord`: The theta coordinate `θ_t`, `t ∈ T`: the normalised
  translate (`New.ThetaTori.normalizedShift`) of
  `New.ThetaTori.PeriodMap.exists_generator_thetaSpace` by the chosen lift `a_t` of `t`.
* `New.RealComplexForm.thetaShift` B a: the twisted translation f ↦ (z ↦ exp(−B(a,z) − B(a,a)/2)
  f(z + a)).
* `New.ThetaTori.LatticeForm.thetaNorm`: the supremum over torsion points x of the sizes
  `New.ThetaTori.LatticeForm.sizeAt` v(exp(−B(x,x)/2) f(x)). `New.ThetaTori.HasGoodReduction` asks,
  for an ample type on the lattice L, that this norm be multiplicative, that r > 1 and v(r) = 1, and
  that some N with v(N) = 1 multiply the dual lattice into L.

## Relation to the literature

Known result: Normal generation of sections on abelian varieties, kept under good reduction. Only
degrees that are powers of one integer r are treated, over a rank-one valuation ring of the complex
numbers, where powers of the sup-norm ball of theta functions are the balls and reduction keeps the
ranks. No cohomology or vanishing theorem is used. Source: S. Koizumi, Theta relations and
projective normality of abelian varieties, Amer. J. Math. 98 (1976); T. Sekiguchi, J. Math. Soc.
Japan 29 (1977) for characteristic p; G. Kempf, Multiplication over abelian varieties, Amer. J.
Math. 110 (1988).

Known result: Riemann's theta relations. Here they are stated in one variable for the theta
coordinates of a PEL torus, with multipliers in the ring of integers of a CM field in place of the
matrix with entries ±1/2. They are proved by Schur orthogonality for the theta group. Source: C.-L.
Chai, Riemann's theta formula (2014), Theorem 1.2; A. Nagano, On Riemann type relations for theta
functions on bounded symmetric domains of type I, arXiv 2301.09243 (2023), Theorem 1.1; D. Mumford,
On the equations defining abelian varieties I, Invent. Math. 1 (1966) §3; G. Kempf, Linear systems
on abelian varieties, Amer. J. Math. 111 (1989) 65–94.


### `instance : Module (𝓞 E) D.dualTorsion`

 The ring of integers `𝓞 E` acts on the torsion group `D.dualTorsion`: the action of `𝓞 E` on
adelic torsion classes preserves `D.dualTorsion`. 

 ### Systems of coefficients 

### `IsRiemannTuple`

 The pairs `p l = (a_l, b_l)` in `𝓞 E` satisfy `∑ ā_l a_l = r` and `∑ ā_l b_l = 0`, where
`r = D.paddedNorm` is the degree attached to the PEL datum `D` and `ā` is the complex conjugate
(`star`). 

### `IsRiemannTuple.sum_star_fst_mul_fst`

 For a Riemann tuple `p` with `p l = (a_l, b_l)`, `∑ ā_l a_l = D.paddedNorm`. 

### `IsRiemannTuple.sum_star_fst_mul_snd`

 For a Riemann tuple `p` with `p l = (a_l, b_l)`, `∑ ā_l b_l = 0`. 

### `doubledCoeffs`

 The family of coefficient pairs on two copies of the index set `K`: `(0, b_l)` on the first
copy, where `k l = (a_l, b_l)`, and `p l` on the second. 

 ### Products of theta functions and Riemann's relation 

### `thetaProduct`

 The function `z ↦ ∏_k θ_{μ_k}(a_k z + b_k w)` on `V`, where `p k = (a_k, b_k)`, `θ_s` is the
theta coordinate `x.thetaCoord s` and `x.intAction a` is multiplication by `a ∈ 𝓞 E` on `V`. 

### `thetaShift_thetaProduct`

 Let `p k = (a_k, b_k)` with `∑ ā_k a_k = r` and `∑ ā_k b_k = 0` (`hp`), let `∑ ā_k μ_k = t`
(`ht`), and let `y` lie in the lattice over `D.dualTorsion`. Write `x.thetaProduct p μ w` for the
function `z ↦ ∏_k θ_{μ_k}(a_k z + b_k w)`, where `θ_s` is `x.thetaCoord s`. If the twisted
translation (`New.RealComplexForm.thetaShift`) by `a_k u` sends `θ_{μ_k}` to
`χ(a_k u) e(⟨a_k y, μ_k⟩) θ_{μ'_k}` for every `k`, then the twisted translation by `u` for `r B`
sends `x.thetaProduct p μ w` to `χ(u)^r e(⟨y, t⟩)` times `x.thetaProduct p μ' w`. Here `χ` is
`x.multiplier`, and `e(⟨y, s⟩)` (`riemannPhase`) is `exp(2πi E(y, ·))` of the chosen lift of `s`,
with `E` the Riemann form of `B = x.automorphyForm`, and `r` is `D.paddedNorm`. 

### `thetaShift_periodPoint_thetaProduct`

 Translation by a rational point shifts the indices of a theta product. Let `y` be a rational
vector whose class `[y]` lies in `D.dualTorsion` (`hy`), let `u = x.periodPoint y` be its image in
`V`, and let `p` be a Riemann tuple (`hp`). Then the twisted translation by `u` for `r B` sends
`x.thetaProduct p μ w` to `χ(u)^r e(⟨β u, ∑ ā_k μ_k⟩)` times the product for `μ + a [y]`, where `χ`
is `x.multiplier`, `β = D.rescaledBeta ∈ 𝓞 E`, for which `β u` lies in
`x.latticeOver D.dualTorsion`, `p k = (a_k, b_k)`, `r = D.paddedNorm` and
`B = x.automorphyForm`. 

### `riemann_relation`

 Riemann's theta relation in one variable. Here x is a theta torus on V for the PEL datum `D`.
T = `D.dualTorsion` is the finite group of classes pairing trivially with all integral vectors, r =
`D.paddedNorm` ≥ 3, and T[r] = `D.rTorsion` is the r-torsion of T. For a tuple p = (a, b) with
values in 𝓞 E, `x.thetaProduct p μ w` is P(μ; z) = ∏_k θ_{μ_k}(a_k z + b_k w), where θ_s =
`x.thetaCoord s`.

Let p = (a, b) satisfy ∑ ā a = r, ∑ ā b = 0 (`hp`) and ∑ ā μ = t. Let q = (a', b') satisfy the same
with μ' in place of μ, and write P' for the product attached to q. Then |T| P'(μ'; 0) P(μ; z) = √[T
: T[r]] ∑_{s ∈ T} P(μ − a s; 0) P'(μ' + a' s; z), with both products taken at the same point w. 

### `valuation_thetaCoord_le_of_le_inf`

 Let `θ_o(0)` have the largest valuation among the theta constants `θ_t(0)` (`ho`), and let that
valuation be at most those of `θ_{s-u}(0)` and `θ_{-u}(0)` (`h_best`). Then each of `θ_u(0)`,
`θ_{-u}(0)`, `θ_{s-u}(0)` has the largest valuation. 

### `mul_sizeAt_le_inf_mul_thetaNorm_pow`

 The bound on the values of the size function in the proof of
`exists_forall_valuation_thetaCoord_zero_le`. Let `r = D.paddedNorm = k + 3` and `v |T| = 1` (`hv`),
let `θ_o(0) ≠ 0` have the largest valuation `top` among the theta constants (`ho`), and let `u`
maximise `min (v θ_{s-t}(0)) (v θ_{-t}(0))` over `t`, with maximum `best` (`hu`). If every
`v θ_t(z)` is at most `v (exp (B(z, z) / 2)) ρ` (`h_le`), `ρ` the norm of `θ_0`, then at each
torsion point `z` the product of the sizes (`New.ThetaTori.LatticeForm.sizeAt`) of `θ_s`,
`θ_{r o - s}` and `θ_0 ^ (k + 1)`, times `top`, is at most `best ρ ^ r`. The proof applies Riemann's
relation and the ultrametric inequality. Here `T = D.dualTorsion` and `B = x.automorphyForm`. 

### `exists_forall_valuation_thetaCoord_zero_le`

 Under good reduction at `v` (`h_good`, see `New.ThetaTori.HasGoodReduction`) and
`v |T| = 1` (`hv`), for every `s` in `T = D.dualTorsion` there is `u` such that each of the theta
constants `θ_u(0)`, `θ_{-u}(0)`, `θ_{s-u}(0)` has the largest valuation among all `θ_t(0)`. So `s`
is both a sum `u + (s - u)` and a difference `(s - u) - (-u)` of such indices. 

### `surjective_map_homogeneous`

 Along a surjective ring map `φ : A →+* B`, every form of degree `d` over `B` is the image of a
form of degree `d` over `A`: mapping coefficients by `φ` is surjective on homogeneous
polynomials of degree `d`. 

### `IsSmallForm`

 A form `f` of degree `r ^ j` in the theta coordinates is small at the chart `c` if the theta
function `f(θ)` has norm (`New.ThetaTori.LatticeForm.thetaNorm` at `v` for `r ^ j • B`) below
`‖θ_c‖ ^ (r ^ j)`, the norm of `θ_c ^ (r ^ j)`. Here `r = D.paddedNorm` and
`B = x.automorphyForm`. 

### `range_aeval_thetaCoord_eq_normBall`

 Under good reduction, the forms of degree `r ^ j` in the theta coordinates with integral
coefficients give exactly the norm ball of `θ_c ^ (r ^ j)`: the theta functions of `r ^ j • B` with
norm at most that of `θ_c ^ (r ^ j)` (`h_good.pow j` is good reduction for `r ^ j • B`). Here
`r = D.paddedNorm` and `B = x.automorphyForm`. 

### `isSmallForm_iff_forall_eval_map_eq_zero`

 Smallness is read off from reductions at points that represent the dual lattice. Let `x` have
good reduction at `v` (`h_good`) and let `φ` map the valuation ring of `v` onto a field `k`. Let the
points `a b` represent the dual lattice of `r ^ j • B` modulo `x.periodLattice` (`ha`), and let
`p b` be integral coordinates of the theta vector at `a b` (`hp`). Then a form `f` of degree
`r ^ j` is small at `c` iff its reduction by `φ` vanishes at every point `φ ∘ p b`. Here
`r = D.paddedNorm` and `B = x.automorphyForm`. 

### `isSmallForm_iff_forall_eval_map_eq_zero_of_ne_zero`

 Smallness is read off at the points of the chart `c`. Under good reduction (`h_good`), with
`φ` onto a field and `q z` integral coordinates of the theta vector at every `z ∈ V` (`hq`), a
form `f` of degree `r ^ j` is small at `c` iff its reduction vanishes at each point `φ ∘ q z`
whose coordinate `c` is nonzero. Here `r = D.paddedNorm`. 

### `isCutOutAt_reduction`

 Under good reduction at `v` (`h_good`), with `φ` onto a field `k`, `q z` integral coordinates of
the theta vector `(θ_s(z))_s` at every `z ∈ V` and `p l` those at the lift of each level point `l`:
if each `N l` has the coordinates `φ ∘ p l` at `t`, then `N` cuts out at `t` the reduced vectors
`φ ∘ q z` (`New.Variety.ThetaNull.IsCutOutAt`). That is: in all charts of the `N l` at `t` and each
chart `c`, the ideal of those vectors with `c`-coordinate ≠ 0, scaled to 1, satisfies
`IsCutOut D.paddedNorm D.exponentBound` with ranks `thetaRanks D.dualTorsion D.paddedNorm` (the
dimensions of the theta spaces of `r ^ j • x.automorphyForm`; for `j ≤ D.exponentBound` the level
points `D.levelTorsion` represent its dual lattice mod `x.periodLattice`) for the affine coordinates
of the `N l` at `t`. Here `r = D.paddedNorm`. 

### `_root_.New.paddingTuple`

 The family of coefficient pairs in `𝓞 E` consisting of `(1, 0)` twice (on the first copy of
`Bool`), `(c, 1)` and `(1, −c̄)` (at `true` and `false` of the second copy), and `(a l, 0)` for
every `l : K`. 
