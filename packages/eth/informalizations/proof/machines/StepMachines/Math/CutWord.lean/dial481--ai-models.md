---
{
  "module": "proof/machines/StepMachines/Math/CutWord.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/machines/StepMachines/Math/CutWord.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/machines/StepMachines/Math/CutWord.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 One rectangle of the grid; n is the length λ of the strings on an edge. The factorisation of the
piece A_i (`A` n i here), which is built from single bits, across rows (tr = false) or across
columns
(tr = true). This A_i is not the A_i of Definition 5, which is built from blocks of three bits. Its
labels are strings of n two-bit states with few positions off a frequent state, named by the codes
of StepMachines/Math/Sparse.lean with their number of bits; and its two
parts as functions of words, in the form in which the machine evaluates them: the top part is a
product over the n
positions, the bottom part a sum over all 2^n sets of positions, of which those with i elements
count. 

 ### λ-bit indices as words 

### `bitsOf`

 The index written by a word. 

### `bitsOf_bijOn`

 The words of n bits write the n-bit indices, one each. 

### `bitsC`

 The words of n bits name the n-bit indices. 

### `bitsOf_inj`

 Two indices are equal iff their words are. 

### `bitsOf_eq_zero`

 A word names the index 0…0 iff all its bits are false. 

 ### The cut of one rectangle 

### `sideBit`

 The tables of one bit: rows or columns. 

### `sideS0`

 The frequent state: the singlet for rows, Φ⁺ for columns. 

### `sideCnt`

 The number of other states allowed in a label of A_i: n − i for rows, i for columns. 

### `sideCut`

 A_i cut across rows or columns, charged with the length of the names of its labels. 

### `sideCut_factors_row`

 Across rows the cut is a factorisation of A_i. 

### `sideCut_factors_col`

 Across columns the cut is a factorisation of A_i, its arguments in the order x, u | y, v. 

### `card_sideCut_lab`

 There are at most 2^cap labels. 

### `sideCut_cap_le`

 A name has at most 4n bits. 

### `abs_sideCut_top`

 The top part is at most 2^n in absolute value. 

### `abs_sideCut_bot`

 The bottom part is at most 2^n in absolute value. 

 ### The two parts on words. The length n is the length of the word x. 

### `topTerm`

 One factor of the top part: position k. x, y are the words of the two ends, w the name of the
label. 

### `botTerm`

 One factor of the bottom part: position k in the term of the set of positions written by the
number s. 

### `topW`

 The top part. 

### `botW`

 The bottom part. 

### `cutW`

 The part of the cut of A_i on one side (top or bottom), 0 at the words that name no label. 

### `val_bijOn`

 The positions 0, …, n − 1 as numbers. 

### `sum_powersetCard_eq_sum_range`

 A sum over the sets of i positions is a sum over all numbers s below 2^n, read as sets of
positions, of which those with
i elements count. 

### `topW_eq`

 The top part on words is the top part of the string that w names. 

### `botW_eq`

 The bottom part on words is the bottom part of the string that w names. 

### `cutW_eq`

 What the machine evaluates is the part of the cut, read through the codes. 
