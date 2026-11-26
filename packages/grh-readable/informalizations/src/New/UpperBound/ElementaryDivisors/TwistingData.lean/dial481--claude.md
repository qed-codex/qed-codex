---
{
  "module": "src/New/UpperBound/ElementaryDivisors/TwistingData.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/ElementaryDivisors/TwistingData.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/ElementaryDivisors/TwistingData.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Frobenius cycles, the twisted action of GL_k(W), depth and defect

This file contains the definitions for the theorem on elementary divisors
(`New.FrobeniusCycle.elementary_divisors`). Let `W` be a local ring with finite residue field.
Variables are pairs `(b, s)` of an index `b : Fin k` and a letter `s : ZMod N`.

## Main definitions and results

* `New.FrobeniusCycle`: a prime number `p` with a square root `sqrtPrime` in `R`, a power `P` of
  `p`, and ring maps `embedding s : W → R`, each marked even or odd, and each the `P`-th power of
  the one before modulo `p`.
* `New.FrobeniusCycle.letterMatrix`, `New.FrobeniusCycle.polyAction`,
  `New.FrobeniusCycle.letterRep`: `g` acts on the letter `s` through the image under `embedding s`
  of `g` (even) or of its inverse transpose (odd), both on polynomials and on coefficient vectors of
  forms of degree `n` in each letter. `New.FrobeniusCycle.polyAction_polyOfCoeffs` says that the two
  actions agree.
* `New.FrobeniusCycle.depth`, `New.FrobeniusCycle.defectWeight`: the depth of a monomial, and the
  weight of a variable in the defect of a monomial at a letter.
* `New.FrobeniusCycle.translatesIn`, `New.FrobeniusCycle.defectConditions`: vectors whose
  translates have given coefficients in an ideal.
* `New.FrobeniusCycle.deepForms`: vectors all of whose translates have only monomials of large
  depth.

Notions from other files:
* `New.linSubst z`: for a matrix `z` over `R`, the `R`-algebra map of polynomial rings that sends
  `X b` to `∑ t, z t b • X t`.
* `New.Monomials σ n`: the exponent vectors of degree `n` on the variables `σ`.
* `New.exponentOf β`, `New.polyOfCoeffs F`: the exponent vector on the variables `(b, s)` that is
  `β s` in the letter `s`, and the polynomial `∑ β, F β • x ^ β`.
* `New.symPowMatrix n`, `New.kroneckerPi`: the `n`-th symmetric power of a matrix, and the Kronecker
  product of a family of matrices.
* `New.levi W τ`, `New.parahoric W τ`: for a labelling `τ : Fin k → ℕ` of the indices, the matrices
  in `GL_k(W)` whose entry `(i, j)` is zero whenever `τ i ≠ τ j`, and those whose entry `(i, j)`
  lies in the maximal ideal of `W` whenever `τ i < τ j`.

## Notation

Matrices act on vectors of coefficients, so they are the transposes of the matrices substituted in
the variables: for both parities, the translate of a polynomial `h` in the letter `s` by `g` is
`h ∘ g_sᵀ`, where `g_s = T.letterMatrix s g`.

## Relation to the literature

See `New.UpperBound.ElementaryDivisors.DefectCount` for related work.


### `Exponents`

 The exponents of the monomials that are homogeneous of degree `n` in each of the `N` letters,
with `k` variables in each letter. 

### `twoBlock`

 For natural `r`, the labelling of the indices `b : Fin k` that is `0` if `b < r` and `1`
otherwise. 

### `defectThreshold`

 The number `c* = 3 k c`, for the rank `k` and a precision `c` of congruences modulo powers of
the square root of `p`. It is the unit in which later files state their thresholds for defects. 

### `FrobeniusCycle`

 A Frobenius cycle: a prime `p` with `P = p ^ frobExp ≥ 5`, where the residue field of `W` has
`P ^ N` elements. It also gives ring maps `embedding s : W → R` for `s` in `ℤ/N`, alternately even
and odd, with `embedding (s + 1) ≡ embedding s ^ P` modulo `p`, and an element `sqrtPrime` of `R`
with `sqrtPrime ^ 2 = p`. 

### `FrobeniusCycle.p`

 The prime `p`. 

### `FrobeniusCycle.frobExp`

 The exponent `frobExp`, with `P = p ^ frobExp`. 

### `FrobeniusCycle.embedding`

 The ring maps `ι_s : W → R`, one for each letter `s ∈ ℤ/N`. 

### `FrobeniusCycle.isEven`

 Whether the letter `s` is even (`true`) or odd (`false`). 

### `FrobeniusCycle.sqrtPrime`

 A square root of `p` in `R`. 

### `FrobeniusCycle.prime`

 `p` is prime. 

### `FrobeniusCycle.five_le_P`

 `P = p ^ frobExp` is at least `5`. 

### `FrobeniusCycle.sqrtPrime_sq`

 `sqrtPrime ^ 2 = p` in `R`. 

### `FrobeniusCycle.frobenius_congr`

 `embedding (s + 1) ≡ embedding s ^ P` modulo `p`. 

### `FrobeniusCycle.isEven_succ`

 Even and odd letters alternate. 

### `FrobeniusCycle.card_residueField`

 The residue field of `W` has `(p ^ frobExp) ^ N` elements. 

 ### The twisted action 

### `P`

 The prime power `P = p ^ frobExp` of the Frobenius cycle. 

### `q`

 The number `q = P ^ N` of elements of the residue field of `W`. 

### `map`

 For a Frobenius cycle over `R` and a ring map `φ : R →+* R'`, the Frobenius cycle over `R'`
obtained by composing each ring map `embedding s` with `φ` and applying `φ` to `sqrtPrime`. 

### `letterMatrix`

 The homomorphism sending g in GL_k(W) to the matrix g_s over R: ι_s(g) if the letter s is
even, ι_s of the inverse transpose if s is odd. 

### `polyAction`

 The action of GL_k(W) on polynomials in the variables x_{bs}: g sends x_{bs} to ∑_c
(g_s)_{cb} x_{cs}, with g_s = `New.FrobeniusCycle.letterMatrix` s g. 

### `letterRep`

 The matrix ρ(g) of g in GL_k(W) on forms of degree n in each letter: the Kronecker product
over s of the n-th symmetric powers of `New.FrobeniusCycle.letterMatrix` s g. 

 ### Depth, defect and the coefficient condition 

### `deepIndicator`

 The indicator of the deep variables `x = (b, s)`, with `b` counted from `0`: it is `1` if `s`
is even and `r ≤ b`, or `s` is odd and `b < r`, and `0` otherwise. 

### `depth`

 The depth of a family β of exponent vectors of degree n, one for each letter: the total degree
of the monomial x^β in the variables that are deep for r (`New.FrobeniusCycle.deepIndicator`). 

### `rootVar`

 For indices a,a' and letter s, the variable index (a',s) if s is even and (a,s) if s is odd. 

### `defectWeight`

 The weight of the variable `x = (b, s)` in the defect of a monomial at the letter `i` along the
root `(a, a')`; the defect is the sum of these weights over the monomial. Write
`u_s = T.rootVar a a' s` and `ū_s = T.rootVar a' a s`. The weight is `P ^ ((s - i) mod N) / (q - 1)`
times `[x = u_s] - [x = ū_s]`, plus `1` if `x = u_i`. For the recursive description of the defect
see `New.FrobeniusCycle.defectWeight_dotProduct_permStep`. 

### `translatesIn`

 The submodule of the coefficient vectors `F : Exponents N k n → R` with `(ρ(g) F) β ∈ I` for
all `g` in the Levi subgroup `levi W τ` and all `β` in the set `B` of exponents, where
`ρ = T.letterRep n`. Here `τ` labels the indices `Fin k` by natural numbers, and `levi W τ`
consists of the matrices in `GL_k(W)` whose entry `(i, j)` is zero whenever `τ i ≠ τ j`. 

### `defectConditions`

 The coefficient vectors F such that (ρ(g)F)_β lies in I, with ρ = `New.FrobeniusCycle.letterRep`
n. This must hold whenever g is block diagonal with blocks of sizes a' and k − a' and β has defect
along the root (a, a') (`New.FrobeniusCycle.defectWeight`) above h at some letter. 

### `deepForms`

 The coefficient vectors F of forms of degree n in each letter such that, for every g in GL_k(W),
all monomials of ρ(g)F have depth (`New.FrobeniusCycle.depth`, for r) at least d. 

 ### First properties 

### `frobenius_pow_congr`

 For a Frobenius cycle `T` and natural `n`, the ring map of the letter `s + n` is the `P ^ n`-th
power of that of the letter `s` modulo `p`. 

### `p_dvd_embedding_of_mem_maximalIdeal`

 The ring map `T.embedding s : W → R` of the letter `s` sends the maximal ideal of `W` into
`(p)`. 

### `p_dvd_letterMatrix_of_mem_parahoric_of_isEven`

 Let `g` lie in the parahoric subgroup of `τ`. Each letter `s` in `ℤ/N` is marked even or odd by
`T.isEven s`, neighbouring letters differently, and on an even letter the matrix
`T.letterMatrix s g` is the entrywise image of `g` under the ring map `T.embedding s : W → R`. If
`s` is even and `τ i < τ j`, then `p` divides the entry `(i, j)` of this matrix. 

### `p_dvd_letterMatrix_of_mem_parahoric_of_not_isEven`

 Let `g` lie in the parahoric subgroup of `τ`. Each letter `s` in `ℤ/N` is marked even or odd by
`T.isEven s`, neighbouring letters differently, and on an odd letter the matrix `T.letterMatrix s g`
is the entrywise image of the transpose of `g⁻¹` under the ring map `T.embedding s : W → R`. If `s`
is odd and `τ j < τ i`, then `p` divides the entry `(i, j)` of this matrix. 

### `p_dvd_letterMatrix_of_mem_parahoric`

 Let `g` lie in the parahoric subgroup of `τ`. Suppose that `τ i < τ j` if `s` is even, and
`τ j < τ i` if it is odd. Then `p` divides the entry `(i, j)` of `T.letterMatrix s g`. 

### `polyAction_X`

 Under `T.polyAction`, an element `g` of GL_k(W) sends the variable `X x`, where `x = (c, s)`, to
`∑ b, (g_s) b c • X (b, s)`, where `g_s = T.letterMatrix s g`. 

### `diagonal_pow_depth`

 Fix a threshold `r`. The variable `(b, s)` is deep if `s` is even and `r ≤ b`, or `s` is odd and
`b < r`; the number `T.deepIndicator r (b, s)` is `1` on deep variables and `0` on the others.
An element `β` of `Exponents N k n` is a monomial of degree `n` in each letter, and
`T.depth k n r β` is its degree in the deep variables. The diagonal matrix with entries
`t ^ T.depth k n r β` is the Kronecker product over the letters `s` of the `n`-th symmetric powers
of the diagonal matrices that scale the deep variables of `s` by `t` and fix the others. 

### `polyAction_polyOfCoeffs`

 For a Frobenius cycle `T`, an element `g` of `GL_k(W)` acts on polynomials in the variables
`x_{(b, s)}` by `T.polyAction g`: in each letter `s` it substitutes linearly by the matrix
`T.letterMatrix s g`, which is the image in `R` of `g` (even `s`) or of its inverse transpose
(odd `s`). A coefficient vector `F` stands for the form `∑ β, F β • x ^ β` of degree `n` in each
letter. The matrix `T.letterRep n g`, the Kronecker product over the letters of the `n`-th symmetric
powers of these matrices, represents the action on such forms. 

### `letterRep_map`

 The matrix of `g` on forms for the Frobenius cycle `T.map φ`, obtained from `T` along the ring
map `φ : R →+* R'`, is the entrywise image under `φ` of the matrix of `g` for `T`. 

 ### Bounds on the defect weights 

### `five_mul_P_pow_le_q`

 For a Frobenius cycle `T`, let `P = T.P` be its prime power, which is at least `5`, and let
`q = T.q = P ^ N`. For every letter `s` one has `5 P ^ s ≤ q`, where `s` is read in
`{0, …, N - 1}`. 

### `defectWeight_sub_mem_Icc`

 Let `a ≠ a'`. In the letter `s` let `u = T.rootVar a a' s` be the variable `(a', s)` if `s` is
even and `(a, s)` if `s` is odd, and let `ū = T.rootVar a' a s` be the other of these two variables.
The defect of a monomial at the letter `i` along the root `(a, a')` is its weighted degree for the
real weights `T.defectWeight i a a'`. These are `P ^ (1 + (s - 1 - i).val) / (q - 1)` at `u`,
`-P ^ (s - i).val / (q - 1)` at `ū` and `0` at the other variables. The weight of `u` minus the
weight of `ū` lies in `[0, 3 / 2]`. 

### `sum_P_pow_le`

 Let `P = T.P` be the prime power of the Frobenius cycle, which is at least `5`, and let
`q = T.q = P ^ N`. As `s` runs over the letters, the exponent `1 + (s - 1 - i).val` runs over
`1, …, N`, and the sum `P + P ^ 2 + ⋯ + P ^ N` is at most `2 (q - 1)`. 

### `abs_weight_defectWeight_le`

 The defect of an exponent vector `α` at the letter `i` along the root `(a, a')` is the sum of
`α x * T.defectWeight i a a' x` over the variables `x = (b, s)`. If `α` has degree at most `d` in
each letter, then its defect has absolute value at most `2 d`. 
