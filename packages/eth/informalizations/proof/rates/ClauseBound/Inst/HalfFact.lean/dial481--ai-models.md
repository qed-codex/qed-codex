---
{
  "module": "proof/rates/ClauseBound/Inst/HalfFact.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/ClauseBound/Inst/HalfFact.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/ClauseBound/Inst/HalfFact.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # The two programs of a factorization of a piece: the sum over the labels

The piece number i is A_s with s = i − 2h. With a pad that is long enough, the program for the upper
and the program for the lower function of a factorization return, at the label θ, the
entries of two matrices at the pair (j, τ) that θ stands for, and 0 if θ stands for no pair. So the
sum over all labels of the product of the two is the sum over the list of the pairs, which
is the double sum over j ≤ 2h and the monomials τ of weight s + j (row-wise) or 2h − s − j
(column-wise) in which the piece was written out. The lemmas on the words, the list of the
labels and the values enter as hypotheses. 

### `deltaF_eq`

 The number of all partitions of 0, …, 4h. 

### `sOf_eq`

 s = i − 2h for the numbers of pieces. 

### `cap_eq`

 The number of bits of the labels: nothing is cut off. 

### `sum_words_eq`

 The sum over all labels of the product of the two programs is the double sum over j and the
monomials of the weight that belongs to j. 
