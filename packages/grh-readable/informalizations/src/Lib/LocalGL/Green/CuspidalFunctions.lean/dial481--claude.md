---
{
  "module": "src/Lib/LocalGL/Green/CuspidalFunctions.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/LocalGL/Green/CuspidalFunctions.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/LocalGL/Green/CuspidalFunctions.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Cuspidal class functions on GL_n over a finite field: μ, supports, values, inner products

Let `k` be a finite field. `New.Hall k` is the ring of functions on the similarity classes
`New.SimClass k` of endomorphisms over `k`, with the parabolic induction product. In it,
𝟙 = `New.Hall.constOne` is the constant function 1, μ = `New.Hall.moebius` is its inverse, and
C_η = `New.Hall.greenCuspidal k η`. The file proves that C_η is cuspidal and that cuspidal functions
vanish off classes whose characteristic polynomial is a power of an irreducible polynomial. It
computes μ and C_η at multiplication by a field generator, and writes the inner product of C_η with
B·μ as a mean over the units of a field extension.

## Main definitions and results

* `New.Hall.crapo_complementation`, `New.Hall.isSemisimple_of_moebius_ne_zero`: μ is a Möbius
  function on the lattice of stable subspaces, so it vanishes off semisimple classes.
* `New.Hall.greenCuspidal_mul_constOne`, `New.Hall.isCuspidal_greenCuspidal`: C_η ∗ 𝟙 = −β_η, and
  C_η is cuspidal.
* `New.Hall.IsCuspidal.exists_charpoly_eq_pow`: a cuspidal function vanishes at the class of `g`
  unless the characteristic polynomial of `g` is a power of an irreducible one.
* `New.greenCuspidal_simClassOf_eq_mul`: the value of `New.Hall.greenCuspidal k η` at the class of
  `g` depends on `η` only at the elements whose Frobenius orbit gives all eigenvalues of `g`.
* `New.rankInner_greenCuspidal_mulMoebius`: the inner product on GL_{[L:k]}(k) of C_η
  (`New.Hall.greenCuspidal`) with B·μ (`New.Hall.mulMoebius`) is the mean over z ∈ L^× of conj η(φz)
  times B at multiplication by z.

Notions from other files:
* `New.Hall.IsCuspidal`: F is cuspidal when its average over block triangular endomorphisms with
  diagonal blocks a, b vanishes whenever both a and b have nonzero dimension.
* `New.Hall.brauerLift`: The class function β_η sending an endomorphism to the sum of η over the
  roots in K of its characteristic polynomial, counted with multiplicity.
* `New.Hall.greenCuspidal`: The class function C_η = (β_η·μ) ∗ 𝟙: the pointwise product of the
  eigenvalue sum β_η with the inverse μ of 𝟙, multiplied in the induction product by the constant
  function 𝟙.

## Relation to the literature

Known result: Brauer lift is a virtual character; cuspidal times Steinberg is induced from a torus.
Brauer induction is not used here. The character induced from the Coxeter torus is instead divided
by the Steinberg character, read as a Möbius function on semisimple classes compatibly with the
Galois action, and only the vanishing half of Crapo's theorem is used. Source: Green 1955, Thm 1; T.
A. Springer, Sém. Bourbaki 441 (1973/74), 1.1-1.7; R. Carter, Finite groups of Lie type (1985), for
Steinberg times a torus character; P. Hall's lemma, D. Krasula, arXiv 2403.05656, Lemma 23, and H.
Crapo's complementation theorem, for the vanishing of the Möbius number off semisimple modules.

See also `Lib.LocalGL.Green.TauFunctions`.


 ## Crapo's lemma, the inverse μ of 𝟙, and cuspidality of C_η 

### `crapo_complementation`

 A form of Crapo's complementation theorem. Let `μ` be a function on a finite modular lattice
whose sum over the elements below `X` vanishes for every `X ≠ ⊥`. If `μ ⊤ ≠ 0`, every element
has a complement. 

 ### The inverse of the constant function 

### `moebius_mul_constOne`

 `μ` is inverse to `New.Hall.constOne`; at `g` this reads: the sum of `μ (g|W)` over the stable
subspaces `W` is `1` in dimension `0` and `0` otherwise. 

### `sum_moebius_simClassOf_endOnSub`

 At the class of `g`, the sum of `μ (g|W)` over the `g`-stable subspaces `W` is the value of the
unit `1` of `New.Hall k` at the class of `g`. 

### `isSemisimple_of_moebius_ne_zero`

 An endomorphism at whose class `μ` does not vanish is semisimple. 

### `blockAverage_mulMoebius`

 Let μ (`moebius`) be the inverse of the constant class function 1 for the parabolic-induction
product on similarity classes over the finite field k. For any class function `B`, the average of
the pointwise product `B μ` over the block triangular endomorphisms with diagonal blocks `a`, `b` is
`μ a * μ b * B (b ⊕ a)`. Here `b ⊕ a` is the block diagonal map of the chosen representatives of `b`
and `a`. 

### `conj_moebius`

 `μ` takes real values: each value is its own complex conjugate. 

 ### The cuspidal function attached to `η` 

### `greenCuspidal_mul_constOne`

 The induction product of `New.Hall.greenCuspidal k η` with the constant function
`New.Hall.constOne` is minus the eigenvalue sum `New.Hall.brauerLift k η`. 

### `greenCuspidal_eq_zero_of_dim_lt_one`

 The value of `New.Hall.greenCuspidal k η` in dimension zero is zero. 

### `isCuspidal_greenCuspidal`

 `New.Hall.greenCuspidal k η` is cuspidal: its block averages vanish when both blocks have
positive size. 


## Supports of cuspidal class functions

Idea: the Fitting decomposition for an irreducible factor of the characteristic polynomial makes all
block triangular maps with the two given diagonal blocks similar.


### `charpoly_eq_pow_of_isNilpotent`

 If `P(g)` is nilpotent, with `P` monic irreducible, the characteristic polynomial of `g` is a
power of `P`. 

### `Hall.IsCuspidal.exists_charpoly_eq_pow`

 Let `F` be a cuspidal element of `Hall k`, the complex-valued functions on similarity classes of
endomorphisms of finite-dimensional `k`-spaces. Cuspidal means that the average of `F` over block
triangular endomorphisms with diagonal blocks `a`, `b` vanishes whenever both blocks have nonzero
dimension. If `F` does not vanish at the similarity class of `g`, then the characteristic polynomial
of `g` is `P ^ j` for some irreducible `P ∈ k[X]` and some `j`. 

### `greenCuspidal_simClassOf_eq_mul`

 Let k be a finite field, `q = |k|`, `d = finrank k V`, and let `greenCuspidal k η` be the class
function (β_η·μ) ∗ 𝟙, where β_η is the eigenvalue sum of η, μ is the inverse of the constant
function 𝟙 for the parabolic-induction product ∗, and β_η·μ is pointwise. Suppose `η'` is `a` times
`η` at every `z` in `K` with `z ^ q ^ d = z` whose Frobenius orbit `z, z ^ q, …, z ^ q ^ (d - 1)`
lists the eigenvalues of `g` in `K`. Then the value of `greenCuspidal` at the class of `g` for `η'`
is `a` times the value for `η`. 


## Values of μ and C_η at multiplication by a field generator

Let z generate a finite extension F = k[z] of k; class functions are evaluated at multiplication by
z.


### `card_GL_eq_prod`

 The order of GL_n(k), for a finite field k with q elements, is the product of q^i (q^{i+1} − 1)
over 0 ≤ i < n, as an identity in any field. 

### `sum_moebius_endOnQuot_eq_zero_of_ne_top`

 Let `g` be an endomorphism of a finite space `V` and `U ≠ V` a `g`-stable subspace. The sum of
μ at the classes of `g` on `V/W`, over the `g`-stable subspaces `W ⊇ U`, is `0`. 

### `moebius_and_greenCuspidal_lsmul`

 Let `F = k[z]` be a finite field extension of the finite field `k`, given by a power basis `z`,
and let `Q` be the number of elements of `F`. Let `V` be an `F`-space of dimension `d`, let
`N = ∏_{0≤i<d} (X − Q^i)`, and let `g` be multiplication by `z` on `V`, viewed as a `k`-linear
endomorphism. Then `moebius` (the inverse μ of the constant function 𝟙 under the induction product
on functions of similarity classes) takes the value `N(0)` at the class of `g`, and
`greenCuspidal k η` (the class function `C_η = (β_η·μ) ∗ 𝟙`) takes the value `−N′(1)` times the sum
of `η` over the roots in `K` of the minimal polynomial of `z`. 

### `moebius_simClassOf_lsmul`

 Let F = k[z] have Q elements and let V be an F-space of dimension d. At multiplication by z
on V, μ = 𝟙⁻¹ takes the value N(0), where N = ∏_{0≤i<d} (X − Q^i). 

### `greenCuspidal_simClassOf_lsmul`

 Let F = k[z] have Q elements and let V be an F-space of dimension d. At multiplication by z
on V, C_η takes the value −N′(1) times the sum of η over the roots in K of the minimal polynomial
of z, where N = ∏_{0≤i<d} (X − Q^i). 

### `mulMoebius_greenCuspidal_lsmul`

 Let k be a finite field, μ (`moebius`) the inverse of the constant class function 𝟙 for the
parabolic-induction product ∗, and C_η = `greenCuspidal k η` = (β_η·μ) ∗ 𝟙 for η : K → ℂ, where β_η
is the eigenvalue sum of η. Let F = k[z] and V a non-zero finite-dimensional F-space. Then the value
of the pointwise product C_η·μ at multiplication by z on V, times #V - 1, is the sum of η over the
roots in K of the minimal polynomial of z, times the order of the centraliser of z in GL_k(V). 


## The inner product of C_η with B·μ

Let L be a finite extension of the finite field k, and let φ be a k-embedding of L into a field K.
Let η be a function K → ℂ.


### `exists_conj_mulLeft_eq`

 Let `L` be a finite field that is a `k`-algebra, and `g` a semisimple `k`-linear endomorphism of
`L` whose characteristic polynomial is a power `P ^ j` of an irreducible `P`. Then `g` is conjugate
to a multiplication: there are a `k`-linear automorphism `e` of `L` and `y ∈ L` with
`e ∘ (y * ·) ∘ e⁻¹ = g`. Both `g` and a root of `P` in `L` make `L` a vector space over `k[X]/(P)`,
of the same dimension. 

### `rankInner_greenCuspidal_mulMoebius`

 Let k be a finite field, K a field over k, η : K → ℂ, and C_η = `greenCuspidal k η` = (β_η·μ)
∗ 𝟙. Here β_η is the eigenvalue sum of η, μ (`moebius`) is the inverse of the constant class
function 𝟙 for the parabolic-induction product ∗, and B·μ is the pointwise product. For a finite
extension L of k with a k-embedding φ : L → K and any class function B, the average over
GL_{[L:k]}(k) of conj C_η times B·μ (`rankInner`) is the mean (`finMean`) over z ∈ L^× of conj η(φz)
times B at the class of multiplication by z on L. 

### `instance : Fact (ringChar k).Prime`

 The characteristic of a finite field is prime. 
