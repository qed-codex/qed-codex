---
{
  "module": "ThreeSumApsp/Programs/Sec3/Theorem21b/Apsp/Host.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Anthropic, PBC",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Programs/Sec3/Theorem21b/Apsp/Host.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Programs/Sec3/Theorem21b/Apsp/Host.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# APSP from the (min,+)-product

For Theorem 21(b): if no closed walk has negative weight, then squaring the weight matrix ⌈log₂ n⌉
times in the (min,+)-product yields the distance matrix, and all finite entries that occur have
absolute value at most nU, where U bounds the edge weights.  The host below does this over an
arbitrary solver of the (min,+)-product.

ap(n, U, adj, w, out, fr) keeps the current matrix in the `n²` cells from `fr`, with `3nU` for `+∞`;
the product is written to the next `n²` cells, and the solver gets the free pointer `fr + 2n²`.
After each product the entries above `nU` are set back to `3nU` while the matrix is copied back.
The rounds are counted by doubling a number that starts at 1, as long as it is below `n`: these are
`⌈log₂ n⌉` rounds.

The proof follows the text: one round squares the matrix (`ApspHost.round_spec`), the last call
writes the answer (`ApspHost.out_spec`, `ApspHost.answer_correct`), and `ap_spec` puts the parts
together.  The result is `isHost_ap : IsHost mpTask apTask apTime apNeed`.


### `Verts`

 The number n of vertices. 

### `Bound`

 The bound U on the weights. 

### `AdjAt`

 The address of the adjacency matrix. 

### `WtsAt`

 The address of the weights. 

### `Out`

 The address of the answer. 

### `Free`

 The free pointer, where the current matrix is kept. 

### `Cells`

 n². 

### `Thresh`

 nU. 

### `Big`

 3nU, which stands for +∞. 

### `ProdAt`

 fr + n², where the product is written. 

### `SolverFree`

 fr + 2n², the free pointer of the solver. 

### `Power`

 The power of two that counts the rounds. 

### `Res`

 Takes the results of the calls. 

### `apRound`

 One round: the product of the matrix with itself, clipped and copied back. 

### `apBody`

 ap(n, U, adj, w, out, fr), over the procedures number pMP (a solver of the (min,+)-product),
pInit, pClip and pOut (the three passes). 

### `apTime`

 The time of the host, given the time of the solver: `⌈log₂ n⌉` products at the bound `3nU`, and
`O(n²)` steps for each product and at both ends. 

### `apNeed`

 The need of the host, given the need of the solver. 

### `locals`

 The locals of the host during the loop; pw is the power of two that counts the rounds, res the
result of the last call.  Local 9 is not used and stays 0. 

### `Inv`

 The invariant of the loop before round t: the matrix after t squarings stands at the free
pointer, and nothing below it has changed. 

### `Ctx`

 The program has the solver and the three passes, the instance is as the task prescribes, and the
limits allow for the need of the host. 

### `Ctx.places`

 The arithmetic facts of the hypotheses as one conjunction: what the limits allow and what the
instance satisfies. 

### `answer_correct`

 The pairs that apOut writes for the matrix after ⌈log₂ n⌉ squarings are the answer. 

### `round_spec`

 **One round of the host** squares the matrix at the free pointer: a (min,+)-product, the
clipping of the large entries, and the doubling of Power. 

### `out_spec`

 **The end of the host**: the answer is written. 

### `ap_spec`

 **The host is correct**, in every program that begins with the solver's program and has the
three passes. 

### `polyNeed_apNeed`

 The need of the host is polynomially bounded if the need of the solver is. 

### `isHost_ap`

 **APSP from the (min,+)-product**, as a host. 
