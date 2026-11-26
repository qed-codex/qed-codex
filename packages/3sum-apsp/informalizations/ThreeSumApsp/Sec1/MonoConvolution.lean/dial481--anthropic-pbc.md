---
{
  "module": "ThreeSumApsp/Sec1/MonoConvolution.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Anthropic, PBC",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Sec1/MonoConvolution.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Sec1/MonoConvolution.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# The introduction: the exponent of MonoConvolution (Section 1.2)

The consequence of Theorem 2 for MonoConvolution, by a cited reduction: the exponent
`3/2 - ε/(8 - 2ε)` with `ε = 0.0008` is below 1.4999 (`monoConvolution_exponent_lt`), so the
logarithmic factors are absorbed (`monoConvolution_isBigO`). No other file uses this one.


### `monoConvolution_exponent_lt`

 Section 1.2, MonoConvolution: "an O(n^{2-ε})-time algorithm for 3SUM gives an
Õ(n^{3/2-ε/(8-2ε)})-time algorithm for MonoConvolution. Our approach gives O(n^{1.4999}) time for
MonoConvolution".  With the bound O(n^{1.9992}) of Theorem 2, ε = 0.0008, and the exponent is
1.49989998: below 1.4999 by 2 · 10⁻⁸. 

### `monoConvolution_isBigO`

 Section 1.2, MonoConvolution: the bound `Õ(n^{3/2-ε/(8-2ε)})` with `ε = 0.0008` is
`O(n^{1.4999})`, whatever the power `c` of the logarithm that `Õ` hides. 
