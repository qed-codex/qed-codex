---
{
  "module": "proof/networks/Eight/SecCrossing_Identity.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/networks/Eight/SecCrossing_Identity.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/networks/Eight/SecCrossing_Identity.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # The eight-square identity (Degen 1818, Graves 1843): the rule of signs

This file proves `Eight.signs : Eight.Signs` (the rule of signs, the first display of the
statement), along the appendix «Proof of the eight-square identity» of the paper (Appendix F). In
quotations, [the rule of signs] stands for the number of that display.
Every step of that proof is a lemma here, with its sentence quoted, and the lemmas are put together
as in the text. Each step is proved by the reason that the text gives for it; no step runs through
the values of a block. Only two facts on single bits are read off their values: a ⊕ b ≡ a + b modulo
2 (`toNat_xor`, the four values of two bits) and b² = b (`toNat_mul_self`).
At the head of the file are small facts on ⊕ for the other files: the laws of ⊕ on blocks, which
come bit by bit from the laws of ⊕ on a bit. 

 ## Small facts on ⊕ 

### `block_ext`

 Two blocks with the same three bits are equal. 

### `bxor_bit1`

 The three bits of p ⊕ q (by definition). 

### `bxor_comm`

 p ⊕ q = q ⊕ p: the same law in each bit. 

### `bxor_assoc`

 (p ⊕ q) ⊕ r = p ⊕ (q ⊕ r): the same law in each bit. 

### `bxor_self`

 p ⊕ p = 000: the same law in each bit. 

### `bxor_zero`

 p ⊕ 000 = p: the same law in each bit. 

### `bxor_bxor_cancel`

 (p ⊕ d) ⊕ d = p. 

### `bxor_cancel_left`

 p ⊕ (p ⊕ q) = q. 

 ## The rule of signs 

### `d_ne_zero`

 «Let d = q ⊕ q'; it is not 000 because q ≠ q'»: if d were 000, then q' = q ⊕ (q ⊕ q') = q ⊕ 000 =
q. 

### `d_eq`

 «and it equals p ⊕ p' because p ⊕ q = p' ⊕ q'»: q ⊕ q' = p ⊕ (p ⊕ q) ⊕ q' = p ⊕ (p' ⊕ q') ⊕ q' =
p ⊕ p'. 

### `p'_eq`

 «So p' = p ⊕ d». 

### `q'_eq`

 «and q' = q ⊕ d». 

### `toNat_xor`

 «and compute modulo 2»: on bits, a ⊕ b ≡ a + b. (The definition of ⊕ on a bit: the four values
of (a,b).) 

### `modEq_of_eq`

 Equal numbers are congruent modulo 2. 

### `lin1`

 What stands beside q₁, q₂ and q₃ in φ(p,q): p₁ + p₂p₃, p₁ + p₂ + p₁p₃ and p₁ + p₂ + p₃ + p₁p₂. 

### `phi_linear`

 «Every term of φ(p,q) contains exactly one bit of q»: collected by that bit, φ(p,q) = (p₁ +
p₂p₃)·q₁ + (p₁ + p₂ + p₁p₃)·q₂ + (p₁ + p₂ + p₃ + p₁p₂)·q₃. 

### `mul_add_mul_xor`

 For one bit: c·a + c·(a ⊕ b) ≡ c·a + c·(a + b) = 2·c·a + c·b ≡ c·b (modulo 2). 

### `phi_add_phi_bxor`

 «so φ(p,q) + φ(p,q ⊕ d) ≡ φ(p,d) for all p» (modulo 2): the line before for each of the three
bits of q. 

### `four_phi`

 «and the sum is φ(p,d) + φ(p ⊕ d,d)»: the line before, used for p and for p ⊕ d. 

### `phiQ`

 The first part of φ: Σ_{1 ≤ i ≤ j ≤ 3} p_i q_j. 

### `phi1`

 The three other terms of φ: q₁p₂p₃, p₁q₂p₃ and p₁p₂q₃. 

### `phi_parts`

 φ is the sum of its four parts (by definition). 

### `chg1`

 The changes of the three terms of degree 3: d₁(p₂d₃ + d₂p₃ + d₂d₃), d₂(p₁d₃ + d₁p₃ + d₁d₃) and
d₃(p₁d₂ + d₁p₂ + d₁d₂). 

### `change_Q`

 «Replacing p by p ⊕ d changes Σ_{1 ≤ i ≤ j ≤ 3} p_i d_j by Σ_{1 ≤ i ≤ j ≤ 3} d_i d_j» (modulo 2).
In this and the next three: put p_i + d_i for each bit of p ⊕ d (toNat_xor) and multiply out. 

### `change_1`

 «and it changes d₁p₂p₃ by d₁(p₂d₃ + d₂p₃ + d₂d₃)»: d₁(p₂ + d₂)(p₃ + d₃) = d₁p₂p₃ + d₁(p₂d₃ +
d₂p₃ + d₂d₃). 

### `change_2`

 «p₁d₂p₃ by d₂(p₁d₃ + d₁p₃ + d₁d₃)»: (p₁ + d₁)d₂(p₃ + d₃) = p₁d₂p₃ + d₂(p₁d₃ + d₁p₃ + d₁d₃). 

### `change_3`

 «and p₁p₂d₃ by d₃(p₁d₂ + d₁p₂ + d₁d₂)»: (p₁ + d₁)(p₂ + d₂)d₃ = p₁p₂d₃ + d₃(p₁d₂ + d₁p₂ + d₁d₂). 

### `three_changes`

 «In these three changes each of p₁d₂d₃, p₂d₁d₃, p₃d₁d₂ occurs twice and d₁d₂d₃ three times». 

### `phi_add_phi_shift`

 «So φ(p,d) + φ(p ⊕ d,d) is congruent to the sum of the four changes». 

### `toNat_mul_self`

 «d_i² = d_i»: the square of a bit is the bit (0² = 0 and 1² = 1). 

### `phiQ_self`

 «With d_i² = d_i», for the first change: Σ_{1 ≤ i ≤ j ≤ 3} d_i d_j = d₁ + d₂ + d₃ + d₁d₂ + d₁d₃ +
d₂d₃. 

### `four_changes`

 «in which the terms that occur twice cancel. With d_i² = d_i this is d₁ + d₂ + d₃ + d₁d₂ + d₁d₃ +
d₂d₃ + d₁d₂d₃». 

### `seven_terms`

 «≡ 1 + (1 + d₁)(1 + d₂)(1 + d₃)». 

### `exists_bit`

 «some d_i is 1», since d is not 000. 

### `one_add_prod`

 «which is 1 because some d_i is 1»: the factor 1 + d_i is then 2, so the product is even. 

### `four_phi_odd`

 «We have to show that φ(p,q) + φ(p ⊕ d,q ⊕ d) + φ(p,q ⊕ d) + φ(p ⊕ d,q) is odd»: the chain of
the congruences above. 

### `neg_one_pow_add_neg_one_pow`

 Why oddness is what «we have to show»: (−1)^m + (−1)^n = 0 if m + n is odd. 

### `signs`

 **The eight-square identity, first form** (the rule of signs): for all blocks p, q, p', q' with
p ⊕ q = p' ⊕ q' and q ≠ q', σ(p,q)σ(p',q') + σ(p,q')σ(p',q) = 0. Same proof as in the paper, step by
step. 
