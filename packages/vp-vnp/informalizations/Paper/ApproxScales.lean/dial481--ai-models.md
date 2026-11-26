---
{
  "module": "Paper/ApproxScales.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/vp-vnp/Paper/ApproxScales.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/vp-vnp/Paper/ApproxScales.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# The paper, appendix "Approximate computation": no approximate accelerators


### `def_approx_acc`

 **Paper: the definition of an approximate accelerator.** "An approximate accelerator is defined as in Definition
def:acc, with constants in R[ε,ε⁻¹] and values only required to lie in pv(z) + εR[ε]." As the values are in R[ε,ε⁻¹],
this says that the difference has no coefficient at an exponent ≤ 0. 

### `LargeScale`

 The scales that are large enough. 

### `cube_le`

 The bound of all logarithmic quantities. 

### `prop_approx_acc_step`

 **Paper: proof of Proposition prop:approx-acc, One round, repeated from a scale to its fifth power.** "The time again
has a factor u to spare." 

### `prop_approx_acc_all_scales`

 Arbitrarily large scales, with one power of time to spare. 

### `prop_approx_acc_hasAcc`

 **Paper: proof of Proposition prop:approx-acc, Back to exact values, with the sizes.** At a scale that is large against the numbers of the invariant there is an
exact accelerator of size a fixed power of the scale. 

### `prop_approx_acc_first`

 **Paper: proof of Proposition prop:approx-acc, the first step**, to a scale at which everything is small. 

### `prop_approx_acc`

 **Paper: Proposition prop:approx-acc.** "Theorem thm:noacc holds for approximate accelerators." An approximate
accelerator has constants in R[ε,ε⁻¹] and values in pv(z) + ε R[ε]; here R is any nonzero commutative A-algebra. 

### `prop_approx_acc_setting`

 Proposition prop:approx-acc for "A and H of Theorem thm:cut", in the contracting case. 

### `lem_circuit_approx`

 **Paper: proof of Theorem thm:approx, Lemma lem:circuit for approximating circuits.** "The proofs of Lemmas lem:lowdeg
and lem:circuit work over this ring and give approximate accelerators: the output Φ + εg may have a large degree, but the
program gives the part of degree at most d, which is Φ plus ε times that part of g." 

### `contracting_approx_complete`

 The contracting case for approximating circuits of a family that is complete for grid sums. 
