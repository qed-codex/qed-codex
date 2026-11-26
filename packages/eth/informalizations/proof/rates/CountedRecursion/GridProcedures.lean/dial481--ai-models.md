---
{
  "module": "proof/rates/CountedRecursion/GridProcedures.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/CountedRecursion/GridProcedures.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/CountedRecursion/GridProcedures.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # The contexts, the two networks of a pattern, and the procedure for an entry

Definitions only; nothing is stated or proved here.

**The text** (proof of Theorem A (b)): «Follow the proof of Proposition 3, with this g, with the
A_i, i ∈ 𝓘, in place of A_0, …, A_t and with d in place of 2^t … each Z_ι is the value of the row
network and of the column network.» Proof of Proposition 3, «Two networks for each ι»: «W_a is the
product of the g table entries of row a and of the factors of the
straight edges inside row a. Ψ_{a,a'} is the product of the factors of the g straight edges between
rows a and a' and of A_{ι(q)}(x_q, y_q, u_q, v_q) over the g(g−1)/2 rectangles q with these two
rows.»

**What is here.**
* `Ctx`: the context of an instance: (ℓ, λ, B) in unary, «the (K_ℓ, λ)-clique with |W_w| < 2^B»,
  and, for an instance that was called, its `Parent`: what is needed to compute an entry of ITS
  tables from the caller's.
* `listsAsPieces`: the numbers |𝓘|, c^row_i, c^col_i, read from the lists in the context, in the
  form in which the plain functions of proof/rates/ClauseBound/Alg/Data.lean take them.
* `gridProcsData c`: the row or column network of ι as Definition 2(iii) asks, with g, λ, the
  direction, ι and the lists read from the context. As `Printed.gridProcs` (fixed g, the pieces of
  Lemma 2, computed in a step); here a value of A_i or of a function of a factorization is a query
  to the pieces.
* `procedure c`: an entry of the callee's tables: `entryData` (EntryDefs.lean), each of its queries
  of Definition 2(iii) answered by these procedures (`QueryMachines.QueryMachine.subst`).

The plain functions of the grid (`nodeG`, `heG`, `chkG`, `digG`, `lenG`, `capG`, `rectIxG`) are
those of proof/rates/ClauseBound/Alg/Data.lean, called with p = d = g and h = 0; the layout of the
four strings of a rectangle is that of `Eight.ViaGrouping.rectPsi`, and that of f_{a,a'} is that of
`ClauseBound.Alg.gridFf`. 

 ### Contexts 

### `Lists`

 «The set 𝓘 and the numbers … c^row_i, c^col_i»: the list of 𝓘 in increasing order, and the
numbers c^row_i and c^col_i in the same order (in binary). 

### `Parent`

 What the procedure needs to compute an entry of a callee's tables: (K, g) in unary; the CALLER's
(λ, B) in unary; the lists for the caller's λ; the direction (false: row network), the number y of
the pattern ι, the number x of the grouping. 

### `Head`

 (ℓ, λ, B) in unary: «the (K_ℓ, λ)-clique with |W_w| < 2^B». This is all that the solver reads of
a context. 

### `Ctx`

 The context of an instance: (ℓ, λ, B) in unary; and the parent, if the instance was called. 

### `pK`

 The parts of a parent: K. 

### `pG`

 g. 

### `pLam`

 The caller's λ. 

### `pB`

 The caller's B. 

### `pLists`

 The lists for the caller's λ. 

### `pTr`

 The direction: false for the row network, true for the column network. 

### `pY`

 The number y of the pattern ι. 

### `pX`

 The number x of the grouping. 

### `hLev`

 The level, the label length and the bound on the bits of an instance: ℓ. 

### `hLam`

 λ. 

### `hB`

 B. 

### `cLev`

 The level of an instance. 

### `cLam`

 Its label length. 

### `cB`

 Its bound on the bits of the tables. 

### `parentOf`

 The parent of an instance. (The procedure is run on instances that were called; for the
outermost instance this is a dummy.) 

### `top`

 The outermost instance. 

### `listsAsPieces`

 The numbers of the pieces, read from the lists. The pieces are numbered by their place in the
list of 𝓘. Only `cnt` and `cap` are read by the functions that are called with it. «We may and do
assume c^row_i, c^col_i ≤ 2λ»: a number in the list is cut at 2λ, so that on EVERY context the
lengths made from it can be written in unary in polynomial time. 

 ### The numbers of the two networks 

### `bitsOne`

 «B₁ = gB + g²(2λ)^c in the role of B». 

### `netP`

 «P = g³λ». 

### `netB`

 B₁ for the caller's λ and B. 

### `netLen`

 P_a: every setting of a row has g·g²·λ bits (this development keeps, for each grid point, a slot
of λ bits for the edge to itself, where the paper encodes a row in g(g² − 1)λ bits). 

### `netCap`

 c_{a,a'} = gλ + Σ_{q with rows a, a'} c^row_{ι(q)} (or c^col). 

### `netData`

 The input of Definition 2(iii) for the network, with K and g beside it. 

 ### The queries 

### `UpQuery`

 The queries of the procedure: to the caller's tables, or to the pieces. 

### `pointQuery`

 The entry of the caller's tables at the grid point number i of the row a = q.1, at the strings
that the setting z = q.2 of the row has for it. As in `ClauseBound.Alg.gridW`. 

### `ordered`

 A query for Ψ with the smaller row first: Ψ_{a,a'}(z, z') = Ψ_{a',a}(z', z). 

### `straightOK`

 «the factors of the g straight edges between rows a and a'»: the two copies agree on each of
them. As in `Eight.ViaGrouping.psiLt`. 

### `rectStrings`

 The four strings (x_q, y_q, u_q, v_q) of the rectangle on the rows a < b and the columns i < i'
(tr = true: on the columns a < b and the rows i < i'). As in `Eight.ViaGrouping.rectPsi`. 

### `pieceAt`

 ι(q) ∈ 𝓘 for the rectangle number κ of the pair of rows number r: the digit of y in base |𝓘|
gives its place in the list. 

### `rectQuestion`

 The question «A_{ι(q)}(x_q, y_q, u_q, v_q)?» for the rectangle with the columns j / g < j % g. 

### `labelOK`

 In f_{a,b}(z, θ): the first gλ bits of θ are the strings of z on the g straight edges to b. As
in `ClauseBound.Alg.gridFf`. 

### `factorQuestion`

 The question for the factor of the rectangle with the columns j / g < j % g in f_{a,b}(z, θ):
the function of the first pair of strings if a < b, of the second if a > b, at the two strings of z
and the chunk of θ that belongs to the rectangle. As in `ClauseBound.Alg.gridFf`. 

 ### The four procedures 

### `rowWeight`

 «W_a is the product of the g table entries of row a and of the factors of the straight edges
inside row a»: the check, then g queries to the caller's tables. 

### `rowPair`

 «Ψ_{a,a'} is the product of the factors of the g straight edges between rows a and a' and of
A_{ι(q)}(x_q, y_q, u_q, v_q) over the g(g−1)/2 rectangles q with these two rows»: the check, then
one query to the pieces for each rectangle. The loop runs over all j = i·g + i' < g², with the
factor 1 unless i < i'. 

### `rowFactor`

 f_{a,a'}(z, θ): the check of the straight edges against θ, then one query to the pieces for each
rectangle. 

### `gridProcsData`

 **«Two networks for each ι»**: the row network (direction false) or the column network
(direction true) of ι, as Definition 2(iii) asks; everything is read from the context. Every string
of g³λ bits is a setting; W_a is 0 unless the slots for the edges from a grid point to itself are 0
and the straight edges inside the row agree. 

 ### The procedure 

### `calleeInput`

 From the callee's context and its query (γ, Θ): the context of the four procedures, and the
input of `entryData`: K, g, the input of Definition 2(iii), the grouping number x, and Θ cut into
its K − 1 strings of L bits; L is the callee's label length. 

### `procedure`

 **«answer each query by computing the entry»**: the entry (γ, Θ) of the tables W̃ of the callee,
computed with queries to the caller's tables and to the pieces. 
