---
{
  "module": "Paper/Next.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/vp-vnp/Paper/Next.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/vp-vnp/Paper/Next.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# The paper, section "One scale is all scales": from one scale to the next


### `prop_next_round`

 **Paper: proof of Proposition prop:next, one round.** "One round, from f+8 to f, for f ≥ α(H−32)+40": from values
in v^(f+8) steps to values in v^f steps, with exponent bound max(B_p+J, B); the program grows by v^(h₀α+2) + v^(H+1).
Here e is the paper's f. 

### `prop_next`

 **Paper: Proposition prop:next.** "Let v be large, α ≥ 5 an integer and (lg v)^(Cα) ≤ v for a suitable
constant C, which depends on the fixed power below. A
program with the two properties of an accelerator at scale v, with Q ≤ v^(h₀α), program size at most v^(h₀α) and with B
and the height of its trie at most a fixed power of α lg v gives a program with the two properties of an accelerator at
scale v′ = v^α (without the bounds on height and exponents of Definition def:acc), with the same constants, exponent
bound B + O(α² lg v) and program size at most v′^(4h₀). Its accepting runs take at most v′^(H−17) steps." The two properties are the fields of IsAccT,
k is the fixed power, and H = 16h. 
