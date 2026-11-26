---
{
  "module": "ThreeSumApsp/Programs/Sec4/ChoosingParameters/OfflineStatement.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Anthropic, PBC",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Programs/Sec4/ChoosingParameters/OfflineStatement.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Programs/Sec4/ChoosingParameters/OfflineStatement.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# Section 4.4, the offline form as a light program

Sections 4.1 and 4.4. The routine offline32 preprocesses the two matrices and then asks one query
for each wanted position. Its parameters c = a/b, θ = p/q and the threshold m₀ are part of the
program text (`RatParams`). This file passes from the specification of the routine to a statement
about the light program on the input of the problem (`programSolves_of_costsWithin`), with the
regime and the two bounds as parameters: for a set `dom` of instances and functions `Tp`, `Tq` such
that on `dom` the two cost expressions of Theorem 30 are at most `C Tp` and `C Tq`, the wanted
entries are computed in time `O(Tp + |W| Tq)`. The offline statements of Section 4 (Corollaries 26
and 32, Theorem 25) are instances; the compiler takes the statement to the word RAM in
`solves_of_costsWithin`.


### `programSolves_of_costsWithin`

 **The offline form as a light program**: on the regime the wanted entries are computed in time
O(Tp + |W| Tq). 
