---
{
  "module": "proof/sparsification/SparsificationLemma/Mach/Full.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/sparsification/SparsificationLemma/Mach/Full.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/sparsification/SparsificationLemma/Mach/Full.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # Parts (a) to (d) of the theorem on sparsification `SparsABCD` of Mach/Defs.lean, on a Turing machine
This four-part form, for k-CNFs, is not stated in the paper; it belongs to Lemma 4, Appendix C and
Step 5 of Appendix D.
`sparsABCD` derives `SparsABCD` from `Prints`, the statement that one machine prints the outputs of
the sparsification with the thresholds given by τ = 2^(4s+17) (a threshold of the sparsification,
not the τ of Definition 2) within C₀·(length of the input + 2^k)^C₀·2^(C₀·⌊n/2^s⌋) steps.
The machine is the same, and C = C₀ + 81. Let s = `precE C k ε`, the larger of `s0U k` and
⌈log₂⌈C/ε⌉⌉, and B = Ck/ε.
From C/ε ≤ 2^s we get n/2^s ≤ εn, which gives (a) by `Geo.StThmS`, and C₀·⌊n/2^s⌋ ≤ εn, which gives
(d). Part (b), and that the outputs are k-CNFs without repeated clauses, are in `Geo.StThmS`.
For (c): 2^(s0U k) ≤ 4k² and 2^⌈log₂⌈C/ε⌉⌉ ≤ 4C/ε, and both are at most 4B²/C. So 81·2^s ≤ 4B²,
hence 2^(4s+17) = (2^s)^4·2^17 ≤ (2^25/3^16)·B^8 ≤ B^8 and (2^(4s+17))^(2k) ≤ B^(16k). 

### `two_pow_s0U_le`

 2^(s0U k) ≤ 4k² for k ≥ 1. 

### `two_pow_clog_le`

 2^⌈log₂ N⌉ ≤ 2N for N ≥ 1. 

### `div_le_two_pow_precE`

 C/ε ≤ 2^s for s = `precE C k ε`. 

### `two_pow_precE_le`

 C·2^s ≤ 4·(Ck/ε)² for s = `precE C k ε`, if C ≥ 1, k ≥ 1 and ε ∈ (0,1]. 

### `two_pow_betaU_le`

 Part (c): 2^(2k(4s+17)) ≤ (Ck/ε)^(16k) for s = `precE C k ε`, if C ≥ 81, k ≥ 1 and ε ∈ (0,1]. 

### `mul_div_le_eps`

 c·⌊n/2^s⌋ ≤ εn, if c ≤ C, C/ε ≤ 2^s and ε > 0. 

### `sparsABCD_of`

 The theorem on sparsification, parts (a) to (d), from `Geo.StThmS` (the theorem for the
thresholds with τ = 2^(4s+17)) and `Prints`. 

### `sparsABCD`

 The theorem on sparsification, parts (a) to (d), from `Prints`, the statement that one machine
prints the outputs (proved as `prints` in Mach/Main.lean). 
