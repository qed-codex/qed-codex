---
{
  "module": "src/New/Congruences/Selmer/OneSystem.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Congruences/Selmer/OneSystem.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Congruences/Selmer/OneSystem.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# The universal twist and one system of equations for all twists

For homomorphisms `h_j : G → ℤ / q` let `ψ_X(g) = ∏ (1 + X_j) ^ (h_j g)`, and let `Sel(x)` be the
Selmer module of the twist of a representation by the value `ψ_x` at a point `x`. The members of all
`Sel(x)` are functions on one finite quotient of the Galois group, and the cocycle rule and the
other conditions are linear equations over `O[X]` for their values.

* `New.Selmer.universalChar`, `New.Selmer.IsTiedPrimes.universalChar_frob`,
  `New.Selmer.IsTiedPrimes.universalChar_tame_gen`: the polynomial `ψ_X` and its values at the
  auxiliary primes.
* `New.Selmer.finite_selmerModule`: for finite `S` and `ρ` locally constant modulo `ℓ ^ M`, the
  Selmer module with coefficients in a finite `O / a`, `a ∣ ℓ ^ M`, is finite.
* `New.Selmer.exists_matrix_selmerAtPoint_equiv`: there is one matrix `A` over `O[X]` such that each
  `Sel(x)` is isomorphic to the kernel of `A(x)` on a power of `O' / ℓ ^ M`.
* `New.Selmer.exists_isLeast_length_selmerAtPoint`, `New.Selmer.exists_sharp_polynomial`: the
  valuations of a set of polynomials (in the proof, maximal minors) bound the lengths of `Sel(x)` at
  all points over discrete valuation rings of characteristic zero, and one is sharp at a given
  point.

Notions from other files:
* `New.selmerModule ρ S L B`: the locally constant cocycles for `ρ` with values in `B ^ n` that are
  unramified outside `S` and obey the relations `L`.
* `New.obeying`, `New.mapRel`: a relation is a finitely supported `f : Γ →₀ Matrix n n O`; a
  function `c` obeys it if `∑ γ, f γ • c γ = 0`, and `mapRel e f` applies `e` to all entries of `f`.
* `New.Selmer.IsTiedPrimes ℓ S₀ V W N P₀ J d`: a finite set `J` of primes that, with their
  conjugates, avoid `S₀`, and a first prime `P₀ ∈ J`. At `v ∈ J`, `(d v).1` holds a place, a
  Frobenius element `φ`, a tame generator `γ` and a character to `ℤ / ℓ ^ N`, and `(d v).2 i ∈ O` is
  the slope for the index `i : ι`. The Frobenius element of `P₀` lies in `W`, and where the slope
  for `i` is not zero, the condition `V i` holds at `φ` and at `(c φ c)⁻¹` for the complex
  conjugation `c`.
* `New.QuotSpan a`, `New.Selmer.reduceModPow ℓ M ρ`: the ring `O / a`, and `ρ` modulo `ℓ ^ M`.

## Relation to the literature

See `New.Congruences.Selmer.TwistingTheorem` for related work.


### `map_mk_smul`

 A matrix over `O` acts on `(O / a) ^ n` as its reduction modulo `a` does; `QuotSpan a` is the
ring `O / a`. 

### `universalChar`

 The polynomial `ψ_X(g) = ∏ (1 + X_j) ^ (h_j g)` attached to homomorphisms `h_j : G → ℤ / q`;
for `q ≠ 0` the exponents are taken in the interval `[0, q)`. 

### `aeval_sub_one_universalChar`

 At the point `(ζ_j - 1)_j` for `q`-th roots of unity `ζ_j`, the polynomial
`universalChar h g = ∏ (1 + X_j) ^ (h_j g)` takes the value at `g` of the character
`pointChar h ζ hζ = ∏ ζ_j ^ h_j`. 

### `IsTiedPrimes.universalChar_eq_one_add_X`

 Let `ℓ` be prime and `N ≠ 0`. Let `J` be a finite set of primes of the CM field `E` with data
`d` as in `IsTiedPrimes`: each `w ∈ J` carries an anticyclotomic character `h_w = (d w).1.character`
of `Gal(Ω/E)` to `ℤ / ℓ ^ N`. Let `ψ_X = ∏ (1 + X_w) ^ h_w` be the polynomial over a commutative
ring `R` in variables `X_w`, `w ∈ J`. If `h_v(g) = 1 ∈ ℤ / ℓ ^ N` and the other `h_w` vanish at `g`,
then `ψ_X` is `1 + X_v` at `idOrConjInv b g`, that is, at `g` and at `(c g c)⁻¹` for the complex
conjugation `c`. 

### `IsTiedPrimes.universalChar_frob`

 Let `ℓ` be prime and `N ≠ 0`. Let `J` be a finite set of primes of the CM field `E` with data
`d` as in `IsTiedPrimes`: each `w ∈ J` carries an anticyclotomic character
`h_w = (d w).1.character` to `ℤ / ℓ ^ N`, and at the Frobenius element `φ = (d v).1.frob` of a prime
`v ∈ J` other than the distinguished prime `P₀ ∈ J`, the character `h_{P₀}` is `1` and the other
`h_w` vanish; `S₀`, `V`, `W` and the slopes play no part. Then at `φ` and at `(c φ c)⁻¹` for the
complex conjugation `c`, the two values of `idOrConjInv b φ`, the polynomial
`ψ_X = ∏ (1 + X_w) ^ h_w` over `R` in variables `X_w`, `w ∈ J`, is `1 + X_{P₀}`. 

### `IsTiedPrimes.universalChar_tame_gen`

 Let `ℓ` be prime and `N ≠ 0`. Let `J` be a finite set of primes of the CM field `E` with data
`d` as in `IsTiedPrimes`: each `w ∈ J` carries an anticyclotomic character
`h_w = (d w).1.character` to `ℤ / ℓ ^ N` and a tame generator of inertia; `P₀`, `S₀`, `V`, `W` and
the slopes do not enter the claim. Let `γ = (d v).1.tameGenerator` be the tame generator at a prime
`v` of `J`. At `γ` and at `(c γ c)⁻¹` for the complex conjugation `c`, the two values of
`idOrConjInv b γ`, the polynomial `ψ_X = ∏ (1 + X_w) ^ h_w` over `R` in variables `X_w`, `w ∈ J`, is
`1 + X_v`. 

### `finite_selmerModule`

 Let `E` be a number field embedded in the algebraic closure `Ω` of `ℚ`, let `ρ` be a
representation of `Gal(Ω/E)` by matrices over `O` that is locally constant modulo `ℓ ^ M`, and let
`S` be a finite set of primes of `E`. Let `a ∣ ℓ ^ M` with `QuotSpan a = O / a` finite, and let `L`
be a set of relations `∑ γ, f γ • c γ = 0` on functions `c`. Then the Selmer module of `ρ` with
coefficients in `O / a` is finite. 

### `mapRel_mapRel`

 Mapping the entries of a relation by `e` and then by `ev` is mapping them by `ev ∘ e`. 

### `mapRel_image_cocycleRelations`

 Applying `ev` to all matrix entries carries the relations that express the cocycle identity for
`ρ` onto those that express it for `g ↦ ev (ρ g)`. 

### `relationMatrix`

 The linear equations that a set `R` of relations imposes on the functions on `Γ` that factor
through `π : Γ → 𝒢`. The unknowns are the coordinates of the values on `𝒢`, and there is one
equation for each relation and each coordinate. 

### `sum_mapDomain_smul_eq_relEval`

 For `π : Γ → 𝒢`, let `f.mapDomain π` be `f` pushed forward along `π`, adding the matrices over
each fibre. Then `∑ c, ev (f.mapDomain π c.1 i c.2) • w c` is coordinate `i` of
`relEval B (mapRel ev f)` applied to `g ↦ w (π g, ·)`, that is, of `∑ g, ev (f g) • w (π g, ·)`. 

### `mem_matrixKernel_relationMatrix`

 A vector `w` solves the linear system `relationMatrix π R`, with entries mapped by `ev`, if and
only if the function `g ↦ w (π g, ·)` obeys the relations of `R` mapped by `ev`. 

### `eq_zero_of_forall_hom_zmod_eq_zero`

 Let `B` be an abelian group killed by `m ≠ 0`. An element of `B` that is killed by every
homomorphism `B → ℤ / m` is zero. 

### `exists_openNormalSubgroup_forall_apply_eq_apply_one`

 Finitely many locally constant functions on an open subgroup `G'` of `Gal(Ω/E)` are all constant
on some open normal subgroup `G''` of `Gal(Ω/E)` that is contained in `G'`. 

### `exists_openNormalSubgroup_forall_eq_zero`

 Let `G'` be an open subgroup of `Gal(Ω/E)`, let `m ≠ 0` and let `S` be a finite set of primes of
the number field `E`. There is one open normal subgroup `G''` such that, for every abelian group `B`
killed by `m`, each locally constant `z : Gal(Ω/E) → B` that is additive on `G'` and vanishes on
`inertiaAbove Sᶜ`, the union of the inertia groups above the primes outside `S`, vanishes on
`G''`. 

### `exists_matrix_selmerModule_equiv`

 Let `ρ` be a function from `Gal(Ω/E)` to matrices over a ring `Λ`, let `L` be a set of relations
`∑ γ, f γ • c γ = 0` with matrix coefficients over `Λ`, let `G'` be an open subgroup, let `m ≠ 0`
and let `S` be a finite set of primes of `E`. There is one matrix `A` over `Λ`, with columns indexed
by a finite type `k`, such that for every `ev : Λ → O'` and every `O'`-module `B` killed by `m`, if
`G'` acts trivially on `B ^ n` through `ev ρ`, the Selmer module of `ev ρ` in `B ^ n` is isomorphic
to the kernel of `ev A` on `B ^ k`. 

### `pointTwist`

 The matrices `ψ_x(g) ρ(g)` over `O'`, where `ψ_x(g)` is the value of
`ψ_X(g) = universalChar h g` at the point `x` and `ρ(g)` is mapped by `e`. The function `ψ_x` need
not be multiplicative. 

### `pointTwist_smul_eq_self`

 Let `h j : G → ℤ / q` be finitely many homomorphisms, `ρ` a representation of `G` by matrices
over `O`, `e : O → O'` a ring homomorphism and `x` a point with coordinates `x j ∈ O'`. If all
`h j` vanish at `g` and `ρ g` is the identity modulo `ℓ ^ M`, then the twisted matrix
`pointTwist h x e ρ g = (∏ (1 + x_j) ^ (h_j g)) • e (ρ g)` acts trivially on `(O' / ℓ ^ M) ^ n`. 

### `selmerAtPoint`

 The module `Sel(x)`: the locally constant cocycles in `(O' / ℓ ^ M) ^ n` for the twist
`pointTwist h x e ρ` of `ρ` by `ψ_x` that are unramified outside `S` and obey the relations `L`,
with coefficients mapped by `e`. 

### `exists_matrix_selmerAtPoint_equiv`

 Let `ℓ ≠ 0` and `q` be natural numbers, let `h j : Gal(Ω/E) → ℤ / q` be finitely many locally
constant homomorphisms, and let `ρ` be a representation of `Gal(Ω/E)` by matrices over `O` that is
locally constant modulo `ℓ ^ M`. Let `S` be a finite set of finite places of `E`. There is a matrix
`A` over `MvPolynomial σ O`, with finitely many columns and possibly infinitely many rows, such that
`Sel(x)` is isomorphic to the kernel of `A` evaluated at `x` on a power of `O' / ℓ ^ M`. This holds
for all `e : O → O'` and all points `x : σ → O'`. 

### `exists_isLeast_length_selmerAtPoint`

 Let `ℓ ≠ 0`, let the homomorphisms `h j : Gal(Ω/E) → ℤ / q` and the representation `ρ` over `O`,
taken modulo `ℓ ^ M`, be locally constant, let `S` be a finite set of primes of `E` and let `L` be
any set of relations `∑ γ, f γ • c γ = 0` on cocycles `c`. There is a set `𝓜` of polynomials over
`O` such that, at every point `x` over a discrete valuation ring `O'` of characteristic zero, the
length of `Sel(x)` is the least valuation of a value `P(x)`, `P ∈ 𝓜`. 

### `exists_sharp_polynomial`

 Let `ℓ ≠ 0`, let the homomorphisms `h j : Gal(Ω/E) → ℤ / q` and the representation `ρ` over `O`,
taken modulo `ℓ ^ M`, be locally constant, let `S` be a finite set of primes of `E` and let `L` be
any set of relations `∑ γ, f γ • c γ = 0` on cocycles `c`. Let `x₀` be a point over a discrete
valuation ring `O₀` of characteristic zero, with `e₀ : O → O₀`. There is a polynomial `P` over `O`
such that the valuation of `P(x₀)` is the length of `Sel(x₀)`, and the valuation of `P(x)` is at
least the length of `Sel(x)` at every point `x` over a ring of the same kind. 
