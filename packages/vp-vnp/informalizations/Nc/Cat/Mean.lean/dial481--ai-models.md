---
{
  "module": "Nc/Cat/Mean.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/vp-vnp/Nc/Cat/Mean.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/vp-vnp/Nc/Cat/Mean.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# Means over large windows

Windows: two sheets (`Bool`), `0 ≤ i < n²`, `0 ≤ k < n`. `mean f` is the limit (along an
ultrafilter) of the means of `f n` over the `n`-th window: a positive linear functional on bounded
functions, invariant under translations, with the inequality of Cauchy and Schwarz.


### `Fn`

 Functions on two sheets of `ℤ²`, one for every `n`. 

### `avg`

 The mean over the `n`-th window. 

### `Bd`

 Bounded functions. 

### `mean`

 The mean of a bounded function over large windows. 

 ### Translations 

### `le_mean_tele`

 A telescoping sum. 

### `mean_steps`

 Many steps of a telescoping sum. 

 ### Cauchy and Schwarz 

### `nm`

 The root of the mean square. 
