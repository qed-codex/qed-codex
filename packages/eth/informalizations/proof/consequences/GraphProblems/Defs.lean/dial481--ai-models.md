---
{
  "module": "proof/consequences/GraphProblems/Defs.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/consequences/GraphProblems/Defs.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/consequences/GraphProblems/Defs.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # Corollary 7: the programs (definitions only)

How the input word is read, the formulas that express the five problems, the formulas that fix the
number of true variables block by block, and the tree that shortens the long clauses of
Dominating Set. A formula is a `Fml` = list of clauses = list of lists of (variable, wanted value),
with natural numbers as variables, as in the namespace `CountKSat`. 

 ### Reading the input 

### `ones`

 The number of ones at the start of a word. 

### `rest`

 The word after its first ones and the zero that ends them. 

### `read1`

 `code G` as (n in unary, adjacency matrix). 

### `read2`

 `codeWith G s` as (n in unary, s, adjacency matrix). 

### `adjB`

 The entry (u, v) of an n × n matrix written row by row. 

### `pairs`

 All pairs (u, v) with u, v < n. 

 ### Counting with a prescribed number of true variables 

### `cntS`

 The number of assignments to x₀ … xₙ₋₁ that make a literal of every clause of ψ true and make
exactly s variables true. 

 ### The formulas of the problems: the variable x_v says that the vertex v is in the set 

### `indepF`

 Independent set: ¬x_u ∨ ¬x_v for every edge. 

### `cliqueF`

 Clique: ¬x_u ∨ ¬x_v for all u ≠ v that are not adjacent. 

### `coverF`

 Vertex cover: x_u ∨ x_v for every edge. 

### `nbhd`

 The closed neighborhoods, as lists of vertices. 

### `posC`

 A list of variables as a clause of positive literals. 

### `domF`

 Dominating set: for every vertex v the clause x_v ∨ ⋁ x_u over the neighbors u of v. Its width
is not bounded. 

### `colorF`

 Proper colorings with k colors, on n·k variables: x_{v·k+c} says that the vertex v has the color
c. Every vertex has a color, no vertex has two, and the ends of an edge do not have
the same color. 

 ### Exactly s true variables, block by block

The variables are cut into blocks of b. There are n/b + 1 blocks, so that the b·(n/b + 1) > n
variables of the blocks include x₀ … xₙ₋₁; the others are set to false. A number
y < (b+1)^(n/b+1) is read in base b + 1: its digit i is the number of true variables wanted in block
i. 

### `pats`

 All words of length b. 

### `nBlocks`

 The number of blocks. 

### `digit`

 The digit i of y in base b + 1. 

### `blockCl`

 «Exactly d of the b variables of block i are true»: one clause against every pattern with
another number of ones. 

### `blockF`

 ψ, the variables from n on false, and digit i of y true variables in block i; a formula without
satisfying assignment if the digits of y do not add up to s. 

 ### The tree for Dominating Set (after Calabro, Impagliazzo and Paturi, as in the paper's proof of Corollary 7)

A node holds (n in unary, s), the clauses of positive literals that may still be long, and a formula
that is not touched any more. While some clause C has more than w literals, let H be its first w
variables. Light child: C is replaced by H. Heavy child: the variables of H are false, and are
deleted from all clauses. 

### `DNode`

 A node of the tree. 

### `stepD`

 The two children of a node; none if no clause has more than w literals. 

### `rootD`

 The root: the closed neighborhoods. 

### `leafD`

 What is counted at a node: (n in unary, s, formula). 
