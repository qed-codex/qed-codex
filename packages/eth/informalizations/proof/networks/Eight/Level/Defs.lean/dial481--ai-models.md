---
{
  "module": "proof/networks/Eight/Level/Defs.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/networks/Eight/Level/Defs.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/networks/Eight/Level/Defs.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # Proposition 3 through Lemma 2 from the eight-square identity: definitions and interface statements

One level of the recursion, for the pieces of Lemma 2 from the eight-square identity, is built on
the functions A_0, …, A_t, t = ⌈λ/3⌉, of `EightSquareStatement.lean` and their factorizations
`Eight.fTop`, `Eight.fBot` (one step per value): for every
ι : ℛ → {0, …, t} the network with the smaller total, and the final division by 2^{t|ℛ|}. ρ = 11/12
(`Eight.rho`).
The networks of a grid on words, for any family of pieces given by plain functions, are those of
proof/rates/ClauseBound/Alg/GridNet.lean (`ClauseBound.Alg.GridNet.gridN`), taken at p = d = g. The
procedure for the weights of a row or a column is
`Groundwork.Prog.sideWP`, which does not depend on the pieces.
At the end: the numbers e_ℓ of Section 8 («The algorithm in pseudocode»).
This file has definitions and propositions `St… : Prop` only; nothing is proved or assumed here. 

### `numPat8`

 The number of functions ι : ℛ → {0, …, t}: (t + 1)^{|ℛ|}. 

### `netOfι`

 The row network (tr = false) or the column network (tr = true) of ι, on words; ι is written by
the number y in base t + 1. 

### `levelNet`

 The same network given by procedures: a weight is computed with g queries to the tables of the
clique, a value of a factor in one step. 

### `useRowP`

 «Apply Lemma 1 to the network with the smaller total»: is it the row network? 

### `levelAlg`

 Procedure CLIQUE of Algorithm 1 at a level above 0: for every ι : ℛ → {0, …, ⌈λ/3⌉}, the
algorithm `NE` for networks on [g] is run on the row network or on the column network of ι,
whichever has the smaller total; the values are
added up, and the sum is divided by 2^{⌈λ/3⌉|ℛ|}. 

 ### Interface statements 

### `StPieces`

 Lemma 2 in the form that the networks of a grid need. 

### `StPresents`

 The procedures present the network, within a·(B + λ)^a·t steps, t the cost of one query to the
tables of the clique (not ⌈λ/3⌉), and size S + a·(size c + B + λ)^a (the paper: τ = poly(B + λ)). 

### `StNetKeeps`

 The procedures have polynomial-time steps. 

### `StMin`

 The display «the smaller total»: min(U_row, U_col) ≤ N(ρ + 1/g) + 2g⁴, N = g⁴λ; N/g is written
g³λ. 

### `StLevel`

 «Cost»: an algorithm for networks on [g] with the exponent of Lemma 1 gives an algorithm for
cliques on g² nodes with the exponent (ρ + 2/K)e + 2/K. 

### `StLevelKeeps`

 The algorithm of a level has polynomial-time steps if that for networks has. 

 ### The numbers e_ℓ of Section 8 

### `levelE`

 e_ℓ of the first display of Section 8, with ρ = 11/12: e₀ = 1/2, e_{ℓ+1} = (ρ + 2/K_ℓ)·e_ℓ +
2/K_ℓ. K_ℓ is `Paper.levelK`: K₀ = 64, K_{ℓ+1} = 9K_ℓ¹⁶. 
