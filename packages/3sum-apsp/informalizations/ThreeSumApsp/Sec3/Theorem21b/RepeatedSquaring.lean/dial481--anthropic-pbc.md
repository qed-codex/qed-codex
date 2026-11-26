---
{
  "module": "ThreeSumApsp/Sec3/Theorem21b/RepeatedSquaring.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Anthropic, PBC",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Sec3/Theorem21b/RepeatedSquaring.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Sec3/Theorem21b/RepeatedSquaring.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# Theorem 21(b): repeated squaring computes the distances

For Theorem 21(b): if no closed walk has negative weight, then squaring the weight matrix `⌈log₂ n⌉`
times in the (min,+)-product yields the distance matrix, and all finite entries that occur have
absolute value at most `nU`, where `U` bounds the edge weights (`theorem_21b_repeated_squaring`,
`theorem_21b_entries_bounded`).

Under this hypothesis, after `t` squarings the entry at `(i, j)` is the least weight of a walk from
`i` to `j` with at most `2^t` edges: it is the weight of such a walk (`exists_walk_of_entry`) and at
most the weight of every such walk (`entry_le_walkWeight`).  Cutting closed pieces out of a walk
shows that fewer than `n` edges are enough (`exists_short_walk`), and a walk of finite weight with
`k` edges has weight at most `kU` in absolute value (`abs_walkWeight_le`).


### `walkEnd_append`

 The end of a walk that is followed by a second walk. 

### `walkWeight_append`

 The weight of a walk that is followed by a second walk is the sum of the two weights. 

### `exists_walk_of_entry`

 Every entry of the matrix after `t` squarings is the weight of a walk with at most `2^t` edges.


### `exists_closed_piece`

 A walk with at least `n` edges visits some vertex twice: it consists of a walk `p`, a closed
walk `c` with at least one edge, and a walk `q`. 

### `exists_short_walk`

 If no closed walk has negative weight, every walk can be replaced by a walk with the same ends,
fewer than `n` edges, no more edges than before, and no larger weight: cut out closed pieces. 

### `entry_le_walkWeight`

 If no closed walk has negative weight, the entry after `t` squarings is at most the weight of
every walk with at most `2^t` edges. 

### `abs_walkWeight_le`

 If the edge weights are at most `U` in absolute value, a walk of finite weight with `k` edges
has weight at most `kU` in absolute value. 

### `theorem_21b_repeated_squaring`

 For **Theorem 21(b)**, repeated squaring: if no closed walk has negative weight, then squaring
the weight matrix `⌈log₂ n⌉` times in the (min,+)-product yields the distance matrix.
(`Nat.clog 2 n` is `⌈log₂ n⌉`.)  Stated for weights in any linearly ordered commutative group, so
that it covers integer and real weights. 

### `theorem_21b_entries_bounded`

 For **Theorem 21(b)**, repeated squaring: a bound on the entries.  If the edge weights have
absolute value at most `U`, every finite entry of every matrix of the repeated squaring has absolute
value at most `nU`; with `U = n^ν` this is `n^{ν+1}`.

NOTE.  A missing edge has the weight `⊤` here, while the (min,+)-product of Theorem 21(b) is on
integer matrices with entries of absolute value at most `U` (`IsMinPlusProduct`).  Nothing is stated
here about replacing `⊤` by a large number. 
