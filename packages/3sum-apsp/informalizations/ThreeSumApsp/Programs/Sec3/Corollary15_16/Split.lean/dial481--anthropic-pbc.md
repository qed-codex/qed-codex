---
{
  "module": "ThreeSumApsp/Programs/Sec3/Corollary15_16/Split.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Anthropic, PBC",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Programs/Sec3/Corollary15_16/Split.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Programs/Sec3/Corollary15_16/Split.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# Corollary 15: splitting the set of query pairs

Corollary 15: "splitting W into sets of at most n²/√D query pairs".  In full:
if #Lop-AE-SparseTri is solved in time T(n, D, w), then it is solved in time
⌈w/s⌉ (T(n, D, s) + O(n D + 1)) + O(w + 1), where s = max(1, ⌊n²/√D⌋) is `splitCap n D`.  This is
`Claim.LopSplit`, with "the problem is solved in time T" read as `LopSolvedIn lopCountTask T`
(`claim_lopSplit`).

The host computes c = max(1, min(⌊n²/√D⌋, w)) and calls the solver on the pieces of c query pairs
(the last piece may be shorter).  A piece is a segment of the arrays of query pairs and of answers,
so nothing is copied, and the two matrices stay where they are.  The number ⌊n²/√D⌋ is the greatest
c with c² D ≤ n⁴; it is found by counting up, and the counting stops at w, because the claim allows
only O(w + 1) steps outside the calls.  If w is smaller than ⌊n²/√D⌋, all query pairs form a single
piece, whether the length of a piece is ⌊n²/√D⌋ as in the claim or min(⌊n²/√D⌋, w) as computed here.

* `lopSplitCount_spec`, `lopSplitCap_spec`: the counting finds c.
* `lopSplitPiece_spec`: one call.  A piece of an instance is an instance (`piece_pre`), and its
  answers are a piece of the answers (`thinOut_piece`).
* `split_spec`: the loop over the pieces.
* `ceilDiv_capW_le`: there are at most as many pieces as in the claim; `polyNeedN_split`: the need
  stays polynomial.


 ## The procedure 

### `C`

 The local variables of split beside the ten arguments: the length c of the pieces; N⁴; first the
bound of the counting, then the number lo of query pairs that are done; the length len of the
piece; the result of the call. 

### `lopSplitCount`

 c counts up as long as c < lo and (c + 1)² D ≤ N⁴. 

### `lopSplitCap`

 c := max(1, min(⌊N²/√D⌋, w)). 

### `lopSplitPiece`

 The solver is called on the piece of len = min(c, w - lo) query pairs from number lo on. 

### `lopSplitBody`

 split(N, D, w, U, x, y, wi, wj, out, fr). 

### `lopCapW`

 The length of the pieces: max(1, min(⌊n²/√D⌋, w)). 

### `lopSplitTime`

 The number of steps of split, if the solver takes Tn: one call for each piece. 

### `lopSplitNeed`

 What split needs: words for n⁴ and w² D, one more level of calls, and what the solver needs for
any number of query pairs up to w. 

 ## Pieces 

### `ceilDiv_capW_le`

 The number of pieces for w query pairs is at most the number of pieces of the claim,
⌈w'/splitCap n D⌉, for every w' ≥ w. 

### `piece`

 The piece of len query pairs from the query pair number lo on. 

### `zip_piece`

 The pairs of a piece are a piece of the list of the pairs. 

### `thinOut_piece`

 The answers for a piece are a piece of the list of the answers. 

### `piece_pre`

 A piece of an instance is an instance: the matrices are the same, and its query pairs and its
answers lie within those of the instance. 

### `pre_keptBut`

 An instance stays where it is if no cell below the free pointer changes, except the answers. 

 ## The host 

### `ok_piece`

 What split needs covers what the solver needs for a piece. 

### `locals`

 The local variables of split, as a list. 

### `lopSplitCount_spec`

 **The counting**: from c = 1 and lo = w it ends with c = max(1, min(⌊N²/√D⌋, w)). 

### `lopSplitCap_spec`

 **The length of the pieces.** 

### `lopSplitPiece_spec`

 **One piece**: the solver answers the query pairs lo, …, lo + len - 1, where
len = min(c, w - lo). 

### `split_spec`

 **split** solves #Lop-AE-SparseTri. 

 ## The need stays polynomial 

### `own_le_polyBound`

 The numbers that the host itself forms: each parameter is at most X = (n + 1) (D + 1) (w + 1),
so n⁴ + w² D + 2 ≤ X⁴ + X³ + 2 ≤ 4 X⁴. 

### `sup_le_polyBound`

 What the solver needs on the pieces, which have at most w query pairs. 

### `polyNeedN_split`

 The need of the host is polynomially bounded if that of the solver is. 

### `claim_lopSplit`

 **Corollary 15, the general case**: a solver for the instances
of #Lop-AE-SparseTri(n, D) with at most n²/√D query pairs gives one for every set W of query pairs.
"For larger W, apply the theorem [Theorem 5] to each of at most ⌈|W|√D/n²⌉ + 1 pieces." 
