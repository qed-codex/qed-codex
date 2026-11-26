---
{
  "module": "proof/rates/ClauseBound/ParityChecks/Params.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/ClauseBound/ParityChecks/Params.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/ClauseBound/ParityChecks/Params.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # Parameters for the run of ClauseBound.ParityChecks.RunDefs that chooses the checks: a variant, not the parameters of Step 2 of Appendix D
These parameters are a variant that the paper does not state; they are not those of Step 2 of
Appendix D: here nb = ⌊n/⌈log₂(2Δ)⌉⌋ need not be a power of two,
r is chosen with (5/8)^r in place of (3/4)^r, and a binomial series is cut off at i₀. The parameters
nb, β₀, r, i₀, β₁, β are computed from n, Δ and m. Two of the conditions of the run hold for all n.
The others hold for n ≥ n₀(c) if Δ ≤ (⌊log₂ n⌋ + 1)^c.
With ℓ = ⌊log₂ n⌋ and t = ⌈log₂(ℓ + 1)⌉, all that is used of the size of n is 84·(c + 1)·t ≤ ℓ,
which holds as soon as ℓ ≥ 2·(84·(c + 1))². Binomial coefficients are bounded by
C(N, j) ≤ (3N/k)^k for j ≤ k ≤ N. The tail of the binomial series is bounded term by term by a
geometric series with ratio 2^{−⌈ℓ/2⌉}. 

### `LD`

 ⌈log₂(2Δ)⌉. 

### `nbOf`

 nb = ⌊n/⌈log₂(2Δ)⌉⌋. 

### `beta0`

 β₀ = ⌈log₂ C(m, nb + 1)⌉. 

### `rOf`

 r = ⌈(59/40)·(n + β₀ + 3)⌉; 59/40 is just above 1/log₂(8/5). 

### `i0Of`

 i₀ = ⌈20n/⌊log₂ n⌋⌉. 

### `beta1`

 β₁ = max_{i ≤ i₀} ⌈log₂ C(m, i)⌉. 

### `parOf`

 The parameters for n variables, m clauses, and at most Δ occurrences of each variable. 

### `pow_59`

 (8/5)^59 ≥ 2^40. 

### `choose_le_beta0`

 C(m, nb + 1) ≤ 2^{β₀}. 

### `choose_le_beta1`

 C(m, i) ≤ 2^{β₁} for i ≤ i₀. 

### `two_pow_le`

 2^X ≤ (8/5)^r if 59·X ≤ 40·r. 

### `start_parOf`

 The conditions that need no largeness of n. 

 ### Tools 

### `mul_succ_le_two_pow`

 x·(x + 1) ≤ 2^{x+1}. 

### `mul_clog_le`

 A·⌈log₂(ℓ + 1)⌉ ≤ ℓ for ℓ ≥ 2A². 

### `lin_le_two_pow`

 200·ℓ + 300 ≤ 2^ℓ for ℓ ≥ 12. 

### `choose_le_two_pow`

 C(N, j) ≤ 2^{w·k} for j ≤ k ≤ N, if 3N ≤ k·2^w. 

 ### What is used of the size of n 

### `two_Δ_le`

 2Δ ≤ 2^{⌈log₂(2Δ)⌉}. 

### `nb_mul_le`

 nb·⌈log₂(2Δ)⌉ ≤ n. 

### `Big`

 The hypotheses on n, Δ and m, with ℓ = ⌊log₂ n⌋ and t = ⌈log₂(ℓ + 1)⌉. 

### `hA'`

 84·c·t + 84·t ≤ ℓ. 

### `Δ_le`

 Δ ≤ 2^{c·t}. 

### `LDt_le`

 42·(⌈log₂(2Δ)⌉ + t) ≤ ℓ. 

### `beta0_le`

 β₀ ≤ 3·⌈log₂(2Δ)⌉·(nb + 1). 

### `beta0_le'`

 β₀ ≤ 3n + 3·⌈log₂(2Δ)⌉. 

### `i0_spec`

 20n ≤ ℓ·i₀ ≤ 20n + ℓ − 1. 

### `beta1_le`

 β₁ ≤ (⌈log₂(2Δ)⌉ + t)·i₀. 

### `beta1_small`

 2·(⌈log₂(2Δ)⌉ + t)·i₀ ≤ n. 

 ### The tail of the binomial series 

### `term_le`

 One term of the series beyond i₀. 

### `series_real`

 The binomial series cut off at i₀, over the real numbers. 

### `poly_le`

 12·Δ·⌈log₂(2Δ)⌉·ℓ ≤ 2^{⌊ℓ/2⌋}. 

### `key`

 6·m·2^{⌈ℓ/2⌉} ≤ nb·i₀. 

### `ten_n_le`

 10n ≤ ⌈ℓ/2⌉·i₀. 

### `series`

 The binomial series cut off at i₀. 

### `drift`

 The bound 2/2^{10n} of `series`, times 2^n·C(m, nb + 1) and times m·r, is below 1/4. 

### `hyp`

 All that the run needs. 

### `exists_n0`

 For n large enough in terms of c, if 2 ≤ Δ ≤ (⌊log₂ n⌋ + 1)^c and nb < m ≤ Δ·n, the parameters
satisfy all that the run needs, with ε = 2^{1−10n}, and r ≤ 6n, β ≤ 5n. 
