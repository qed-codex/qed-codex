---
{
  "module": "src/Lib/LocalGL/SphericalChainLemma.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/LocalGL/SphericalChainLemma.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/LocalGL/SphericalChainLemma.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Chains of roots of the Hecke polynomial of a spherical vector

Let ρ be a smooth representation of GL_N(E_w) with an invariant scalar product B, q = `w.q` the norm
of w, and x ≠ 0 a vector fixed by GL_N(O_w) = `localIntGL` with eigenvalues t_j for the Hecke
operators `heckeGL ρ j`. Its Hecke polynomial is P = `heckePoly q N t`, where
`heckePoly q m t` = Σ_{j ≤ m} (−1)^j q^(j(j−1)/2) t_j X^(m−j).

* `New.Patching.HasRootChain`: P(dX) is (X − 1)(X − q)⋯(X − q^(t−1)) times a divisor of a given
  polynomial.
* `New.Patching.isRoot_chain_of_norm`: a root c with |c|² q^k = q^N starts a chain c, cq, …,
  cq^(k−1) of roots.
* `New.Patching.pairing_aeval_heckeCoset_eq_zero`: of a chain of roots, the operator U of diag(ϖ, 1,
  …, 1) at the level `proIwahori` sees only the top one. If P is a chain with top root c' times S,
  then x is orthogonal to (U − c') S(U) y for every y fixed by `proIwahori`.
* `New.Patching.chain_lemma`: the common source of both results, with a lower bound for the top root
  of a chain (`New.Patching.le_norm_sq_of_isRoot_of_not_isRoot_mul`).

Notions from other files:
* `New.heckeGL`: The j-th Hecke operator on a representation π of GL_n(E_w): the action
  (`New.heckeFun`) of the indicator function of `New.basicDoubleCoset` j, for K = GL_n(O_w).
* `New.proIwahori`: The pro-p Iwahori subgroup of GL_n(O_w): matrices that are upper triangular with
  ones on the diagonal modulo the maximal ideal. `New.partialHecke ρ r m x` is a partial Hecke sum
  of translates of x, with `partialHecke ρ 0 m x = heckeGL ρ m x` and `partialHecke ρ r 0 x = x`.

## Relation to the literature

Known result: the Satake parameters of unitary unramified representations of GL_N come in chains.
Both statements follow from Tadić's classification of the unitary dual and the geometric lemma of
Bernstein and Zelevinsky. The file proves them directly, by two counts of hyperplanes: a root c with
cq not a root has |c|² ≥ q^(N−2), and with the symmetry y ↦ q^(N−1)/ȳ of the roots this gives the
chain; the same counts let the roots of a chain below the top one be cancelled one at a time.
Source: Tadić, Classification of unitary representations in irreducible representations of general
linear group (non-archimedean case), Ann. ENS 19 (1986); Bernstein, P-invariant distributions on
GL(N), LNM 1041 (1983) for the inequality at the ends of segments.


### `New.Patching.HasRootChain`

 P has the chain of roots d, dq, …, dq^{t−1}, and the other factor divides e after scaling:
P(dX) equals (X − 1)(X − q)⋯(X − q^{t−1}) times a divisor of the polynomial e. 

### `New.Patching.adjoint_aeval_map_starRingEnd`

 If `U'` is adjoint to `U` on a set `S` that `U` keeps, then on `S` the conjugate of `G`,
evaluated at `U'`, is adjoint to `G (U)`. 

### `New.Patching.eq_apply_partialHecke_zero_top`

 Let `x` be fixed by `GL_N(O_w)` and `ϖ` a uniformiser. Then `x` is the translate by
`diag(ϖ⁻¹, …, ϖ⁻¹)` of the top partial Hecke sum `partialHecke ρ 0 N x`. 

### `New.Patching.eq_apply_partialHecke_one_top`

 Let `x` be fixed by `GL_N(O_w)` and `ϖ` a uniformiser. Then `x` is the translate by
`diag(1, ϖ⁻¹, …, ϖ⁻¹)` of the top partial Hecke sum `partialHecke ρ 1 (N - 1) x`. 

### `New.Patching.compactMean_apply_inv_partialHecke_one_succ`

 Let `x` be fixed by `GL_N(O_w)`, let `ϖ` be a uniformiser (valuation `exp (-1)`), and let `a` be
the inverse of `ρ(diag(ϖ, 1, …, 1))`. Write `M(y)` for the mean of `ρ` over `proIwahori` applied to
`y`, and let `partialHecke ρ r m x` be the partial Hecke sum of `ρ g x` over the cosets in
`New.partialCosets r m`. If `1 + (i + 1 + j) = N`, the count of `New.partialHecke_hyperplane_count`,
read in the dual representation, gives `q^(N-1) • M(a (partialHecke ρ 1 (i+1) x)) = q^j • (M(a
(partialHecke ρ 0 (i+1) x)) - partialHecke ρ 1 i x)`, where `q = w.q`. 

### `New.Patching.apply_inv_partialHecke_zero_top`

 Let `x` be fixed by `GL_N(O_w)` and `ϖ` a uniformiser. The inverse of `ρ(diag(ϖ, 1, …, 1))`
carries the top partial Hecke sum `partialHecke ρ 0 N x` to `partialHecke ρ 1 (N - 1) x`. 

### `New.Patching.eq_zero_of_partialHecke_zero_top`

 Let `x` be fixed by `GL_N(O_w)` and `ϖ` a uniformiser. The top partial Hecke sum
`partialHecke ρ 0 N x` vanishes only for `x = 0`. 

### `New.Patching.partialHecke_hyperplane_count_dual`

 Let x be fixed by GL_N(O_w) (`hx`) and ϖ a uniformiser, and let a be the inverse of ρ(diag(ϖ, 1,
…, 1)). Then (a) the count of `New.partialHecke_hyperplane_count`, read in the dual representation,
gives, for i + 1 + j = N − 1, a recursion between the mean over `proIwahori` of a applied to the
partial Hecke sums `partialHecke ρ 0` and `partialHecke ρ 1`; (b) a carries `partialHecke ρ 0 N x`
to `partialHecke ρ 1 (N - 1) x`; (c) `partialHecke ρ 0 N x` vanishes only for x = 0. 

### `New.Patching.aeval_cofactor_eq_zero`

 Suppose that `P (U)` kills `y`, and that `(P / (X - c)) (U)` still kills `y` for every root
`c ≠ 0` of `P` for which `q * c` is also a root. Let `P = (∏ i < k, (d X - q ^ i)) * R`. If
`q ^ k / d` is a root of `P`, then `R (U)` kills `y`: the chain `q ^ i / d`, `i < k`, cancels. 

### `New.Patching.aeval_conj_eq_zero`

 If `R (U)` kills every `T j` and the adjoint `U'` of `U` keeps the span of `T 0, …, T n`, then
the conjugate of `R`, evaluated at `U'`, kills `T 0`. 

### `New.Patching.heckePoly_succ`

 The Hecke polynomial of degree `m + 1` is `X` times that of degree `m`, plus the constant
`(-1) ^ (m + 1) * q ^ ((m + 1).choose 2) * t (m + 1)`. 

### `New.Patching.aeval_heckePoly_apply`

 Let `U (T j) = q ^ j • (t (j + 1) • T 0 - T (j + 1))` for all `j`, and `t 0 • T 0 = T 0`. Then
the Hecke polynomial of degree `m`, evaluated at `U`, sends `T 0` to
`(-1) ^ m * q ^ (m.choose 2)` times `T m`. 

### `New.Patching.exists_mul_eq_sub_eval_and_apply`

 The action of `U'` on the quotient of a Hecke polynomial by `X - c`. Let `p m` be the Hecke
polynomial of degree `m`, with `p m (U) (T 0) = (-1) ^ m * q ^ (m.choose 2) • T m`, let
`T (n + 1) = 0`, and let `U' (T (i + 1)) = q ^ (n - i - 1) • ((t (i + 1) / q ^ n) • U' (T 0) - T i)`
for `i < n` and `U' (T 0) = q ^ n • (t (n + 1))⁻¹ • T n`, as in
`New.Patching.chain_lemma_of_adjoint`. For `m ≤ n + 1` and `c : ℂ` there is a polynomial `D` with
`(X - c) * D = p m - p m (c)` and `U' ((c • D + p m) (U) (T 0)) = (p m (q * c) / q ^ m) • U' (T 0) +
(q ^ n / q) • D (U) (T 0)`. 

### `New.Patching.le_norm_sq_of_pairing`

 The root bound behind `New.Patching.chain_lemma_of_adjoint`. Let `B` be positive definite, `U'`
adjoint to `U`, `x ≠ 0`, `1 < q` and `a ≠ 0`. Let `z` be an eigenvector of `U` for `c` with
`c • U' z = (a / q ^ (n + 1)) • U' x + (q ^ n / q) • z` and
`c * B x z * (q ^ (n + 1) - 1) = a * B x x`. Then `q ^ (n + 1) / q ^ 2 ≤ ‖c‖ ^ 2`. 

### `New.Patching.chain_lemma_of_adjoint`

 The linear algebra of the chain lemma. Let `B` be a positive definite sesquilinear form, and let
`U`, `U'` be mutually adjoint for `B`. Let `P = heckePoly q (n+1) t` with `1 < q`, `T 0 ≠ 0`,
`t 0 • T 0 = T 0` and `t (n+1) ≠ 0`, and suppose `U (T j) = q^j • (t (j+1) • T 0 - T (j+1))`, `U' (T
(i+1)) = q^(n-i-1) • ((t (i+1) / q^n) • U' (T 0) - T i)` for `i < n`,
`U' (T 0) = q^n • t (n+1)⁻¹ • T n` and `U (T n) = q^n • t (n+1) • T 0`. Then (a) every root `c` of
`P` such that `q * c` is not a root satisfies `q^(n+1) / q^2 ≤ ‖c‖^2`; and (b) if `d ≠ 0`, `q^k / d`
is a root of `P`, and `P = (∏_{i<k} (d X - q^i)) * R`, then `R` with complex-conjugated
coefficients, evaluated at `U'`, kills `T 0`. 

### `New.Patching.chain_lemma`

 Let x ≠ 0 be a spherical eigenvector with Hecke polynomial P in a smooth unitary representation
of GL_N(E_w), q the norm of w, ϖ a uniformiser.
* Root bound: if P(c) = 0 and P(qc) ≠ 0, then |c|² ≥ q^(N−2), written q^N / q² to avoid subtraction.
* Orthogonality: let U be the Hecke operator of diag(ϖ, 1, …, 1) for the group `proIwahori`. If
d ≠ 0 and P(X/d) = ∏_{i ≤ k} (X − q^i) · S with S dividing R, so that c, cq, …, cq^k are roots for
c = 1/d, then x is orthogonal to ((dX − q^k) · R(dX))(U) y for every y fixed by `proIwahori`.

The root bound also follows from Tadić's classification of unitary spherical representations of
GL_N; the proof here is direct and does not use the classification. 

### `New.Patching.le_norm_sq_of_isRoot_of_not_isRoot_mul`

 The top root of a chain is large. Let x ≠ 0 be a spherical Hecke eigenvector in a smooth unitary
representation of GL_N(E_w), with Hecke polynomial P. If P(c) = 0 and P(qc) ≠ 0, then
|c|² ≥ q^(N−2), written q^N / q² to avoid subtraction. 

### `New.Patching.isRoot_chain_of_norm`

 Let x ≠ 0 be a spherical Hecke eigenvector in a smooth unitary representation of GL_N(E_w), with
Hecke polynomial P. If P(c) = 0 and |c|² q^k = q^N, then c, cq, …, cq^(k−1) are all roots of P.

This also follows from Tadić's classification of the unitary spherical representations of GL_N; the
proof here is direct, from `le_norm_sq_of_isRoot_of_not_isRoot_mul` and the symmetry y ↦ q^(N−1)/ȳ
of the roots of P. 

### `New.Patching.pairing_aeval_heckeCoset_eq_zero`

 Of a chain of roots, U sees only the top root. Let x ≠ 0 be a spherical Hecke eigenvector in a
smooth unitary representation of GL_N(E_w), with Hecke polynomial P, and let U be the Hecke operator
of diag(ϖ, 1, …, 1) for the group `proIwahori`. If d ≠ 0 and P(X/d) = ∏_{i ≤ k} (X − q^i) · S with S
dividing R, then x is orthogonal to ((dX − q^k) · R(dX))(U) y for every y fixed by `proIwahori`. 
