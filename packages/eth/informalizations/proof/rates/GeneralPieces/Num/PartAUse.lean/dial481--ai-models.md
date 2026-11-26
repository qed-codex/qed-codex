---
{
  "module": "proof/rates/GeneralPieces/Num/PartAUse.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/GeneralPieces/Num/PartAUse.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/GeneralPieces/Num/PartAUse.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # What the proofs of parts (b) and (c) of Theorem A take from part (a)

After its proof, Appendix A uses the bounds of part (a) on K_ℓ and e_ℓ in these sentences: in the
proof of part (b), «by the induction hypothesis and e ≤ 1»; in the proof of part (c), «by (a), K ≥
m^{1/90} and e = O((log m)^{−α'})» at the largest ℓ with
K_ℓ ≤ m^{1/9}; and, at the end of that proof, «e_ℓ ≥ ρ^ℓ/2 ≥ 2^{−ℓ−1} ≥ 1/log K_ℓ». Each is a named
theorem here, with the small consequences that the programs of this development need besides. All
are drawn from the four assertions of part (a): a hypothesis
`hA : TheoremAa ρ x₀`, or `PartA.thmRunningTime_a` itself in `e_le_rPow` and `e_mul_le`; only
`one_le_e_mul_K` also uses a sentence of the proof of part (a), K_ℓ ≥ 2^{18(ℓ+1)}. (The formula for
log K_{ℓ+1} is also used where case (ii) of Lemma 8
is shown to apply.) `e_le_rPow` is «e = O((log m)^{−α'})» in the form that the proof of the bound in
m uses, with log(m + 2) for log m; the last section has what the proof of the bound in n (Theorem D)
uses. 

 ## The numbers K_ℓ 

### `two_le_K`

 K_ℓ ≥ 2, because K_ℓ < K_ℓ^10. 

### `two_pow_le_logK`

 log K_ℓ ≥ 2^{ℓ+1} for x₀ ≥ 2, by the formula for log K_ℓ. 

 ## The numbers e_ℓ 

### `e_nonneg`

 e_ℓ ≥ 0, by e_ℓ ≥ ρ^ℓ/2. 

### `e_le_one`

 Proof of part (b), «by the induction hypothesis and e ≤ 1»: e_ℓ ≤ 0.85·ρ^ℓ ≤ 1. 

### `inv_two_pow_le_e`

 End of the proof of part (c), «e_ℓ ≥ ρ^ℓ/2 ≥ 2^{−ℓ−1}». 

### `one_le_e_mul_K`

 e_ℓ·K_ℓ ≥ 1, by e_ℓ ≥ 2^{−ℓ−1} and the sentence «K_ℓ ≥ 2^{18(ℓ+1)}» of the proof of part (a). 

### `inv_logK_le_e`

 «… 2^{−ℓ−1} ≥ 1/log K_ℓ», so e_ℓ ≥ 1/log K_ℓ. 

### `inv_logK_pow_le_e`

 The same with a power of the logarithm, the form in which a sequence of levels asks for it: e_ℓ
≥ 1/(log K_ℓ)^C for C ≥ 1. 

 ## The level picked for m 

### `lt_pow_ninety`

 Proof of part (c), «by (a), K ≥ m^{1/90}»: if K_{ℓ+1} > m^{1/9} then m < K_ℓ^90, by K_{ℓ+1} ≤
K_ℓ^10. 

### `e_le_of_log_le`

 «… and e = O((log m)^{−α'})»: if 0 < y ≤ d·log K_ℓ then e_ℓ ≤ 0.85·ρ^ℓ ≤ 0.85·(d·(3x₀+6)/y)^{α'}.
The text has y = log m and d = 90. 

### `e_le_div_rpow`

 The same without the power on the constant: if 1 ≤ y ≤ d·log K_ℓ for an integer d ≥ 1, then e_ℓ
≤ d·(3x₀+6)/y^{α'}, because α' ≤ 1. 

### `log_le_of_le_pow`

 If M ≤ K_ℓ^d then log M ≤ d·log K_ℓ. 

### `add_two_le_pow`

 If ⌊m^{1/9}⌋ < K_{ℓ+1} then m + 2 ≤ K_ℓ^91. 

### `e_le_rPow`

 «e = O((log m)^{−α'})» in the form that the proof of the bound in m uses: if ⌊m^{1/9}⌋ < K_{ℓ+1}
then e_ℓ ≤ 91·(3x₀+6)/(log(m+2))^{α'}. The proof is from part (a) as proved
in `Num/PartA.lean`. 

 ## The level picked for n

The second sentence of part (c) of Theorem A rests on Theorem D, whose «hypothesis holds by (a) and
(b)». The proof of the bound in n in this development asks for integers s(ℓ) with 2^{−s(ℓ)} ≤ e_ℓ
and 2^{s(ℓ)} ≤ (2/e_ℓ)^{O(1)}, in place of the text's number
between 0.85·ρ^ℓ and ρ^ℓ; s(ℓ) = ℓ + 1 will do, by `inv_two_pow_le_e` and `two_pow_le_div`. 

### `two_pow_le_div`

 2^{ℓ+1} ≤ (2/e_ℓ)^{C+1} if ρ^C ≤ 1/2, by e_ℓ ≤ 0.85·ρ^ℓ ≤ ρ^ℓ. 

### `add_four_le_pow`

 If n < K_{ℓ+1}^17 then n + 4 ≤ K_ℓ^171, by K_{ℓ+1} ≤ K_ℓ^10. 

### `e_mul_le`

 At the level picked for n, that is K_ℓ^17 ≤ n < K_{ℓ+1}^17: e_ℓ·(ℓ + 2) ≤ 3·171·(3x₀+6)·log
log(n+4)/(log(n+4))^{α'}. Here log(n+4) ≤ 171·log K_ℓ bounds e_ℓ, and 2^ℓ ≤ log K_ℓ ≤ log(n+4)
bounds ℓ. 
