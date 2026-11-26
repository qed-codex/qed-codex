---
{
  "module": "Paper/LowDeg.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/vp-vnp/Paper/LowDeg.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/vp-vnp/Paper/LowDeg.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# The paper, section "One scale is all scales": low degree is fast


### `line_coeff_eq`

 The part of degree i is what the point scales by the ith power. 

### `lem_lowdeg`

 **Paper: Lemma lem:lowdeg.** "Let a polynomial over R in variables (place, symbol), with n places, have a circuit
with S gates. A program of size O(log S + log n + d), with O((S+n)³) constants, has as value the sum of its parts of
degree at most d at the code of the word of every z with |z| < n, in (d+|z|+1)(log(S+n+d))^O(1) steps. All its runs halt, and it names only constants, not powers." The bound on
the height of the trie, O(log S + log n), is the one that Lemma lem:circuit needs. 
