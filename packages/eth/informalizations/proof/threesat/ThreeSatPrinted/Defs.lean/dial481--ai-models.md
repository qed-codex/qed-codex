---
{
  "module": "proof/threesat/ThreeSatPrinted/Defs.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/threesat/ThreeSatPrinted/Defs.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/threesat/ThreeSatPrinted/Defs.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # The deciding form of procedure #Sat of Algorithm 1 on the tree of the sparsification procedure of Appendix C, with NETWORK as in the printed proof of Lemma 1: definition

`SATCp ℓ τ` is `ThreeSatOnTree.satC τ` (proof/threesat/ThreeSatOnTree/Defs.lean: decode the input,
walk depth first the tree of the sparsification procedure of Appendix C at width 3, test the formula
ψ at every leaf) with
`Eight.ViaGrouping.COUNTp ℓ` as the test (proof/networks/Eight/ViaGrouping/AlgDefs.lean: COUNT of
Algorithm 1 at level ℓ, in which NETWORK is the algorithm of the printed proof of Lemma 1 and CLIQUE
that of the proof of Proposition 3 on the pieces of Lemma 2).
The thresholds of the procedure are θ 0 = 1, θ i = 4·τ^(2i−1) (`UniformInK.thetaU τ`), not
Calabro's, which Appendix C takes. This is the tree whose leaves the Lean statement of Lemma 4
(`SparsificationLemma.Mach.LemSparsification`) lists; the paper cites Lemma 4 and does not say which
procedure
computes its list.
This file has one definition and no proof. 

### `SATCp`

 **The deciding form of procedure #Sat(φ)** of Algorithm 1, for a fixed level ℓ and a fixed
parameter τ: the tree of the sparsification procedure of Appendix C is walked, and every leaf is
tested with COUNT at level ℓ. 
