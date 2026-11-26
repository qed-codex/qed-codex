---
{
  "module": "Zeta23/FromPNTPlus/Mathlib/Analysis/SpecialFunctions/Log/Basic.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "PrimeNumberTheoremAnd contributors",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright the PrimeNumberTheoremAnd contributors; Apache License 2.0",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/FromPNTPlus/Mathlib/Analysis/SpecialFunctions/Log/Basic.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/FromPNTPlus/Mathlib/Analysis/SpecialFunctions/Log/Basic.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Ported from https://github.com/AlexKontorovich/PrimeNumberTheoremAnd
at commit 10e1218932db7e2432aa5881d750acb819e91f19, file
PrimeNumberTheoremAnd/Mathlib/Analysis/SpecialFunctions/Log/Basic.lean.
Copyright the PrimeNumberTheoremAnd contributors; Apache License 2.0
(http://www.apache.org/licenses/LICENSE-2.0).
Local modifications: removed the Architect blueprint
tooling (import Architect, blueprint_comment blocks, @[blueprint ...] attributes),
redirected intra-project imports to Zeta23.FromPNTPlus.*.  Mathematical content unchanged.
Modified 2026 by Anthropic PBC.
-/
```

### `Real.tendsto_pow_log_div_pow_atTop`

 log^b x / x^a goes to zero at infinity if a is positive. 
