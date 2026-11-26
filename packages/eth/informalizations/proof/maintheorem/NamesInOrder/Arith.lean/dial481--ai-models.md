---
{
  "module": "proof/maintheorem/NamesInOrder/Arith.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/maintheorem/NamesInOrder/Arith.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/maintheorem/NamesInOrder/Arith.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # The inequalities by which the added polynomial goes

If the variables are x₀ … x_(n−1) and each of them occurs, the input has at most 6·(km)² bits; as no
clause is repeated, it has at most k·(2n+1)^(k+3) bits. The first number is at most 2^{6X} for X =
km/√(log m), the second at most 2^{9Y} for Y = k²·n·log log n/√(log n). So a polynomial c·L^c in the
length L of the input is at most 2^{7c·X} and at most 2^{10c·Y}, hence at most 2^{10c·min(X, Y)},
and it goes into the constant of the exponent.

**What is proved.** `variablesAreFew`, `codeIsShort`, `polynomialIsBelowTheBoundInM` (c′ = 7c),
`polynomialIsBelowTheBoundInN` (c′ = 10c), `polynomialIsBelowTheBound` (c′ the larger of these two),
`alternationCostGoesIntoC` (C = q·(max(C₁, C₂, c′ + 1) + 2), c′ that of `polynomialIsBelowTheBound`
at c = 1) and `boundInMWithoutThePolynomial` (C′ = max(C, c′) + 1, c′ that of
`polynomialIsBelowTheBoundInM` at C).

**Who uses whom.** `codeIsShort` takes n ≤ km from `variablesAreFew`. `polynomialIsBelowTheBoundInM`
and `polynomialIsBelowTheBoundInN` come from one lemma (`poly_le_two_rpow`): if N ≤ 2^{aX} and X ≥
1, then c·N^c ≤ 2^{(c + ac)X}. `polynomialIsBelowTheBound` follows from these two and `codeIsShort`,
with `MinOfBounds.min_time_le`. `alternationCostGoesIntoC` takes the bound on the length of the
input from `polynomialIsBelowTheBound`; the cost itself is bounded by `PairsToBound.choice_le`.
`boundInMWithoutThePolynomial` follows from `codeIsShort` and `polynomialIsBelowTheBoundInM`. 

 ### The length of the input 

### `variablesAreFew`

 As every variable occurs and a clause has at most k literals, n ≤ k·m. 

### `log2_succ_le`

 ⌊log₂(2n)⌋ + 1 ≤ 2x if n ≤ x and x ≥ 1. 

### `length_le_sq`

 If every variable occurs and there is at least one clause, the input has at most 6·(km)² bits (k
≥ 1; n may be 0). 

### `length_le_pow`

 As no clause is repeated, the input has at most k·(2n+1)^(k+3) bits (k ≥ 1, n ≥ 1). 

### `codeIsShort`

 The length of the input, and the two bounds on it. 

 ### Below the exponential terms 

### `poly_le_two_rpow`

 If N ≤ 2^{aX} and X ≥ 1, then c·N^c ≤ 2^{(c + ac)X}. 

### `le_expM`

 k ≤ km/√(log m) and log m ≤ km/√(log m), for k ≥ 1 and m ≥ 2. 

### `sq_le_two_rpow`

 6·(km)² ≤ 2^{6X}, X = km/√(log m), for k ≥ 1 and m ≥ 2. 

### `pow_le_two_rpow`

 k·(2n+1)^(k+3) ≤ 2^{9Y}, Y = k²·n·log log n/√(log n), for k ≥ 1 and n ≥ 4. 

### `polynomialIsBelowTheBoundInM`

 A polynomial in km is below the bound in m. 

### `polynomialIsBelowTheBoundInN`

 A power of k·(2n+1)^(k+3) is below the bound in n. 

### `two_le_min`

 The smaller of the two exponents is at least 2. 

### `polynomialIsBelowTheBound`

 So a polynomial in the length of the input is below the bound of the Main Theorem: by
`codeIsShort` it is below both polynomials, which are below the two bounds. 

### `alternationCostGoesIntoC`

 The cost of the alternation goes into C: the length of the input is below the bound by
`polynomialIsBelowTheBound` at c = 1. 

 ### The first sentence of Theorem A (c) with nothing added 

### `timeM_add_timeM_le`

 2^{aX} + 2^{bX} ≤ 2^{(max(a, b) + 1)X}, all rounded down, X = km/√(log m). 

### `boundInMWithoutThePolynomial`

 EVERY machine that meets the bound in m with a polynomial in the length of the input added meets
it with nothing added, with another constant: by `codeIsShort` the length is at most 6·(km)², and by
`polynomialIsBelowTheBoundInM` the polynomial is below the bound in m. 
