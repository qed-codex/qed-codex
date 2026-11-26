---
{
  "module": "ThreeSumApsp/Machine/Realized.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Anthropic, PBC",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Machine/Realized.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Machine/Realized.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# A running time that is realized on the word RAM

The deductions between running-time claims are made for an arbitrary reading `M : DetTimeModel` of
"is solved by a deterministic algorithm in time T".  `RealizedWithin` is the link to programs: the
problem is solved on the word RAM, in its input layout, within `c T + c` steps.


### `RealizedWithin`

 For every exponent `κ` some program solves the problem `prob` on all instances in `dom` of size
`n ≥ 1` whose numbers are bounded by `U = n^κ`, within `c T + c` steps for some constant `c ≥ 0`.

On the machine every number occupies one cell, and the slope of the word size is chosen after the
exponent `κ`.  The running-time claims allow for numbers that take several words; their bounds are
correspondingly larger, and hold all the more when a number fits into one word. 

### `Realized`

 `RealizedWithin` for a problem of the form of `EndStatement.lean`, on the instances of all
sizes, 0 included: for every exponent `κ` some program solves all instances whose numbers are
bounded by `U = n^κ`, within `c max(T, 0) + c` steps. (A running time `T n U` says nothing at
`n = 0`.) 
