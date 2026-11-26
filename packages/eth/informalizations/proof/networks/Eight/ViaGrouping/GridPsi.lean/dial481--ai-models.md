---
{
  "module": "proof/networks/Eight/ViaGrouping/GridPsi.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/networks/Eight/ViaGrouping/GridPsi.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/networks/Eight/ViaGrouping/GridPsi.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # Ψ_{a,a'} in the two networks of Proposition 3, as a program: proofs

The program `gridPsi` of proof/networks/Eight/ViaGrouping/GridPsiDefs.lean renders the sentence
«Ψ_{a,a'} is the product of the factors of the g straight edges between rows a and a' and of
A_{ι(q)}(x_q, y_q, u_q, v_q) over the g(g−1)/2 rectangles q with these two rows»
(proof of Proposition 3, «Two networks for each ι») on settings written as words. Here:
* `gridPsi_eq`, `stGridPsi`: it computes Ψ of the network that Algorithm 1 runs
  (`Eight.Level.netOfι`). That network is the row network or the column network of the proof with
  settings written as words (`netOfι_row`, `netOfι_col`), whose Ψ, defined as the sum
  ∑_θ f_{a,a'}·f_{a',a}, is the product of the sentence by `Eight.rowNetwork_Ψ` and
  `Eight.colNetwork_Ψ`; the program `aMul` computes A_i (`Eight.stAMul`).
* `gridPsi_polyT`, `stGridPsiPoly`: it is polynomial-time («computable in time poly(λ)», Lemma 2(a),
  for each of the at most g² factors). 

 ## The program as a product 

### `psiLt_eq`

 The loop and the test of `psiLt` written as products: over the g straight edges, and over the
pairs i < i'. 

### `A_bitsOf`

 The program of the proof of Lemma 2(a) computes A_i at four words of λ bits. 

 ## Correctness 

### `psiLt_row`

 Ψ_{a,a'} of the row network that Algorithm 1 runs, for a < a'. 

### `psiLt_col`

 Ψ_{j,j'} of the column network that Algorithm 1 runs, for j < j'. 

### `psiLt_eq_Ψ`

 Both directions at once. 

### `gridPsi_eq`

 **The program computes Ψ_{a,a'}** of the row network and of the column network that Algorithm 1
runs, at all words of g·g²·λ bits. «Ψ_{a,a'} is the product of the factors of the g straight edges
between rows a and a' and of A_{ι(q)}(x_q, y_q, u_q, v_q) over the
g(g−1)/2 rectangles q with these two rows.» Same as in the paper; it holds for every number y,
because a digit in base t + 1 is at most t. 

### `stGridPsi`

 The same in the form of the interface. 

### `stPsiOK`

 The program `gridPsi` computes Ψ: for λ ≥ 1, every ι (a number y < (t + 1)^{|ℛ|}), two different
rows (columns) a, b and settings z, z' of them, gridPsi g tr λ y ((a, b), (z, z')) is Ψ_{a,b}(z, z')
of the network `Eight.Level.netOfι` that Algorithm 1 runs. This is what the
algorithm of one level asks of the function for Ψ (`StPsiOK`). 

 ## Polynomial time 

### `rectPsi_polyT`

 The factor of one rectangle is polynomial-time: four strings are cut out of the two settings, a
digit of y is computed, and A_i is «computable in time poly(λ)» (Lemma 2(a)). 

### `psiLt_polyT`

 Ψ_{a,b} for a < b is polynomial-time: a test on g pairs of strings and a product of g² factors. 

### `gridPsi_polyT`

 **The program for Ψ is polynomial-time**, as a function of λ, y and the query, for fixed g and a
fixed direction. 

### `stGridPsiPoly`

 The same in the form of the interface: λ is a function of the context, given in unary. 

### `stPsiPoly`

 The program `gridPsi` is a polynomial-time function of (context, y, query), for λ given in unary
(`StPsiPoly`). 
