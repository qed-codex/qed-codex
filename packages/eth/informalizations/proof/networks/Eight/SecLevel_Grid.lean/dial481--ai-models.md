---
{
  "module": "proof/networks/Eight/SecLevel_Grid.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/networks/Eight/SecLevel_Grid.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/networks/Eight/SecLevel_Grid.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # Section 5 «One level of the recursion», the mathematics of one level: the grid, and displays (34) and (36)

The part of the proof of Proposition 3 that is pure mathematics (finite sums and counting, no
algorithm), for the functions A_0, …, A_t, t = ⌈λ/3⌉, of Lemma 2 (`Eight.A`), in the form and with
the constants of the paper. The definitions are in
proof/networks/Eight/SecLevel_GridDefs.lean.

* the functions ι : ℛ → {0, …, t}: `patterns`;
* the expansion (34), with the factor 2^{t|ℛ|}: `Zι`, `eqExpansion`;
* the row network and the column network of a term Z_ι, made with the factorizations `Eight.fTop`,
  `Eight.fBot` of the proof of Lemma 2(b) (`rowCut_factors`, `colCut_factors`): `rowNetwork`,
  `colNetwork`; their edge functions written out: `rowNetwork_Ψ`, `colNetwork_Ψ`;
  their values: `value_rowNetwork`, `value_colNetwork`;
* conditions (i) and (ii) of Definition 2 for both networks, with P = g³λ and all values at most
  2^{gB + g²t} (the paper has below 2^{B₁}, B₁ = gB + g²λ + 1): `rowNetwork_sized_t`,
  `colNetwork_sized_t`;
* the two totals and the smaller total (36): `U_rowNetwork`, `U_colNetwork`, `eqMinTotal_chain`,
  `eqMinTotal`.

The grid, its rectangles and their number (`Paper.rectangles`, `Paper.card_rectangles`,
`Paper.card_rectangles_le`), the four strings of a rectangle and Definition 1
(`Paper.FactorsThrough`) do not depend on the pieces and are taken from
proof/networks/Paper/SecLevel_Grid.lean and proof/networks/Paper/SecNetworks_DefFactor.lean; the sum
over a grid and the network of merged rows, for any functions at the rectangles and any
factorizations of them, are in proof/networks/Groundwork/ (`Groundwork.Grid.ZG`,
`Groundwork.Grid.rowNet`).
λ is written `lam`; a string of λ bits has the type `Bits lam` (= `Fin lam → Bool`); rows and
columns are numbered by `Fin g`. Lemma 2 speaks of λ ≥ 1 and i ≤ t, so the statements that use it
have the hypotheses `1 ≤ lam` and `∀ q, ι q ≤ tOf lam`;
every ι of display (34) satisfies the second one.
The networks that Algorithm 1 runs are these networks with settings and indices written as words:
see proof/networks/Eight/SecLevel_GridWords.lean. 

 ## The expansion (34) 

### `eqExpansion`

 **Display (34) of the paper**: 2^{t|ℛ|} · Z = ∑_ι Z_ι, the sum over all ι : ℛ → {0, …, t}.
«Multiply Z by 2^{t|ℛ|}, apply Lemma 2(a) to every rectangle, and expand.»
Here Z = `W.Z d` is the value of the clique with tables W on a node set J with g² elements, with one
string per edge: Z = ∑ over all choices of one string per edge of ∏_w W_w(the strings on the edges
at w).
Different from the paper: the nodes are identified with the grid points by an arbitrary bijection e;
a table W_w is a function of one string for every node w', where the entry at w' = w is a dummy that
is always the fixed string d
(`Grid.onGrid` carries the tables to the grid and makes them 0 unless the dummy entry is d). 

 ## The two networks of a term Z_ι 

### `rowCut_factors`

 Lemma 2(b), first factorization. 

### `colCut_factors`

 Lemma 2(b), second factorization. 

### `rowNetwork_Ψ`

 «Ψ_{a,a'} is the product of the factors of the g straight edges between rows a and a' and of
A_{ι(q)}(x_q, y_q, u_q, v_q) over the g(g−1)/2 rectangles q with these two rows.» Same as in the
paper. 

### `colNetwork_Ψ`

 Ψ_{j,j'} in the column network: the product of the factors of the g straight edges between
columns j and j' and of A_{ι(q)}(x_q, y_q, u_q, v_q) over the rectangles q with these two columns.
«There x_q, u_q and y_q, v_q are separated.» 

### `value_rowNetwork`

 «Each factor in (34) is used exactly once, so the value is Z_ι»: the row network. Same as in the
paper. 

### `value_colNetwork`

 The column network has the value Z_ι too. Same as in the paper. 

 ## Definition 2 for the two networks: P = g³λ, and all values at most 2^{gB + g²t} 

### `rowNetwork_sized_t`

 «Indeed ∑_{a' ≠ a} c_{a,a'} ≤ g³λ, |W_a| < 2^{gB}, and Ψ_{a,a'} and the functions of its
factorization are products of indicators and of g(g−1)/2 numbers of absolute value at most 2^t»: the
row network, with the bound 2^{gB + g²t} for all
values; the paper then uses 2^t ≤ 2^λ. Different from the paper: values «at most 2^{gB + g²t}» where
the paper has «below 2^{B₁}», B₁ = gB + g²λ + 1, and tables with |W_w| ≤ 2^B where the paper has <
2^B. 

### `colNetwork_sized_t`

 The same for the column network. 

 ## The smaller total (36) 

### `U_rowNetwork`

 «U_row = g²(g−1)λ + 2 ∑_{q ∈ ℛ} c^row_{ι(q)}», «because U counts ordered pairs». Same as in the
paper. 

### `U_colNetwork`

 «U_col = g²(g−1)λ + 2 ∑_{q ∈ ℛ} c^col_{ι(q)}». Same as in the paper. 

### `eqMinTotal_chain`

 **Display (36) of the paper**, all three inequalities: min(U_row, U_col) ≤ ½(U_row + U_col) ≤
N/g + |ℛ|(11λ/3 + 8) ≤ N(ρ + 1/g) + 2g⁴, where N = g⁴λ and ρ = 11/12. The second one is Lemma 2(c),
the third one |ℛ| ≤ g⁴/4.
Same as in the paper (N/g is written g³λ, so that g = 0 needs no exception). 

### `eqMinTotal`

 **Display (36) of the paper**, its two ends: min(U_row, U_col) ≤ N(ρ + 1/g) + 2g⁴. Same as in
the paper. 
