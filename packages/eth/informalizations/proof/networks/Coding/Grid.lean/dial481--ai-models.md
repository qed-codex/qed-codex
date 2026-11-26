---
{
  "module": "proof/networks/Coding/Grid.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/networks/Coding/Grid.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/networks/Coding/Grid.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # The strings at the grid points' own positions are padding

Proof of Proposition 3: «A setting of row a is the tuple (z_{(a,j)})_{j ∈ [g]} of the settings of
its g grid points; S_a is the set of these tuples, encoded by concatenation in g(g² − 1)λ ≤ P bits,
where P = g³λ.» Lean's settings have g³λ bits: for each grid point of the row a string of λ bits for
EVERY grid point, also for itself.
`stGridPadding`: Lean's network is the same network read at settings of g(g² − 1)λ bits, with
padding (`Coding.padRow`). Three of the seven fields have content:
* a padded setting has g³λ bits (`length_padRow`), and its string for the grid point at position u,
  held at the x-th grid point of the row, is `pieceRow` (`heG_padRow`);
* padding is one to one (`padRow_inj`): the strings at the other positions are those of z;
* a string of g³λ bits that has 0^λ at each grid point's own position is a padded setting
  (`exists_padRow`), and at all other strings W_a is 0 (`W_eq_zero`): this is the condition
  `if h w = d` of `Groundwork.Grid.onGrid`, read on words by `ClauseBound.Alg.GridNet.stC_dec`.
  `import all StepMachines.Math.CodeMore` gives access to `Groundwork.Code.block_ext`, which is not
  public. 

 ### Concatenations of strings of one length 

### `length_flatMap_range`

 A concatenation of n strings of c bits has n·c bits. 

### `block_flatMap_range`

 The j-th block of a concatenation of n strings of c bits is the j-th string. 

 ### The padded setting, string by string 

### `nMemb_self`

 On the g × g grid, a row or a column has g grid points. 

### `pieceRow`

 The string that the padded setting holds, at the x-th grid point of the row, for the grid point
at position u. 

### `padRow_eq`

 `padRow` written with `pieceRow`. 

### `nodeG_lt'`

 The position of the x-th grid point of a row or column is one of the g² positions. 

### `length_block_row`

 The part of z for the x-th grid point of the row has (g² − 1)λ bits. 

### `length_pieceRow`

 Each string of the padded setting has λ bits. 

### `length_rowPart`

 The part of the padded setting for one grid point has g²λ bits. 

### `length_padRow`

 A padded setting has g³λ bits. 

### `heG_padRow`

 The strings of the padded setting. 

### `pieceRow_skip`

 At the positions other than its own, a grid point holds the strings of z. 

### `padRow_inj`

 Padding is one to one. 

### `exists_padRow`

 A string of g³λ bits with 0^λ at each grid point's own position is a padded setting. 

 ### W is 0 off the padded settings 

### `eq_replicate_of_bitsOf`

 A string of λ bits that writes the index 0 is 0^λ. 

### `W_eq_zero`

 W_a is 0 unless the string at each grid point's own position writes the index 0. 

 ### The statements 

### `stGridPadding`

 **The strings at the grid points' own positions are padding**: «S_a is the set of these tuples,
encoded by concatenation in g(g² − 1)λ ≤ P bits, where P = g³λ» (proof of Proposition 3), where
Lean's settings have g³λ bits. 

### `stGridLength`

 «g(g² − 1)λ ≤ P», P = g³λ (proof of Proposition 3). 
