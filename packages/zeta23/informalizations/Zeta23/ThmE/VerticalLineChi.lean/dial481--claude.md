---
{
  "module": "Zeta23/ThmE/VerticalLineChi.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/ThmE/VerticalLineChi.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/ThmE/VerticalLineChi.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/

/-
Zeta23/ThmE/VerticalLineChi.lean.  The twisted prime side for L(s,χ):
(1/2π)∫ H(c+it)·(−L'/L)(c+it) dt = Σ_n Λ(n)χ(n)n^{−1/2} k(log n), by the same tilted-inversion
device as Zeta23/WeilEF/VerticalLine.lean (tilt/tilted_inversion/Hfn_line are k-generic, reused).
-/
```

### `neg_logDeriv_LFunction_eq`

 −L'/L = the twisted Dirichlet series on Re s > 1 (glue of Mathlib's
LSeries_twist_vonMangoldt_eq with the LFunction/LSeries identification). 

### `integrand_eq_tsum_chi`

 Pointwise on the line: the integrand as a twisted tsum. 

### `per_n_line_integral_chi`

 Per-n line integral, twisted: the χ(n)-coefficient rides through the tilted inversion. 

### `line_integral_swap_chi`

 Twisted tsum/integral swap (domination: ‖χ(n)‖ ≤ 1 reduces to the ζ-side majorant). 

### `prime_side_line_chi`

 **The twisted prime side**: (1/2π)∫ H(c+it)(−L'/L)(c+it)dt = Σ Λ(n)χ(n)n^{−1/2}k(log n). 
