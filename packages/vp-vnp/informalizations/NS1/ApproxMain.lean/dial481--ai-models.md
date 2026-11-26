---
{
  "module": "NS1/ApproxMain.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/vp-vnp/NS1/ApproxMain.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/vp-vnp/NS1/ApproxMain.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# No approximate accelerators

An approximate accelerator is carried to scales that are large against the exponents and the number of its constants;
there it gives an exact accelerator, which does not exist.


### `HasAccA`

 **Paper: the definition of an approximate accelerator, with its size.** An approximate accelerator of size `s` at the scale `V = v ^ H`
over E: a trie of at most `s` nodes with constants in E[ε,ε⁻¹], and a program of size at most `s` whose values lie in
the universal plain sums + ε E[ε]. 

### `InvA`

 **Paper: proof of Proposition prop:approx-acc, the invariant.** An approximate program at a scale, small; the exponents of its
constants are at most 2 to a power that is polylogarithmic in the scale; the numbers b₀, Δ and cΔ may depend on the
first program, not on the scale. 
