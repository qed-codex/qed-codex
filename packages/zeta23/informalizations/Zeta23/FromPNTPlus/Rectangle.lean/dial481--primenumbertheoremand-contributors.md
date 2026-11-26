---
{
  "module": "Zeta23/FromPNTPlus/Rectangle.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "PrimeNumberTheoremAnd contributors",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright the PrimeNumberTheoremAnd contributors; Apache License 2.0",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/FromPNTPlus/Rectangle.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/FromPNTPlus/Rectangle.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Ported from https://github.com/AlexKontorovich/PrimeNumberTheoremAnd
at commit 6a380f0c4658c04a420a9eb00b1ed62a1e3fde01 (tag v4.32.2), file
PrimeNumberTheoremAnd/Rectangle.lean.
Copyright the PrimeNumberTheoremAnd contributors; Apache License 2.0
(http://www.apache.org/licenses/LICENSE-2.0).
Local modifications: removed the Architect blueprint tooling (import Architect,
@[blueprint ...] attributes).
Re-ported from the
v4.29.0 port (commit 10e1218932db7e2432aa5881d750acb819e91f19) when the project
moved to Lean v4.32.2 / Mathlib 905b95818eb32af7874a58b427f50c1711a5e96c.
Modified 2026 by Anthropic PBC.
-/
```

### `RectangleBorder`

 A `RectangleBorder` has corners `z` and `w`. 

### `segment_reProdIm_segment_eq_convexHull`

 The axis-parallel complex rectangle with opposite corners `z` and `w` is complex product of
  two intervals, which is also the convex hull of the four corners. Golfed from mathlib4\#9598. 

### `rectangle_in_convex`

 If the four corners of a rectangle are contained in a convex set `U`, then the whole
  rectangle is. Golfed from mathlib4\#9598. 

### `rectangle_disjoint_singleton`

 Note: try using `by simp` for `h`. 
