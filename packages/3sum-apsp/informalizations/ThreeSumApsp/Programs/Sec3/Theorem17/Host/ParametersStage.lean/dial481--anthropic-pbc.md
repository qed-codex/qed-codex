---
{
  "module": "ThreeSumApsp/Programs/Sec3/Theorem17/Host/ParametersStage.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Anthropic, PBC",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Programs/Sec3/Theorem17/Host/ParametersStage.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Programs/Sec3/Theorem17/Host/ParametersStage.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# The host of Theorem 17: the parameters and the small case

The first part of the host procedure `et17` (Exact Triangle by Theorem 17) computes `D`, `g` and
`s = ⌊√D⌋` and tests whether `n` is small (`et17Params_spec`).  If it is, the host calls the brute
force (`et17Small_spec`; proof of Theorem 19: "smaller instances are solved by brute force").


### `et17Params_spec`

 **The first part of et17**: the parameters, and whether n is small.  No cell changes. 

### `et17Small_spec`

 **The small case**: the call of the brute force. 
