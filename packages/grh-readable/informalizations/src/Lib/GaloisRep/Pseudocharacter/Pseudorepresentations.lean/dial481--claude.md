---
{
  "module": "src/Lib/GaloisRep/Pseudocharacter/Pseudorepresentations.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/GaloisRep/Pseudocharacter/Pseudorepresentations.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/GaloisRep/Pseudocharacter/Pseudorepresentations.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Spanning criteria, limits of traces and pseudorepresentations

This file gives a criterion for the image of a lattice to span the matrix algebra over the
coefficient ring `O`, using a tame pair with incongruent eigenvalues. It studies uniform
approximation of eigensystems through `New.IsApproximatingMonoid`, and Newton's identities through
`New.newtonPoly`. It proves that over an algebraically closed field of characteristic `0`, a
function obeying every polynomial identity among traces is the trace of a representation. It also
proves that a limit of traces of continuous representations is such a trace.

## Main definitions and results

* `New.exists_rep_of_trace_identities`: over an algebraically closed field of characteristic `0`, a
  function on `G` that obeys every polynomial identity among traces of homomorphisms `G → GL n k` is
  the trace of such a homomorphism with non-degenerate trace form (`New.IsTraceNondeg`).
* `New.GaloisRep.exists_continuous_isTraceNondeg_of_tendsto_trace`: a limit, in the sense of
  `IsApproximatingMonoid` (uniform approximation by linear combinations), of traces of continuous
  representations is the trace of a continuous representation.

Notions from other files:
* `New.IsTraceNondeg`: Non-degeneracy of the trace form on the span of r(G): any x in that span with
  tr(x r(g)) = 0 for all g is zero.
* `New.CoeffRing`: Rings of integers of finite Galois extensions of `ℚ_ℓ` inside `ℚ̄_ℓ`, where the
  class `ThePrime ℓ` records that ℓ is the fixed prime.
* `New.Selmer.IsLatticeIn`: an `O`-valued representation `u` is conjugate in `GL n ℚ̄_ℓ` to a given
  ℓ-adic representation `r`.

## Relation to the literature

Known result: a function obeying the trace identities is the trace of a representation
(pseudocharacters), and the lattice stable under a family spanning the matrix algebra is unique up
to scalars. Here all polynomial identities among traces are assumed, not only the Frobenius
identity, so no invariant theory is needed.
Semisimple means a non-degenerate trace form on the span of the image, in characteristic 0. The file
also proves that a limit of traces of continuous representations is the trace of a continuous
representation. Source: R. Taylor, Galois representations associated to Siegel modular forms of low
weight, Duke Math. J. 63 (1991), Theorem 1; R. Rouquier, Caractérisation des caractères et
pseudo-caractères, J. Algebra 180 (1996); K. Conrad, Compact subgroups of GL_n(Qbar_p) (note).

See also `Lib.GaloisRep.WeightCongruence`.



## A spanning criterion from a tame pair with incongruent eigenvalues

A criterion for residual absolute irreducibility, in the strong form that the image of the group
spans the matrix algebra over the coefficient ring
(`New.Selmer.IsLatticeIn.span_range_eq_top_of_map_pow_eq_map_conj`). In the application `γ` and `φ`
come from tame inertia and Frobenius at an auxiliary place. A spanning family has an absolutely
irreducible reduction (`New.Selmer.eq_bot_or_eq_top_of_span_eq_top`), and its stable lattice is
unique up to scalars (`New.Selmer.exists_eq_smul_of_conj_eq`).


### `Matrix.stdBasis_repr_apply`

 The coordinates of a matrix in the standard basis are its entries. 

### `mul_pow_eq_pow_mul_pow_pow_of_pow_eq_inv_mul_mul`

 In a group, if `x ^ q = y⁻¹ * x * y`, then `x * y ^ k = y ^ k * x ^ q ^ k` for every `k`. 

### `commute_map_pow_mul_pow_map_inv_pow`

 Let `R : G →* M` be a homomorphism of groups and `R (γ * φ ^ d) = R (φ ^ d * γ)`. Then every
`R (φ ^ a * γ ^ b)` commutes with `R (φ⁻¹ ^ d)`. 

### `New.injective_residue_pow_pow_of_norm_sub_eq_one`

 If the differences `ζ ^ q ^ i - ζ ^ q ^ j` for distinct `i, j < d` have norm `1`, then the
residues of the `ζ ^ q ^ i`, `i < d`, are pairwise distinct: a difference of norm `1` is a unit of
`O`, so its residue is not zero. 

### `Matrix.exists_eq_smul_one_of_commute_of_span_eq_top`

 A square matrix that commutes with every member of a family spanning all matrices is a scalar
multiple of `1`. 

### `New.Selmer.IsLatticeIn.span_range_eq_top_of_map_pow_eq_map_conj`

 A tame pair with incongruent conjugate eigenvalues spans all matrices. Let `u` be an
`O`-lattice in `R`, `d = card n`, let conjugation by `φ` raise `R γ` to the power `q`, let
`R (γ ^ q ^ d) = R γ`, and let `R γ` have an eigenvalue `ζ ∈ O` whose powers `ζ ^ q ^ i`, `i < d`,
differ by elements of norm `1`. Then (a) `u` spans all matrices over `O` and (b) `u (φ⁻¹ ^ d)` is
a scalar: a case of Burnside's theorem, lifted to `O` by Nakayama's lemma. 

### `New.Selmer.eq_bot_or_eq_top_of_span_eq_top`

 If the matrices `T g` span all of `M_n(O)` over a commutative ring `O`, then for every ring map
`f` from `O` to a field `k`, the only subspaces of `kⁿ` stable under all `f (T g)` are `0` and `kⁿ`.
For a local ring `O` this says that the reduction of `T` is absolutely irreducible. 

### `New.Selmer.exists_eq_smul_of_conj_eq`

 Let the matrices `T g` span all of `M_n(O)` over a coefficient ring `O`, and let `a` in
`GL_n(ℚ̄_ℓ)` conjugate each `T g` to a matrix `T' g` over `O`. Then `a` is a scalar times an element
of `GL_n(O)`. So the lattice `a Oⁿ` is a multiple of `Oⁿ`. 


## Uniform approximation of eigensystems and pseudorepresentations

* `New.IsApproximatingMonoid`: a closed submonoid of pairs of a value and a family of values, in
  which each value is a uniform limit of linear combinations of the family.
* `New.exists_isApproximatingMonoid_of_mem_uniformClosure`: an eigenfunction in the closure of the
  span of eigenfunctions of operators that do not increase the sup norm gives such an approximation
  of its eigenvalues.


### `uniformClosure`

 For a set `S` of functions `ι → K`, `K` a normed field, the closure of the `K`-span of `S` in
the topology of uniform convergence. 

### `mem_uniformClosure`

 A function lies in the uniform closure of the span of `S` exactly when, for every `ε > 0`, some
element of the span is within `ε` of it at all points. 

### `IsApproximatingMonoid`

 Approximation of a submonoid `N` of pairs `(t, φ)`, with `t` in `K` and `φ` a family indexed by
pairs `(η, i)` with `i < s η`. The set `N` is closed. As `η > 0` tends to `0`, the sum over `i` of
`c η i * φ (η, i)` tends to `t`, uniformly over `(t, φ) ∈ N`. 

### `IsApproximatingMonoid.isClosed_carrier`

 The monoid `N` of an approximation `New.IsApproximatingMonoid s c N` is closed. 

### `IsApproximatingMonoid.tendstoUniformly`

 In an approximation `New.IsApproximatingMonoid s c N`, the sum over `i` of
`c η i * p.val.snd (η, i)` tends to `p.val.fst` as `η > 0` tends to `0`, uniformly over `p ∈ N`. 

### `exists_isApproximatingMonoid_of_mem_uniformClosure`

 Let `S` be a set of functions `ι → K`, with `K` a normed field, and let `f ≠ 0` lie in the
closure of the `K`-span of `S` for uniform convergence. Then there exist `s : (η > 0) → ℕ`,
coefficients `c η i ∈ K`, a closed submonoid `N` of pairs `(t, φ)` (with `t ∈ K` and `φ` a family
indexed by pairs `(η, i)`, `i < s η`) such that `∑_i c η i * φ (η, i) → t` as `η → 0` uniformly on
`N`, and functions `y (η, i)` in `S`, with the following property. If a linear operator that does
not increase the sup norm has `f` as eigenfunction with eigenvalue `t` and each `y (η, i)` as
eigenfunction with eigenvalue `φ (η, i)`, then `(t, φ) ∈ N`. 

### `IsApproximatingMonoid.tendstoUniformly_eval`

 Given `New.IsApproximatingMonoid s c N`, let `B` be a polynomial in the variables `ι`, and let
`f p x` be elements of `N`. Then the sum over `i` of `c η i` times the value of `B` at the `(η, i)`
components of the `f p x` tends to the value of `B` at their first components, uniformly in `p`. 

### `newtonPoly`

 The polynomials `newtonPoly j m` over k in X_0, X_1, … are defined by `newtonPoly 0 m = 1` and
`newtonPoly (j + 1) m = X m * newtonPoly j 1 - j • newtonPoly j (m + 1)`. At the power sums,
`newtonPoly j 1` equals j! times the j-th elementary symmetric function. 

### `newtonPoly_succ`

 The recursion that defines `newtonPoly`. 

### `eval_newtonPoly`

 The polynomials `newtonPoly j m` over `k` in variables X_0, X_1, … are defined by
`newtonPoly 0 m = 1` and `newtonPoly (j + 1) m = X m * newtonPoly j 1 - j • newtonPoly j (m + 1)`.
Newton's identities: for a multiset `s` in `k`, evaluating `newtonPoly j 1` at X_m ↦ ∑_{a ∈ s} a ^ m
(the power sums of `s`) gives `j!` times the `j`-th elementary symmetric function of `s`. 

### `eval_newtonPoly_eq_pow_mul_prod_of_pow_succ_eq_smul`

 Let `τ` be a linear form on a `k`-algebra `A` and `y : A` with `y ^ (m + 1) = l ^ m • y` for all
`m`. At the values `τ (y ^ i)`, the Newton polynomial `newtonPoly (j + 1) (m + 1)` takes the value
`l ^ m` times the product of `τ y - i * l` over `i ≤ j`. 

### `exists_eq_nat_mul_of_eval_newtonPoly_eq_zero`

 Let `τ` be a linear form on a `k`-algebra `A` and `y : A` with `y ^ (m + 1) = l ^ m • y` for all
`m`. If the Newton polynomial `newtonPoly (d + 1) 1` vanishes at the values `τ (y ^ i)`, then
`τ y = j * l` for some natural number `j`. 

### `_root_.Matrix.not_linearIndependent_trace_mul_of_card_lt`

 More than `card n ^ 2` linear forms `A ↦ trace (M i * A)` on the `n × n` matrices over a
field are linearly dependent. 

### `linearExtension`

 The linear form on `k[G]` that extends `T : G → k`. 

### `eval_linearExtension_eq_zero`

 If `T : G → k` obeys every polynomial identity among traces of homomorphisms `G →* GL n k`, then
its linear extension to `k[G]` obeys every polynomial identity among traces of algebra maps
`k[G] →ₐ[k] Matrix n n k`. 

### `pairingKernel`

 The kernel of the pairing `(x, y) ↦ t (x * y)` on `k[G]`, for a linear form `t` with
`t (x * y) = t (y * x)`; this symmetry makes the kernel a left ideal. 

### `finite_quotient_pairingKernel`

 Let `t` be a linear form on `k[G]` that obeys every polynomial identity among traces of algebra
maps `k[G] → Matrix n n k`. Then the quotient of `k[G]` by the kernel of the pairing `t (x * y)` is
finite-dimensional: for `card n ^ 2 + 1` elements `s i`, independent modulo the kernel, the forms
`y ↦ t (s i * y)` would be independent, but their minors `det (t (s i * b j))` are polynomial
identities among traces, and these vanish since the `ρ (s i)` are dependent in every `ρ`. 

### `exists_rep_of_trace_identities`

 A weak form of the Procesi–Taylor theorem: over an algebraically closed field `k` of
characteristic `0`, a function `T : G → k` that satisfies every polynomial identity holding among
the traces of homomorphisms `G →* GL n k` is the trace of such a homomorphism `r` with
non-degenerate trace form (`New.IsTraceNondeg`). 

### `GaloisRep.exists_continuous_isTraceNondeg_of_tendsto_trace`

 A limit of traces is a trace. Let `N` be a closed submonoid of pairs `(t, φ)` on which
`∑ i, c η i * φ (η, i)` tends to `t` uniformly as `η → 0` (`IsApproximatingMonoid s c N`). For each
`g` let `F g` be a nontrivial filter on `N` along which `t` eventually lies in the complete set `L`
and each `φ x` tends to the trace of `r x g`, with each `r x` continuous. Then some continuous `R`,
whose trace form is non-degenerate on the span of its matrices, has `(tr (R g), (tr (r x g))_x) ∈ N`
for all `g`. 
