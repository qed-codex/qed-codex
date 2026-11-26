---
{
  "module": "src/New/UpperBound/ElementaryDivisors/RootLemma.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/ElementaryDivisors/RootLemma.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/ElementaryDivisors/RootLemma.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Gauss filtrations, Stepanov's count and the root lemma

The group GL_k(W) acts on polynomials over R in variables x_{b,s} (b < k, s ∈ ℤ/N) through a
`New.FrobeniusCycle`: a power P of a prime p, ring maps ι_s : W → R with ι_{s+1} ≡ ι_s^P mod p,
and w in R with w² = p. The indices s ∈ ℤ/N are called letters and are alternately even and odd.
This file shows which monomials can carry the least w-adic order plus weight among all translates
of a polynomial.

* `New.stepanov_count`: Stepanov's count of zeros at the residue classes of a local ring.
* `New.IsRealFiltration`, `New.adicFiltration`, `New.gaussFiltration`: multiplicative filtrations
  indexed by ℝ, the w-adic one, and the Gauss filtration on polynomials with weighted variables.
* `New.FrobeniusCycle.RootAt`: a root and a letter, with the variables X_s, Y_s, the substitution
  that defines the auxiliary polynomial, and its expansions at the rational points.
* `New.FrobeniusCycle.defect_nonpos_of_extreme_term`: for weights that rise by an amount in [1/2, 1]
  from X_s to Y_s, a term of least order plus weight among all translates by SL₂(W) has defect at
  most 0 (see `New.FrobeniusCycle.defectWeight`).

The proof compares the degree of an auxiliary binary form with its zeros at the q + 1 rational
points of the projective line, in the affine coordinate t. For an extreme term it writes the defect
in the two variables X_s, Y_s of each letter, substitutes polynomials in t for them, and expands one
coefficient at infinity (which gives its degree) and at the q finite points.

Notions from other files:
* `New.FrobeniusCycle.polyAction`: the action of GL_k(W) on polynomials in the variables x_{b,s}; g
  sends x_{b,s} to ∑_c (g_s)_{cb} x_{c,s}, where g_s is ι_s(g) for even letters s and ι_s of the
  inverse transpose of g for odd s.
* `New.levi`: the Levi subgroup of a labelling τ of the indices, the matrices in GL_k(W) whose (i,j)
  entry vanishes whenever τ(i) ≠ τ(j).
* `New.FrobeniusCycle.rootVar`: for indices a, a' and a letter s, the variable (a',s) if s is even
  and (a,s) if s is odd.
* `New.FrobeniusCycle.defectWeight`: at a letter i along a root (a, a'), the weight of x_{b,s} is a
  signed multiple of P^((s - i) mod N) / (q - 1) at the variables X_s, Y_s and 0 elsewhere, plus 1
  at Y_i; the sum of these weights over a monomial is its defect.

## Notation

After the substitution the variable Y_s, s ≠ i, is kept by `mainSubst` as the variable
`X (D.varY s)` of the letter s. The functions `RootAt.sign` and `RootAt.moveSign` carry the signs.

## Relation to the literature

The group SL₂(W), placed in two rows and columns of GL_k(W), acts on polynomials in a circle of
variable sets, alternately by Frobenius twists and by inverse transposes, and a term that is least
for valuation plus a suitable weight among all translates has exponents obeying linear inequalities.
Other files use them to bound the elementary divisors of the Hecke operator. Twisted Dickson forms
on Frobenius twists of symmetric powers, weight inequalities via the Lang map, and the count of
zeros against degree are known in the literature. Related work: Ghate–Jana, Modular representations
of GL2(F_q) using calculus, 2025; Imai–Koskivirta, Automorphic vector bundles on the stack of
G-zips, 2021; Bombieri, Counting points on curves over finite fields, Sém. Bourbaki 430, 1973.


### `stepanov_count`

 Stepanov's count. Let `W` be a local ring with `q` residue classes and `ι : W → R` a ring map.
If a non-zero polynomial `Φ` over `R` is divisible by `(X - ι x) ^ E` for every `x` in `W` (that
is, `X ^ E` divides `Φ(X + ι x)`), then `E * q ≤ deg Φ`. 

 ### Filtrations and Gauss weights 

### `IsRealFiltration`

 A decreasing multiplicative filtration of a commutative ring by additive subgroups F_t, t
real: 1 ∈ F_0, F_s·F_t ⊆ F_{s+t}, and F_t ⊆ F_s for s ≤ t. 

### `IsRealFiltration.antitone`

 The filtration is decreasing: `F t ≤ F s` for `s ≤ t`. 

### `adicFiltration`

 For a ring element `w` and real `t`, the additive subgroup of elements divisible by `w` to the
power `max(⌈t⌉, 0)`. 

### `gaussFiltration`

 The Gauss filtration: for subgroups `F t` of `R` and weights `c` of the variables, the additive
group of polynomials whose coefficient at each `x ^ α` lies in `F (t - c · α)`. 

### `monomial_mem_gaussFiltration`

 The term `x * X ^ α` lies in the level `t` of the Gauss filtration if `x` lies in
`F (t - c · α)`. 

### `algHom_sub_mem_of_mem_gaussFiltration`

 Substitution respects weights. Let `G` be a filtration of the `R`-algebra `A` such that the
algebra map sends `F t` into `G t`, and let `f` lie in the level `t` of the Gauss filtration for
`F` and the weights `c` of the variables. Let `χ`, `ψ` be substitutions with `χ X_i` in `G (c i)`
and `ψ X_i - χ X_i` in `G (c i + 1 / 20)`. Then `ψ f` lies in `G t` and `ψ f - χ f` in
`G (t + 1 / 20)`. 

 ### One root and one letter 

### `rootSL`

 The group `SL₂(W)` placed in the rows and columns `a`, `a'` of `GL_k(W)`: the matrices of
determinant `1` that agree with the identity matrix at `(i, j)` unless both `i` and `j` are among
`a`, `a'`. It is trivial for `a = a'`. 

### `FrobeniusCycle.RootAt`

 A root `(a, a')` of `GL_k` and a letter `i`, the data at which a defect is measured. 

### `FrobeniusCycle.RootAt.letter`

 The letter `i`. 

### `FrobeniusCycle.RootAt.fst`

 The index `a`. 

### `FrobeniusCycle.RootAt.snd`

 The index `a'`. 

### `FrobeniusCycle.RootAt.ne`

 The two indices differ. 

### `varX`

 The variable `X_s`: index `a` at even and `a'` at odd letters `s`. 

### `varY`

 The variable `Y_s`: index `a'` at even and `a` at odd letters `s`. 

### `IsFixed`

 The variables whose index is neither `a` nor `a'`. 

### `swapVar`

 The permutation of the variables that swaps `X_s` and `Y_s` in each letter. 

### `merge`

 The map of variables that sends `Y_i` to `X_i` and fixes the others. 

### `sign`

 The sign at `Y_s`: `-1` if `s` has the parity of `i = D.letter` and `1` otherwise. It is `0` at
the other variables. The parity of a letter is its mark `T.isEven` in the twisting data, which
alternates from `s` to `s + 1`. 

### `card`

 The number `q = P ^ N` of residue classes of `W`, as a constant whose casts `simp` keeps. 

### `frobPower`

 The power `P_s = P ^ (s - i)`, with `s - i` read in `[0, N)`. 

### `poleOrder`

 The weights `q P_s` at `X_s` and `0` at the other variables, where `q = D.card` and
`P_s = D.frobPower s`. Under the hypotheses of `HasBoundedIncrements.weight_zeroOrder_mul_card_le`,
the weight of the exponent `α` bounds the degree in `t` of the auxiliary polynomial: the coefficient
`D.mergedCoeff α` after the substitution `D.mainSubst - D.crossSubst`, modulo `w ^ (l + 1)`. 

### `zeroOrder`

 The weights `q = D.card` at `Y_i`, `P_s = D.frobPower s` at `Y_s` for `s ≠ i`, and `0` at the
other variables, where `i = D.letter`. Under the hypotheses of
`HasBoundedIncrements.weight_zeroOrder_mul_card_le`, the weight of the exponent `α` bounds from
below the order of vanishing of the auxiliary polynomial (see `poleOrder`) at the points
`t = ι_i(r)`, `r ∈ W`. 

### `crossSign`

 The sign of `Y_s` at both `X_s` and `Y_s` for `s ≠ i`, and `0` at the other variables. 

### `var_cases`

 Every variable is `Y_i`, `X_i`, some `Y_s` or `X_s` with `s ≠ i`, or lies off the root. 

### `IsFixed.swapVar_merge_eq_self_and_weights_eq_zero`

 Let `D` consist of two distinct indices `D.fst`, `D.snd` in `Fin k` and a letter. Let the
variable `z = (b, s)` lie off the root. Then the maps of variables `D.swapVar` and `D.merge` fix
`z`, and the signs `D.sign`, `D.crossSign` and the weights `D.poleOrder`, `D.zeroOrder` vanish at
`z`. 

### `defectWeight_eq`

 The defect weight `T.defectWeight D.letter D.fst D.snd z` of a variable `z` equals
`(D.zeroOrder z - D.poleOrder z / q) / (q - 1)` with `q = D.card`. Summing, the defect of an
exponent is `(ν - ν') / (q - 1)`, where `ν` is its weight for `D.zeroOrder` and `q ν'` its weight
for `D.poleOrder`. 

### `swapTransvection`

 The matrix `!![0, 1; -1, x]` in the rows and columns `a`, `a'`, with `x = -r` if `i` is even and
`x = r` otherwise, written as a transposition times a transvection times the diagonal matrix with
`-1` at `a`. It relates the point at infinity of the projective line to the finite point with the
affine coordinate `ι_i(r)`. 

### `moveSign`

 The sign `-1` at the variables with index `a`, and `1` at the other variables. 

### `swapTransvection_mem_rootSL`

 Let `T : FrobeniusCycle N W R` give each letter `s ∈ ℤ/N` a parity `T.isEven s`, and let
`D : T.RootAt k` consist of two distinct indices `a = D.fst`, `a' = D.snd` below `k` and a letter
`i = D.letter`. The matrix `D.swapTransvection r`, which is `!![0, 1; -1, x]` in the rows and
columns `a`, `a'` with `x = -r` for even `i` and `x = r` for odd `i`, lies in `SL₂(W)` placed there
(`rootSL`): its three factors, the transposition of `a` and `a'`, the transvection by `x` and the
diagonal matrix with `-1` at `a`, agree with the identity elsewhere and have determinants
`-1`, `1`, `-1`. 

### `polyAction_swapTransvection_X`

 The action of the matrix `D.swapTransvection r` on the variable `z = (b, s)` with index
`b : Fin k` and letter `s : ZMod N`. Let `a = D.fst` and `a' = D.snd`. The variable
`X_s = D.varX s` is `(a, s)` for even and `(a', s)` for odd `s`, and `Y_s = D.varY s` is the other
of the two; `D.swapVar` swaps them and fixes all other variables. Up to the sign `D.moveSign z`,
which is `-1` if `b = a` and `1` otherwise, the matrix sends `X_s` to `Y_s`, sends `Y_s` to
`X_s + ε_s ι_s(r) Y_s` and fixes the other variables. Here `ι_s = T.embedding s : W → R`, and
`ε_s = D.sign Y_s` is `-1` if `s` has the parity of the letter `D.letter` and `1` otherwise;
`D.sign` is `0` at the variables other than the `Y_s`. 

### `HasBoundedIncrements`

 The weights `c` of the variables rise from `X_s` to `Y_s` by an amount in `[1 / 2, 1]`. 

### `slope`

 The slope `ρ = (c Y_i - c X_i) / q` of weights `c` of the variables, where `i = D.letter` and
`q = D.card`. The variable `t` of the auxiliary polynomial weighs `-ρ` in the expansion at infinity
and `ρ` in the expansion at a finite point, after the shift `t ↦ t + ι_i(r)`. 

### `HasBoundedIncrements.frobPower_mul_slope_le`

 If the steps of `c` lie in `[1 / 2, 1]`, then `P_s` times the slope is at most `1 / 5`, because
`5 P_s ≤ q`. 

### `HasBoundedIncrements.two_le_card_mul_frobPower_mul_slope`

 If the steps of `c` lie in `[1 / 2, 1]` and `s ≠ D.letter`, then `q P_s` times the slope is at
least `2`, because `P_s ≥ 5`. 

 ### The auxiliary polynomial 

### `mainSubst`

 The main part of the substitution, with a new variable `t = X ()`: `Y_i ↦ X_i`,
`X_s ↦ t ^ (q P_s) X_s`, and the other variables are fixed. 

### `crossSubst`

 The cross terms: for `s ≠ i`, `Y_s ↦ ε_s X_s` and `X_s ↦ ε_s t ^ P_s Y_s`, where `ε_s` is the
sign `D.sign` at `Y_s`; the other variables go to `0`. The substitution that defines the auxiliary
polynomial is `D.mainSubst - D.crossSubst`. For `ε_s = -1` it sends `(X_s, Y_s)` to
`Y_s (t ^ P_s, 1) + X_s (t ^ (q P_s), 1)`, and for `ε_s = 1` to the same with `-Y_s` for `Y_s` on
both sides. 

### `_root_.New.FrobeniusCycle.iteratedGaussFiltration`

 The Gauss filtration on polynomials over `R[t]` in which `w` weighs `1`, `t` weighs `ρ` and
each variable `z` weighs `c z - v z * ρ`. 

### `C_monomial_mul_X_mem_iteratedGaussFiltration`

 The term `C (monomial (single () n) r) * X z`, that is `r t ^ n` times the variable `X z`, lies
in `T.iteratedGaussFiltration c ρ v b` if `r = 0` or `b ≤ c z - v z * ρ + n * ρ`. That bound is the
weight of `t ^ n * X z`. 

### `HasBoundedIncrements.aeval_mem_and_sub_mem_iteratedGaussFiltration`

 Expansion at infinity. Let `w = T.sqrtPrime`, a square root of the prime `T.p` in `R`, let
`i = D.letter` and let `q = D.card = P ^ N` with `P = T.P`. In each letter `s`, `X_s = D.varX s` and
`Y_s = D.varY s` are the variables with index `D.fst`, `D.snd` if `s` is even, in reverse order if
it is odd. Let the weights `c` rise from `X_s` to `Y_s` by amounts in `[1 / 2, 1]`, let each term of
`f` have `w`-adic order plus `c`-weight at least `b`, and put
`P_s = D.frobPower s = P ^ (s - i).val` and `ρ = D.slope c = (c Y_i - c X_i) / q`.

In the filtration on polynomials in the variables `z` over `R[t]`, `w` weighs `1`, `t` weighs `-ρ`,
`X_s` weighs `c X_s + q P_s ρ` and any other variable `z` weighs `c z`. The main part `D.mainSubst`
minus the cross terms `D.crossSubst` sends `f` to level `b`, and the cross terms change the image of
`f` only in level `b + 1 / 20`. 

### `_root_.New.FrobeniusCycle.frobeniusError`

 The error in the rule `(t + ι_i(r)) ^ P ^ n = t ^ P ^ n + ι_{i + n}(r)`. 

### `frobeniusError_mul_X_mem`

 For a letter `i`, `r` in `W` and natural `n`, take the polynomial in `t` `T.frobeniusError i r
n = (t + ι_i(r)) ^ P ^ n - t ^ P ^ n - ι_{i + n}(r)`. In `T.iteratedGaussFiltration c ρ v`, `w`
weighs `1`, `t` weighs `ρ` and a variable `z` weighs `c z - v z * ρ`. So for `ρ ≥ 0` the product of
this polynomial with `z` has level `2` more than the weight of `z`. 

### `_root_.New.shiftCoeff`

 The substitution `t ↦ t + x` in the coefficients. 

### `shiftCoeff_aeval_swapTransvection_X`

 The shift of `t` undoes the transvection in `D.swapTransvection r` up to Frobenius errors. For
`a = D.fst`, `a' = D.snd` and a letter `s ∈ ℤ/N`, `X_s = D.varX s` is `(a, s)` for even and
`(a', s)` for odd `s`, and `Y_s = D.varY s` is the other of the two. Let `i = D.letter`,
`q = P ^ N`, `P_s = P ^ (s - i).val` with `P = T.P`, and `ι_s = T.embedding s : W → R`.

Act on the variable `z` by `D.swapTransvection r` through `T.polyAction`, the action of `GL_k(W)` on
polynomials in the variables `(b, s)`. Then substitute `D.mainSubst - D.crossSubst`, with values in
the polynomials over `R[t]`, and replace `t` by `t + ι_i(r)` (`shiftCoeff`). Here `ε_s = D.sign Y_s`
is `-1` if `s` has the parity of `i` and `1` otherwise.

Up to the sign `D.moveSign z`, which is `-1` if `z` has index `a` and `1` otherwise, the result is
the polynomial substituted for `D.swapVar z` plus errors `T.frobeniusError i r n = (t + ι_i(r)) ^ P
^ n - t ^ P ^ n - ι_{i + n}(r)`. They occur only for `z = Y_s`: with `d = (s - i).val`, the error
for `n = N + d` multiplies `X_s`, and `-ε_s` times the error for `n = d` multiplies `Y_s`. 

### `HasBoundedIncrements.subst_swapVar_mem_iteratedGaussFiltration`

 In each letter `s`, `X_s = D.varX s` and `Y_s = D.varY s` are the variables with the two indices
of the root, and `D.swapVar` swaps them and fixes the others. Let the weights `c` rise from `X_s` to
`Y_s` by amounts in `[1 / 2, 1]`, and put `i = D.letter`, `q = D.card = P ^ N`,
`P_s = P ^ (s - i).val` with `P = T.P` and `ρ = D.slope c = (c Y_i - c X_i) / q`. Filter polynomials
over `R[t]` so that `w = T.sqrtPrime` weighs `1`, `t` weighs `ρ` and a variable `y` weighs
`c y - D.zeroOrder y * ρ`.

Then the substitution `D.mainSubst - D.crossSubst` (`Y_i ↦ X_i`,
`X_s ↦ t ^ (q P_s) X_s - ε_s t ^ P_s Y_s`, `Y_s ↦ Y_s - ε_s X_s` for `s ≠ i`, where
`ε_s = D.sign Y_s` is `± 1`) sends `D.swapVar z` to level `c z`. 

### `HasBoundedIncrements.add_le_sub_zeroOrder_mul_slope_add_two`

 Let `i = D.letter`, and let `X_s = D.varX s`, `Y_s = D.varY s` be the two variables of the root
in the letter `s`. At a finite point a variable `y` weighs `c y - D.zeroOrder y * D.slope c`. If `c`
rises from `X_s` to `Y_s` by amounts in `[1 / 2, 1]`, then `c z + 1 / 20` is at most `2` plus the
weight of `y`, both for `y = z` and for `y = D.swapVar z`, the image of `z` when `X_s` and `Y_s` are
exchanged. 

### `HasBoundedIncrements.shiftCoeff_aeval_mem`

 Expansion at the finite point `ι_i(r)`, where `i = D.letter` and `ι_i = T.embedding i : W → R`.
In each letter `s`, `X_s = D.varX s` and `Y_s = D.varY s` are the variables with the indices
`a = D.fst`, `a' = D.snd` if `s` is even and in reverse order if it is odd. The matrix
`D.swapTransvection r` is `!![0, 1; -1, ± r]` in the rows and columns `a`, `a'` and acts on
polynomials by `T.polyAction`. Let the weights `c` rise from `X_s` to `Y_s` by amounts in
`[1 / 2, 1]`, and let each term of the translate of `f` by `(D.swapTransvection r)⁻¹` have order for
`w = T.sqrtPrime` plus `c`-weight at least `b`.

In `f`, substitute `D.mainSubst - D.crossSubst` (`Y_i ↦ X_i`,
`X_s ↦ t ^ (q P_s) X_s - ε_s t ^ P_s Y_s`, `Y_s ↦ Y_s - ε_s X_s` for `s ≠ i`, with `q = D.card`,
`P_s = D.frobPower s = T.P ^ (s - i).val` and `ε_s = D.sign Y_s`, which is `-1` if `s` has the
parity of `i` and `1` otherwise), then replace `t` by `t + ι_i(r)`. The result has level `b` when
`w` weighs `1`, `t` weighs `ρ = D.slope c = (c Y_i - c X_i) / q` and a variable `z` weighs
`c z - D.zeroOrder z * ρ`. 

### `mergedCoeff`

 The coefficient, a polynomial in `t`, of the monomial obtained from `x ^ α` by writing `X_i`
for `Y_i`. 

### `mergedCoeff_shiftCoeff`

 Shifting `t` by `x` in the coefficients of `p` shifts the polynomial `D.mergedCoeff α p` by
`x`. 

### `pow_dvd_coeff_mergedCoeff`

 In `T.iteratedGaussFiltration c ρ v`, `w = T.sqrtPrime` weighs `1`, `t` weighs `ρ` and a
variable `z` weighs `c z - v z * ρ`. Let the polynomial `p` over `R[t]` have level `b` there, and
let `X_i = D.varX i` and `Y_i = D.varY i` have the same weight, where `i = D.letter` is the letter
of the root `D`. The univariate polynomial `D.mergedCoeff α p` in `t` is the coefficient in `p` of
the monomial obtained from `x ^ α` by writing `X_i` for `Y_i`. Its coefficient of `t ^ j` is
divisible by `w ^ (l + 1)` once `b` less the weight of `t ^ j x ^ α` exceeds `l`. 

### `eq_of_mapDomain_merge_eq`

 Let `i = D.letter`. The map of variables `D.merge` sends `Y_i = D.varY i` to `X_i = D.varX i`
and fixes the others, and the weights `D.poleOrder` are `D.card * D.frobPower s` at `X_s` and `0`
at the other variables, in particular non-zero at `X_i` and `0` at `Y_i`. An exponent is determined
by its image under `D.merge` and its weight for `D.poleOrder`: the first forgets only how the degree
splits between `X_i` and `Y_i`, and the second recovers it. 

### `coeff_mergedCoeff_aeval_mainSubst`

 Put `i = D.letter`. In each letter `s`, `X_s = D.varX s` and `Y_s = D.varY s` are the two
variables of the root. The weights `D.poleOrder` are `q P_s` at `X_s` and `0` at the other
variables, where `q = D.card = P ^ N` and `P_s = D.frobPower s = P ^ (s - i).val` for `P = T.P`. In
`f` substitute `D.mainSubst`, which sends `Y_i` to `X_i` and any other variable `z` to
`t ^ D.poleOrder z * z`. Take the coefficient, a polynomial in `t`, of the monomial obtained from
`x ^ α` by writing `X_i` for `Y_i` (`D.mergedCoeff α`). Its coefficient of `t ^ d`, with `d` the
weight of `α` for `D.poleOrder`, is the coefficient of `x ^ α` in `f`: no other monomial of `f`
contributes to it. 

### `HasBoundedIncrements.weight_zeroOrder_mul_card_le`

 Zeros against degree. Let `w = T.sqrtPrime`, a square root of the prime `T.p` in `R`, let
`i = D.letter` and let `q = D.card = P ^ N` be the number of residue classes of `W`. In each letter
`s`, `X_s = D.varX s` and `Y_s = D.varY s` are the variables with the indices `a = D.fst`,
`a' = D.snd` if `s` is even and in reverse order if it is odd. Let the weights `c` rise from `X_s`
to `Y_s` by amounts in `[1 / 2, 1]`. Suppose that in all translates of `f` by `SL₂(W)`, placed in
the rows and columns `a`, `a'` (`rootSL`), each term has `w`-adic order plus `c`-weight at least
`l + c · α`, and that `w ^ (l + 1)` does not divide the coefficient of `x ^ α` in `f`.

Let `ν` be the weight of `α` for `D.zeroOrder`, which is `q` at `Y_i` and `P_s = P ^ (s - i).val` at
`Y_s` for `s ≠ i`, and `q ν'` its weight for `D.poleOrder`, which is `q P_s` at `X_s`; both weights
vanish at all other variables. Then `ν q ≤ q ν'`. 

### `FrobeniusCycle.defect_nonpos_of_extreme_term`

 The root lemma. Let `T` be a Frobenius cycle: ring maps `ι_s : W → R` for the letters `s ∈ ℤ/N`,
alternately even and odd, with `ι_{s+1} ≡ ι_s ^ P` modulo a prime `p`, where `P = T.P` is a power of
`p` and `W` has `q = P ^ N` residue classes, and a square root `w = T.sqrtPrime` of `p` in `R`.

Let `a ≠ a'`. In the letter `s` let `Y_s = T.rootVar a a' s` be the variable `(a', s)` for even and
`(a, s)` for odd `s`, and let `X_s = T.rootVar a' a s` be the other of the two. Let the weights `c`
of the variables rise from `X_s` to `Y_s` by amounts in `[1 / 2, 1]`. Suppose that in all translates
of `f` by `SL₂(W)` in the rows and columns `a`, `a'` each term has `w`-adic order plus weight at
least `l + c · α`, and that `w ^ (l + 1)` does not divide the coefficient of `x ^ α` in `f`. Then
the defect of `α` at the letter `i` is at most `0`.

These bounds along the roots are Pieri's inequalities for the exponent of a term that is least among
all translates. 

 ### Consequences 

### `FrobeniusCycle.totalDegree_polyAction_le`

 The translate of a polynomial `f` by `g` in `GL_k(W)` has total degree at most that of `f`. 

### `FrobeniusCycle.weight_sub_defectWeight_div_three`

 For the variable weights `fun x ↦ depth x - T.defectWeight i a a' x / 3`, the weight of `α` is
`weight depth α` minus a third of `weight (T.defectWeight i a a') α`. 

### `FrobeniusCycle.mem_gaussFiltration_sub_defect_div_three`

 A large defect forces a divisible coefficient. Let `a ≠ a'`, and in each letter `s ∈ ℤ/N` let
`Y_s = T.rootVar a a' s` be the variable `(a', s)` for even and `(a, s)` for odd `s`, and
`X_s = T.rootVar a' a s` the other of the two. Let `depth` be weights of the variables that rise by
`1` from `X_s` to `Y_s` in each letter. If in all translates of `f` by `SL₂(W)` in the rows and
columns `a`, `a'` each term has order for `w = T.sqrtPrime` plus depth at least `v₀`, then each term
of `f` has order plus depth at least `v₀` plus a third of its defect at the letter `i` along the
root `(a, a')`. 

### `FrobeniusCycle.weight_defectWeight_nonpos_of_least`

 The root lemma for weights that rise by `1`, over a field of characteristic `T.p`. Let `a ≠ a'`,
and let `height` be weights of the variables that rise by `1` from `X_s = T.rootVar a' a s` to
`Y_s = T.rootVar a a' s` in each letter `s ∈ ℤ/N`; these are the variables with index `a`, `a'` for
even `s` and in reverse order for odd `s`. A term of `f` whose height is least among the terms of
all translates of `f` by `SL₂(W)` in the rows and columns `a`, `a'` has defect at most `0`. 
