---
{
  "module": "Zeta23/ThmE/Final.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/ThmE/Final.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/ThmE/Final.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/

/-
Zeta23/ThmE/Final.lean — **Theorem E**.

The four target statements of Zeta23/ThmE/Statement.lean, proved here as theorems (same names,
same signatures — placed downstream so they can consume SeamL, GzGpChi, RvMChi, TracesChi and
EFLitChi/MainChi), plus the zero-hypothesis headlines thmE_A₀/thmE_B₀/thmE_C₀ for
Mathlib's DirichletCharacter.LFunction: nothing is assumed (the χ-explicit formula is the
theorem EF_lit_chi_L; every other input is proved elsewhere in the repository).

Faithfulness caveat: EF_lit_chi's statement is a transcription of [IK04, Thm 5.12] for L(s,χ),
which is not displayed in the paper; the Lean proofs are unconditional regardless.
-/
```

### `thmE_A_lam`

 **Theorem E, first bound, at fixed λ ∈ (0,1)** [thm:E]. 

### `thmE_A`

 **Theorem E, first bound** [thm:E]. 

### `thmE_B`

 **Theorem E, second bound** [thm:E]. 

### `thmE_C`

 **Theorem E, third bound** [thm:E]. 

 ## Zero hypotheses 

### `paperInputsChi_L`

 the full input package, from theorems alone. 

### `thmE_A₀`

 **Theorem E, bound 1, no hypotheses**: for every primitive Dirichlet character mod q > 1,
at least (2/3 − ε)·N_χ(T,2T) of the zeros of Mathlib's `DirichletCharacter.LFunction χ` with
ordinate in (T,2T], counted with multiplicity, are matched by distinct critical-line zeros. 

### `thmE_B₀`

 **Theorem E, bound 2, no hypotheses** (1/2 simple-and-on-line). 

### `thmE_C₀`

 **Theorem E, bound 3, no hypotheses** (3/4 distinct). 
