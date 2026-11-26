---
{
  "module": "Challenge/PaperStatements.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Anthropic, PBC",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/Challenge/PaperStatements.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/Challenge/PaperStatements.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# The statements of `PaperStatements.lean`

`PaperStatements.lean`, which stands beside `EndStatement.lean`, defines propositions. This file
states that they hold, in the order of that file.


 ## Section 2: statements 

 ## Section 3: statements 

 ## Section 4: statements 

 ## Section 5: statements 

 ## Agreement with the definitions of EndStatement.lean 


## The word RAM: running times

Each statement says that an item statement holds: a proposition `Items.Theorem_5`, … about programs
of the machine of `EndStatement.lean`, whose docstring quotes the sentence of the paper that it
renders.  The statements stand in the order of these propositions: Sections 2 to 5, then Theorems 1
to 4 of the introduction.


### `wordRam_theorem_5`

 **Theorem 5**, on the word RAM. 

### `wordRam_corollary_15`

 **Corollary 15**, on the word RAM. 

### `wordRam_corollary_16`

 **Corollary 16**, on the word RAM. 

### `wordRam_theorem_19`

 **Theorem 19**, on the word RAM. 

### `wordRam_theorem_22_first`

 **Theorem 22**, on the word RAM: the bounds using Theorem 5. 

### `wordRam_theorem_22_second`

 **Theorem 22**, on the word RAM: the bounds using Corollary 26. 

### `wordRam_theorem_22_threeSum`

 **Theorem 22**, on the word RAM: 3SUM in `n^{2−1/1296+o(1)}` and in `n^{2−ε'/2+o(1)}`
time. 

### `wordRam_theorem_24`

 **Theorem 24**, on the word RAM. 

### `wordRam_theorem_25`

 **Theorem 25**, on the word RAM. 

### `wordRam_corollary_26`

 **Corollary 26**, on the word RAM: the two-stage data structure. 

### `wordRam_corollary_26_wanted`

 **Corollary 26**, on the word RAM: the offline form. 

### `wordRam_theorem_30`

 **Theorem 30**, on the word RAM: the two-stage data structure. 

### `wordRam_theorem_30_wanted`

 **Theorem 30**, on the word RAM: the offline form (9). 

### `wordRam_corollary_31`

 **Corollary 31**, on the word RAM. 

### `wordRam_corollary_32`

 **Corollary 32**, on the word RAM. 

### `wordRam_corollary_39_zero`

 **Corollary 39**, the zero-weight case, on the word RAM. 

### `wordRam_corollary_39_min_max`

 **Corollary 39**, the minimum-weight and maximum-weight cases, on the word RAM. 

### `wordRam_corollary_40_times`

 **Corollary 40**, on the word RAM: the running times for `τ < 1/18`. 

### `wordRam_corollary_40_general_times`

 **The proof of Corollary 40**, paragraph "General τ", on the word RAM: the running times for
`τ < ε*`. 

### `wordRam_corollary_40_fail`

 **Corollary 40**, on the word RAM: the three conjectures fail for `τ < 1/18`, and more
generally for `τ < ε*`. 

### `wordRam_theorem_1`

 **Theorem 1**, on the word RAM. 

### `wordRam_theorem_2`

 **Theorem 2**, the four deterministic lines, on the word RAM. 

### `wordRam_theorem_2_graphs`

 **Theorem 2**, first line for `n`-vertex graphs, on the word RAM. 

### `wordRam_theorem_3`

 **Theorem 3**, on the word RAM. 

### `wordRam_theorem_4`

 **Theorem 4**, on the word RAM. 
