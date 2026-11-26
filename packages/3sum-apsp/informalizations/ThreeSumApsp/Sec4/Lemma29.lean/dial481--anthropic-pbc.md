---
{
  "module": "ThreeSumApsp/Sec4/Lemma29.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Anthropic, PBC",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Sec4/Lemma29.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Sec4/Lemma29.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# Lemma 29: the number of boxes, and their values (Section 4.3)

*The count* (`lemma_29_count`): there are at most `(m+1) ∑_{d=t}^{m} β_d` boxes. A box with `f`
symbols `P₀` or stars is a leaf with `f` symbols `P₀` in which the `e` lowest of them have been
turned into stars, for some `e ≤ f`. So these boxes correspond to the pairs of such a leaf and a
number `e ≤ f`, there are `(f+1) β_{m-f}` of them (`Lemma29.card_filter`), and we sum over
`f ≤ m - t`.

*The values* (`lemma_29_values`): the dynamic program `dpValue`, run on the two encodings of a tile,
returns the value of every box. This is an induction on the number of stars. The boxes without stars
are leaves (`Lemma29.no_stars`), and their values are products of two encoded numbers
(`Lemma29.val_ofLeaf`). Replacing the highest star of a box by the ten terms gives ten boxes with
one star fewer (`lemma_29_split`), whose values add up to the value of the box
(`Lemma29.recurrence`).


### `mem_boxes`

 Membership in the set of all boxes. 

### `mem_boxesWithStars`

 Membership in the set of the boxes with `e` stars. 

 ### The count 

### `card_leaves_P0`

 For `f ≤ m ≤ L`, the number of leaves that choose `P₀` at exactly `f` levels is `β_{m-f}`
(Section 2.4.3). 

### `Lemma29.card_filter`

 Proof of Lemma 29, "The count": "There are hence (f+1) binom(L, f) 9^{L-f} = (f+1) β_{m-f} such
boxes", namely boxes with `f` symbols `P₀` or stars, for `f ≤ m - t`. 

### `lemma_29_count`

 **Lemma 29**, first sentence.  "There are at most (m+1) ∑_{d=t}^{m} β_d boxes." 

 ### The values 

### `Lemma29.no_stars`

 Proof of Lemma 29, "The values": "The boxes without stars are the leaves with at most m - t
symbols P₀". 

### `Lemma29.val_ofLeaf`

 Proof of Lemma 29, "The values": "the value of each of them is the product of its two numbers in
the encodings." 

### `lemma_29_split`

 Proof of **Lemma 29**, "The values": "For a box π with e ≥ 1 stars, let ℓ be the highest
level at which π has a star. [...] each of these strings is again a box, with e - 1 stars."  The
strings are the `π[ℓ ← λ]`, and `e + 1` stands for the paper's `e`. 

### `Lemma29.recurrence`

 Proof of Lemma 29, "The values", the displayed recurrence: "val(π) = ∑_λ val(π[ℓ ← λ])", because
"The leaves of π are the leaves of the ten strings π[ℓ ← λ]". It holds for a star at any level `ℓ`
of any cube `π`. 

### `lemma_29_values`

 **Lemma 29**, second sentence, correctness: "Given the two encodings of a tile, we can compute
the values of all these boxes". The recurrence of the dynamic program of the proof (`dpValue`), run
on the two encodings, returns `val(π)` for every box `π` with `e` stars. That the ten strings π[ℓ ←
λ] are boxes with `e - 1` stars, so that their values can be looked up, is `lemma_29_split`. (For
the time and space bound see `docs/REMARKS.md`, "Section 4: running times".) 
