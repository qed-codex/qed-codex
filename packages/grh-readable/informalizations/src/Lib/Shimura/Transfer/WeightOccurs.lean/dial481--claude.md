---
{
  "module": "src/Lib/Shimura/Transfer/WeightOccurs.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Shimura/Transfer/WeightOccurs.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Shimura/Transfer/WeightOccurs.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Coefficient systems from weights and the degrees where Hecke eigensystems occur

A weight `κ` gives a coefficient system on `GL_a(E)`. Its Hecke eigensystems occur in the degrees
given by the jumps of `κ`, in the sense of `New.Variety.OccursInWeight`: the local terms of the
Lefschetz side do not all cancel.

`Φ v` is the embedding that the CM type chooses at `v`, and `v₀` is the base infinite place fixed by
`New.CMBase E`.

* `New.Variety.occursInWeight_of_isTestEigenform`: the Hecke eigenvalues of a test eigenform occur,
  if the character of the coefficients is given by a Schur polynomial and powers of the determinant.
* `New.Variety.exists_isCoefficientSystem`: the coefficient system attached to a weight, and the
  occurrence of the eigensystems of its test vectors.

Notions from other files:
* `New.Weight`: For `κ : Weight E` and an infinite place `v` of `E`, `κ.1 v h` is the number of
  columns of height `h` of a Young diagram, and `κ.2 v` is an integer exponent of the determinant.
* `New.Variety.entryConj`: The endomorphism of the unitary group {g : gᴴg = 1} of matrices over R
  indexed by `n` that applies the involution of R to each entry.
* `New.jumps`: The multiset {j − 1 − λ_j} if σ is in the CM type, else {λ_j + a − j}, 1 ≤ j ≤ a,
  with λ the highest weight of κ at σ.
* `New.Space.weightRep`: The representation of the rational unitary group on coordinate vectors of
  weight `(κ.1, κ.2)`, through its components at the infinite places and `New.conjWeylRep`.

## Relation to the literature

Known result: Transfer of eigensystems between unitary inner forms differing at a real place. Only
the occurrence is proved here, namely that the Hecke eigensystem of a definite form occurs, in each
Hodge weight, on the variety for signature (1, n-1), with n odd and a cuspidal type at one split
place. It is proved by comparing two finite counts, without stabilisation. Source: Harris and
Labesse, Conditional base change for unitary groups, Asian J. Math. 8 (2004), Thm 2.1.2; Labesse,
Changement de base CM et séries discrètes (2011), Thm 5.4; count as in Goresky and MacPherson, The
topological trace formula (2003), and Shimura, On the trace formula for Hecke operators, Acta Math.
132 (1974).


### `New.Variety.isNilpotent_of_trace_pow_succ_eq_zero`

 An endomorphism of a finite-dimensional complex vector space all of whose positive powers have
trace zero is nilpotent. 

### `New.Variety.rootCoeffEval_X_zero_of_odd`

 For `a` odd, `rootCoeffEval` sends the variable `X 0` to minus the product of the `a` roots. 

### `New.Variety.prod_map_tauHecke_mem_spanOn`

 Let `E` be a CM field containing ℚ(i√d₀), and let `w₁` be a finite place of `E` that is split
over the maximal real subfield and divides the level `𝔑`. Any product of the Hecke elements
`τ_{w,j}` (`tauHecke`, in the Hecke algebra of level `K(𝔑)`) at places `w` safe for `𝔑` (among other
things, `𝔑 ∉ w` and `𝔑` lies in no place over the conjugate of the place below `w`) lies in the span
of the group elements `[g]` with `g` a unitary similitude (`gᴴ g` a scalar finite idele of ℚ) whose
component at `w₁` is trivial. Here the component is taken via `dualComponent w₁`, the inverse
transpose of the `w₁`-component in `GL_a(E_{w₁})`. 

### `New.Variety.asAlgebraHom_prod_map_tauHecke_apply`

 A word `L` in the Hecke operators `tauHecke` at safe places acts on a common eigenvector `φ`
of the operators `heckeSum`, with eigenvalues `θ`, by the product of the eigenvalues of its
letters. 

### `New.Variety.sum_basis_comp_mul_prod_rootCoeffEval_eq`

 The local terms of a regular element `y`, summed over the marked eigenvalue. Let `q` be the
Schur polynomial of `l` at `Φ v₀`, and `(-X 0) ^ m` (for `a` odd, the `m`-th power of the product of
the roots) at the conjugate of `Φ v₀` and at the `Φ v` with `v ≠ v₀`. Let `μ k` be the numbered
roots of `y` at `Φ v₀`. The `k`-th term is the `k`-th Lagrange basis polynomial of the `μ` at
`μ k * X`, times the product over `σ` of `q σ` at `lieRoots`. These are the roots `r` of `σ y`,
taken as `r X` if the eigenline of `r` lies in the Lie algebra and as `r` otherwise: at `Φ v₀` only
the marked root, at its conjugate all but one, at the other `Φ v` all, at their conjugates none.
Then the sum is the product over `σ` of the values of `q σ` at the eigenvalues of `σ y`, times
`∑ k, X ^ l k` shifted by a fixed power of `X`. 

### `New.Variety.trace_definiteForms_rep_eq_zero_of_isNullHecke`

 Comparison of trace formulas, for `a` odd and `𝔑` neat. Let the trace of `ξ y⁻¹` at regular `y`
be the product of the values of `q σ` at the eigenvalues of `σ y` (`q` as in
`sum_basis_comp_mul_prod_rootCoeffEval_eq`), and let `f` be regular of cuspidal type `χ` at `w₀`. If
`f` is null (`New.Variety.IsNullHecke`) in the weight `l j + m (a - 1 + a (n - 1))`, `n` the number
of infinite places of `E`, then `f` has trace zero on the definite forms with coefficients in
`ξ`. 

### `New.Variety.IsTestEigenform`

 `φ` is a definite form of level `𝔑` with coefficients in `ξ`, a test vector, and an
eigenvector of the Hecke operators at the safe places with eigenvalues `θ`. 

### `New.Variety.IsTestEigenform.mem_definiteForms`

 `φ` is a form on the definite frames. 

### `New.Variety.IsTestEigenform.exists_isTestVector`

 `φ` is a test vector at some split places `w₀`, `w₁`, for some type `(J, χ)` at `w₀`. 

### `New.Variety.IsTestEigenform.heckeSum_apply`

 The `j`-th Hecke operator at `w` multiplies `φ` by `θ w j`. 

### `New.Variety.occursInWeight_of_isTestEigenform`

 Let `a` be odd and `𝔑` neat. Suppose the trace of `ξ y⁻¹` at regular `y` is the product over `σ`
of the values of `q σ` at the eigenvalues of `σ y`, where `q` is the Schur polynomial of `l` at
`Φ v₀` and `(-X 0) ^ m` at the other `Φ v` and at the conjugate of `Φ v₀`. Let `θ` be the Hecke
eigenvalues at the safe places of a test eigenform of level `𝔑` with coefficients in `ξ`. Then `θ`
occurs (`New.Variety.OccursInWeight`, with parameter `∑ σ, deg (q σ) + 1`) in the weight
`l j + m (a - 1 + a (n - 1))` for every `j`, where `n` is the number of infinite places of `E`:
every combination `p` of `tauHecke` words with `p θ = 1` has a Hecke multiple `b p` that is not null
in that weight. 

### `New.Variety.det_inv_rev_zpow`

 Inverting nonzero numbers `r i` and reversing their order in a generalized Vandermonde
determinant amounts to replacing the exponents `w j` by `a - 1 - w j.rev`, up to the factor
`(∏ r) ^ (1 - a)`. 

### `New.Variety.rootCoeffEval_genericSchur_mul_det_zpow`

 The bialternant formula with integer exponents: if `l = m + k`, then the Schur polynomial of `l`
at nonzero numbers `r i`, times the Vandermonde determinant, is `(∏ r) ^ m * det (r i ^ k j)`. 

### `New.Variety.mul_trace_weylRep_eq_prod_rootCoeffEval`

 Weyl's character formula for a twist of `weylRep κ.1 κ.2`, for `a` odd. At the places `v` with
`p v` the regular element `y` enters through `Φ v y⁻¹`, at the others through the transpose of
its conjugate. The character, times the `m`-th power of the norm of `det y`, is the product of the
values of `q σ` at the eigenvalues of `σ y`. Above each place one `q σ` gives `det ^ m`; the other
is a Schur polynomial whose exponents come from those, `u v`, of Weyl's formula. 

### `New.Variety.weylRep_of_scalar`

 In the representation `weylRep κ.1 κ.2` of weight `κ` (`New.weylRep`), a family whose component
at `v` is the scalar `t ^ ε v` acts by a power of `t`: the exponent is the sum of the `ε v` times
the degree of the weight at `v`. 

### `New.Variety.pair_star_eq_univ`

 The complex embeddings of `QuadField d₀` are `s₀` and its conjugate. 

### `New.Variety.conjugate_eq_iff_ne`

 Exactly one of `s` and its conjugate is `s₀`. 

### `New.Variety.apply_eq_ite_comp_eq`

 An embedding of `E` restricts to `s₀` or to its conjugate. 

### `New.Variety.extendedEmbedding`

 An extension to `GL (Fin a) E` of the embedding of the unitary group at the infinite places:
`z` goes to `Φ v z` if `p v` holds, and to the inverse transpose of its conjugate if not. 

### `New.Variety.twistedWeylMatrix`

 The matrices of weight `κ` along `extendedEmbedding p`, twisted by the `-m`-th power of the
norm of the determinant. 

### `New.Variety.twistedWeylRep`

 The representation given by the matrices `twistedWeylMatrix κ p m`. 

### `New.Variety.weightRep_entryConj_eq_twistedWeylRep`

 For unitary `y`, `twistedWeylRep κ p m y` is the action of `ȳ` in weight `κ`. 

### `New.Variety.exists_twistedWeylRep_scalar`

 Let `E` be a CM field with chosen embeddings `Φ v`, let `i : ℚ(i√d₀) →+* E`, and let `s₀` be a
complex embedding of ℚ(i√d₀). Let `p v` mean that `Φ v` extends `s₀`, and consider the
representation `twistedWeylRep κ p m` of `GL_a(E)` given by the matrices `twistedWeylMatrix κ p m`
for the weight `κ`. Then there is one integer `A` such that, for every `x` in `(QuadField d₀)ˣ`, the
scalar matrix `i(x̄)` acts by `s̄₀ x ^ (-A) * s₀ x ^ (-μ)`, where `μ` is `m * a` times the number of
infinite places of `E`. 

### `New.Variety.IsCoefficientSystem`

 Let `i` embed the imaginary quadratic field `QuadField d₀` in `E`, and let `s₀` be a complex
embedding of `QuadField d₀`. The representation `ξ` extends the weight `κ` to `GL (Fin a) E`. The
centre acts through the exponents `A`, with `A s₀ = μ`. The eigenvalues of the test eigenforms with
coefficients in `ξ` occur in the weights `z + μ`, for `z` a jump of `κ` at an embedding over `s₀`
(`New.Variety.OccursInWeight` with the parameter `N + 1`). 

### `New.Variety.IsCoefficientSystem.exponent_self`

 The central exponent at `s₀` is `μ`. 

### `New.Variety.IsCoefficientSystem.weightRep_entryConj`

 For unitary `y`, `ξ y` is the action of `ȳ` in weight `κ`. 

### `New.Variety.IsCoefficientSystem.map_scalar`

 For `x` in `(QuadField d₀)ˣ`, the scalar `x̄` acts by `∏ s, s x ^ (-A s)`. 

### `New.Variety.IsCoefficientSystem.jump_add_nonneg`

 The jumps of `κ` at embeddings over `s₀` are at least `-μ`. 

### `New.Variety.IsCoefficientSystem.occursInWeight`

 Let `z` be a jump of `κ` at `σ` over `s₀`, for the given CM type. Let `Ψ` be any CM type with
  base place `v₀` whose only embedding over `s₀` is `σ`, at `v₀`. Then the eigenvalues of every
  test eigenform of neat level for `Ψ` occur in weight `z + μ`. 

### `New.Variety.trace_twistedWeylRep_inv`

 The trace of `twistedWeylRep κ p m` at `y⁻¹` is the left side of
`mul_trace_weylRep_eq_prod_rootCoeffEval`: the `m`-th power of the norm of `det y` times the trace
of `weylRep κ.1 κ.2` at the family that is `Φ v y⁻¹` where `p v` holds and the transpose of the
conjugate of `y` elsewhere. 

### `New.Variety.exists_isCoefficientSystem`

 Let `a` be odd, `i` an embedding of the imaginary quadratic field `QuadField d₀` in `E` and `s₀`
a complex embedding of `QuadField d₀`. A weight `κ` extends to a representation `ξ` of
`GL (Fin a) E` on which the scalars from `(QuadField d₀)ˣ` (through `i`) act through exponents `A`
with `A s₀ = μ`, and whose test eigenforms occur in the weights `z + μ` for `z` a jump of `κ` at an
embedding over `s₀`, for some `N` (`New.Variety.IsCoefficientSystem`). The proof compares traces
directly and does not pass through automorphic representations of `GL_n`.

In the literature the same occurrence follows from the description, due to Labesse and to
Moeglin–Waldspurger, of automorphic representations of unitary groups via `GL_n`. 
