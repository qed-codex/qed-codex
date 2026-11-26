---
{
  "module": "Nc/Cat/Window.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/vp-vnp/Nc/Cat/Window.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/vp-vnp/Nc/Cat/Window.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# Windows: clamping, the relative place in a window, and two elementary inequalities

Helpers for the proof of Theorem thm:cn (Paper/Fan.lean); nothing here is about prices.


### `cl`

 Clamping an integer to `0, …, N`. 

### `eventually_large`

 What "n large" means below. 

### `place`

 The relative place in the window. 

### `conc`

 A sequence f with second differences at most `2ω`, where `φ` stands for the value f(−1): then
f(A) ≤ f(0) + A(f(0) − φ + ω) + A²ω. For ψ(l) = f(l) − l²ω this says ψ(A) ≤ ψ(0) + A(ψ(0) − ψ(−1)). 

### `sq_core`

 Squaring |rn²(L′ − L) + aL′| ≤ W, with 2L′(L′ − L) ≥ L′² − L², 1 − r ≤ 2θ and n²(L′² − L²) ≤ K:
W² ≥ a²L′² + a·n²(L′² − L²) − 2aθK. 
