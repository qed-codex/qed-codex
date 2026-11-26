---
{
  "module": "src/Lib/Weil/MixedModel/ZeroTerm.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Weil/MixedModel/ZeroTerm.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Weil/MixedModel/ZeroTerm.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Zero term and mixed model of the Weil representation: slices and θ as a sum of slices

This file works with a splitting (Witt decomposition) `D` of `V = (range l ⊕ range k) ⊥ ι V₀`.
A vector `f` of `𝒮 V` is applied to an adelic vector `x` through its theta function:
`f x = θ (ϱ(x) f)` (`New.Space.theta_rho`). The file defines the zero term ev = `D.zeroTerm` :
𝒮 V → 𝒮 V₀ and the slices f[x] = `D.slice x f` = ev(ϱ(l x) f), and proves that the slices obey
the mixed law. It shows that zero terms can be taken in stages and that the zero term depends only
on `ι` and the span of `k`. It studies families obeying the mixed law at adapted points, bounds
sums of slices over rational points and writes θ_V as the sum of θ_{V₀} over the slices.

## Main definitions and results

* `New.Space.Splitting.zeroTerm`: the zero term `𝒮 V → 𝒮 V₀`, the mean of `f (ι y + k b)` over
  `b ∈ 𝔸^p / E^p`; `New.Space.Splitting.slice x` is `D.zeroTerm ∘L V.ϱ (D.lAdelic *ᵥ x)`.
* `New.Space.Splitting.tsum_enorm_slice_le`, `New.Space.Splitting.hasSum_theta_slice`:
  over the rational points `ξ`, `∑_ξ ‖f[ξ]‖ ≤ M ‖f‖` and `θ_V f = ∑_ξ θ_{V₀} (f[ξ])`.
* `New.Space.Splitting.IsAdapted.slice_omega_vacElem`: for `g` adapted to `t`, the slices of
  ω(g) vac are a nonzero constant times `‖vacuumFn (tᴴ x)‖ ^ 2` times the vacuum of `V₀`. The case
  of any `g` when `V₀` is zero needs the Iwasawa decomposition and is
  `New.Space.Splitting.exists_slice_omega_vacElem_of_isEmpty`, in
  `Lib.SiegelWeil.Formula.LagrangianZeroTerms`.

Notions from other files:
* `New.Space`: a hermitian space with a point, given by a matrix J over E and x in GL_n(𝔸) with xᴴJx
  equal to diag(s) at the infinite places and 1 at the finite places.
* `New.𝒮`: The Banach space 𝒮(V) of integrable functions c on 𝔸^n with c(x) = ∫ c(y)β(y,x)e(x−y) dy,
  under the L¹ norm; β is the adelic bicharacter and e the vacuum function `New.vacuumFn`.
* `New.Space.Splitting`: A decomposition V = (lE^p ⊕ kE^p) ⊥ ιV₀ over E: isotropic frames l, k with
  l*Jk = 1, an isometry ι from V₀ orthogonal to both, and rk V = rk V₀ + 2p.
* `New.Space.Splitting.IsMixedLaw`: The law T x (ϱ(la + ιw + kb) f) = β(2x + a, b) ϱ(w) T (x + a) f
  of a mixed Schrödinger model, for maps `T x : 𝒮 V → 𝒮 V₀` with `x` in `𝔸^p`.
* `New.WeilData`: Weil data on a stably unramified E. They consist of ȷ in E with ȷ = −ȷ̄, Im τȷ > 0
  for every τ in the CM type and (1 − ȷ⁻¹)/2 integral; a finite idele α for which the completed
  integers Ô are self-dual under (z, u) ↦ ψ_f(ȷαᾱzu); and a splitting character υ equal to −1 at
  uniformisers of the places w with w = w̄.

## Relation to the literature

Known; see `Lib.Weil.MixedModel.ThetaInvariance` for sources.



## The zero term and the slices

The Heisenberg operators `V.ϱ y` and the unitary group (`V.ω g`) act on the Banach space `𝒮 V`.
`D.lAdelic`, `D.iAdelic`, `D.kAdelic` are the frames l, ι, k in adelic coordinates. `D.lCoord`,
`D.iCoord`, `D.kCoord` send `l a + ι w + k b` to `a`, `w`, `b`.


### `isContPeriodic_along_k`

 For a splitting, f in 𝒮(V) and an adelic vector y of V₀, the function b ↦ f(ιy + kb) on 𝔸^p
is continuous and periodic under E^p. 

### `exists_zeroTerm`

 The mean of `f (ι y + k b)` over `b ∈ 𝔸^p / E^p`, as a function of `y`, defines a bounded
linear map from `𝒮 V` to `𝒮 V₀`. 

### `zeroTerm`

 The zero term along k: the bounded map 𝒮(V) → 𝒮(V₀) with (ev f)(y) the mean of f(ιy + kb)
over b in 𝔸^p modulo E^p. Here f(x) = θ(ϱ(x)f) is the theta function of f. 

### `zeroTerm_apply`

 The zero term of f at y is the mean of f(ιy + kb) over b in 𝔸^p / E^p. 

### `zeroTerm_rho_kAdelic`

 For a Witt decomposition `D` of `V` with isotropic frame `k` and complement `V₀`, the zero term
`D.zeroTerm : 𝒮(V) → 𝒮(V₀)` averages the theta function of `f` over translates by `k 𝔸^p` modulo
`E^p`. It is unchanged when `f` is first moved by `V.ϱ` at `D.kAdelic *ᵥ x`, which is the vector
`k x` in standard coordinates, for every `x : p → 𝔸 E` (a vector of 𝔸^p). 

### `slice`

 The slice at x in 𝔸^p: the bounded map f ↦ f[x] = ev(ϱ(lx)f) from 𝒮(V) to 𝒮(V₀), where ev is the
zero term `New.Space.Splitting.zeroTerm`. 

### `isMixedLaw_slice`

 For a Witt decomposition `D` of `V` as `(l E^p ⊕ k E^p) ⊥ ι V₀`, the slices
`D.slice x : f ↦ f[x]` (x in 𝔸^p) satisfy the mixed Schrödinger law
`New.Space.Splitting.IsMixedLaw`: (ϱ(la + ιw + kb)f)[x] = ψ(½ȷ b*(2x + a)) ϱ(w) f[x + a], for x, a,
b in 𝔸^p, w an adelic vector of V₀ and f in 𝒮(V). Here the phase is the bicharacter `β (2 x + a) b`
of `adelicHeisenberg E 1`, and ȷ = −ȷ̄ is the element of E from the Weil data. 

 ## Zero terms in stages and independence of the splitting 

### `ratMap_mul_toAdele`

 The rational map of a matrix i carries the frame x₀⁻¹k of V₀, for a rational matrix k, to the
frame x⁻¹(ik) of V, where x and x₀ are the points of V and V₀. 

### `ratMap_mul_ratMap`

 The rational maps x⁻¹ i x₀ between spaces, formed with their points, compose like the matrices i
that define them. 

### `comp_kAdelic`

 The adelic frame k of a composite splitting consists of the frame k of the first splitting and
the image under its embedding ι of the frame k of the second. 

### `zeroTerm_comp`

 Zero terms can be taken in stages. For splittings `D` of V over V₀ and `D'` of V₀ over V₁, the
zero term of the composite splitting `D.comp D'` is the zero term of `D'` applied after that of `D`.
Here the zero term along `k` is the map 𝒮(V) → 𝒮(V₀) sending f to y ↦ the mean of θ(ϱ(ιy + kb) f)
over b ∈ 𝔸^p modulo E^p. 

### `kAdelic_mul_kCoord_mul_kAdelic`

 If the frame k′ of a second splitting D′ of V over V₀ has no l-coordinate in D and both
splittings read off the same V₀-coordinate, then k′ is spanned by k, with its k-coordinates in D as
coefficients. 

### `zeroTerm_congr`

 The zero term depends only on the embedding ι of V₀ and the span of the frame k. Two splittings
of V over V₀, with isotropic frames k and k′ (of possibly different index sets), have the same
zero-term map 𝒮(V) → 𝒮(V₀) if their embeddings of V₀ coincide and k*Jk′ = 0; given the first
condition, the second says that k and k′ span the same subspace. 


## Vacua and named finite data in the mixed model at adapted points

This section treats any family `T` of maps that obeys the law of a mixed Schrödinger model of a
splitting `V = l Eᵖ ⊕ V₀ ⊕ k Eᵖ` (`New.Space.Splitting.IsMixedLaw`), at a point `g` adapted to `t`
(`New.Space.Splitting.IsAdapted`). The slices `New.Space.Splitting.slice` are such a family.

* `New.Space.Splitting.IsAdapted.omega_projOn_adelic_of_isMixedLaw`: the values of `T` on a
  vector that is a vacuum above a set `S` of finite places and its conjugate.
* `New.Space.Splitting.IsAdapted.exists_omega_vacElem_of_isMixedLaw`: the law determines the values
  of `T` on ω(g) vac up to a constant.
* `New.Space.Splitting.IsAdapted.omega_schrodingerOp_of_isMixedLaw`: the datum named by `Ψ` becomes
  the datum named by the partial Fourier transform `New.Space.Splitting.sliceDatum` of `Ψ`.

`S.conjClosure` is the union of `S` and its conjugate, `idem S • x` the part of `x` above `S`,
`New.integralBox n S` the vectors integral on `S`, `New.finVec x` the adelic vector `(0, α x)`,
and `half` the finite adele `1/2`.


### `finFrameVector`

 The finite adelic vector g⁻¹(l t*⁻¹a + ιw + ktb), formed with the finite parts of the
matrices g⁻¹l t*⁻¹, g⁻¹ι and g⁻¹kt. 

### `sliceDatum`

 The function Ψ_x(y) = ∫ ψ_f(ȷαᾱ x*b_S) Ψ(g⁻¹(l t*⁻¹x + ιy + ktb)) db. The integral runs over
finite adelic b integral off S, b_S is the S-part of b, and Ô^p has mass one. Here ψ_f(ȷαᾱ ·) is
`selfDualAddChar E`, the character from the Weil data for which Ô is self-dual. 

 ### Coordinates in the frame at `g` 

### `adjoint_mulVec_finFrameVector`

 The adjoint of the frame recovers the three parts, with those along `l` and `k` exchanged. 

### `exists_eq_finFrameVector`

 Every finite adelic vector is given by its three parts in the frame. 

### `star_dot_finFrameVector`

 The hermitian product in the frame: the parts along `l` and `k` pair with each other. 

### `IsAdapted.finFrameVector_mem_integralBox`

 In an adapted frame, a vector is integral on `S` if and only if its three parts are. Here `g` is
adapted to `t` when the frame matrix g⁻¹(l t*⁻¹, kt, ι) has orthonormal columns at the infinite
places and integral finite entries. 

 ### The law at the finite places 

### `IsMixedLaw.apply_omega_rho_finFrameVector`

 The law of the mixed model for the translation by a finite vector with parts `a`, `w`, `b`:
`a` shifts the point `x`, `w` translates the value, and `b` gives the factor
`selfDualAddChar E (½ bᴴ (2 x + a))`. 

### `IsAdapted.omega_projOn_of_isMixedLaw`

 Let `P = V.projOn S` be the projection on the vacua above `S ∪ S̄` (the mean of the finite
Heisenberg operators over `Ô^n` above `S ∪ S̄`, with `S̄` the set of conjugate places), let `T` obey
the law of a mixed model, and let `g` be adapted to `t`. Then the value of `ω(g) P f` at the finite
point `x` vanishes unless `x` is integral on `S ∪ S̄`, and then it is `V₀.projOn S` applied to the
value at the part of `x` off `S ∪ S̄`. The value at a finite point `x` means the value of `T` at
`t⁻¹ᴴ (α x)`, with `α` the finite idele of the Weil data. 

### `IsAdapted.omega_projOn_adelic_of_isMixedLaw`

 For a splitting `D` of `V` as `(l E^p ⊕ k E^p) ⊥ ι V₀`, a set `S` of finite places, `g` adapted
to `t` (`g⁻¹ (l (t⁻¹)ᴴ, k t, ι)` has orthonormal columns at every infinite place and integral finite
entries) and `T` obeying the law of a mixed Schrödinger model (`D.IsMixedLaw`), let `F = ω(g) P f`,
where `P = V.projOn S` is the mean of the finite Heisenberg operators over `Ô^n` above `S ∪ S̄` and
`S̄` is the set of conjugate places. For an adelic point `y`, the value `T (t⁻¹ᴴ y) F` vanishes
unless the finite coordinate `α⁻¹ y_f` (`New.finCoord`) is integral at every place of `S ∪ S̄`. In
that case it equals `V₀.projOn S (T (t⁻¹ᴴ y') F)`, where `y'` is `y` with its finite part above
`S ∪ S̄` removed. 

### `IsAdapted.exists_omega_vacElem_of_isMixedLaw`

 Let `D` split `V` as `V₀ ⊥ (l E^p ⊕ k E^p)` via `ι`, let `g` be adapted to `t`
(`g⁻¹ (l (t⁻¹)ᴴ, k t, ι)` has orthonormal columns at every infinite place and integral finite
entries), and let `T` obey the mixed-model law `T x (ϱ y f) = β (2 x + a) b • ϱ w (T (x + a) f)` for
`y = l a + ι w + k b`. Then there is a constant `c` (possibly zero) such that for every adelic `x`,
`T x (ω(g) vacElem)` is `c * ‖vacuumFn (tᴴ x)‖ ^ 2` times the vacuum `vacElem` of `V₀`. Here
`vacElem` is the vacuum of `V` (Gaussian times twisted lattice indicator), and `vacuumFn y` is
`exp(−π ∑ Im(τȷ)|y_{i,τ}|²)` times `ψ_f(½c₀ȷ y_f*y_f)` when the finite part `y_f` lies in `αÔ^p`,
and `0` otherwise. 

### `IsAdapted.omega_schrodingerOp_of_isMixedLaw`

 Let `S` be disjoint from its conjugate `S̄`, `Ψ` Schwartz–Bruhat above `S` and `g` adapted to
`t`. The value of `ω(g) (Ψ ⊗ f)` at the finite point `x` is `Ψ_x ⊗` applied to the value of
`ω(g) P f` at the part of `x` off `S ∪ S̄`. Here `⊗` is `New.Space.schrodingerOp`, and
`P = V.projOn S` is the mean of the finite Heisenberg operators over `Ô^n` above `S ∪ S̄`.
`Ψ_x` (`sliceDatum`) is y ↦ ∫ ψ_f(ȷαᾱ x*b_S) Ψ(g⁻¹(l t*⁻¹x + ιy + ktb)) db over `b` integral off
`S`, with `α` the finite idele of the Weil data. The value at the finite point `x` means the value
of a map `T` obeying the law of a mixed model, taken at `t⁻¹ᴴ (α x)`. 


## Sums over rational points, θ as a sum of slices, and the slices of the vacuum

* `New.Space.Splitting.exists_tsum_slice_le`: a bound on `∑_ξ ‖f[φ ξ]‖` along any additive map
  `φ`. The bound is `#(φ⁻¹B) · M · ‖f‖`, with a compact `B` and a constant `M` that are independent
  of `φ` and `f`; it may be infinite.


### `exists_tsum_slice_le`

 There are a compact B in 𝔸^p and M such that, for every additive group homomorphism φ into 𝔸^p
and every f in 𝒮(V), ∑_ξ ‖f[φ(ξ)]‖ ≤ #(φ⁻¹B) · M · ‖f‖, where f[x] is the mixed model along the
splitting D. 

### `tsum_enorm_slice_le`

 There is M such that ∑_{ξ ∈ E^p} ‖f[ξ]‖ ≤ M‖f‖ for all f in 𝒮(V). 

### `hasSum_theta_slice`

 For a splitting `D` of `V` as `(l E^p ⊕ k E^p) ⊥ ι V₀` and f in 𝒮(V), the family θ_{V₀}(f[ξ]), ξ
in E^p, is summable with sum θ_V(f). Here f[ξ] = `D.slice ξ f` in 𝒮(V₀) is the zero term along `k`
of ϱ(lξ)f. 

### `zeroTerm_ne_zero`

 For a Witt decomposition `D` of `V` as `(l E^p ⊕ k E^p) ⊥ ι V₀` over a CM field `E` with Weil
data, the zero term along `k` is not the zero map. This zero term is the bounded map 𝒮(V) → 𝒮(V₀)
sending `f` to `y ↦` the mean of `θ(ϱ(ιy + kb) f)` over `b` in 𝔸^p modulo E^p. 

### `IsAdapted.slice_omega_vacElem`

 Let `D` be a Witt decomposition `V = (l E^p ⊕ k E^p) ⊥ ι V₀` over a CM field `E` with Weil data.
Suppose `g` is adapted to `t` (`New.Space.Splitting.IsAdapted`): the columns of
`g⁻¹ (l (t⁻¹)ᴴ, k t, ι)` are orthonormal at every infinite place and have integral finite entries.
Then for `f = ω(g) vacElem` there is `c ≠ 0` such that, for every `x` in 𝔸^p, the slice (mixed
model) of `f` at `x` is `c * ‖vacuumFn (tᴴ x)‖ ^ 2` times the vacuum of `V₀`, where `vacuumFn` is
the standard adelic vacuum (Gaussian at the infinite places, twisted lattice indicator at the finite
places). 

### `IsAdapted.slice_omega_eq_integral`

 The mixed model as an integral. Let `g` be adapted to `t`, and for an adelic vector `y` write
`g y = l a + ι w + k b`. There is `c ≠ 0` such that, for all `f` and `x`, the value `(ω(g) f)[x]`
is `c` times the integral over `y` of the coefficient `⟨ϱ(y) vac, f⟩`, times
`β (2 x + a) b * ‖vacuumFn (tᴴ (x + a))‖ ^ 2`, times the translate by `w` of the vacuum of `V₀`.
Here `β` is the bicharacter of `adelicHeisenberg E 1`. The middle factor is the value at `x` of the
translate by `l a + k b` of the function `‖vacuumFn (tᴴ ·)‖ ^ 2` in the Schrödinger model. 
