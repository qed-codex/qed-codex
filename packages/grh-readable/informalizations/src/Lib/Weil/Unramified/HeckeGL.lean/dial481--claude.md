---
{
  "module": "src/Lib/Weil/Unramified/HeckeGL.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Weil/Unramified/HeckeGL.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Weil/Unramified/HeckeGL.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Hecke operators of GL_n at a finite place and local criteria for principal level

Let w be a finite place with uniformiser ϖ, let K = `New.localIntGL` = GL_n(O_w), and let k_w be the
residue field. `New.basicDoubleCoset` n w j is the set of g with g and ϖ g⁻¹ integral and det g of
order j. T_j = `New.heckeGL` is the action of its indicator function with vol K = 1. On K-fixed
vectors, T_j is computed as a sum over subspaces of k_w^n, and T_i and T_j are related when
n = i + j.

## Main definitions and results

* `New.basicCosetRep`, `New.basicDoubleCoset_eq`: a representative for each subspace;
  `New.basicDoubleCoset` is one double coset.
* `New.heckeGL_eq_sum`: on K-fixed vectors, T_j is a sum over the subspaces of dimension j.
* `New.heckeGL_dual`: for n = i + j, T_j is ϖ times the operator of the inverse coset of T_i.
* `New.sub_one_mem_span_iff_atPlace`: for an integral point, a congruence modulo `a` is tested at
  the primes dividing `a`.
* `New.inf_supportedOn_le_principalLevel`: integral points supported on primes that, with their
  conjugates, do not divide `a` have principal level `a`.
* `New.block_embFin`: the block matrix `diag (γ, 1)`, relabelled along `ε`, commutes with the
  embedding into finite adeles.

Notions from other files:
* `New.levelSpace`: For a representation π of G, a subgroup K and a character χ of K, the submodule
  of vectors v with π(k)v = χ(k)v for all k in K.
* `New.heckeFun`: For a function f on G, the operator ∑ f(g)π(g), summed over chosen representatives
  g of G/K (zero if infinitely many terms are nonzero): the action of f for vol K = 1.
* `New.U.block`: The block diagonal embedding U(1_m) × U(1_l) → U(1_n) of unitary groups of identity
  matrices, along a bijection of the disjoint union of m and l with n.

## Relation to the literature

Known result: the decomposition of the double coset of diag(ϖ 1_j, 1) in GL_n(E_w) into single
cosets, indexed by the subspaces of dimension j of k_w^n.

See also `Lib.Adelic.Unitary.CongruenceLevels`.



## Basic double cosets of GL_n at a place, indexed by subspaces

For g in `New.basicDoubleCoset` n w j, the coset K g is determined by the kernel of g mod w
(`New.residueKer`), a subspace of k_w^n of dimension j. Every such subspace occurs.

Valuations are multiplicative: `v x ≤ 1` means integral and `v ϖ = exp (-1)`.


### `instance : CompactSpace 𝒪[LocField w]`

 The ring of integers O_w of the local field E_w is compact. 

### `instance : CompactSpace (localIntGL n w)`

 The group GL_n(O_w) = `New.localIntGL` n w is compact. 

 ### Congruence subgroups of GL_n(O_w) 

### `localCongruence`

 The subgroup of GL_n(O_w) of matrices congruent to 1 modulo 𝔭^(m+1), 𝔭 the maximal ideal of
O_w. 

### `mem_localCongruence`

 A matrix g lies in `New.localCongruence` n w m exactly when it lies in GL_n(O_w) and every
entry of g - 1 has valuation at most exp (-(m + 1)), that is, lies in 𝔭^(m+1). 

### `isOpen_localCongruence`

 The congruence subgroups `New.localCongruence` n w m are open in GL_n(E_w). 

### `mem_localCongruence_zero`

 The first congruence subgroup is the kernel of the reduction of GL_n(O_w). 

### `eventually_localCongruence_subset`

 Every neighbourhood s of 1 contains, for all sufficiently large m, the group
`New.localCongruence` of matrices congruent to 1 modulo 𝔭^(m+1), 𝔭 the prime at w. 

### `pow_pow_mem_localCongruence`

 Lifting the exponent in GL_n(E_w): if the natural number q lies in the prime 𝔭 of w and
g ≡ 1 mod 𝔭, then g^(q^k) ≡ 1 mod 𝔭^(k+1). 

 ### Reduction of matrices and the kernel of the reduction 

### `residueOrZero`

 The map from E_w to the residue field at w that reduces integral elements and sends all
others to 0. 

### `residueKer`

 The kernel, in column vectors over the residue field at w, of the entrywise reduction
`New.residueOrZero` of the matrix z. 

### `residueOrZero_eq_zero`

 `New.residueOrZero` x vanishes exactly when x is not a unit of the local integers, that is
when v x ≠ 1. 

### `map_residueOrZero_mul`

 For matrices z and y with integral entries, the entrywise reduction `New.residueOrZero` of
z * y is the product of the reductions of z and of y. 

### `card_sub_rank_eq_finrank_ker`

 For a matrix x over a field k with columns indexed by n, the number of columns minus the rank
of x is the dimension of the kernel of x acting on column vectors. 

### `index_stabilizer_line`

 Over a field with q elements, the subgroup H of GL_n of matrices whose i-th column vanishes
off the diagonal (the stabiliser of a line) has index 1 + q + ⋯ + q^(n − 1). 

 ### The double cosets and their parametrisation by subspaces 

### `diagGL_ite_mem_basicDoubleCoset`

 For a uniformiser ϖ of E_w and a set s of indices, the diagonal matrix with ϖ on s and 1
elsewhere lies in the double coset `New.basicDoubleCoset` n w #s. 

### `finrank_residueKer_diagGL`

 For a uniformiser ϖ of E_w and a set s of indices, the kernel of the reduction modulo w of
the diagonal matrix with ϖ on s and 1 elsewhere has dimension #s. 

### `diagGL_mem_basicDoubleCoset`

 For a uniformiser ϖ of E_w and a set s of indices, the diagonal matrix with ϖ on s and 1
elsewhere lies in the double coset `New.basicDoubleCoset` with j = #s, and the kernel of its
reduction has dimension #s. 

### `mul_mul_mem_basicDoubleCoset`

 The set `New.basicDoubleCoset` n w j is stable under multiplication on both sides by elements
of GL_n(O_w) = `New.localIntGL` n w. 

### `v_mul_inv_le_one_iff`

 For g in the double coset of diag(ϖ 1_j, 1) in GL_n(E_w) and a matrix z over E_w with n
columns, z g⁻¹ is integral if and only if z is integral and the kernel of g mod w lies in
that of z mod w. 

### `mul_inv_mem_localIntGL_iff`

 For g in `New.basicDoubleCoset` n w j and g' in `New.basicDoubleCoset` n w i, the element
g g'⁻¹ lies in GL_n(O_w) if and only if g and g' have the same kernel mod w. 

### `exists_residueKer_eq_and_inv_mul_mem_localIntGL`

 Let g lie in `New.basicDoubleCoset` n w j and let U have the same dimension as the kernel of g
mod w. Then some k in the same double coset has kernel U mod w and lies in g GL_n(O_w). 

### `exists_mem_basicDoubleCoset_residueKer_eq`

 Every subspace U of k_w^n is the kernel of the reduction modulo w of some element of
`New.basicDoubleCoset` n w j with j = dim U. 

### `basicCosetRep`

 For a subspace U of k_w^n (k_w the residue field at w), a chosen element of the double coset
`New.basicDoubleCoset` n w j of diag(ϖ 1_j, 1), j = dim U, whose reduction modulo w has kernel U.
As U runs over the subspaces of dimension j, these elements represent the cosets K g in that
double coset, K = GL_n(O_w). 

### `basicCosetRep_mem_and_residueKer_eq`

 The representative `New.basicCosetRep` U lies in `basicDoubleCoset` d with d = dim U, that is,
in GL_n(O_w) diag(ϖ 1_d, 1) GL_n(O_w). The kernel of its reduction modulo w is U. 

### `finrank_residueKer`

 For g in `New.basicDoubleCoset` n w j, the kernel of the reduction of g modulo w has
dimension j. 

### `basicDoubleCoset_eq`

 For every g in the set `New.basicDoubleCoset` of index j, that set is the double coset GL_n(O_w)
g GL_n(O_w). 

### `instance : Fintype (Submodule (ResField w) (n → ResField w))`

 The space k_w^n over the finite residue field has finitely many subspaces. 

 ### The Hecke operators on vectors fixed by GL_n(O_w) 

### `isHeckeFunction_basicDoubleCoset`

 The indicator function of `New.basicDoubleCoset` n w j is invariant on both sides under
K = GL_n(O_w) and is nonzero on finitely many cosets g K (`New.IsHeckeFunction`). 

### `indicator_basicDoubleCoset_mul_inv`

 The function g ↦ 1_D(g⁻¹), D = `New.basicDoubleCoset` n w j, is invariant under right
multiplication by GL_n(O_w). 

### `heckeFun_basicDoubleCoset_inv`

 Let x be fixed by K = GL_n(O_w), and let D = `New.basicDoubleCoset` j, which is K diag(ϖ 1_j, 1)
K for j ≤ n. Then the Hecke operator `heckeFun` of the function g ↦ 1_D(g⁻¹) sends x to ∑_U
π(γ_U⁻¹)x. The sum runs over the j-dimensional subspaces U of k_w^n (k_w the residue field), and
γ_U = `New.basicCosetRep` U is the chosen element of D whose reduction modulo w has kernel U. 

### `heckeGL_eq_sum`

 Let T_j = `heckeGL` j be the Hecke operator of the double coset K diag(ϖ 1_j, 1) K,
K = GL_n(O_w). On a K-fixed vector x, T_j x is the sum of π(γ_Uᵀ) x over the j-dimensional subspaces
U of k_w^n. Here γ_U = `New.basicCosetRep` U is the chosen element of that double coset whose
reduction modulo w has kernel U. 

### `scalar_mul_mem_basicDoubleCoset_iff`

 Let ϖ be a uniformiser of E_w and n = i + j. Then ϖ x lies in `New.basicDoubleCoset` n w j
exactly when x⁻¹ lies in `New.basicDoubleCoset` n w i: the two integrality conditions are
exchanged, and det (ϖ x) has order n = i + j plus that of det x. 

### `heckeGL_dual`

 Let ϖ be a uniformiser of E_w, n = i + j, and x fixed by GL_n(O_w). Acting on x by the
indicator of the inverse of the double coset of T_i and then by the scalar matrix ϖ gives
T_j x. 

### `heckeGL_zero`

 On a GL_n(O_w)-fixed vector x, the Hecke operator T_0 = `New.heckeGL` π 0 acts as the
identity. 

 ## Local criteria for principal level and block embeddings 

### `sub_one_mem_span_iff_atPlace`

 Let `g` be in `New.stdLevel E n`. The `(i, j)` entry of `g - 1` lies in the `Ô`-ideal generated
by `a` if and only if a local condition holds at every finite place `u` with `a ∈ u`. The condition
is that the valuation of the `(i, j)` entry of `g_u - 1` is at most the valuation of `a` at `u`. 

### `inf_supportedOn_le_principalLevel`

 Suppose that for every place `w` in `S`, neither `w` nor its conjugate `star w` contains `a`.
Then every element of `New.stdLevel E n` lying in `New.Gf.supportedOn n S` lies in
`New.principalLevel n a`. 

### `block_embFin`

 Let `γ` be in the unitary group `U` (`New.U`) of the standard space of `E` with basis `n`.
Form the block matrix `diag (γ, 1)`, relabelled along `ε : n ⊕ Unit ≃ n'` by `New.U.block`. This
block construction commutes with the embedding into the finite adelic group: on the left
`New.Space.embFin`, on the right `New.stdEmbFin`. 
