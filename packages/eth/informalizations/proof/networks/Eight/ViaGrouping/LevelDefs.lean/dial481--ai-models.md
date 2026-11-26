---
{
  "module": "proof/networks/Eight/ViaGrouping/LevelDefs.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/networks/Eight/ViaGrouping/LevelDefs.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/networks/Eight/ViaGrouping/LevelDefs.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # One level of the recursion on an algorithm for networks in the printed form (definitions and statements only)

proof/networks/Eight/Level/Defs.lean builds one level of the recursion (Proposition 3; procedure
CLIQUE of Algorithm 1 above level 0) on an algorithm for networks in the form of
`Groundwork.Prog.NetEvaluator`, which is given no procedure for Ψ and no P. Here the same level is
built
on an algorithm `NA : SecNetworks.NetAlg` for networks as Definition 2 prints them. The row network
and the column network of ι are the same (`Eight.Level.netOfι`, `Eight.Level.levelNet`); the
algorithm is given in addition
* P = g³λ, the number of the sentence «Both networks satisfy Definition 2 with P = g³λ» of the proof
  of Proposition 3, and
* a procedure for Ψ_{a,b}: a plain function `psi λ y ((a, b), (z, z'))`, one step per value.
The function for Ψ is a parameter here, one for the rows and one for the columns; `StPsiOK` and
`StPsiPoly` say what is asked of it.
The loop over ι, the choice of the network with the smaller total and the final division by 2^{t|ℛ|}
are those of `Eight.Level.levelAlg`.
This file has definitions and propositions `St… : Prop` only; nothing is proved or assumed here. 

 ## The algorithm of one level 

### `levelProcs`

 The row network (tr = false) or the column network (tr = true) of ι, given as Definition 2(iii)
asks: the procedures of `Eight.Level.levelNet`, the number P = g³λ, and the function `psi` for Ψ,
one step per value. Every string of g³λ bits is a setting, so the test for membership says yes; B is
not given
(see `ofProcs`). The context is (c, y); y is the number of ι. 

### `levelNetP`

 The row network (tr = false) or the column network (tr = true) of ι as the data of Definition 2:
the network `Eight.Level.netOfι` that Algorithm 1 runs, with Ψ_{a,a'} the sum that its factorization
defines and P_a = g³λ for every a (in the paper P_a = g(g² − 1)λ; the λ bits more per grid point are
the dummy string of proof/networks/Eight/SecLevel_Grid.lean). It has g nodes
(`nParts g g tr` is g). 

### `levelAlgP`

 Procedure CLIQUE of Algorithm 1 at a level above 0, on an algorithm `NA` for networks in the
printed form: for every ι : ℛ → {0, …, ⌈λ/3⌉}, `NA` is run on the row network or on the column
network of ι, whichever has the smaller total; the values are
added up, and the sum is divided by 2^{⌈λ/3⌉|ℛ|}. `psiR`, `psiC` compute Ψ for the row networks and
for the column networks. 

 ## Interface statements 

### `StPsiOK`

 The function `psi` computes Ψ_{a,b} of the network of ι on settings: for λ ≥ 1, y < (t + 1)^{|ℛ|},
a ≠ b, z ∈ S_a, z' ∈ S_b. (Ψ does not depend on the tables of the clique.) 

### `StPsiPoly`

 The function `psi` is computed in polynomial time, for λ in unary. 

### `StOfPaperNetwork`

 The bound of Lemma 1 read on a network given as a `PNet`: if NA has the bound of Lemma 1
(`Correct`), then on the procedures of such a network, together with a function that gives P and a
procedure Q that computes its Ψ within t steps, NA has the
bound that `Groundwork.Prog.NetEvaluator.Correct` states. 

### `StLevelP`

 «Cost»: an algorithm for networks on [g], in the printed form, with the exponent of Lemma 1
gives an algorithm for cliques on g² nodes with the exponent (ρ + 2/K)e + 2/K. 

### `StLevelKeepsP`

 The algorithm of a level has polynomial-time steps if that for networks has and the two
functions for Ψ are computed in polynomial time. 
