---
{
  "module": "proof/networks/Eight/Level/Pieces.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/networks/Eight/Level/Pieces.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/networks/Eight/Level/Pieces.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # Lemma 2 from the eight-square identity in the form that the networks of a grid need

The counterpart of proof/networks/SingleBitPieces/Level/Pieces.lean for the pieces of Lemma 2 from
the eight-square identity. `stPieces_of`: the functions A_0, …, A_t, t = ⌈λ/3⌉, add up to 2^t·[x =
v][y = u] (Lemma 2(a)); the programs `Eight.fTop`, `Eight.fBot` factorize A_i over all words of
c_i^row bits row-wise and of c_i^col bits column-wise (Lemma 2(b), in the form `Eight.StFact`);
these numbers of bits are at most 2λ (Lemma 2(c)); and all values are at most 2^t in absolute value
(Lemma 2(a) and (b)).
Parts (a) and (b) are hypotheses here; `stPieces_of_lemPieces` takes part (a) from `LemPieces`. From
proof/networks/SingleBitPieces/Level/Pieces.lean only `sum_ofFn` is used, which does not speak of
any pieces. 

### `stPieces_of`

 Lemma 2 in the form that the networks of a grid need, from Lemma 2(a), that A_0 + … + A_t =
2^t·[x = v][y = u] and |A_i| ≤ 2^t (`ha_sum`, `ha_abs`: the fields `a_sum` and `a_abs` of
`Eight.LemPieces`), and Lemma 2(b) for the
programs (`hF`). The bounds c_i^row ≤ 2λ and c_i^col ≤ 2λ of Lemma 2(c) hold by the definition of
the two numbers as minima. 

### `stPieces_of_lemPieces`

 The same, with part (a) taken from `LemPieces` (its fields `a_sum` and `a_abs`); part (b) for
the programs stays a hypothesis (`hF`). 
