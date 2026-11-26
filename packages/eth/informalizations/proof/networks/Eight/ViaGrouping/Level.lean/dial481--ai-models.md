---
{
  "module": "proof/networks/Eight/ViaGrouping/Level.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/networks/Eight/ViaGrouping/Level.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/networks/Eight/ViaGrouping/Level.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # The cost of one level, on an algorithm for networks in the printed form

`stLevelP_of`: the paragraph «Cost» of the proof of Proposition 3, for the algorithm `levelAlgP`
(proof/networks/Eight/ViaGrouping/LevelDefs.lean), which calls an algorithm for networks as
Definition 2 prints them. For every ι : ℛ → {0, …, t}, t = ⌈λ/3⌉, that algorithm is run on
the network with the smaller total, which is at most N(ρ + 1/g) + 2g⁴, ρ = 11/12; both networks
satisfy Definition 2 with P = g³λ, so that gP = N, and this P is what the algorithm is given; there
are (t + 1)^{|ℛ|} functions ι; the values add up to 2^{t|ℛ|}·Z, and
the last step divides.
The proof follows the paragraph: the bound of Lemma 1 (`Correct`) is applied to the network
`levelNetP` of ι, which satisfies Definition 2 as printed by the sentence «Both networks satisfy
Definition 2 …» (`levelNetP_isNetworkP_of`, proof/networks/Eight/ViaGrouping/LevelNet.lean), has
the value Z_ι (`value_levelNetP`) and the total of the display (`U_levelNetP`). The other facts are
those of proof/networks/Eight/SecLevel_GridWords.lean and proof/networks/Eight/Level/Min.lean:
display (34) (`eqExpansion_words`), the bound on the values (`netOfι_sized_t`), display (36)
(`stMin`). 

### `stLevelP_of`

 The paragraph «Cost» of the proof of Proposition 3, with ρ = 11/12, for the algorithm
`levelAlgP`: the bound of Lemma 1 is applied to the row network or the column network of ι, a
network in the sense of Definition 2 (`levelNetP_isNetworkP_of`); then displays (34) and (36). The
hypothesis: the procedures for W_a and f_{a,a'} present the
two networks. Same as in the paper, except for what LevelNet.lean lists for the two networks, and
that sizes are bounded too. 
