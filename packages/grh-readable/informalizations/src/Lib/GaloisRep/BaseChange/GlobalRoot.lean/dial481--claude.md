---
{
  "module": "src/Lib/GaloisRep/BaseChange/GlobalRoot.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/GaloisRep/BaseChange/GlobalRoot.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/GaloisRep/BaseChange/GlobalRoot.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Idele Hasse principle, unitary roots and rationality of adelic roots up to coboundary

The main setting is a cyclic extension `E'/E` of CM fields of prime degree with character `μ`
(`New.IsStep`: `μ` kills `Eˣ`, and each idele `t` of `E` with `μ (t * star t) = 1` is a norm from
`E'` times an element of `Eˣ`) and Galois automorphism `σ`. For a unitary matrix `γ` and a
polynomial `z`, `New.IsRootQuotient γ z a` means `a * z(γ)ᴴ = z(γ)`. The file proves a Hasse
principle for ideles in a single CM field `L` and develops the calculus of this relation. It
combines the two to show that an adelic root for a `σ`-fixed characteristic polynomial is rational
up to a coboundary.

## Main definitions and results

* `New.exists_isSelfAdjoint_principalIdele_mul`: an adele `w` with `w = x * star w`, `x` in `L`,
  becomes conjugation invariant after multiplication by an element of `Lˣ`.
* `New.IsStep.exists_isSelfAdjoint_of_mem_kerCompNorm`: the twisted form, for an idele in
  `kerCompNorm L μ` whose norm under a Galois automorphism `g` has this property, where `x` is fixed
  by `g` and `E'[x] = ⊤`. It uses the Artin map, Hasse's norm theorem and Hilbert 90 for ideles.
* `New.U.existsUnique_isRootQuotient`: if `z(γ)` is invertible there is exactly one unitary `a`.
* `New.exists_global_root`: let `z` be a root for `P`, where `P` is the characteristic polynomial of
  a unitary matrix over `E'` and is fixed by `σ`. Then there are a rational `w` and an adelic `c`
  with the following property. Let `x = w * z * σ c`. At every adelic unitary `γ` killed by the
  radical of `P`, `x(γ)` is invertible, and `a = x(γ) / x(γ)ᴴ` satisfies `a * c(γ)ᴴ = c(γ)`.

Notions from other files:
* `New.adeleMap`: For an embedding f: K → L of number fields, the induced ring homomorphism from the
  finite adeles of K to those of L.
* `New.kerCompNorm`: The group of finite ideles of E' whose norm to E is killed by μ.
* `New.U.mapEnd`: The endomorphism of the unitary group {g : gᴴg = 1} over R given by applying
  entrywise a ring endomorphism σ commuting with the involution.

## Relation to the literature

Known; see `Lib.GaloisRep.BaseChange.PrimeDegreeTransfer` for sources.



## The Hasse principle for ideles in one CM field

The Hasse principle behind `New.exists_global_root`, in a single CM field `L`.


### `New.exists_isSelfAdjoint_principalIdele_mul`

 Let `L` be a CM field. If the finite adele `w` satisfies `w = x * star w` with `x` in `L`, then
`y * w` is invariant under conjugation for some `y` in `Lˣ`. 

### `New.finAdeleIncl_adeleNorm_fixedField_zpowers`

 The norm from `L` to the fixed field of `g` is the product of the conjugates under the powers
of `g`. 

### `New.exists_principalIdele_div_mul_adeleMap_eq`

 Let `K` be the fixed field of `g ∈ Gal(L/E)`, and let `t` be a finite idele of `L` whose norm to
`K` is the principal idele of a totally positive `k`. Then `z / t * g c = c` for some `z` in `Lˣ`
and some invertible finite adele `c`. 

### `New.isCMField_fixedField_zpowers`

 Let `L` be a CM field and `g` an automorphism of `L` over the CM field `E`. Then the fixed field
of `g` is a CM field: it is stable under conjugation, which commutes with `g`. 

### `New.IsStep.exists_isSelfAdjoint_of_mem_kerCompNorm`

 Hasse principle in one CM field. Let `E'/E` be a step with character `μ` (`IsStep`): `E`
contains a primitive 5040th root of unity, `E'` is a CM field Galois over `E` of prime degree, and
`μ` is a finite idele character of `E` with open kernel, trivial on `Eˣ`. Let `L = E'[x]` be a CM
field, and let `g ∈ Gal(L/E)` fix `x` and have order `n`. Let `u` be a finite idele of `L` with
`μ (N_{L/E} u) = 1` whose norm `N = ∏_{i < n} g ^ i u` satisfies `N = x * star N`. Then
`star c * (z * u * g c)` is self-adjoint for `star` for some `z` in `Lˣ` and some invertible finite
adele `c`. 

 ## Unitary roots, twisted norms and products of matching pairs 

### `instance : IsStarNormal γ.val.val`

 A unitary matrix commutes with its adjoint, which is its inverse. 

 ### Roots 

### `U.isRootQuotient_conj`

 Suppose `γ * c = c * γ'` in the unitary group and `a` satisfies `a * z(γ')ᴴ = z(γ')`
(`New.IsRootQuotient`). Then the conjugate `c * a * c⁻¹` satisfies the same relation for `γ`
and `z`. 

### `U.isRootQuotient_map`

 Let `f` be a ring homomorphism commuting with the involutions. If `a * z(γ)ᴴ = z(γ)`, then
applying `f` to `γ`, to `a` and to the coefficients of `z` preserves this relation. 

### `U.existsUnique_isRootQuotient`

 If `z(γ)` is invertible, exactly one unitary `a` satisfies `a * z(γ)ᴴ = z(γ)`
(`New.IsRootQuotient`), namely `z(γ) * (z(γ)ᴴ)⁻¹`. 

### `IsRootQuotient.mul`

 If `x * z(γ)ᴴ = z(γ)` and `y * w(γ)ᴴ = w(γ)`, then `(x * y) * (z * w)(γ)ᴴ = (z * w)(γ)`: the
values of polynomials at `γ` commute with their adjoints. 

 ### Matching pairs and norms 

### `IsMatchingPair.mul`

 Let `u`, `v` be orthogonal self-adjoint idempotents. If `(f, φ)` is a matching pair for `u` and
level `K` and `(f', φ')` one for `v` and level `L`, then the products `(f * f', φ * φ')` form a
matching pair for `u + v` and level `K ⊓ L`. 

### `IsRootQuotient.twistedNorm_eq_mul`

 Let `z(γ)` be invertible, and let `a * z(γ)ᴴ = z(γ)`. Let `γ * N(γ)ᴴ = N(γ)` for
`N = twistedNorm (.map σ) p z = z * σ(z) * ⋯ * σ^(p-1)(z)` (likewise `twistedNorm (mapEnd hσ) p
c = c * σ(c) * ⋯ * σ^(p-1)(c)`), and let `c` conjugate `σ γ` to `γ`. Then the twisted norm of `c` is
`γ` times that of `a⁻¹ * c`. 


## Rationality of adelic roots up to a coboundary

The global step of the comparison of traces for a cyclic extension `E'/E` of prime degree
(`New.IsStep`, with its character `μ`). A root (`New.IsNormRoot`) for a polynomial `P` is an adelic
polynomial `z` whose `σ`-norm `N` satisfies `γ = N(γ) / N(γ)ᴴ` at unitary `γ` with characteristic
polynomial `P`, with a determinant condition given by `μ`.

The proof of `New.exists_global_root` works in the CM fields `E'[X] / (q)` for the prime factors `q`
of `P`, applies the Hasse principle `New.IsStep.exists_isSelfAdjoint_of_mem_kerCompNorm` at each
prime factor fixed by `σ`, and glues along the orbits of `σ`.


### `New.U.conjTranspose_aeval`

 If `v(γ)` inverts the unitary matrix `γ`, the adjoint of `f(γ)` is obtained by conjugating the
coefficients of `f` and substituting `v` for `X`. 

### `New.U.mul_star_eq_one_of_isRoot_charpoly`

 The complex eigenvalues of a unitary matrix over a CM field have absolute value `1`. 

### `New.exists_forall_map_dvd_sub`

 The Chinese remainder theorem for the prime factors of `P`, after a change of coefficients. 

### `New.aeval_eq_of_forall_map_dvd_sub`

 Polynomials congruent modulo every prime factor of `P` agree at an element killed by the
radical of `P`. 

### `New.exists_orbit_representatives`

 Each orbit of a permutation `τ` of a finite type has a representative `r a`, and the position
`j a` of `a` on its orbit, counted from `r a`, grows by one modulo the period under `τ`. 

### `New.exists_isSelfAdjoint_along_orbits`

 Transport along the orbits of `τ`. Let `θ a` read `B` in a star ring `A a`, with
`θ (τ a) (T b) = u (τ a) * g a (θ a b)` for units `u`. If at each `a` some `b` with `θ a b` a unit
and `y` in `Y a` make `star (θ a b) * (ι a y * θ a (T^[period of a] b))` self-adjoint, then some
`y a`, `c a` make `ι a (y a) * θ a (T b)` a unit and `star (θ a b)` times it self-adjoint, at every
`a`, whenever `θ a b = θ a (c a)` for all `a`. 

### `New.orderOf_eq_of_semiconj`

 An automorphism of `E'[X] / (q)` that extends `σ` and fixes the root has the prime order
of `σ`. 

### `New.IsRootQuotient.charpoly_dvd_pow`

 If `γ * N(γ)ᴴ = N(γ)` and `v(γ)` inverts `γ`, the same relation holds for the polynomial `N`
up to nilpotents modulo the characteristic polynomial of `γ`. 

### `New.isUnit_and_isRootQuotient_of_isSelfAdjoint`

 Let the maps `θ i` detect equality of values at `γ`, and let `β` represent both the adjoint at
`γ` and `star` under each `θ i`. If `x` has an inverse `x'` and `star c * x` is self-adjoint
under every `θ i`, then `x(γ)` is invertible, and every `a` with `a * x(γ)ᴴ = x(γ)` also has
`a * c(γ)ᴴ = c(γ)`. 

### `New.U.mul_star_eq_one_of_mem_roots_of_dvd`

 The complex roots of a factor `q` of the characteristic polynomial `P` of a unitary matrix over
a CM field have absolute value `1`. 

### `New.smul_mem_primeFactors_of_smul_eq`

 An automorphism `σ` of `E'` over `E` that fixes the nonzero polynomial `P` maps each prime
factor of `P` to a prime factor of `P`. 

### `New.IsNormRoot.dvd_pow_of_charpoly_eq`

 Let `z` be a norm root for `P` over `R` with `u = 1` (`New.IsNormRoot`), let `γ` be a unitary
matrix with characteristic polynomial `P`, and let `v' * P + v * X = 1`. Then `P` divides a power
of `X * N̄(v) - N`, where `N` is the twisted norm of `z` under `σ` and `N̄` has conjugated
coefficients. 

### `exists_mem_coe_eq_norm_aeval_of_forall_det_aeval_mem`

 Let `A` be a finite free algebra over `R` and `D` a subgroup of `Rˣ`. If `det z(M)` lies in `D`
for every square matrix `M` over `R` with `P(M) = 0`, then the norm of `z(a)` from `A` to `R` lies
in `D` for every `a` in `A` with `P(a) = 0`. 

### `Polynomial.mapRingHom_pow_apply`

 The `i`-th power of `Polynomial.mapRingHom f` maps the coefficients by `f ^ i`. 

### `New.coe_principalIdele`

 The finite idele of `y` in `Lˣ` is the image of `y` in the finite adeles. 

### `New.IsStep.exists_isSelfAdjoint_principalIdele_of_dvd_pow`

 The Hasse principle at one prime factor `q`, for the step `E'/E` with character `μ` and `σ` of
prime order `p`. Here `θ` presents the adeles of the CM field `L = E'[X] / (q)` as adelic
polynomials modulo `q`, and `T c = z * σ c`. Here `θ (f̄(v)) = star (θ f)`, `θ z` is a unit with
norm in `kerCompNorm E' μ`, and `q` divides `(X * N̄(v) - N) ^ m` for the twisted norm `N` of `z`.
For `l = p`, or `l = 1` when `σ` fixes `q`, some `y` in `Lˣ` and `c` with `θ c` a unit make
`star (θ c) * (y * θ (T^[l] c))` self-adjoint. 

### `New.exists_isSelfAdjoint_principalIdele_of_forall_minimalPeriod`

 Transport along the orbits of `σ` (as `τ` on the prime factors `q` of `P`). `θ q` evaluates at
the root of `q` in `𝔸f (E'[X] / (q))`, and `T c = z * σ c` with all `θ q z` units. If at each `q`
some unit `y` and `c` with `θ q c` a unit make `star (θ q c) * (y * θ q (T^[period of q] c))`
self-adjoint, then some `y q`, `c₀ q` make `y q * θ q (T c)` a unit and `star (θ q c)` times it
self-adjoint at all `q`, for every `c` with `θ q c = θ q (c₀ q)` for all `q`. 

### `New.exists_isUnit_aeval_and_isRootQuotient_of_isSelfAdjoint`

 From solutions on the orbits to one global solution: transport along the orbits of `σ`, which
permutes the prime factors `q` of `P` as `τ`, then glue by the Chinese remainder theorem. Here
`v * X ≡ 1` mod `P`, and `θ q` presents the adeles of `E'[X] / (q)` as adelic polynomials modulo
`q`. Also `z` is a unit mod each `q` and `T c = z * σ c`. For each `q`, some unit `y` of `E'[X]/(q)`
and some `c` that is a unit mod `q` make `star c · y · T^[k] c` self-adjoint mod `q`, where `k` is
the length of the `τ`-orbit of `q`. Then some `w` over `E'` and adelic `c` make `x = w * T c`
satisfy, at each adelic unitary `γ` killed by the radical of `P`: `x(γ)` is a unit, and
`a * x(γ)ᴴ = x(γ)` implies `a * c(γ)ᴴ = c(γ)`. 

### `New.exists_global_root`

 Let `E'/E` be a step with character `μ`, `σ ≠ 1` with `σ ^ p = 1`, `p` prime, `P` the `σ`-fixed
characteristic polynomial of a unitary matrix over `E'`, and `z` a norm root for `P` (its twisted
norm `N` has `γ * N(γ)ᴴ = N(γ)` at adelic unitary `γ` with charpoly `P`;
`det z(A) ∈ kerCompNorm E' μ` if `P(A) = 0`). Then some `w` over `E'` and adelic `c` make
`x = w * z * σ c` satisfy, at each `γ` killed by the radical of `P`: `x(γ)` is a unit, and
`a * x(γ)ᴴ = x(γ)` gives `a * c(γ)ᴴ = c(γ)`. 
