---
{
  "module": "Paper/Scales.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/vp-vnp/Paper/Scales.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/vp-vnp/Paper/Scales.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# The paper, section "One scale is all scales"


### `def_acc`

 **Paper: Definition def:acc.** "An accelerator at scale v with Q constants from R and exponent bound B is a program
D with two properties. On every instance z with |z| ≤ v^(H−32) all its runs halt, the accepting ones within v^(H−16) steps, and every name
in their bills stands for a power κ_l^(2^i) with i < B. If moreover z is v^H-plain, its value, the sum over accepting
runs of the weight times the named powers, is pv(z). The constants sit at the leaves of a binary trie with Q nodes, and
their names are paths. It is of size s if Q and the size of D are at most s and, with L = lg(max(v^H, s)), the height of
the trie is at most L² and B ≤ L³." 

### `quasi_of_exponents`

 If circuits with M^a gates are impossible whenever (lg M)^(Ca) ≤ M, then more than 2^(c(log M)²/log log M) gates
are needed. 

### `exists_scale`

 "Otherwise let v = ⌊m^(1/B₀)⌋": at a large m = M it is large, v^B₀ ≤ M, and M^a ≤ v^(a′) for a′ = 2B₀a with
(lg v)^(E(a′+1)) ≤ v, if (lg M)^(Ca) ≤ M for a suitable C. 

### `scales_setting`

 **Paper: "We keep A and H of Theorem thm:cut".** In the contracting case there are the ring A, its generators and
H = 16 h₀ with the conclusion of Theorem thm:cut, and for them Proposition prop:next and Theorem thm:noacc hold. 

### `contracting_complete`

 The contracting case for a family that is complete for grid sums. 

### `thm_contracting`

 **Paper: Theorem thm:contracting.** "In the contracting case there are c > 0 and m₀ such that for m ≥ m₀ every
circuit over k for PERM_m has more than 2^(c(log m)²/log log m) gates." 
