---
{
  "module": "Zeta23/FromPNTPlus/MediumPNT.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "PrimeNumberTheoremAnd contributors",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright the PrimeNumberTheoremAnd contributors; Apache License 2.0",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/FromPNTPlus/MediumPNT.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/FromPNTPlus/MediumPNT.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Ported from https://github.com/AlexKontorovich/PrimeNumberTheoremAnd
at commit 6a380f0c4658c04a420a9eb00b1ed62a1e3fde01 (tag v4.32.2), file
PrimeNumberTheoremAnd/MediumPNT.lean.
Copyright the PrimeNumberTheoremAnd contributors; Apache License 2.0
(http://www.apache.org/licenses/LICENSE-2.0).
Local modifications: removed the Architect blueprint tooling (import Architect,
blueprint_comment blocks, @[blueprint ...] attributes), redirected intra-project
imports to Zeta23.FromPNTPlus.*, and added (name := ...) tags to the three local notations.
Re-ported from the
v4.29.0 port (commit 10e1218932db7e2432aa5881d750acb819e91f19) when the project
moved to Lean v4.32.2 / Mathlib 905b95818eb32af7874a58b427f50c1711a5e96c.
Adjusted for Lean v4.33.0-rc2 / Mathlib 51e6992efd06: one redundant `rfl` after `simp` removed.
Modified 2026 by Anthropic PBC.
-/
```

### `MediumPNT`

 *** Prime Number Theorem (Medium Strength) *** The `ChebyshevPsi` function is asymptotic to `x`. 
