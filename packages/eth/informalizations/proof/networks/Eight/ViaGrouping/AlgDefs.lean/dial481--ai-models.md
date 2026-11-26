---
{
  "module": "proof/networks/Eight/ViaGrouping/AlgDefs.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/networks/Eight/ViaGrouping/AlgDefs.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/networks/Eight/ViaGrouping/AlgDefs.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # Section 8, «The algorithm in pseudocode»: Algorithm 1 on the algorithm of the printed proof of Lemma 1 (definitions only)

The procedures COUNT, NETWORK and CLIQUE of Algorithm 1. NETWORK is the algorithm of the printed
proof of Lemma 1 (`netAlg`, proof/networks/Eight/ViaGrouping/Defs.lean): it is given a network as
Definition 2(iii) says, with the number P and procedures for
membership in S_a, W_a, Ψ_{a,b} and f_{a,b}. So the two callers of NETWORK hand these over:
* CLIQUE above level 0 (`levelAlgP`, proof/networks/Eight/ViaGrouping/LevelDefs.lean) gives, for the
  row network and the column network of ι, P = g³λ and the program `gridPsi` for Ψ_{a,a'}
  (proof/networks/Eight/ViaGrouping/GridPsiDefs.lean);
* COUNT gives, for the network of Φ, P = 6m̄ and Ψ_{a,b}(z_a, z_b) = [z_a|_b = z_b|_a] (`satProcs`,
  proof/networks/Eight/ViaGrouping/SatPsiDefs.lean).
The numbers K_ℓ, g_ℓ are `Paper.levelK`, `Paper.levelG`; the numbers e_ℓ are `Eight.Level.levelE` (ρ =
11/12).
This file has no proofs. 

 ## The procedures CLIQUE, NETWORK and COUNT of Algorithm 1 

### `CLIQUEp`

 **procedure CLIQUE(ℓ, λ, the tables (W_w) of a (K_ℓ, λ)-clique)** of Algorithm 1. Level 0 is
brute force; level ℓ + 1 is `levelAlgP` on top of NETWORK(ℓ, ·), which calls CLIQUE(ℓ, ·, ·). 

### `NETWORKp`

 **procedure NETWORK(ℓ, a network on g_ℓ nodes)** of Algorithm 1: the algorithm of the printed
proof of Lemma 1 with K = K_ℓ, which calls CLIQUE(ℓ). 

### `COUNTp`

 **procedure COUNT(Φ)** of Algorithm 1, for a fixed level ℓ: NETWORK(ℓ, the network of Φ on g_ℓ
clusters). Different from the paper: the line «choose the level ℓ» is not part of the machine; for
Theorem 2 the level depends on δ only and is chosen once,
outside. 
