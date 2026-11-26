---
{
  "module": "src/Lib/GaloisRep/BaseChange/IwahoriEigenforms.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/GaloisRep/BaseChange/IwahoriEigenforms.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/GaloisRep/BaseChange/IwahoriEigenforms.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Hilbert 90 for the pro-p Iwahori group and base change of Iwahori eigenforms

`F` is a valued field with compact ring of integers, and `σ` is an isometric endomorphism with
`σ ^ p = 1`. `New.proIwahori` is the pro-`p` Iwahori subgroup of `GL n F`, the matrices that are
upper unitriangular modulo the maximal ideal. `New.twistedNorm τ p δ = δ * τ δ * ⋯ * τ ^ (p - 1) δ`
is the twisted norm. The file proves a Hilbert 90 statement and a matching of dominant double cosets
for this group. These local results give matching local data at a place with exactly one place above
it.

## Main definitions and results

* `New.exists_coboundary_proIwahori`: if some integer of `F` has `σ`-trace `1`, an element of
  `New.proIwahori` of norm `1` is a coboundary `t * (σ t)⁻¹` with `t` in `New.proIwahori`.
* `New.proIwahori_doubleCoset_match`: the double cosets of a strictly dominant diagonal matrix over
  `F` and of its norm over the fixed field correspond under `γ ↦ z γ` for a polynomial `z`
  (`New.IsIwahoriMatchingPolynomial`).
* `New.isLocalMatching_proIwahori`: the indicator functions of the double cosets `K N(t) K` at `w`
  and `K' t K'` at `u` are matching local data (`New.IsLocalMatching`). It globalises
  `New.proIwahori_doubleCoset_match` and `New.exists_coboundary_proIwahori`.
* `New.exists_baseChange_isIwahoriEigen`: feeding these into
  `New.exists_isWeakBaseChange_of_matching` gives a base change whose eigencharacter at `u` is that
  of `f` at `w` composed with `N`.

Notions from other files:
* `New.IsStep E' μ`: a step `E'/E`. The field `E` contains a primitive `5040`-th root of unity,
  `E'` is a CM field Galois over `E` of prime degree with an integer of trace `1`, and `μ` is the
  character of the finite ideles of `E` that goes with the extension.
* `New.locIdele`: the homomorphism that sends `x` in the units of the completion at `v` to the
  finite idele with component `x` at `v` and `1` elsewhere.
* `New.iwahoriDoubleCoset t`: the double coset `K t K` of the diagonal matrix `t`, where `K` is
  `New.proIwahori`.
* `New.diagGL t`: the diagonal matrix with the units `t i` on the diagonal, as an element of `GL`.

## Relation to the literature

Known; see `Lib.GaloisRep.BaseChange.PrimeDegreeTransfer` for sources.



## Hilbert 90 and matching of dominant double cosets

The matching uses that such a double coset is `σ`-conjugate into the torus
(`New.exists_inv_mul_mul_map_eq_diagGL_mul`) and that the eigenvalues are told apart by their
valuations.


### `map_mem_proIwahori_iff_of_isometry`

 Let `σ` be an endomorphism of `F` that keeps the valuation. Then `g ∈ GL N F` lies in the
pro-`p` Iwahori subgroup `New.proIwahori` exactly when `σ g`, with `σ` applied to the entries,
does. 

### `exists_coboundary_proIwahori`

 Hilbert 90 for the pro-`p` Iwahori subgroup `New.proIwahori` of `GL N F`. Let `σ` be an
endomorphism of `F` that keeps the valuation, with `σ ^ p = 1`, and let `c` be an integer of `F`
with trace `∑ i < p, σ ^ i c = 1`. If `s ∈ proIwahori` has twisted norm
`s * σ s * ⋯ * σ ^ (p - 1) s = 1` (`New.twistedNorm`, with `σ` acting on the entries), then
`s * σ t = t` for some `t ∈ proIwahori`. 

### `exists_twisted_conj_diag_and_twistedNorm_conj`

 Let `σ` be a continuous endomorphism of `F` that keeps the valuation, with `σ ^ p = 1` for some
`p > 0`, and let `t` be diagonal with `v (t i)` strictly increasing. Let `K` be the pro-`p` Iwahori
subgroup `New.proIwahori`. Every `δ` in the double coset `K t K` (`New.iwahoriDoubleCoset t`) is
`σ`-conjugate to `t * d` for some `d` diagonal in `K`: `k⁻¹ * δ * σ k = t * d` with `k ∈ K`. The
same `k` conjugates the twisted norm of `δ` (`New.twistedNorm`) to that of `t * d`. 

### `exists_conj_map_eq_twistedNorm_diagGL`

 A point `x` of the double coset `K' s K'` over `F'` (`New.iwahoriDoubleCoset s`) is sent by `ι`
to a conjugate, by some `k ∈ New.proIwahori`, of the twisted norm (`New.twistedNorm`) of
`diagGL (t * d)` with `diagGL d ∈ New.proIwahori`. This uses that `ι s` is the twisted norm of
`diagGL t` (`hs_norm`) and that the `1`-units of `F'` are norms of `1`-units of `F` (`h_norms`). 

### `eq_of_prod_ringHom_pow_apply_eq`

 Let `σ` be an endomorphism of `F` that keeps the valuation, let `p > 0`, let `t` be diagonal
with `v (t i)` strictly increasing, and let `d`, `d'` be diagonal in the pro-`p` Iwahori subgroup
`New.proIwahori`. If the norms `∏ l < p, σ ^ l (t i * d i)` and `∏ l < p, σ ^ l (t j * d' j)` agree,
then `i = j`, since the valuation of the first is `v (t i) ^ p`. 

### `charpoly_diagonal_dvd_twistedNorm_sub_X`

 Let `σ ^ p = 1`, and let the values `c i = ∏ l < p, σ ^ l (e i)` be distinct. If the polynomial
`z` takes the value `e i` at `c i` for every `i`, then the characteristic polynomial
`∏ i, (X - c i)` of `diagonal c` divides `N(z) - X`, where `N(z) = ∏ l < p, σ ^ l z` is the
twisted norm (`New.twistedNorm`) of `z`. 

### `aeval_eq_conj_diagonal_eval`

 Let `γ` have the characteristic polynomial of the diagonal matrix `diagonal c`, and let
`k⁻¹ * γ * k = diagonal c'`, where `c' i = c l` holds only for `i = l`. Then for every polynomial
`z` the matrix `z γ` is `k * diagonal (z ∘ c) * k⁻¹`. 

### `mem_iwahoriDoubleCoset_of_conj_map_eq_twistedNorm`

 Descent for clause (a) of `New.proIwahori_doubleCoset_match`. Let `σ` preserve `v` and let the
`σ`-fixed elements of `F` lie in the range of `ι : F' →+* F`, with `v ∘ ι` equivalent to `v`. Let
`ι (diagGL s)` be the twisted norm (`New.twistedNorm`, over `σ`, `p` factors) of `diagGL t`, and let
`k, diagGL d ∈ New.proIwahori`, `a = k * diagGL (t * d₀) * k⁻¹` and
`k⁻¹ * a * σ k = diagGL (t * d)`. If `k⁻¹ * ι x * k` is the twisted norm of `diagGL (t * d)`, then
`x` lies in `I₁ diag(s) I₁` over `F'` (`New.iwahoriDoubleCoset s`). 

### `inv_mul_mem_proIwahori_of_twisted_conj`

 Let `σ` be an endomorphism of `F` that keeps the valuation, let `k`, `diagGL d₀` and `diagGL d`
lie in the pro-`p` Iwahori subgroup `New.proIwahori`, and let `k⁻¹ * δ * σ k = diagGL (t * d)` and
`a = k * diagGL (t * d₀) * k⁻¹`. Then `a⁻¹ * δ = k * diagGL (d₀⁻¹ * d) * (σ k)⁻¹` lies in
`New.proIwahori`. 

### `IsIwahoriMatchingPolynomial`

 The polynomial `z` over `F` matches the double cosets `K' s K'` over `F'` and `K t K` over `F`
at the polynomial `P`. Here `K`, `K'` are the pro-`p` Iwahori subgroups `New.proIwahori`, the
double cosets are `New.iwahoriDoubleCoset`, twisted norms (`New.twistedNorm`) are taken with the
endomorphism `σ` of `F` and length `p`, and `ι : F' →+* F`. In the last two fields `γ` has
characteristic polynomial `P` and `a = z γ`. 

### `IsIwahoriMatchingPolynomial.dvd_twistedNorm_sub_X`

 The twisted norm `z * σ z * ⋯ * σ ^ (p - 1) z` is `X` modulo `P`. 

### `IsIwahoriMatchingPolynomial.mem_iwahoriDoubleCoset_iff`

 If `γ = ι x` and `γ` is the twisted norm of `a`, then `x ∈ K' s K'` exactly when
  `a ∈ K t K`. 

### `IsIwahoriMatchingPolynomial.inv_mul_mem_proIwahori`

 Every `δ ∈ K t K` with twisted norm `γ` has `a⁻¹ * δ ∈ K`, so it lies in the coset `a K`. 

### `proIwahori_doubleCoset_match`

 Matching at pro-`p` Iwahori level. Let `σ` be a continuous endomorphism of `F` that keeps the
valuation, with `σ ^ p = 1` and `p > 0`. Let `ι : F' →+* F` be a map whose image holds the points
fixed by `σ` (`h_range`), along which `v` restricts to a valuation equivalent to that of `F'`
(`h_val`), and such that every `x` with `v (ι x - 1) < 1` has `ι x = ∏ i < p, σ ^ i y` for a unit
`y` with `v (y - 1) < 1` (`h_norms`). Let `t` over `F` and `s` over `F'` have strictly increasing
valuations, with `ι (diagGL s)` the twisted norm (`New.twistedNorm`) of `diagGL t`. Let `P` be the
characteristic polynomial of `ι x` for `x` in `K' s K'`, or of the twisted norm of a point of
`K t K` (`New.iwahoriDoubleCoset`, with `K`, `K'` the groups `New.proIwahori`). Then some polynomial
`z` matches the two double cosets at `P` (`New.IsIwahoriMatchingPolynomial`): its twisted norm is
`X` modulo `P`, and for `γ` with characteristic polynomial `P` and `a = z γ`, (a) if `γ = ι x` is
the twisted norm of `a`, then `x ∈ K' s K' ↔ a ∈ K t K`; (b) every `δ ∈ K t K` with twisted norm `γ`
lies in `a K`. 


## Base change of Iwahori eigenforms at a place with one place above

Base change of Iwahori eigenforms along a step `E'/E` (`New.IsStep E' μ`), at a split place `w` of
`E` where `μ` is trivial and that has exactly one place `u` of `E'` above it, also split. `N` is the
local norm from `(LocField u)ˣ` to `(LocField w)ˣ`.

`New.proIwahori` is the pro-`p` Iwahori subgroup; `New.dominantTorus` the diagonal `t` with
non-decreasing absolute values; `New.IsIwahoriEigen ρ ξ f` says that `f ≠ 0` is fixed by
`New.proIwahori` and that the average of `ρ t f` over it is `ξ t • f` for dominant `t`. For a family
`θ` of `r` characters, `New.torusChar θ` is the character `t ↦ ∏ i, θ i (t i) * |t i| ^ (r - 1 - i)`
of the diagonal torus.


### `iterate_adeleMap_apply`

 At a place `u` of `E'` fixed by `τ`, the component at `u` of the `i`-th iterate of `τ` on
finite adeles is the `i`-th iterate of the local action `locMap τ hs` of `τ` on the completion at
`u`, applied to the component at `u`. 

### `exists_local_norm_eq`

 Local norms are onto the `1`-units at a place with one place above. Let `E'/E` be a step, `u`
the only place of `E'` above `w = u.below E` (`h_unique`), and `τ ≠ 1` fix `u`. Then every `x` at
`w` with `v (x - 1) < 1` is a norm `∏ i < [E' : E], (σ ^ i) y` of a unit `y` at `u` with
`v (y - 1) < 1`, where `σ = locMap τ hs` is the action of `τ` on the completion at `u`. 

### `locMap_pow_finrank_eq_one`

 At a place `u` of `E'` fixed by `τ`, the local action `locMap τ hs` of `τ` on the completion
at `u` has order dividing `[E' : E]`. 

### `mem_range_locMap_of_locMap_eq_self`

 Fixed points of the local action come from below. Let `E'/E` be a step (so Galois of prime
degree), `u` the only place of `E'` above `w = u.below E` (`h_unique`), and `τ ≠ 1` fix `u`. Then
every `x` in the completion at `u` fixed by the local action `locMap τ hs` of `τ` is the image of an
element of the completion at `w`. 

### `locMap_localNorm_eq_prod`

 The local norm as a product of conjugates. At a place `u` of `E'` fixed by `τ ≠ 1`, along a step
`E'/E`, the local norm of `y`, mapped into the completion at `u`, is the product of the conjugates
`(σ ^ i) y`, `i < [E' : E]`, where `σ = locMap τ hs`. 

### `cocyclesSplit_comap_proIwahori`

 Cocycles split at pro-`p` Iwahori level at a place `u` fixed by `τ ≠ 1`, along a step `E'/E`.
Let `ρ` be a retraction of `embedAtSplit hu` at the places above `u.below E` and its conjugate
(`New.IsLocalRetraction`) that carries `galoisGf τ` to the entrywise action of `σ = locMap τ hs`.
Then at the level of the `δ` with `ρ δ ∈ proIwahori`, every `galoisGf τ`-cocycle is a coboundary on
those places (`New.CocyclesSplit`). 

### `map_evalAt_twistedNorm_one_add_idem_smul`

 At a place `u` of `E'` fixed by `τ`, the twisted norm under `τ` of the adelic polynomial
`1 + idem {u} • (y - 1)`, which is `y` at `u` and `1` elsewhere, read at `u`, is the twisted norm
under the local action `locMap τ hs` of `y` read at `u`. 

### `isMatchingPairAbove_proIwahori`

 The indicators of `K N(t) K` (through `r`) and of `K t K` (through `ρ`) are a matching pair
above `w = u.below E` (`New.IsMatchingPairAbove`), for `t` with strictly increasing `v (t i)`. Here
`K = proIwahori`, `N(t) = localNorm E u ∘ t`, and `ρ`, `r` are the components at `u` and `w` of the
adelic groups `Gf E' m` and `Gf E m` (`baseChangeGf` maps `Gf E m` into `Gf E' m`), renumbered: `ρ`
carries `galoisGf τ` to `locMap τ hs`, keeps characteristic polynomials, and sends a base change to
`r` followed by the inclusion of the completion at `w`. 

### `isLocalMatching_proIwahori`

 Matching local data at a place with one place above. Let `E'/E` be a step, `w = u.below E` split
(`hw`) with `μ` trivial at `w` (`hμ_loc`), and `u` the only place above `w` (`h_unique`), split
(`hu`). Then the indicators of `K N(t) K` at `w` and `K' t K'` at `u`, with `K`, `K'` the pro-`p`
Iwahori subgroups and `N(t) = localNorm E u ∘ t`, are matching local data (`New.IsLocalMatching`)
for the dominant `t` whose valuations `v (t i)` increase strictly. 

### `heckeFun_iwahoriDoubleCoset_mul`

 The operators of dominant double cosets multiply like the torus. Let `ρ` be a smooth
representation of `GL_N` over the completion of a number field at `o`, and `s`, `t` elements of
`New.dominantTorus`. On vectors `x` fixed by `New.proIwahori`, applying the operator of the double
coset of `t` and then that of `s` is applying that of `s * t`. 

### `exists_baseChange_isIwahoriEigen`

 Base change keeps an Iwahori eigencharacter. Let `E'/E` be a step with `E'` containing a
primitive `5040`-th root of unity (`HasPrimitiveRoot5040`). Let `w = u.below E` be split (`hw`) with
`μ` trivial at `w` (`hμ_loc`), and let `u` be the only place above `w` (`h_unique`), split (`hu`).
If `f`, an element of `localFormRep (stdSpace E m) κ hw` (the forms of weight `κ`, as a
representation of `GL` at `w`), is an Iwahori eigenvector at `w` (`New.IsIwahoriEigen`) with
character `torusChar θ`, some form `f'` over `E'` is (a) an eigenform, (b) a weak base change of `f`
off `w` and its conjugate, and (c) an Iwahori eigenvector at `u` with character
`torusChar (θ i ∘ N)`, `N = localNorm E u`. 
