---
{
  "module": "ThreeSumApsp/Programs/Sec4/Theorem30/SumTen.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Anthropic, PBC",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Programs/Sec4/Theorem30/SumTen.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Programs/Sec4/Theorem30/SumTen.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# The value of a box with stars (proof of Lemma 29, "The values")

"For a box π with e ≥ 1 stars, let ℓ be the highest level at which π has a star.  The leaves of π
are the leaves of the ten strings π[ℓ ← λ] obtained by replacing that star by a term λ, and each of
these strings is again a box, with e - 1 stars. […] Hence we compute val(π) = ∑_λ val(π[ℓ ← λ]) with
ten lookups in the trie, in O(L) operations."  The routine writes the ten digits one after the other
at the position of the star, looks each string up, adds, and puts the star back.  It looks in the
trie of the tile, which is being filled.

Before round j the sum of the first j values has been formed, and the memory differs from the
original one at the position of the star only (`SumTen.Inv`).  `SumTenPre` collects what the
routine assumes.  In a round the string with the digit j at the position of the star stands in the
memory (`segN_set`), so lookup returns its value (`SumTen.round_spec`); `sumTen_spec` is the
specification.


### `Area`

 The local variables of sumTen: the arguments (the base of the trie area, the root of the trie,
the address of the box, its length, the position of the star), the digit that stood at that
position, the digit written, the sum, and a value looked up.  Local 0 also takes the result. 

### `sumTenRound`

 One round: write the digit at the position of the star, look the string up, and add. 

### `sumTenBody`

 sumTen(area, root, box, len, star): the sum of the values of the ten strings; the digit at the
position of the star is put back at the end. 

### `segN_set`

 A string with one digit replaced, in the memory. 

### `Inv`

 Before round j: the sum of the first j of the ten values has been formed, and the memory differs
from μ at the position of the star only. 

### `tRound`

 The time of a round. 

### `round_spec`

 One round adds the value of the string with the digit j.  The conclusion has the form that the
rule for counting loops asks for: the loop itself then raises the digit. 

### `sumTen_spec`

 **sumTen** returns the sum of the values of the ten strings, and leaves the memory as it
was. 
