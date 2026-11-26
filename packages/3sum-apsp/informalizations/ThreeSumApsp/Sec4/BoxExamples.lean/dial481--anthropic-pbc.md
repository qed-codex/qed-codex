---
{
  "module": "ThreeSumApsp/Sec4/BoxExamples.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Anthropic, PBC",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Sec4/BoxExamples.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Sec4/BoxExamples.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# The two worked examples of Section 4.2

For `m = 4` and `t = 2`: the box of the leaf `P₁₂ P₀ P₃₁ P₂₂` is `∗ ∗ P₃₁ P₂₂`, in the first row of
Figure 10 (`boxOfLeaf_example_first`), and it has 100 leaves (`leaves_example_first`); the box of
the leaf `P₀ P₂₃ P₀ P₁₁` is `∗ P₂₃ P₀ P₁₁`, in the second row (`boxOfLeaf_example_second`). Nothing
else rests on this file.


### `allInner`

 Figure 10 and the two examples show the four levels `ℓ₁ < ℓ₂ < ℓ₃ < ℓ₄` of `Q` only. Here there
are no other levels: `L = m = 4`, the output string is `z₀ z₀ z₀ z₀`, and the four levels are
`0, 1, 2, 3`. 

### `boxOfLeaf_example_first`

 Section 4.2, for `m = 4` and `t = 2`: "suppose that τ chooses the terms P₁₂, P₀, P₃₁, P₂₂ at the
four levels ℓ₁ < ℓ₂ < ℓ₃ < ℓ₄ of Q. We see P₂₂ at level ℓ₄ and P₃₁ at level ℓ₃, and we stop there,
so the box of τ is ∗ ∗ P₃₁ P₂₂ (in the first row of the figure)." The first row of Figure 10 is the
set `V = {ℓ₁, ℓ₂}`. Lean counts levels and indices from 0, so that `P₁₂` is `.P 0 1`. 

### `leaves_example_first`

 Section 4.2, on the box `∗ ∗ P₃₁ P₂₂` of the leaf `τ = P₁₂ P₀ P₃₁ P₂₂`: "This box contains τ
along with the 99 other leaves that differ from τ only at the levels ℓ₁ and ℓ₂." 

### `boxOfLeaf_example_second`

 Section 4.2, for `m = 4` and `t = 2`: "Similarly, for a leaf that chooses the terms P₀, P₂₃, P₀,
P₁₁, we stop at level ℓ₂, so its box is ∗ P₂₃ P₀ P₁₁ (in the second row of the figure)." The second
row of Figure 10 is the set `V = {ℓ₁, ℓ₃}`. 
