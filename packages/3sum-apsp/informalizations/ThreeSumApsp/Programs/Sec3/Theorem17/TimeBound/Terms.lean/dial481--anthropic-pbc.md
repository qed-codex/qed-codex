---
{
  "module": "ThreeSumApsp/Programs/Sec3/Theorem17/TimeBound/Terms.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Anthropic, PBC",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Programs/Sec3/Theorem17/TimeBound/Terms.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Programs/Sec3/Theorem17/TimeBound/Terms.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# Theorem 17: the time of each routine, up to a constant

The running time of the reduction of Theorem 17 is a sum of the time functions of its routines.  The
theorem bounds the additional time by "O(ν n³ log n/g + n^{ω+o(1)} D^{3/2} + n² D g)", where ν is
the exponent in `|w(e)| ≤ n^ν`; it is `κ` below.  The form for programs, `Claim.Theorem_17`, has,
here, Strassen's exponent `log₂ 7` in the second term.  This file bounds each
routine by a monomial in `n`, `√D` and `κ log n`, uniformly in `n`, `D`, `g`, `U` and `κ` under the
hypotheses of the theorem, and says which monomials are within which of the three terms.  No
constant is computed.

* `Steps t B` says that the number `t` of steps is `O(B)`, uniformly in the parameters.  Such bounds
  can be added and multiplied, and they absorb constant factors.
* Every time function is a polynomial in a few quantities, and each of these is at most a monomial
  `mon a b c = n^a (√D)^b (κ log n)^c`: `⌊√D⌋`, `g` and the size `⌈s/g⌉` of a piece are at most
  `√D`; `2^⌈log₂ n⌉ ≤ 2n`; the number of binary digits of `U ≤ n^κ` is `O(κ log n)` (section "The
  basic quantities").  So a routine takes `O(mon a b c)` steps (`StepsMon t a b c`), and the
  exponents are read off its time function, in the calculus `Scale.SoftO` on the scale `costScale`.
* All three bases are at least 1.  So a monomial is within the first term if its exponents are at
  most `(2, 1, 1)`, within the second if they are at most `(2, 3, 0)`, within the third if they are
  at most `(2, 2, 0)` (`Scale.SoftO.withinScans`, `Scale.SoftO.withinPrime`,
  `Scale.SoftO.withinBuild`).
* The choice of the prime runs through at most `√D` primes (`steps_chooseTime`).  The product of the
  two matrices is within the second term, as in the paper: Strassen's recursion makes
  `7^⌈log₂ n⌉ = O(n^{log₂ 7})` products of polynomials of degree below `p ≤ √D`
  (`steps_sqrt_mul_strSteps`).  The residues of the weights, computed bit by bit for each prime,
  take `O(√D n² κ log n)` steps, which is within the first term.


 ## The hypotheses 

### `CostParams`

 The parameters of Theorem 17 as one record, so that a bound up to a constant can be stated
uniformly in all of them. 

### `CostParams.n`

 The number of vertices per part. 

### `CostParams.D`

 The parameter `D` of the reduction. 

### `CostParams.g`

 The parameter `g` of the reduction. 

### `CostParams.U`

 The bound on the absolute values of the weights. 

### `CostParams.κ`

 The exponent in `U ≤ n^κ`. 

### `CostParams.Hyp`

 The hypotheses of Theorem 17, with the bound `U` on the weights.  The claim for
programs adds `κ ≥ 1`, as in Theorem 19. 

### `CostParams.Hyp.hD16`

 `D ≥ 16`. 

### `CostParams.Hyp.hDn`

 `D ≤ n`. 

### `CostParams.Hyp.hg`

 `g ≥ 1`. 

### `CostParams.Hyp.hgD`

 `g ≤ √D`. 

### `CostParams.Hyp.hκ`

 `κ ≥ 1`. 

### `CostParams.Hyp.hUn`

 The weights are at most `n^κ` in absolute value. 

### `one_le_D_nat`

 `D ≥ 1`, as a natural number. 

### `sixteen_le_n`

 `n ≥ 16`. 

### `one_le_n_nat`

 `n ≥ 1`, as a natural number. 

### `one_le_n`

 `n ≥ 1`. 

### `one_le_g`

 `g ≥ 1`. 

### `g_pos`

 `g > 0`. 

### `one_le_sqrt`

 `√D ≥ g ≥ 1`. 

### `sqrt_pos`

 `√D > 0`. 

### `one_le_log`

 `log n ≥ 1`, because `n ≥ 16`. 

### `one_le_κ_mul_log`

 `κ log n ≥ 1`. 

### `sqrt_mul_g_le`

 `√D g ≤ D ≤ n`. 

### `sqrt_le_n`

 `√D ≤ n`. 

 ## Numbers of steps up to a constant 

### `Steps`

 The number `t` of steps is `O(B)`, uniformly in the parameters, under the hypotheses of
Theorem 17. 

### `mono_left`

 A smaller number of steps. 

### `mono_right`

 A larger bound. 

### `add`

 `O(B) + O(B) = O(B)`. 

### `mul`

 `O(B₁) · O(B₂) = O(B₁ B₂)`. 

### `const_mul`

 A constant factor is absorbed. 

### `const`

 A constant number of steps is `O(B)` if `B ≥ 1`. 

 ## Monomials 

### `costScale`

 The scale of Theorem 17: monomials in `n`, `√D` and `κ log n`, under the hypotheses of the
theorem. 

### `mon`

 The monomial `n^a (√D)^b (κ log n)^c`. 

### `StepsMon`

 The number `t` of steps is `O(n^a (√D)^b (κ log n)^c)`. 

### `steps_of_softO`

 A bound by a monomial, as a bound up to a constant. 

 ## The basic quantities 

### `steps_n`

 The number of vertices per part. 

### `steps_sqrt`

 `s = ⌊√D⌋ ≤ √D`. 

### `steps_D`

 `D = (√D)²`. 

### `steps_g`

 `g ≤ √D`. 

### `steps_two_pow_clog`

 `2^⌈log₂ n⌉ ≤ 2n`. 

### `steps_clog`

 `⌈log₂ n⌉ ≤ 2^⌈log₂ n⌉`. 

### `steps_bitLen`

 The number of binary digits of `U ≤ n^κ` is `O(κ log n)`: `2^{len - 1} ≤ U` gives
`(len - 1) log 2 ≤ κ log n`. 

### `steps_pieceSizeNat`

 A piece has `⌈s/g⌉ ≤ s` vertices. 

### `cast_queryCapNat_le`

 `⌊n²/√D⌋ ≤ n²/√D`. 

### `steps_queryCapNat`

 `⌊n²/√D⌋ ≤ n²`. 

 ## The routines 

### `steps_tBitLen`

 The number of binary digits of `U`. 

### `steps_tDblTable`

 The table of the doubles of the prime. 

### `steps_tResidues`

 The residues of the `n²` weights of one kind: `O(log U)` steps for each. 

### `steps_tClasses`

 Sorting the pairs into classes. 

### `steps_tChunks`

 Cutting the classes into chunks. 

### `steps_tPrimes`

 The list of the primes in `[√D/2, √D)`. 

### `steps_tWriteX`

 Writing the matrix `X` of an instance takes `O(nD)` steps. 

### `steps_tWriteY`

 Writing the matrix `Y` of an instance takes `O(nD)` steps. 

### `steps_tSzTable`

 The table of the sizes of the blocks. 

### `steps_buildZTime`

 One of the matrices `P`, `Q` over `ℤ[x]/(x^p - 1)` in Z-order: `O(n² √D)`. 

### `steps_countZeroTime`

 Reading the count off the product. 

### `steps_tQueryCapNat`

 `⌊n²/√D⌋`, by counting up. 

### `steps_tCeilDiv_piece`

 The number `⌈s/g⌉` of vertices of a piece, by counting up. 

### `steps_tCeilDiv_num`

 The number of pieces, by counting up. 

 ## The three terms of the bound dominate the monomials 

### `rpow_three_half`

 `D^{3/2} = (√D)³`. 

### `mon_le_termScans`

 `n² √D κ log n ≤ κ n³ log n/g`, because `√D g ≤ n`. 

### `mon_le_termPrime`

 `n² (√D)³ ≤ n^{log₂ 7} D^{3/2}`. 

### `mon_le_termBuild`

 `n² (√D)² ≤ n² D g`. 

### `budget`

 The sum of the three terms of the bound of Theorem 17. 

### `termScans_nonneg`

 The first term is not negative. 

### `termPrime_nonneg`

 The second term is not negative. 

### `termBuild_nonneg`

 The third term is not negative. 

### `budget_nonneg`

 The sum is not negative. 

### `termScans_le_budget`

 The first term is at most the sum. 

### `termPrime_le_budget`

 The second term is at most the sum. 

### `termBuild_le_budget`

 The third term is at most the sum. 

### `_root_.ThreeSumApsp.Scale.SoftO.withinScans`

 Within the first term, `κ n³ log n/g`. 

### `_root_.ThreeSumApsp.Scale.SoftO.withinPrime`

 Within the second term, `n^{log₂ 7} D^{3/2}`. 

### `_root_.ThreeSumApsp.Scale.SoftO.withinBuild`

 Within the third term, `n² D g`. 

### `mul_add`

 A factor is distributed over a sum. 

 ## The choice of the prime 

### `le_mul_seven_pow`

 A sequence with `a(j+1) = 7 a(j) + b 4^j x + c` grows like `7^j`. 

### `steps_seven_pow_clog`

 `7^⌈log₂ n⌉ = O(n^{log₂ 7})`. 

### `steps_sqrt_mul_strSteps`

 Strassen's recursion on matrices over `ℤ[x]/(x^p - 1)`, for all primes of the range:
`O(√D · 7^⌈log₂ n⌉ p²) = O(n^{log₂ 7} D^{3/2})`. 

### `steps_sqrt_mul_countTime`

 The counts for all primes of the range: at most `√D` times the time of one count and a constant
`k`.  The summands stand in the order of `countTime`. 

### `steps_chooseTime`

 **The choice of the prime** is within the bound.  The summands stand in the order of
`chooseTime`: the list of the primes, the number of binary digits of `U`, `⌈log₂ n⌉`, and the
counts. 
