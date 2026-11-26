---
{
  "module": "src/Lib/Cyclotomic/Voronoi.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Cyclotomic/Voronoi.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Cyclotomic/Voronoi.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# A small nonzero integer in all Stickelberger ideals via Voronoi's congruence

The analytic input to the bound for the odd part of Ш: one nonzero integer X of controlled size
that, times c ^ (e + 1) - 1, lies in all the Stickelberger ideals for N and e.

* `New.OddPart.IsStickelbergerBound`: the two properties required of X, as a structure.
* `New.OddPart.exists_isStickelbergerBound`: such an X exists with X ≤ 2 ^ (N + e + 3) ^ 6, for
  e ≥ 1.

The idea: the generalised Bernoulli numbers of all characters mod N, corrected where they vanish for
reasons of parity, are the eigenvalues of one integer matrix. Its determinant is nonzero
(`New.OddPart.sum_mul_bernoulli_ne_zero`), is divisible by each eigenvalue, and is bounded by
the Fourier series of the Bernoulli polynomial. Voronoi's congruence
(`New.OddPart.voronoi_congruence_bernoulli`) links the Bernoulli numbers to the Stickelberger sums;
it rests on a congruence for power sums along an arithmetic progression
(`New.OddPart.exists_sq_dvd_factorial_mul_sum_pow_sub`).

## Relation to the literature

Known result: Voronoi's congruence for twisted power sums and the trivial zeros of Dirichlet
L-functions. Here the congruence is twisted by a possibly imprimitive character and stated for power
sums. One non-zero integer with an explicit size bound has the following property. For c ≡ 1 mod N,
(c ^ (e + 1) - 1) X is congruent, modulo every m prime to c, to 2 w times the twisted Stickelberger
sum, where w does not depend on m. This holds for every character ψ with ψ(-1) = -(-1) ^ e and
values in a domain of characteristic 0. In addition, for every prime l, some c ≡ 1 mod N prime to l
has (c ^ e - 1) (c ^ (e + 1) - 1) ∣ X. Source: K. Ireland, M. Rosen, A Classical Introduction to
Modern Number Theory, 2nd ed. 1990; for the untwisted statement also M. Eberl, Kummer's congruence,
Archive of Formal Proofs 2024.


### `exists_intCast_eq_factorial_mul_bernoulli`

 For every `i`, the number `(i + 1)! Bᵢ` is an integer. 

### `exists_map_eq_bernoulli_sub_comp`

 The polynomial `(e + 1)! N ^ (e + 2) (B_{e+2}(X / N) - B_{e+2}(0))` has integer coefficients. 

### `exists_sq_dvd_factorial_mul_sum_pow_sub`

 Power sums along an arithmetic progression. For a natural number `a`, the number
`β = (e + 2)! N ^ (e + 1) B_{e+1}(a / N)` is an integer, and for every `u`,
`(e + 2)! ∑_{i<u} (a + i N) ^ (e + 1) ≡ β u` modulo `u²`. 

### `IsStickelbergerBound`

 The Stickelberger property of `X` for `N` and `e`: a divisibility for each prime, and a
congruence for the Stickelberger sums. 

### `IsStickelbergerBound.exists_modEq_one_coprime_dvd`

 For every prime `l`, some `c ≡ 1 mod N` prime to `l` has
  `(c ^ e - 1) (c ^ (e + 1) - 1) ∣ X`. 

### `IsStickelbergerBound.exists_natCast_dvd_sub_mul_sum`

 Let `c ≡ 1 mod N`, and let `ψ` be a character mod `N` with values in a domain `O` of
  characteristic `0` and `ψ(-1) = -(-1) ^ e`. Then some `w` in `O`, the same for every `m`, has
  `(c ^ (e + 1) - 1) X ≡ 2 w ∑ ⌊c a / (N m)⌋ a ^ e ψ(a)` modulo `m` for all `m ≥ 1` prime to `c`,
  the sum over `0 ≤ a < N m`. 

### `LFunction_neg_nat_eq_zero_iff`

 Trivial zeros: for a complex Dirichlet character χ mod N, not necessarily primitive, and
e ≥ 1, L(χ, −e) = 0 exactly when χ(−1) = (−1)^e. 

### `sum_mul_bernoulli_eq_neg_mul_LFunction`

 Hurwitz's formula for the twisted Bernoulli sums. Let `χ` be a complex Dirichlet character
mod `N`, let `e ≥ 1`, and let `β a` be the integer `(e + 2)! N ^ (e + 1) B_{e+1}(a / N)`. Then
`∑ χ(a) β a = -(e + 2)! (e + 1) N L(χ, -e)`, the sum over `0 ≤ a < N`. 

### `sum_mul_bernoulli_ne_zero`

 The twisted Bernoulli sums of the right parity are nonzero. Let `χ` be a complex Dirichlet
character mod `N` with `χ(-1) = -(-1) ^ e`, let `e ≥ 1`, and let `β a` be the integer
`(e + 2)! N ^ (e + 1) B_{e+1}(a / N)`. Then `∑ χ(a) β a ≠ 0`, the sum over `0 ≤ a < N`. 

### `voronoi_congruence`

 Voronoi's congruence, twisted by a Dirichlet character χ mod N. For f = N m and c ≡ 1 mod N
prime to m, (c ^ (e + 1) - 1) ∑ χ(t) t ^ (e + 1) ≡ (e + 1) c ^ e f ∑ ⌊c t / f⌋ t ^ e χ(t) modulo f²,
both sums over 0 ≤ t < f. 

### `sum_range_mul_eq_sum_sum`

 A sum over `0 ≤ t < N K` equals the double sum over `t = a + i N` with `0 ≤ a < N` and
`0 ≤ i < K`. 

### `voronoi_congruence_bernoulli`

 Voronoi's congruence for the Stickelberger sums. Let `χ` be a character mod `N` with values in
a commutative ring without additive torsion, let `c ≡ 1 mod N` be prime to `m ≥ 1`, and let
`β a = (e + 2)! N ^ (e + 1) B_{e+1}(a / N)`. Then
`(e + 2)! (e + 1) N c ^ e ∑ ⌊c a / (N m)⌋ a ^ e χ(a) ≡ (c ^ (e + 1) - 1) ∑ χ(a) β a` modulo `m`,
the first sum over `0 ≤ a < N m` and the second over `0 ≤ a < N`. 

### `mulVec_mulChar_eq_sum_smul`

 A matrix whose entry at `(s, t)` depends only on `t / s` has every character as an
eigenvector. 

### `det_ne_zero_of_forall_sum_mul_ne_zero`

 Such a matrix has nonzero determinant if no complex eigenvalue `∑ χ t * g t` is zero. 

### `abs_bernoulliFun_lt`

 For `e ≥ 1` and `0 ≤ x ≤ 1`, the Bernoulli function satisfies `|B_{e+1}(x)| < 17 (e + 1)!`,
by its Fourier series. 

### `exists_modEq_one_coprime_dvd_of_prime`

 For a prime `l`, one of `c = 1 + N` and `c = 1 + 2 N` is prime to `l`. This `c` is `≡ 1 mod N`,
and `(c ^ e - 1) (c ^ (e + 1) - 1)` divides, for every `Y`,
`((1 + N) ^ e - 1) ((1 + N) ^ (e + 1) - 1) ((1 + 2 N) ^ e - 1) ((1 + 2 N) ^ (e + 1) - 1) Y`. 

### `mul_sub_one_mul_le_two_pow_of_le`

 The size bound for `X`. If `d ≤ (φ N)! (64 M) ^ φ N`, where
`M = (e + 2)! Nᵉ⁺¹ (e + 1)!`, then
`((1 + N)ᵉ - 1) ((1 + N)ᵉ⁺¹ - 1) ((1 + 2 N)ᵉ - 1) ((1 + 2 N)ᵉ⁺¹ - 1) d ≤ 2 ^ (N + e + 3) ^ 6`. 

### `exists_isStickelbergerBound`

 For `N, e ≥ 1` there is an integer `1 ≤ X ≤ 2^{(N+e+3)^6}` with the Stickelberger property
`New.OddPart.IsStickelbergerBound N e X`, namely a divisibility condition for each prime together
with a congruence for the Stickelberger sums. It comes from one integer matrix over the units mod
`N` whose eigenvalues are built from the twisted Bernoulli sums; Voronoi's congruence links these
sums to the Stickelberger sums.

This is a finite-level analogue of the interpolation property of Kubota–Leopoldt ℓ-adic L-functions
at negative integers; no ℓ-adic L-function appears, and the interpolation formula itself is not
asserted. 
