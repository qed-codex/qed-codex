---
{
  "module": "proof/variables/RecursionToBound/Cert/Thresholds.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/variables/RecursionToBound/Cert/Thresholds.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/variables/RecursionToBound/Cert/Thresholds.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # The thresholds for a fraction ε, and the walk with them, are polynomial-time

Step 5 of Appendix D: «Take ε ≤ 1 between e and 2e». Here ε = min(a/b, 1) for a pair r = (a, b) of
natural numbers **written in binary**. So 1/ε may be exponential in the length of the input, but α =
⌈2(k−1)²·ε⁻¹·⌈log₂(32(k−1)²/ε)⌉⌉ still has polynomially many binary digits.

* `alphaC_polyT`: α is polynomial-time jointly in k and r, by the form without fractions
  (`alphaC_epsOf`).
* `thresholds_polyT`: the threshold θ_i of the sparsification (a number that the sparsification here
  uses and the paper does not print) is polynomial-time jointly in k, r and i, if i is given in
  unary (`StepSparsify.CertThCal.thetaC_polyT`, which takes α in binary).
* `occBound_polyT`: the bound on the occurrences, for k in unary.
* `stepC_polyT`: the two children of a node of the tree, for k and 2^k in unary and ε given by the
  pair r.
* `walkSG_polyT`: the walk that adds up. The state of the walk is cut off at the length of the
  padding string after every round, so there is no side condition.

Where a list is run through and its member must be given in unary (the index of a threshold), the
member j is replaced by min(j, k), which is in unary because k is; on the members of the list the
two agree. 

 ### α and the thresholds 

### `ceilDiv_polyT`

 Division rounded up is polynomial-time. 

### `sqPred_polyT`

 (k − 1)² is polynomial-time. 

### `logN_polyT`

 ⌈log₂(32(k−1)²/ε)⌉ is polynomial-time jointly in k and r. 

### `alphaN_polyT`

 α without fractions is polynomial-time jointly in k and r. 

### `alphaC_polyT`

 α = ⌈2(k−1)²·ε⁻¹·⌈log₂(32(k−1)²/ε)⌉⌉, for ε = min(a/b, 1), is polynomial-time jointly in k and r =
(a, b). 

### `thresholds_polyT`

 The threshold θ_i is polynomial-time jointly in k, r and i, if i is given in unary. 

### `occBound_polyT`

 The bound on the occurrences, 2·(θ₀ + … + θ_(k−1)) + 2, is polynomial-time jointly in k and r,
if k is given in unary. 

 ### One step of the sparsification 

### `thrList_polyT`

 The list of the pairs (j, h), each with the threshold θ_(j−h), is polynomial-time jointly in k
and r, if k is given in unary. 

### `stepC_polyT`

 The two children of a node of the tree of the sparsification with the thresholds for k and ε are
polynomial-time jointly in k, r and the node, if k and 2^k are given in unary. 

 ### The walk 

### `walkSG_polyT`

 «Run Steps 2 to 4 on each of the … outputs and add the results»: the walk that adds up is
polynomial-time jointly in k, r, the padding string, the root and whatever the value function
depends on, if k and 2^k are given in unary. 
