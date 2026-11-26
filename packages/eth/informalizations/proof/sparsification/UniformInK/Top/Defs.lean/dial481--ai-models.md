---
{
  "module": "proof/sparsification/UniformInK/Top/Defs.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/sparsification/UniformInK/Top/Defs.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/sparsification/UniformInK/Top/Defs.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # One function for all widths k: parameters, helper functions and interface statements

The twin of proof/rates/ClauseBound/ParityChecks/TopDefs.lean and
proof/rates/ClauseBound/Both/Defs.lean. The input is 1ᵏ 0 1ⁿ 0 and the clauses; the width k is read
from it (`kOf`, `fmlOf` of proof/rates/ClauseBound/Alg/Top.lean).
What differs from a fixed width:
* the sparsification uses the thresholds `thetaU τ`, so that Δ = 2^β with β = `betaU k s` =
  2k(4s+17), linear in k;
* the precision s is large enough for the width k when s ≥ `s0U` k = 2·(number of binary digits of
  k), which gives k² ≤ 2^s;
* the walk is called with the width cut off at ⌊log₂(n+1)⌋ (`kcU`), so that 2^k can be written in
  unary on every input; whenever the walk is used, the cut-off does nothing.
This file has definitions only. The statements `St…` are propositions; one file proves each of them. 

 ### The parameters for width k and precision s 

### `betaU`

 The code parameter: 2^(betaU k s) = τ^(2k) for τ = 2^(4s+17). It is at least the number of
clauses per variable of a leaf, and at least `bsumU τ k`. 

### `s0U`

 The precision s is large enough for the width k if s ≥ s0U k; then k² ≤ 2^s. 

### `blockU`

 2^β, cut off at n + 1. The function uses the networks only if 2^β ≤ n + 1, and then this is 2^β. 

### `kcU`

 The width, cut off at ⌊log₂(n+1)⌋. 

### `kU`

 The width written in the input. 

### `nU`

 The number of variables written in the input. 

 ### The functions 

### `bruteU`

 Exhaustive counting on the formula written in p.1: how many numbers y below 2^n, cut off at the
length of the pad p.2, code a satisfying assignment. 

### `restU`

 The exponent of a pad that suffices for everything but the networks: the list of profiles, the
lists of the checks, the rounds of the walk, the stack of the walk. 

### `needU`

 The exponent of a pad that suffices for n variables at the index i with precision s. 

### `idxU`

 The index of the level picked for the input x. 

### `precU`

 The precision picked for the input x. 

 ### Whether every variable occurs 

### `allOccU`

 Does every variable below n occur in the formula written in x? 

 ### The budgets 

### `StLeavesU`

 The number of leaves: Σ_{j ≤ kn/τ} C(bsumU τ k · n, j) ≤ 2^(⌊n/2^s⌋ + 1) for τ = 2^(4s+17), k ≥
1 and s ≥ s0U k. 

### `StParU`

 The parameters fit: clauses per variable of a leaf; and the threshold is large enough for the
width. 

 ### Correctness 

### `StAllOccU`

 On the code of an instance, `allOccU` says whether every variable occurs. 

 ### The running time of the padding machine against the bound in n 

### `FallBack`

 What the fall-back to exhaustive counting needs of the rate r: where k² is larger than a
multiple of log n, k²·r(n) is bounded below. 
