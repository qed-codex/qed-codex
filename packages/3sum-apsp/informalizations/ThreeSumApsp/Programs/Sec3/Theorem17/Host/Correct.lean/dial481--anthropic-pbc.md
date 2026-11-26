---
{
  "module": "ThreeSumApsp/Programs/Sec3/Theorem17/Host/Correct.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Anthropic, PBC",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Programs/Sec3/Theorem17/Host/Correct.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Programs/Sec3/Theorem17/Host/Correct.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# The host of Theorem 17: et17 decides Exact Triangle

The three parts of the host procedure `et17` (Exact Triangle by Theorem 17) and the small case are
put together (`et17_spec`).  Correctness is `HostData.found_m`: a zero triangle is found if and only
if there is one.


### `et17_spec`

 **et17 decides Exact Triangle.**  In every program `P₀ ++ R` that satisfies the context
`Et17Ctx` (it holds the solver, the procedures of the host and the two parameter procedures), on an
instance with `x.Pre μ fr` and within limits that allow for `hostNeed`, the body of et17 ends within
`hostTime` steps in a state that satisfies `etTask.Post`. 
