---
{
  "module": "Zeta23/XiPrime/ExplicitFormula/Main.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/XiPrime/ExplicitFormula/Main.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/XiPrime/ExplicitFormula/Main.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/

/-
Zeta23/XiPrime/ExplicitFormula/Main.lean — umbrella + final (EF4) theorem of the ξ′ explicit-formula
development.  Consumers should import this module.
Components: §2 (F2) ZeroFree.lean; §4 (EF1) FullLine.lean;
§5 Archimedean + Expansion; §6 DirichletLine; §7 (EF4) = XiEFAssembly.xiEF_of,
instantiated here with GramBridge, Coeff/LSeries, and the test-weight bounds
(from TestWeight.lean, reshaped into TestWeightFacts by the adapter below).
-/
```

 ### adapter: TestWeight.lean → TestWeightFacts (pure reshaping) 

### `testWeightFacts_hosted`

 TestWeight.lean provides TestWeightFacts. 

 ### the three input Props of XiEFAssembly, discharged 

 ### §7 (EF4) 

### `xiEF`

 **(EF4)** [XF′ Thm 4.2]: Statement.XiEF — the explicit formula for ξ′ with frozen
coefficients, entrywise, with the T-uniform entry error C·T^{−δ}·(1/max(1,(τ_k−τ_l)²) + 1/T).
(hF2 is the theorem
xiDerivZerosInStrip_holds and is not used.) 

### `xiEF_xiDerivZeros`

 the same for Statement's own instance. 
