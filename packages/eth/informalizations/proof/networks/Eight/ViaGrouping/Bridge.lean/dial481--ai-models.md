---
{
  "module": "proof/networks/Eight/ViaGrouping/Bridge.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/networks/Eight/ViaGrouping/Bridge.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/networks/Eight/ViaGrouping/Bridge.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # From a network in the form of proof/networks/Paper to Definition 2 as printed

The networks that Sections 5 and 6 (and the corollaries of Section 7) build are written in the form
of proof/networks/Paper (proof/networks/Paper/SecNetworks_Networks.lean): every string of P_a bits
is a setting, Ψ_{a,b} is defined as Σ_θ f_{a,b}·f_{b,a}, values are «at most 2^B». Lemma 1 along the
printed proof
(`Correct`, proof/networks/Eight/ViaGrouping/Defs.lean) speaks of networks as Definition 2 prints
them. This file passes from the first form to the second, given a procedure Q that computes Ψ_{a,b}
on settings.
* `isNetworkP_ofNetwork`: such a network, with Q, is a network in the sense of Definition 2 with
  parameters P, B + 1, τ; `value_ofNetwork`, `U_ofNetwork`: same value, same total; `stBridge` puts
  the three together.
* `Correct.absorb`: the constant of the bound of Lemma 1 takes up the passage from B to B + 1.
* `keeps_ofProcs`, `keepsP_ofProcs`: the procedures have polynomial-time steps if those of
  proof/networks/Paper and Q have, and give P in unary if Pf does.
Nothing here is a statement of the paper: the file joins two renderings of Definition 2. 

### `value_ofNetwork`

 The value is the same: both are Σ_z ∏_a W_a(z_a) ∏_{a<b} Ψ_{a,b}(z_a, z_b) with the same S, W,
Ψ. 

### `U_ofNetwork`

 The total U is the same. 

### `Ψ_swap_ofPaperNetwork`

 The Ψ that proof/networks/Paper defines from the factors is symmetric: Ψ_{b,a}(z', z) =
Ψ_{a,b}(z, z'). 

### `n_le_ofPaperNetwork`

 P_a ≤ P for a network of proof/networks/Paper: it has 2^{P_a} settings at a, and at most 2^P. 

### `is_ofNetwork`

 Definition 2, all but (iii), with B + 1 for B: «at most 2^B» gives «below 2^{B+1}». 

### `isNetworkP_ofNetwork`

 **The bridge.** A network of proof/networks/Paper with parameters P, B, τ, together with a
procedure Q that computes its Ψ on settings within τ steps, is a network in the sense of Definition
2 (without the part of condition (iii) that gives B to the algorithm as input) with parameters P, B +
1, τ.
The test for membership forgets the query and says yes in one step, on states of size 2; hence S + 2. 

### `stBridge`

 **The bridge** (`StBridge` of proof/networks/Eight/ViaGrouping/Defs.lean): a network of
proof/networks/Paper with parameters P, B, τ, together with a procedure that computes its Ψ within τ
steps, is a network in the sense of Definition 2 (without the part of condition (iii) that gives B
to the algorithm as input), with parameters P, B + 1, τ, and has the same value
and the same total. 

### `Correct.absorb`

 The bound of Lemma 1 with B + 1 and S + 2 taken up by the constant: if NA has the bound of Lemma
1 (`Correct`), then there is a constant A such that NA outputs the value of every network with
parameters P, B + 1, τ, given on states of size at most S + 2,
within A·2^{εU + b·gP/K}·(P + B)^A·τ steps, on states of size at most S + A·(size c + P + B)^A; by P +
B + 1 ≤ 2(P + B). 

### `keeps_ofProcs`

 The procedures `ofProcs Np Pf Q` have polynomial-time steps (and give P_a and c_{a,b} in unary)
if those of proof/networks/Paper have and Q has. 

### `keepsP_ofProcs`

 The same, with P given in unary: what an algorithm for networks asks of its procedures
(`AlgKeeps`). 
