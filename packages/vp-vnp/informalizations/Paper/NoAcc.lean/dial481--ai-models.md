---
{
  "module": "Paper/NoAcc.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/vp-vnp/Paper/NoAcc.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/vp-vnp/Paper/NoAcc.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# The paper, section "One scale is all scales": no small accelerators


### `thm_noacc_finite_field`

 **Paper: proof of Theorem thm:noacc, the finite field.** "As A is finitely generated, so is the ring that its
constants generate over A; modulo a maximal ideal this is a finite field E, over which it is still an accelerator." 

### `thm_noacc_periodic`

 **Paper: proof of Theorem thm:noacc, the number m_E.** "As E is finite, there is m_E such that every j ≥ 0 has an
r(j) < m_E with c^(2^j) = c^(2^r(j)) for all c ∈ E; this is where finiteness is needed." Here M is m_E and red is r. 

### `thm_noacc_diagonal`

 **Paper: proof of Theorem thm:noacc, the diagonal.** "Let v be large against E and the number of constants": the
program P guesses a bit, and for one value accepts with weight 1, for the other guesses exponents e, names λ^e and runs D
on the instance z_e of P applied to P; so its value V satisfies V = 1 + V, "impossible in E". 

### `AllScales`

 What the iteration keeps at a scale u: "programs with the two properties of an accelerator, with programs of size
at most u^(4h₀), the same constants, and exponent bounds O(lg u)³". 

### `thm_noacc_all_scales`

 **Paper: proof of Theorem thm:noacc, all scales.** "Proposition prop:next with α = max(5,a), and then again and
again with α = 5, gives programs with the two properties of an accelerator at arbitrarily large scales v_i, with programs
of size at most v_i^(4h₀), with the same constants and with exponent bounds O(lg v_i)³." 

### `thm_noacc`

 **Paper: Theorem thm:noacc.** "There are C and v₁ such that for all integers a ≥ 0 and v ≥ v₁ with (lg v)^(Ca) ≤ v no
nonzero commutative A-algebra has an accelerator of size v^a at scale v." 
