---
{
  "module": "src/New/UpperBound/Divisibility/ValuationAtLevel.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/Divisibility/ValuationAtLevel.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/Divisibility/ValuationAtLevel.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# N-adic valuation of the lifts between the X_j at the level prime N

This file bounds how many powers of `N` the lifts between the `X_j` lose at the level prime `p = N`.
It first bounds the values of the lift characters at `N` and the loss of the direct datum on the
standard lattices. The lifts with data at `Σ_N` obey the rules of `IsSplitLevel.LiftLaw`. So on
ramified source forms the chain of glued double lifts is a scalar of bounded valuation times the
chain of direct lifts after `Up ^ (m / 2)`. Each direct lift loses at most `f b` powers of `N`. The
main result is that on ramified source forms `φ` with `Up ^ (m / 2) φ` integral for `L_0`, the
composite lift loses at most `2 m f b` powers of `N`.

Notions from other files:
* `Σ_N` is `D.nonInducedPlaces`, the places above `N` conjugate to the induced places;
* `diagN n S` is `diag (1, …, 1, N)` at the places in `S` and `1` at the others, and
  `δ_j = D.diagPointN j` is this matrix on `X_j` for `S` the set `D.piNPlaces` of places dividing
  `π`. It takes the standard lattice to `L_j` at `Σ_N`: if `e` is the last standard basis vector,
  the last vector of the basis of `L_j` is `N e` or `e` at each place, a unit times `π e`. The unit
  is the same for all `j`, and the direct datum and `Up` do not depend on it;
* `ιₚ` is the chosen embedding of `ℂ` into `ℂ_N`, and `D.chainChar ϑ i` is the character of lift
  `i`, from `X_{i-1}` to `X_i`;
* `schrodingerOpAt Ψ v` puts the function `Ψ` of matrices at `Σ_N` on the finite datum `v` of a
  lift;
* `directDatum` is the indicator of the integral matrices whose last column is the last basis vector
  modulo `N`, and `Up` is the operator `upOperator`;
* the data in `k.raises d d' C` give lifts that raise gauges from `d` to `d'` by a factor at most
  `C`.

## Relation to the literature

Denominators at the level prime N are traded for the operator `Up`. Related work: Z. Liu, Test
Schwartz functions at p for theta lifts of Hida families, arXiv 2510.21644, 2025; S. Rallis,
Langlands' functoriality and the Weil representation, 1982.


 ## Values of the lift characters, and the direct datum on the standard lattices 

### `norm_detCharAt_diagN_le`

 Let `E` be the CM field, `N` the level prime, `b` the weight and `m` the number of lifts of the
admissible data `D`, and let `ιₚ : ℂ →+* ℂ_[N]` be the chosen embedding. Each infinite place
`τ : D.Φ` of `E` induces through `ιₚ` a prime `D.inducedPlace τ` above `N`; their complex conjugates
form `Σ_N = D.nonInducedPlaces`. Let `χ` be the base change to `E` of the character
`D.chainChar ϑ i` of `U(1)`, the `i`-th character attached to the tame character `ϑ`, with
`i ≤ 2 m`. Let `g` be the matrix of size `n_j` that is `diag (1, …, 1, N)` at the places of `Σ_N` in
`S` and `1` at the other places of `Σ_N`. Then the `N`-adic absolute value of
`χ (det g) |det g| ^ (-k / 2)` is at most the product of one factor `N ^ (2 b)` for each `τ` whose
conjugate induced prime lies in `S`. 

### `exists_mem_inducedPlace_one_le_norm`

 Let `K = ℚ(√(-d))` with `d = P.d`, let `E ⊇ K` be the CM field and `N` the level prime of the
admissible data `D` for `P`, and let `ιₚ : ℂ →+* ℂ_[N]` be the chosen embedding. There is an
integer `δ` of `K` with `1 ≤ ‖ιₚ (δ̄ d)‖` that lies in every prime `D.inducedPlace σ` of `E`, the
prime above `N` induced by `ιₚ` and the infinite place `σ : D.Φ` of `E`. 

### `projOn_translateDatum_mem_standardData`

 Let `x = (x_j)` be a tuple of finite adelic matrices, and let `D.translateDatum x j` be the
Heisenberg translate by `x_j` of the integral vacuum of the hermitian space
`D.homX j = Hom (X_j, X_{j+1})`. Let `𝔪` be a modulus whose places are those of
`Σ_N = D.nonInducedPlaces`, one from each conjugate pair of places above `N`, so that `projOn` is
the projection on the vacuum at all places above `N`. For every integer `δ` of `K`, the projection
lies in `standardData`, the span over the `N`-integral complex numbers of the translates of the
integral vacuum by the points `z` with `δ z` integral above `N`. 

### `schrodingerOpAt_directDatum_mem_raises`

 Let `j < m`, and let `D.liftKernel ϑ j` be the theta kernel from `X_j` to `X_{j+1}` for the tame
character `ϑ`. Take the Heisenberg translate `D.translateDatum x j` of the integral vacuum of
`Hom (X_j, X_{j+1})`, and put on it (`schrodingerOpAt`), at the set `Σ_N = D.nonInducedPlaces` of
places above `N`, the function `directDatum`: the indicator of the integral matrices whose last
column is the last basis vector modulo `N`. The kernel of this datum multiplies the `N`-adic gauge
(`weylGauge`, the largest absolute value of a coordinate) by at most `N ^ (f b)`, where `f` is the
number of infinite places of `E` and `b` the weight. 

 ## Reduction of all lifts to direct lifts at N 

### `liftCharAtN`

 The character `g ↦ χ (det g) |det g| ^ (-r / 2)` of `GL n` over the product of the completions
at `Σ_N`, for the base change `χ` of the character `chainChar ϑ i` of lift `i`. 

### `lift_schrodingerOpAt_comp`

 Let `φ` be an algebraic form on the definite space `X_j` of rank `n_j = D.n j`, and let `v` be a
vector of the finite part of the Weil representation of `Hom (X_j, X_{j+1})`. For a function `Ψ` of
matrices over `LocProd Σ_N`, the product of the completions at `Σ_N = D.nonInducedPlaces`, write
`θ Ψ` for the theta lift (`D.liftKernel ϑ j`) from `X_j` to `X_{j+1}` by `schrodingerOpAt Ψ v`. Let
`Ψ = liftFn f` be a function `f` of matrices modulo `N`, read on integral matrices and extended by
zero. Let `g`, `k` act on forms by right translation (`smoothFormRep`) through `embedGL`. Then `θ
(T ↦ Ψ (k⁻¹ T g)) φ = (χ_{n_{j+1}} g / χ_{n_j} k) • k (θ Ψ (g⁻¹ φ))`, where
`χ_r = D.liftCharAtN ϑ (j + 1) r` is `χ (det ·) |det ·| ^ (-r / 2)` for the base change `χ` of the
character of this lift. 

### `schrodingerOpAtN`

 Put a function `Ψ` of matrices at `Σ_N`, written in bases of `L_j` and `L_{j+1}`, on a finite
datum. 

### `smulCommClass_formX`

 Complex scalars on forms commute. A shortcut for instance search. 

### `liftAtN`

 The lift from `X_j` to `X_{j+1}` by `v` with the function `Ψ` at `Σ_N`, written in bases of
`L_j` and `L_{j+1}`, as a linear map in `Ψ`. 

### `liftAtN_apply`

 `D.liftAtN ϑ j v Ψ φ` is computed in three steps. First translate `φ` on the right
(`smoothFormRep`) by `δ_j⁻¹`. Then apply the lift of the kernel `D.liftKernel ϑ j` by
`schrodingerOpAt Ψ v`. Finally translate on the right by `δ_{j+1} = D.diagPointN (j + 1)`. 

### `upCommutationFactor`

 The factor by which `Up` moves through the direct lift from `X_j` to `X_{j+1}`: the ratio of the
values of `liftCharAtN` at `diag (1, …, 1, N)` on `X_j` and on `X_{j+1}`. 

### `liftLaw_liftAtN`

 Let `v` be in the finite part of the Weil representation of `Hom (X_j, X_{j+1})`, and let
`L Ψ = D.liftAtN ϑ j v Ψ` be the theta lift, for the tame character `ϑ`, from forms on `X_j` to
forms on `X_{j+1}` by `v` with the function `Ψ` of matrices at `Σ_N = D.nonInducedPlaces`. Then the
two rules of `LiftLaw` hold:
* `b ∘ L (liftFn (T ↦ f (b T a))) ∘ a = L (liftFn f)` for integral invertible `a`, `b` and every
  function `f` of matrices modulo `N`;
* `d ∘ L lastRowDatum = γ • L directDatum ∘ d`, where `d = diagNInv = diag (1, …, 1, N⁻¹)`,
  `γ = D.upCommutationFactor ϑ j`, and the two data are the indicators of the integral matrices
  whose last row, respectively last column, is the last basis vector modulo `N`. 

### `gluedFactor`

 The factor for rewriting the glued datum of `X_{2i} → X_{2i+1} → X_{2i+2}` in bases of `L_{2i}`
and `L_{2i+2}^∨`: the product of the values of `liftCharAtN` at `diag (1, …, 1, N)`, taken on
`X_{2i+2}` at the places of `Σ_N` prime to `π` and on `X_{2i}` at those dividing `π`. 

### `norm_gluedFactor_le`

 For `i ≤ ϱ`, where `m = 2 (ϱ + 1)`, each place of `Σ_N` contributes one character value to
`gluedFactor`, so this factor loses at most `2 f b` powers of `N`. 

### `liftInPairs_gluedDoubleLiftDatum`

 Let `D.liftKernel ϑ j` be the theta kernel from `X_j` to `X_{j+1}` for the tame character `ϑ`,
and let `v j` be in the finite part of the Weil representation of `Hom (X_j, X_{j+1})`. Let `π` be
the integer of `E` with `π π̄ = N`. The places `D.piNPlaces` dividing `π`, like those of
`Σ_N = D.nonInducedPlaces`, give with their conjugates all places above `N`. Project the `v j` on
the vacuum at these places (`vacuumProjFinPart`), glue `v (2 i)` and `v (2 i + 1)` to one tensor
(`gluedDoubleLiftDatum`), and take the double lift `X_{2i} → X_{2i+1} → X_{2i+2}`: `liftInPairs`
sends a pure tensor to the composite of the two lifts. The result is `gluedFactor`, a product of two
values of the lift characters at matrices `diag (1, …, 1, N)`, times a sum over the vectors `y`
modulo `N` at `Σ_N`, followed by the action of `diagNInv = diag (1, …, 1, N⁻¹)`. The term for `y` is
the lift `liftAtN` by `lastColDatum y`, the indicator of the integral matrices with last column `y`
modulo `N`, followed by the lift by `charDatum y`, the character `ψ_N` of the last row paired with
`y`. 

### `doubleLiftChain_gluedDoubleLiftDatum_eq_smul_chain`

 **All lifts become direct.** Let `m = 2 (ϱ + 1)` be the number of lifts, `f` the number of
infinite places of `E` and `b` the weight of the data `D`. There is a scalar `c` with
`‖ιₚ c‖ ≤ N ^ (m f b)` such that the following holds for all finite data `v j` of
`Hom (X_j, X_{j+1})` and all forms `φ` on `X_0` of level `levelX 0` that are ramified. The composite
`doubleLiftChain` of the `ϱ + 1` double lifts, whose data are glued from the projections of the
`v j` on the vacuum above `N`, sends `φ` to `c` times the image of `Up ^ (ϱ + 1) φ` under the
composite `chain` of the `m` direct lifts. 

### `omega_schrodingerOpAtN_directDatum`

 Let `π` be the integer of `E` with `π π̄ = N`, and let `ω` be the Weil action of the finite
unitary groups of `X_j` and `X_{j+1}` on the finite data `v` of the theta kernel
`D.liftKernel ϑ j`. The operator `D.schrodingerOpAtN ϑ j directDatum` puts on `v`, at
`Σ_N = D.nonInducedPlaces`, the indicator of the integral matrices whose last column is the last
basis vector modulo `N`, in bases of the lattices `L_j`, `L_{j+1}` of integral vectors with last
coordinate divisible by `π`. It commutes with `ω (a, b)` for `a`, `b` in the levels `levelX` of
`X_j` and `X_{j+1}`, whose elements have last row congruent to `(0, …, 0, 1)` modulo `π`. 

### `schrodingerOpAtN_directDatum_mem_raises`

 **Direct lifts lose little.** For `j < m`, the direct datum at `Σ_N`, in bases of `L_j` and
`L_{j+1}`, on a translate of the integral vacuum raises `N`-adic gauges from
`δ_j = D.diagPointN j` to `δ_{j+1}` by a factor at most `N ^ (f b)`. 

### `gaugeLe_compositeLift_at_N`

 **The prime `N`, valuation.** Let `m` be the number of lifts, `f` the number of infinite places
of `E`, `b` the weight and `M` the principal level of the data `D`. Let `ϑ` be a twist, a character
of `U(1)` of weight `0` whose tame part is non-trivial exactly on the finite set `ϑ.Q` of places,
and let `q` be the product of their norms. Let `Ψ` be a chain datum for `ϑ`: a finitely supported
function on the tuples of finite adelic matrices by which the integral vacua of the
`Hom (X_j, X_{j+1})` are translated, supported on admissible tuples that vanish at the places prime
to `M q`, with values integral away from `q` (and bounded in size if `ϑ.Q` is empty), whose glued
tensor is fixed by the levels of `X_0, …, X_{m-1}`. Let `φ` be a ramified source form on `X_0` in
`upIntegralForms`: `Up ^ (m / 2) φ`, for the operator `Up = upOperator`, is a source form with
values integral for the lattice `L_0`. The composite lift of `φ` is the chain of double lifts by the
glued tensor of `Ψ`, restricted from `X_m` to `Y_m`. Then at every point `g` its value, moved by
`g⁻¹`, has coordinates of `N`-adic absolute value at most `N ^ (2 m f b)`. 
