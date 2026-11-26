---
{
  "module": "proof/networks/Eight/ViaGrouping/LevelEnd.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/networks/Eight/ViaGrouping/LevelEnd.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/networks/Eight/ViaGrouping/LevelEnd.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # One level of the recursion on an algorithm for networks in the printed form, with the hypotheses filled in

proof/networks/Eight/ViaGrouping/LevelNet.lean, Level.lean and LevelCert.lean take interface
statements as hypotheses. Here they are filled in: Lemma 2 and its programs (`Eight.stPieces`, and
`Eight.stKeeps`, which is about the pieces and is not `Eight.ViaGrouping.stKeeps`) and the
procedures that present the two networks of ι (`Eight.Level.stPresents_of`).
Then the two functions for Ψ are taken to be the program `gridPsi` of
proof/networks/Eight/ViaGrouping/GridPsiDefs.lean. In the four theorems `…_gridPsi…` what is asked
of that program (`StGridPsi`, `StGridPsiPoly`) is a hypothesis; it is proved in
proof/networks/Eight/ViaGrouping/GridPsi.lean. The last
theorem is the sentence «Both networks satisfy Definition 2 …» of the proof of Proposition 3 for the
procedures that Algorithm 1 runs, without hypotheses. 

### `stLevelP`

 The cost of one level (the paragraph «Cost» of the proof of Proposition 3): if NA evaluates
networks on [g], in the printed form, with the exponent e·U + (e + 2)·gP/K of Lemma 1, and psiR,
psiC compute the functions Ψ of the row and of the column networks, then
`levelAlgP g psiR psiC NA` evaluates (g², λ)-cliques with the exponent (ρ + 2/K)e + 2/K, ρ = 11/12. 

### `stLevelKeepsP`

 The algorithm of one level has polynomial-time steps, if NA has (for P in unary) and psiR, psiC
are polynomial-time functions. 

### `stPsiOK_gridPsi`

 The program `gridPsi` computes Ψ in the form that the level asks for. 

### `stPsiPoly_gridPsi`

 The program `gridPsi` is polynomial-time in the form that the level asks for. 

### `levelAlgP_gridPsi_correct`

 «Cost» of the proof of Proposition 3, with the program `gridPsi` for Ψ: an algorithm for
networks on [g], in the printed form, with the exponent of Lemma 1 gives an algorithm for cliques on
g² nodes with the exponent (ρ + 2/K)e + 2/K. 

### `levelAlgP_gridPsi_keeps`

 With the program `gridPsi` for Ψ, the algorithm of one level has polynomial-time steps if the
algorithm for networks has. 

### `levelNetP_isNetworkP`

 **«Both networks satisfy Definition 2 with P = g³λ (so gP = N), with B₁ = gB + g²λ + 1 in the
role of B, and with τ = poly(B + λ)»** (proof of Proposition 3), for the procedures that CLIQUE of
Algorithm 1 hands to NETWORK (Ψ by the program `gridPsi`). What
differs from the paper is said at `levelNetP_isNetworkP_printed_of`. 
