---
{
  "module": "src/Lib/General/LinearAlgebra/Eigenvalues.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/General/LinearAlgebra/Eigenvalues.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/General/LinearAlgebra/Eigenvalues.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Eigenvalues: traces of powers, common eigenvectors, Amitsur's theorem, Sylvester's law

This file collects linear algebra on eigenvalues and characteristic polynomials. It expresses traces
of powers and determinants such as `det (1 - c N)` through the roots of the characteristic
polynomial.

## Main definitions and results

* `New.exists_eigenvector_of_commute`: common eigenvectors of endomorphisms that preserve a
  finite-dimensional subspace `S` and commute on it, over an algebraically closed field.
* `New.exists_eigenvector_of_trace_mul_eq`: if twisted traces of a commuting family `A'` are
  proportional to traces of a commuting family `A`, a generalised eigensystem of `A` on which one
  operator has non-zero trace extends to an eigensystem of `A'` that is invariant under the twist.
* `New.amitsur_charpoly_mem_of_span` (Amitsur): for an algebra map to matrices, it suffices to check
  on a spanning set that the coefficients of the characteristic polynomials lie in the base ring.
  The proof works with det (1 - t ρ(w)) modulo a power of t and factors 1 - t ρ(w) step by step.
* `New.isConj_diagonal_of_isRoot_charpoly`: a complex square matrix whose characteristic polynomial
  vanishes at pairwise distinct numbers x_i, one for each index i, is conjugate to the diagonal
  matrix with entries x_i.
* `New.sylvester_law_of_inertia`: Sylvester's law of inertia for sign matrices.

## Relation to the literature

Known result: Amitsur's theorem that integral characteristic polynomials on a spanning set give them
on the whole algebra. It is a consequence of Amitsur's formula for the characteristic polynomial of
a sum of matrices. Source: S. A. Amitsur, On the characteristic polynomial of a sum of matrices,
Linear and Multilinear Algebra 8 (1980), no. 3, 177-182; G. Chenevier, The p-adic analytic space of
pseudocharacters of a profinite group and pseudorepresentations over arbitrary rings, LMS Lecture
Note Ser. 414 (2014), (1.5).


 ## Traces of powers as power sums of eigenvalues 

### `det_aeval_neg_eq_prod_roots`

 For a square matrix A over an algebraically closed field and a polynomial q, det q(−A) is
the product of q(−x) over the roots x of the characteristic polynomial of A, counted with
multiplicity. 

### `trace_pow_eq_sum_roots`

 Over an algebraically closed field, the trace of A^m is the sum of the m-th powers of the
roots of the characteristic polynomial of A, counted with multiplicity. 

### `charpoly_eq_mul_of_trace_pow_add`

 Over an algebraically closed field of characteristic 0, if tr A^m = tr B^m + ∑_{e∈S} α_e^m
for all m ≥ 0, with S finite, then the characteristic polynomial of A is that of B times
∏_{e∈S} (X − α_e). 

### `New.det_one_sub_smul_eq_prod_roots_of_isAlgClosed`

 For a square matrix N over an algebraically closed field and a scalar c, det (1 − c N) is the
product of 1 − c x over the roots x of the characteristic polynomial of N, counted with
multiplicity. 

### `New.det_one_sub_smul_eq_prod_roots`

 For a complex square matrix N and a complex number c, det (1 − c N) is the product of 1 − c x
over the roots x of the characteristic polynomial of N, counted with multiplicity. 

 ## The trace of an idempotent matrix 

### `New.trace_eq_rank_of_isIdempotentElem`

 The trace of an idempotent matrix over a field is its rank. 

 ## Sorting by adjacent swaps and common eigenvectors 

### `New.exists_antitone_of_swap`

 Sorting by adjacent swaps: let `P` hold for some permutation, and pass from `σ` to `σ * (i j)`
whenever `j = i + 1` and `f (σ i) < f (σ j)`. Then `P σ` holds for some `σ` with `f ∘ σ`
non-increasing. 

### `New.exists_eigenvector_of_commute`

 Let the endomorphisms `φ m` preserve the finite-dimensional subspace `S` and commute on it,
over an algebraically closed field, and let `U : Submodule k S` be proper. Then there are scalars
`χ m` whose joint generalised eigenspace in `S` is not contained in `U` and which are the
eigenvalues of a common non-zero eigenvector in `S`. 

### `New.exists_eigenvector_of_functional`

 Let the `φ m` preserve the finite-dimensional subspace `S` and commute on it, over an
algebraically closed field. If a linear form `l`, non-zero on `S`, satisfies `l ∘ φ m = η m • l`,
then `S` contains a non-zero common eigenvector with eigenvalues `η m`. 

### `New.Variety.exists_words_comb_eq_zero`

 Let Φ map words (lists of letters s) to endomorphisms of a finite-dimensional space over an
algebraically closed field, with Φ[s]Φ(L) = Φ(Ls). Suppose that the Φ[s] commute and have no
non-zero joint eigenvector with eigenvalues η_s. Then some finitely supported family of scalars
(c_L) has ∑ c_L ∏_{s∈L} η_s = 1 and ∑ c_L Φ(L) = 0. 

### `New.exists_eigencharacter_of_ne_bot`

 A representation `ρ` of a commutative monoid over an algebraically closed field has a common
eigenvector in every non-zero finite-dimensional invariant subspace `S`, and its eigenvalues form
a character. 

### `New.exists_eigencharacter`

 The form of `New.exists_eigencharacter_of_ne_bot` for a subspace `S` that is not contained in
the zero subspace. 

 ## Eigensystems from a twisted trace identity 

### `trace_restrict_ne_zero`

 If `p ≠ ⊥` is finite dimensional, stable under `b` and contained in the generalised eigenspace
of `b` for `c ≠ 0`, then `b` has non-zero trace on `p`. 

### `eq_zero_of_pow_apply_eq_zero_of_mem_maxGenEigenspace`

 Generalised eigenspaces for different eigenvalues meet trivially: in a complex vector space
`V`, a vector killed by a power of `f - μ` that lies in the generalised eigenspace of `f` for
`ν ≠ μ` is zero. 

### `trace_mul_mul_eq_of_mul_eq_mul`

 If `s` intertwines `f` and `g`, that is `s * f = g * s`, and `u` commutes with `g`, then
`f * (u * s)` and `g * (u * s)` have the same trace. 

### `exists_pow_sub_smul_mul_eq_zero_of_commute`

 Let `G a` be commuting elements of a complex algebra `R`, and let `S` be a finite-dimensional
subspace of `R` that is stable under left multiplication by the `G a`. If `τ` is a non-zero linear
form on `S`, then `τ z ≠ 0` for some joint generalised eigenvector `z ∈ S` of these
multiplications. 

### `exists_eigenvector_mem_range_of_commute`

 A commuting family `A'`, indexed by `I'`, of operators on a finite-dimensional complex space
`V'` has a common eigenvector in the range of any non-zero operator `f` that commutes with it. 

### `apply_mem_iInf_maxGenEigenspace_of_commute`

 An operator `g` that commutes with every `f a` preserves the joint generalised eigenspace of
the `f a` for any system of eigenvalues `θ`. 

### `apply_mem_inf_iInf_maxGenEigenspace_of_commute_restrict`

 Let the operators `f a` and `g` on `V` preserve a subspace `p`. If the restriction of `g` to `p`
commutes with those of the `f a`, then `g` preserves the part in `p` of the joint generalised
eigenspace of the `f a` for any system of eigenvalues `θ`. 

### `trace_restrict_iInf_maxGenEigenspace_ne_zero`

 Let the operators `f a` and `g` on `V` preserve a subspace `p`. Suppose that `g` preserves the
part in `p` of the joint generalised `θ`-eigenspace of the `f a` and has non-zero trace on it. Then
the restriction of `g` to `p` has non-zero trace on the joint generalised `θ`-eigenspace of the
restrictions of the `f a`. The hypothesis `h_stable_restrict` serves to state the conclusion; it is
equivalent to `h_stable`. 

### `traceIdentityMultipliers`

 For families `A` and `A'` of operators on spaces `W` and `W'`, the pairs `(x, y)` such that
`x` commutes with `A`, `y` with `A'`, and `tr (y * t.2 * s) = c * tr (x * t.1)` for all `t` in `Q`
whose second component commutes with `A'`. 

### `mk_mul_mem_traceIdentityMultipliers`

 The multipliers of a trace identity are stable under left multiplication by a pair
`(A a, A' a')` that maps `Q` into itself, if each of the families `A`, `A'` commutes. 

### `zero_sub_mul_mem_traceIdentityMultipliers`

 If `s * A' a = A' a' * s` in a commuting family `A'`, the multipliers of a trace identity are
stable under left multiplication by `(0, A' a - A' a')`. 

### `exists_eigenvector_and_forall_eigenvalue_eq`

 Let `G a` be operators on a finite-dimensional complex space `V'`. Suppose that the image of a
non-zero operator `f`, commuting with a commuting family `A'` indexed by a type `I'`, lies in the
generalised `χ a`-eigenspace of each `G a`. Then `A'` has a common eigenvector in that image, and
the only eigenvalue that `G a` can have at it is `χ a`. 

### `exists_eigenvector_of_trace_mul_eq`

 Let `A` and `A'` be commuting families of operators on finite-dimensional complex spaces `V`
and `V'`, and let `s` be an operator on `V'`. Suppose that `A b` has non-zero trace on the joint
generalised `θ`-eigenspace of the `A (k a)`. Let `Q` be a set of pairs of operators that contains
`(A b, A' i)` and is stable under left multiplication by the `(A (k a), A' (j a))`. Suppose that
`tr (t.2 * s) = c * tr t.1` for all `t` in `Q`, where `c ≠ 0`. Then `A'` has a common eigenvector in
the image of `A' i` whose system of eigenvalues `Θ` satisfies `Θ ∘ j = θ`, and `Θ a = Θ a'` whenever
`s * A' a = A' a' * s`. The hypothesis `h_stable` serves to state the trace hypothesis; it follows
from `hA` by `New.apply_mem_iInf_maxGenEigenspace_of_commute`. 

### `exists_eigenvector_of_trace_identity`

 The form of `New.exists_eigenvector_of_trace_mul_eq` for operators `B a` on a complex vector
space `V` that preserve a finite-dimensional subspace `p` and commute on it. Let `A'` be a commuting
family on a finite-dimensional space `V'` and `s` an operator on `V'`. Suppose that `B b` has
non-zero trace on the part in `p` of the joint generalised `θ`-eigenspace of the `B (k a)`. Let `Q`
be a set of pairs of operators on `p` and `V'` that contains `(B b | p, A' i)` and is stable under
left multiplication by the `(B (k a) | p, A' (j a))`. Suppose that `tr (t.2 * s) = c * tr t.1` for
all `t` in `Q`, where `c ≠ 0`. Then `A'` has a common eigenvector in the image of `A' i` whose
system of eigenvalues `Θ` satisfies `Θ ∘ j = θ`, and `Θ a = Θ a'` whenever `s * A' a = A' a' * s`.
The hypothesis `h_stable` serves to state the trace hypothesis; it follows from `hB_comm` by
`New.apply_mem_inf_iInf_maxGenEigenspace_of_commute_restrict`. 


## Amitsur's theorem on integral characteristic polynomials

Let ρ be a B-algebra map from a ring Λ to n × n matrices over a commutative B-algebra A. The
question is when the characteristic polynomials of the ρ(w) have coefficients in the image of B, the
range of `algebraMap B A`.


### `exists_adjugate_of_charpoly_mem`

 Let ρ be a B-algebra map from Λ to square matrices over a commutative B-algebra A. If all
characteristic polynomials of the ρ(w) have coefficients in the image of B, then for each w there
are F in B with det ρ(w) = F and v in Λ with ρ(v) ρ(w) = ρ(w) ρ(v) = F • 1.

This is a consequence of the Cayley–Hamilton theorem for ρ(w): when the characteristic polynomial
has coefficients from B, the determinant of ρ(w) is ρ(v) ρ(w) with v in Λ. 

### `amitsur_charpoly_mem_of_span`

 Amitsur's theorem. Let ρ be a B-algebra map from Λ to square matrices over a commutative
B-algebra A. If Λ is spanned over B by the elements s for which the characteristic polynomial of
ρ(s) has all coefficients in the image of B in A, then every w in Λ has this property. 

### `charpoly_smul_coeff`

 Scaling a square matrix of size `card n` by `a` multiplies the `k`-th coefficient of its
characteristic polynomial by `a ^ (card n - k)`. 


## Diagonalisation and Sylvester's law of inertia

Linear algebra over ℂ for square matrices indexed by a finite type n.


### `isConj_diagonal_of_isRoot_charpoly`

 If the characteristic polynomial of a complex square matrix g vanishes at pairwise distinct
numbers x_i, one for each row index i, then g is conjugate by an invertible matrix to the
diagonal matrix with entries x_i. 

### `sylvester_law_of_inertia`

 Sylvester's law of inertia: if hᴴ diag(s) h = diag(t) for families of signs s, t and a complex
square matrix h, then some permutation τ has s_{τ(j)} = t_j for all j. Here `signMatrix s` is the
diagonal matrix diag(s). 
