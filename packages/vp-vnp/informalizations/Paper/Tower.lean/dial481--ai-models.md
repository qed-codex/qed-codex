---
{
  "module": "Paper/Tower.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/vp-vnp/Paper/Tower.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/vp-vnp/Paper/Tower.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# The paper, section "Networks are sums of thin trees": the tower


### `prop_tower`

 **Paper: Proposition prop:tower.** "There are G_n-sets X^(0) = G_n, …, X^(J) with equivariant projections that are b
to one, such that (a) for every i the X_k, k ≠ i, generate a copy of U_h (in order), which acts freely; (b) c and X_i c
always lie in different i-cosets, and π maps every i-coset
bijectively onto one, exactly b of them onto each; (c) |X^(J)| ≤ const, and |G_n| has
bounded quotients; (d) every element of G_n is a word of at most O(n+1)^7 letters X_k." An i-coset of stage j is an orbit of th i; VV are
the chambers with coordinate 1, one in each coset (Paper.prop_tower_representatives), so their fibres count the cosets over a coset. 
