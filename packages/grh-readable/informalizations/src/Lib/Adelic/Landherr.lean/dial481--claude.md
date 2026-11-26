---
{
  "module": "src/Lib/Adelic/Landherr.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Adelic/Landherr.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Adelic/Landherr.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Sums of two squares, Landherr's theorem and the Hasse principle for unitary cocycles

Let `E` be a CM field with `New.HasPrimitiveRoot5040 E`, and let `F` be its maximal real subfield.
The file starts with a result on sums of two squares in quadratic algebras over `F`. It then proves
Landherr's theorem: a hermitian space that has an orthonormal frame at the finite places is
determined up to rational isometry by its signs at the infinite places. Finally it proves the Hasse
principle for cocycles of a cyclic Galois group of prime order in the definite unitary group, which
is used for base change. There `E' / E` is a Galois extension of CM fields of prime degree, and
`σ ≠ 1` generates its group.

## Main definitions and results

* `New.exists_sq_add_sq_quadraticAlgebra`: for `E` with a CM type, a totally positive `p` in `F` is
  a sum of two squares in `F[X] / (X² - (q p - B²))` for every `B` in `F`. This holds when `p` has
  valuation `1` outside a set `S` of finite places of `E`, and `q` has valuation `1` at the places
  of `S` and at their complex conjugates.
* `New.Core.exists_form_eq_one`: a hermitian matrix representing `1` over the adeles does so over
  `E`.
* `New.Core.exists_rat_frame_of_adelic`: the same for a diagonal matrix of signs, by induction on
  the columns.
* `New.Space.landherr`, `New.Space.exists_x_eq_and_ratEmbed_conj_eq`: two spaces with the same signs
  differ by a rational change of basis and by moving the point.
* `New.U.hasse_principle_coboundary`: a cocycle that splits over the finite adeles splits
  rationally; the proof combines Hilbert 90 for `GL n` with Landherr's theorem `New.Space.landherr`.

Notions from other files:
* `New.CMType`: makes the field `E` a CM number field with a chosen complex embedding `Φ w` of `E`
  for each infinite place `w`.
* `New.𝔸`: the product of one copy of `ℂ` for each infinite place of `E` and the finite adeles
  `𝔸f E`; this is the adele ring of `E` when `E` is totally complex.
* `New.Space`: a hermitian space with a point. It is a matrix `J` over `E` and `x : GL n (𝔸 E)`
  with `xᴴ J x` equal to `New.stdForm E s`, which is `diag(s)` at the infinite places and `1` at
  the finite places.

## Relation to the literature

Known result: Landherr's Hasse principle for hermitian forms. The Hasse principle is proved only
for adelically unimodular spaces of equal signature over a CM field containing the roots of unity of
order 5040. It uses Hasse's norm theorem and strong approximation for the adeles instead of
Hasse-Minkowski. Source: W.
Landherr, Äquivalenz Hermitescher Formen über einem beliebigen algebraischen Zahlkörper, Abh. Math.
Sem. Hamburg 11 (1936) 245-248; M. Kneser, Lectures on Galois cohomology of classical groups, TIFR
47 (1969), §5.5.



## A totally positive number as a sum of two squares

Here `QuadraticAlgebra F μ 0` is `F[X] / (X² - μ)`.


### `New.exists_norm_eq_of_forall_mem_closure`

 Hasse principle for sums of two squares: a totally positive element `x` of a number field `M`
that is a limit of sums of two squares in the completion at each finite place is a sum of two
squares. Sums of two squares are written as norms from `M[X] / (X² + 1)`. 

### `New.exists_norm_eq_sq_add_sq`

 Let `E` be a CM field with a primitive root of unity of order `5040` and maximal real subfield
`F`. The norm to `F` of an element of `E` is a sum of two squares in `F`. 

### `New.mem_closure_range_norm_of_apply_eq`

 Let `E` be a CM field with a primitive root of unity of order `5040` and maximal real subfield
`F`, and let `u` be a finite place of `E` above the place `v` of `F`. Let `a` be a finite adele of
`E` that is fixed by conjugation and is a unit at every place. If the component of `a` at `u` is an
element `s` of `F`, then `s` is a limit of norms from `E` in the completion of `F` at `v`. 

### `New.exists_sq_add_sq_quadraticAlgebra`

 Let `E` be a CM field with a CM type and a primitive root of unity of order `5040`, and let `p`,
`q`, `B` lie in its maximal real subfield `F`. Suppose that `p` is totally positive and has
valuation `1` at every finite place of `E` outside `S`. Suppose also that `q` has valuation `1` at
every place of `S` and at its complex conjugate. Then `p` is a sum of two squares in
`F[X] / (X² - (q p - B²))`: it is the norm of an element of the extension of this algebra by a
square root of `-1`. 


## Landherr's theorem

Vectors are one-column matrices `Matrix n Unit _`.


### `Core.exists_norm_eq_norm_one_add_mul`

 Let `E` be a CM field and `σ` an adele of `E`, written as a `1 × 1` matrix. Then there are
adeles `a` and `b = 1 + σ a` of the same norm: `ā a = b̄ b`. 

### `Core.exists_form_pos_and_unit`

 Let `K` be a matrix over `E` that represents `1` over the adeles, into which `toAdele` embeds
`E`, and let `S` be finite. Then the value of `K` at some rational vector has positive real part
under each embedding `Φ w` of the CM type and is a unit at `S.conjClosure`, the places of `S` and
their conjugates. 

### `Core.exists_form_eq_one`

 Hasse principle for representing `1`: let `E` satisfy `New.HasPrimitiveRoot5040` and let `K` be
a hermitian matrix over `E`, possibly degenerate. If `zᴴ K z = 1` for an adelic vector `z`, then
`wᴴ K w = 1` for a vector `w` over `E`. 

### `Core.conjTranspose_one_add_mul_mul_self`

 If `uᴴ u = 1`, and `u` and `uᴴ` are eigenvectors of `D` with eigenvalue `c`, then shearing by
`1 + u ρ` adds `c (u ρ + (u ρ)ᴴ + ρᴴ ρ)` to `D`. 

### `Core.exists_gram_eq_gram_compl_add_single`

 Let `J` be hermitian, `c * c = 1`, `wᴴ (c J) w = 1`, and let `J'` be `J` projected to the
orthogonal complement of `w`. For a matrix `A` there is `A'`, namely `A` with its columns projected
to that complement and `w` added to column `j`, with `A'ᴴ J A' = Aᴴ J' A + c eⱼ eⱼᵀ`. 

### `Core.exists_rat_frame_of_adelic`

 Hasse principle for partial frames: let `E` satisfy `New.HasPrimitiveRoot5040`, let `J` be
hermitian over `E`, possibly degenerate, let `s` be a family of signs indexed by `n`, and let `D` be
the diagonal matrix with the sign `s i` at `i ∈ t` and `0` elsewhere. If `Xᴴ J X = D` for a square
matrix `X` over the adeles `𝔸 E`, into which `toAdele` embeds `E`, then `Aᴴ J A = D` for a square
matrix `A` over `E`. 

### `Space.landherr`

 A case of Landherr's theorem. Let `E` be a CM field containing a primitive root of unity of
order `5040`, and let a `Space E n s` be a Hermitian matrix `J` over `E` together with an adelic
`x : GL n (𝔸 E)` such that `xᴴ J x` is `diag(s)` at the infinite places and `1` at the finite
places. Then any two such spaces `V`, `W` with the same signs `s` are equivalent over `E`: there is
`a : GL n E` with `aᴴ V.J a = W.J`. 

### `Space.exists_x_eq_and_ratEmbed_conj_eq`

 Landherr's theorem for spaces with a point, for a CM field `E` satisfying
`New.HasPrimitiveRoot5040`. A space `Space E n s` is a Hermitian matrix `J` over `E` with a point
`x : GL n (𝔸 E)` such that `xᴴ J x` is `diag(s)` at the infinite places and `1` at the finite
places. Two spaces `V`, `W` with the same signs `s` differ by a rational change of basis `a` and by
moving the point by some `g` in the adelic unitary group `G E s`: `aᴴ V.J a = W.J`,
`W.x = a⁻¹ V.x g`, and under the embeddings `New.Space.ratEmbed` into `G E s` (sending `γ` to
`x⁻¹ γ x`), the map `γ ↦ a γ a⁻¹` from `U W.J` to `U V.J` becomes conjugation by `g`. Here
`g.toUnitary` is `g` as a matrix over `𝔸 E`, and `toAdele` embeds `E` in `𝔸 E`. 


## Galois descent and the Hasse principle for unitary cocycles

`New.twistedNorm τ p δ` is the twisted norm `δ · τ δ ⋯ τ^(p-1) δ`; `New.U.mapEnd` and `New.galoisGf`
are the entrywise actions of `σ` on rational and finite adelic unitary matrices.


### `aeval_radical_charpoly`

 A normal matrix over a CM field (one commuting with its conjugate transpose) is killed by
the radical of its characteristic polynomial. 

### `mem_range_algebraMap_of_fixed_of_prime`

 For E'/E a Galois extension of number fields of prime degree and σ ≠ 1 in its Galois group,
every element of E' fixed by σ lies in E. 

### `mem_range_finAdeleIncl_of_adeleMap_eq`

 For E'/E a Galois extension of number fields of prime degree and σ ≠ 1 in its Galois group,
every finite adele of E' fixed by σ comes from a finite adele of E. Here `adeleMap σ` is the action
of σ on the finite adeles `𝔸f E'` and `finAdeleIncl E E'` includes the finite adeles of E in
these. 

### `U.hasse_principle_coboundary`

 Hasse principle for `H¹(⟨σ⟩, U(n))`, with `U(n) = {g | gᴴ g = 1}`, where `E' / E` is a Galois
extension of CM fields of prime degree `p` and `σ ≠ 1` is in its Galois group. Let `s` be a point
over `E'` such that `s = u σ(u)⁻¹` for a point `u` over the finite adeles of `E'` and the twisted
norm `s σ(s) ⋯ σ^(p-1)(s)` is `1`. Then `s = g σ(g)⁻¹` for a point `g` over `E'`, written as
`σ(g) = s⁻¹ g`. Here `Gf E' n` is the unitary group over the finite adeles, `map` takes `s` into it,
and `U.mapEnd` and `galoisGf` apply `σ` to each entry, `map_star_CM` saying that `σ` commutes with
complex conjugation. Landherr's theorem needs that `E` has a CM type and a primitive root of unity
of order `5040` (`CMType`, `New.HasPrimitiveRoot5040`). 
