---
{
  "module": "src/Lib/GaloisRep/Main/Defs.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/GaloisRep/Main/Defs.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/GaloisRep/Main/Defs.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Weights, Hecke polynomials, eigenforms and the filter of most Frobenii

The automorphic side concerns functions `f` on the finite adelic points `New.Gf E n` of the definite
unitary group, with values in a complex vector space, under right translation `New.rightRegular`. At
a split place `w` (one with `star w ≠ w`), `GL n (E_w)` acts through `New.ofSplitPlace`, and
`q = New.FinPlace.q w` is the order of the residue field. We define weights and their jumps, Hecke
polynomials built from the eigenvalues of the Hecke operators `New.heckeSplit`, and eigenforms.

## Main definitions and results

* `New.Weight`, `New.jumps`: weights, and the multiset of integers attached to an embedding.
* `New.heckePoly`, `New.HasHeckePolyAt`: the polynomial made from the eigenvalues of the Hecke
  operators `New.heckeSplit`, and the statement that `f` is spherical at `w` with this polynomial.
* `New.IsEigenform`, `New.IsSphericalOff`: eigenforms at almost all places of prime norm, and at all
  split places outside a finite set and its conjugate.
* `New.HasHeckePolyAt.isMonicOfDegree`: the Hecke polynomial of a nonzero spherical eigenvector
  (`New.HasHeckePolyAt`) of rank `n` is monic of degree `n`.
* `New.mostFrobenii`: the filter. `New.mostFrobeniiAt` adds that the Frobenius element `frob` tends
  to `g`.
* `New.dense_of_mostFrobenii`: a property of most Frobenius elements holds on a dense set; hence the
  filters `New.mostFrobeniiAt` are not trivial.

Notions from other files:
* `New.IsFrob`: `σ` stabilises the valuation subring `A` and `σ • x ≡ x ^ q` modulo the maximal
  ideal for all `x ∈ A`.
* `New.IsPlaceOver`: The valuation subring A of Ω lies over the prime w of E: an integer of E is in
  the maximal ideal of A exactly when it lies in w.
* `New.stdLevel`: The subgroup K_0 = G_f ∩ GL_n(Ô) of the finite adelic unitary group, the
  stabiliser of the standard lattice Ô^n.

## Relation to the literature

Known; see `Lib.GaloisRep.Main.OddRank`, `Lib.GaloisRep.LocalGlobal.LabelCompatibility` and
`Lib.ClassField.Global.Chebotarev` for sources.



## Weights, Hecke polynomials and eigenforms on the definite unitary group

Besides the notions of the file head, this section defines `New.HasLabel`, a condition on the action
of `GL n` of the residue field at `w`.


### `Weight`

 Weights. For `κ : Weight E` and an infinite place `v` of `E`, `κ.1 v h` is the number of columns
of height `h` of a Young diagram, and `κ.2 v` is an integer exponent of the determinant. 

### `heckePoly`

 For natural numbers q, N and a sequence t in a commutative ring, the polynomial Σ_{j=0}^{N}
(−1)^j q^{j(j−1)/2} t_j X^{N−j}. 

### `HasHeckePolyAt`

 `f` is spherical at the split place `w` with Hecke polynomial `P`: the maximal compact subgroup
`maxCompactAt n w` at `w` and `star w` fixes `f`, the `j`-th Hecke operator at `w` (`heckeSplit`)
acts on `f` by a scalar `t j`, and `P = heckePoly q (Fintype.card n) t`, that is
`P = Σ_j (−1)^j q^{j(j−1)/2} t_j X^{n−j}`, with `q` the order of the residue field at `w`. 

### `IsEigenform`

 `f` is an eigenform for the system `P` of polynomials: `f ≠ 0`, and for all but finitely many
places `w`, if the norm of `w` is prime then `w` is split (`star w ≠ w`) and `f` is spherical
at `w` with Hecke polynomial `P w` (`New.HasHeckePolyAt`). Splitting is part of the assertion. 

### `IsSphericalOff`

 `f` is spherical off the finite set `S` of places with Hecke polynomials `P`: `f ≠ 0`, `f` is
fixed by the integral points `stdLevel E n` that are trivial at the places of `S`
(`Gf.trivialOn n S`), and `f` has Hecke polynomial `P w` (`New.HasHeckePolyAt`) at every split
place `w` with `w ∉ S` and `star w ∉ S`. 

### `HasLabel`

 `f` has the label `Ξ`, a function on `GL n (ResField w)` with `ResField w` the residue field at
the split place `w`: the kernel of the reduction `reduceGL` from the integral matrices
`intGL n Valued.v.integer` at `w` to `GL n (ResField w)` fixes `f`, and the sum over `x` of
`star (Ξ x)` times the translate of `f` by a lift of `x` is nonzero. 

### `jumps`

 The multiset {j − 1 − λ_j} if σ is in the CM type `Φ`, that is if σ equals `Φ v`, the embedding
that `Φ` picks at the place v of σ, else {λ_j + N − j}, 1 ≤ j ≤ N, with λ the highest weight of κ at
the place v of σ: λ_j = `κ.2 v` + Σ_{j ≤ h < N} `κ.1 v h`. The index in the code is j − 1, and `u`
is λ_j + N − j. 


## Coefficients and monicity of Hecke polynomials; distinct jumps

* `New.coeff_heckePoly`: the coefficients of
  `New.heckePoly q N t = ∑ j, (-1) ^ j q ^ (j choose 2) t j X ^ (N - j)`.


### `New.coeff_heckePoly`

 The coefficient of `X ^ j` in `heckePoly q N t` is
`(-1) ^ (N - j) q ^ (N - j choose 2) t (N - j)` for `j ≤ N`, and `0` otherwise. 

### `New.HasHeckePolyAt.isMonicOfDegree`

 Let `f ≠ 0` be a function on the finite adelic unitary group `Gf E n`, and let `P` be its Hecke
polynomial at the split place `w` (`New.HasHeckePolyAt`). Then `P` is monic of degree
`Fintype.card n`. 

### `New.Weight.nodup_jumps`

 The jumps of a weight at an embedding are distinct: the multiset `jumps κ N σ` has no
repetition. 


## The filter of most Frobenii and density by Chebotarev

A filter that expresses that a property holds for most Frobenius elements.


### `FrobeniusDatum`

 A finite place w = `place` of E of prime norm, a valuation subring A = `valuationSubring` of Ω
(a term of `ClosurePlace`) above w in the sense of `IsPlaceOver`, and a geometric Frobenius
s = `frob` in Gal(Ω/E) at A. 

### `FrobeniusDatum.place`

 The finite place of `E`. 

### `FrobeniusDatum.valuationSubring`

 The valuation subring of `Ω`. 

### `FrobeniusDatum.frob`

 The element of the Galois group of `Ω` over `E`. 

### `FrobeniusDatum.prime_q`

 The norm of the place is a prime number. 

### `FrobeniusDatum.isPlaceOver`

 The valuation subring lies over the place. 

### `FrobeniusDatum.isFrob_inv`

 The inverse of the element is an arithmetic Frobenius at the valuation subring. 

### `mostFrobenii`

 The filter 'most Frobenii' on `New.FrobeniusDatum E`. A set `X` of data `(w, A, s)` belongs to
it if each nonempty open `V ⊆ Gal(Ω/E)` has a nonempty open part `O` such that, for almost all `w`,
`X` contains every datum `(w, A, s)` with `s ∈ O`. 

### `mostFrobeniiAt`

 The filter of most Frobenii tending to `g`: `New.mostFrobenii` on data `(w, A, s)`, refined by
the condition that `s` lies near `g`. 

### `tendsto_mostFrobeniiAt`

 For a continuous `f` on `Gal(Ω/E)`, the values of `f` at the Frobenius elements tend to `f g`
along the filter `mostFrobeniiAt E g` of most Frobenii tending to `g`. 

### `tendsto_place_mostFrobenii`

 Along most Frobenius data the place leaves every finite set: a property of all but finitely
many places holds at the place of most Frobenius data. 

### `eventually_mostFrobenii`

 If `p` holds at all but finitely many places, and `p` at the place of a Frobenius datum
implies `q` of the datum, then `q` holds for most Frobenius data. When `q x` is `p x.place`, pass
`fun _ ↦ id` as `h_imp`. 

### `eventually_mostFrobenii_of_isOpenEmbedding`

 Let `φ` be an open embedding of `Gal(Ω/E)` in `Gal(Ω/F)`, `π` a map from the finite places of
`E` to those of `F`, and `X` a set that contains most Frobenius data over `E`. Then for most data
`y` over `F`, the set `X` contains every datum over `E` whose place and Frobenius element are sent
by `π` and `φ` to those of `y`. 

### `dense_of_mostFrobenii`

 If most Frobenius data `(w, A, s)` satisfy `p s`, then `p` holds on a dense subset of
`Gal(Ω/E)`. 
