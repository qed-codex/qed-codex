---
{
  "module": "Nc/Cat/Core.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/vp-vnp/Nc/Cat/Core.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/vp-vnp/Nc/Cat/Core.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# Complete CAT(0) spaces: definitions

`Cat.CN X`: `X` is complete and any two points have a midpoint with the CN inequality.
What follows from the defining inequalities of barycentres (`IsBary`) and of points at
fraction `t` (`IsPt`) in any metric space. The facts on CAT(0) spaces are Lemma lem:toolkit, in Paper/Toolkit.lean.


### `CN`

 Complete CAT(0) spaces: complete, and every two points have a midpoint with the
inequality of Bruhat and Tits. 

### `mid`

 The midpoint. 

 ### Barycentres 

### `IsBary`

 `b` is the barycentre of the points `x i` with weights `w i` (of any total weight):
the inequality of variances. 

### `IsBary.map`

 A barycentre is mapped to a barycentre by a surjective isometry. 

### `IsBary.comp_equiv`

 Barycentres don't depend on the names of the points. 

 ### Points at fraction `t` 

### `IsPt`

 `b` is the point at fraction `t` between `x` and `v`. 

### `IsPt.eq_of_dist`

 A point with the distances of the point at fraction `t` is the point at fraction `t`. 
