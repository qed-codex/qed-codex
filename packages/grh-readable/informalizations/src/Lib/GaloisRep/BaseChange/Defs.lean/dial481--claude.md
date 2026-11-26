---
{
  "module": "src/Lib/GaloisRep/BaseChange/Defs.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/GaloisRep/BaseChange/Defs.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/GaloisRep/BaseChange/Defs.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Twisted norms, matching pairs and base change maps for unitary groups

This file sets up base change for unitary groups along a ring endomorphism `σ` of finite order.
Finally it defines the Galois action on `New.Gf E' n` and the base change map from the finite adelic
unitary group `New.Gf E n`, the matrices `g` over the finite adeles with `gᴴ g = 1`, for an
extension `E'/E` of CM fields.

## Main definitions and results

* `New.twistedNorm`: the twisted norm `δ · τ δ ⋯ τ^(p-1) δ` in a monoid. `New.twistedNorm_conj`
  shows that twisted conjugation of `δ` conjugates the norm. `New.twistedNorm_mem` and
  `New.map_twistedNorm` show that it respects stable subgroups and equivariant maps.
* `New.IsTameAtLevel`: the conditions on a ring endomorphism `σ` and a level `m` under which descent
  works.
* `New.IsRootQuotient`, `New.IsNormRoot`: a polynomial `z`, depending only on the characteristic
  polynomial of `γ`, that gives a candidate `a = z(γ) / z(γ)ᴴ` for an element of norm `γ`.
* `New.IsMatchingPair`: `φ` is invariant under twisted conjugation by `K`, and `f` and `φ` match
  point by point along `γ ↦ a`.
* `New.CocyclesSplit`: the cocycles in `K` are coboundaries on the support of `u`.
* `New.baseChangeGf`: the map `Gf E n → Gf E' n` induced by the inclusion of finite adeles.

Notions from other files:
* `New.U J`: the unitary group of a matrix `J` over a commutative ring with involution, the `g` in
  `GL_n(R)` with `gᴴ J g = J`. In this file `J = 1`.
* `New.U.map`: for a ring homomorphism `f` commuting with the involutions and carrying `J` to `J'`,
  the homomorphism `U(J) → U(J')` applying `f` to each entry.
* `New.FinPlace E`: the finite places of a number field `E`. For a finite place `u`, `u.comap f` is
  the place below `u` along a ring homomorphism `f`, and `u.below E` is the place of `E` below `u`.
* `New.adeleMap`: for an embedding of number fields, the induced ring homomorphism of finite adeles.

## Relation to the literature

Known; see `Lib.GaloisRep.BaseChange.PrimeDegreeTransfer` for sources.


 ## Twisted norms, tame actions and profinite rings 

### `twistedNorm`

 The twisted norm `δ · τ(δ) ⋯ τ^{p−1}(δ)` of `δ` in a monoid `M`: the product, in order, of the
first `p` iterates `τ^[i] δ`. Here `τ : M → M` is any map. 

### `IsTameAtLevel`

 The ring endomorphism `σ` acts tamely at level `m`: (a) `σ m = m`; (b) some `e` has trace
`∑ i < p, (σ ^ i) e` congruent to `1` modulo `m`; (c) `σ ^ p = 1`; (d) `0 < p`; (e) for `0 < i < p`,
every prime ideal `P` modulo which `σ ^ i` is the identity contains `m`, so there is no inertia at
the primes that do not contain `m`. 

### `IsProfiniteRing`

 A form of profiniteness that allows passing to the limit. Every sequence `x` has exactly one `L`
such that, for each natural number `M ≠ 0`, `M` divides `x N - L` for all `N` in a set of the
hyperfilter (a fixed ultrafilter on `ℕ` that contains the cofinite sets). For the topology given by
the ideals `(M)`, existence of `L` is a form of compactness and uniqueness says that only `0` is
divisible by every `M ≠ 0`. 

### `U.mapEnd`

 The endomorphism of the unitary group `{g : gᴴ g = 1}` over `R` given by applying entrywise a
ring endomorphism `σ` commuting with the involution. 

### `twistedNorm_conj`

 For a group endomorphism `τ` and an element `y` with `τ^[p] y = y`, the twisted conjugate
`y⁻¹ * δ * τ y` of `δ` has twisted norm `y⁻¹ * twistedNorm τ p δ * y`. 

### `twistedNorm_mem`

 If `τ` maps the subgroup `K` into itself, then the twisted norm of every `δ ∈ K` lies in `K`. 

### `map_twistedNorm`

 A monoid homomorphism `e` that intertwines `τ` on `Γ` with `σ` on `M` (`e (τ δ) = σ (e δ)`)
carries twisted norms for `τ` to twisted norms for `σ`. 

### `twistedNorm_succ'`

 Splitting off the first factor of the twisted norm, for the monoid endomorphism `τ`. 


## Matching pairs and split cocycles

This section states when test functions on a set `A` (a unitary group over the base, mapped by `j`)
and on the unitary group over `R` match in base change. Here `σ` is a ring endomorphism of `R` that
commutes with `star`. `New.U.mapEnd h` is the action of `σ` on the unitary group, `New.twistedNorm`
is the twisted norm of length `q`, and `u : R` selects the places concerned. "The support of `u`"
means where `u` is `1`, as for an idempotent, though nothing here assumes `u * u = u`. The
conditions multiply by `u` or by `1 - u`.


### `IsRootQuotient`

 The relation `a * z(γ)ᴴ = z(γ)` between a matrix `a`, a polynomial `z` and a unitary `γ`, where
`z(γ)` is `z` evaluated at the matrix `γ.val.val` of `γ` and `ᴴ` is the conjugate transpose.
When `z(γ)ᴴ` is invertible it says `a = z(γ) * (z(γ)ᴴ)⁻¹`. 

### `IsNormRoot`

 `z` is a root for `P` on the support of `u`: `(1 - u) • z = (1 - u) • 1`, and if some unitary
`γ` has characteristic polynomial `P`, then (a) `det z(A)` is the value of a unit in `D` for every
square matrix `A` with `P(A) = 0`, and (b) `(1 + u • (γ - 1)) * (N z)(γ)ᴴ = (N z)(γ)` for every
such `γ`, where `N z` is the product of the `q` conjugates of `z` under `σ`. The matrix in (b) is
`γ` on the support of `u` and `1` off it. 

### `IsMatchingPair`

 `f` and `φ` match, with `Nm = twistedNorm (mapEnd h) q`: `φ` is invariant under
`δ ↦ k⁻¹ * δ * σ(k)` for `k ∈ K`, and each `σ`-fixed characteristic polynomial `P` of some `j g`
with `f g ≠ 0` or some `Nm δ` with `φ δ ≠ 0` has a root `z` (`New.IsNormRoot`) such that every
unitary `a` with `a * (u • z)(γ)ᴴ = (u • z)(γ)`, for `γ` of characteristic polynomial `P`, has
`f g = φ a` when `j g = γ = Nm a`, and `a⁻¹ * δ ∈ K` when `Nm δ = γ` and `φ δ ≠ 0`. 

### `CocyclesSplit`

 The cocycles in `K` split on the support of `u`: every `s ∈ K` whose twisted norm of length `q`
under `τ` is `1` has some `t ∈ K` with `(1 - u) • t = (1 - u) • 1` (`t` is `1` off the support of
`u`) and `u • (t⁻¹ * s * τ t) = u • 1` (on the support of `u`, `s = t * (τ t)⁻¹`). Here `.val.val`
is the matrix of an element of the unitary group. 

 ## Base change and Galois action on finite adelic points 

### `below_comap`

 Moving a finite place `u` of `E'` by `σ ∈ Gal(E'/E)` does not change the place of `E`
below it. 

### `bijective_pow_of_ne_one_of_prime_finrank`

 In a Galois extension `E'/E` of prime degree `q = Module.finrank E E'`, the powers `σ ^ i`,
`0 ≤ i < q`, of any `σ ≠ 1` are the elements of the Galois group, each once. 

### `baseChangeGf`

 The homomorphism from the finite adelic unitary group over E to the one over E' induced by
the inclusion of finite adeles. 

### `galoisGf`

 The action of σ in Gal(E'/E) on the finite adelic unitary group over E', entry by entry. 
