---
{
  "module": "proof/rates/CountedRecursion/PatternPsi.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/CountedRecursion/PatternPsi.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/CountedRecursion/PatternPsi.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # Ψ_{a,a'} is the product that the procedure computes

Proof of Proposition 3, the two networks for each ι: Ψ_{a,a'} is the product of the factors of the g
straight edges between rows a and a' and of A_{ι(q)}(x_q, y_q, u_q, v_q) over the g(g−1)/2
rectangles q with these two rows. The Ψ of `patternNet` is the sum that the factorization defines.
Here:
* `cutsOK_piecesOf`: the pieces, in the form `piecesOf D c`, factor as the grid of this development
  asks (`ClauseBound.Alg.GridNet.CutsOK`), for the functions A_i themselves;
* `pairIsProduct : PairIsProduct`: so, by `Groundwork.Grid.rowNet_Ψ` and
  `Groundwork.Network.Ψ_pull`, Ψ is the product, in the form in which `rowPair` computes it. This is
  the same statement as `Eight.ViaGrouping.psiLt_row` and `psiLt_col`, here for general pieces. 

### `cutsOK_piecesOf`

 The pieces factor as the grid of this development asks. 

### `test_and_loop`

 The test and the loop of `rowPair` written as products: over the g straight edges, and over the
pairs i < i'. 

### `pair_row`

 Ψ_{a,a'} of the row network, for a < a'. 

### `pair_col`

 Ψ_{j,j'} of the column network, for j < j'. 

### `pairIsProduct`

 **Ψ_{a,a'} is the product of the factors of the g straight edges between rows a and a' and of
A_{ι(q)}(x_q, y_q, u_q, v_q) over the g(g−1)/2 rectangles q with these two rows.** 
