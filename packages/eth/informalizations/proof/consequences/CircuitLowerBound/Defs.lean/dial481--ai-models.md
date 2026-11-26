---
{
  "module": "proof/consequences/CircuitLowerBound/Defs.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/consequences/CircuitLowerBound/Defs.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/consequences/CircuitLowerBound/Defs.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # The circuit lower bound for E^NP (Section 7): the objects of the proof (definitions only)

The proof follows R. Williams's sketch (Improving exhaustive search implies superpolynomial lower
bounds, Theorem 6.1). A run of a machine is written as a formula whose clauses are the shifts of a
finite TABLE of clauses; the
formulas `Phi m` are put together so that a fast nondeterministic algorithm for «is `Phi m`
satisfiable?» contradicts itself; the language `L0` holds the bits of a fixed satisfying assignment
of `Phi m`. 

 ### Tables: a formula as the shifts of finitely many clauses

A variable of the formula is a triple (kind, t, q): a kind of statement, a time t, a position q. 

### `TLit`

 A literal of a table: (kind, how t is formed, how q is formed, a number added to q, sign). 

### `TCl`

 A clause of a table: three literals (a literal may be repeated). 

### `MCode`

 A table with its two numbers: (the number of bits for the kind, the number of bits by which
positions are longer than times, the clauses). 

### `bt`

 The number of bits of a time, if a variable is to be written with L bits: times are 0 … 2^bt. 

### `bq`

 The number of bits of a position in the number of a clause. 

### `rb`

 The number of bits for the place of a clause in the table. 

### `nb`

 The number of bits of the number of a clause. 

### `tval`

 The time of a literal in the shift by t: 0, t, t + 1 or the last time 2^b, for the modes 0, 1,
2, 3. 

### `qval`

 The position of a literal in the shift by q, before the number of the literal is added: 0, q or
the parameter P, for the modes 0, 1 and 2, 3. 

### `vidx`

 The number of the variable (kind, time, position): the position in the lowest bq + 1 bits, then
the time in bt + 1 bits, then the kind in kb bits. 

### `litAt`

 A literal of the formula. 

### `zeroCl`

 The clause that stands for the places beyond the end of the table: «the variable 0 is false». 

### `clauseAt`

 Clause number j of the formula: j is (place in the table, t, q), with q in the lowest bq bits
and t in the next bt bits. 

### `tabF`

 The formula of the table e, for variables of L bits and the parameter P. 

### `Fits`

 There is room: the variables fit into L bits, there is at least one bit of time, and the
parameter is small against the number of times. 

 ### Tables from numbers 

### `ones`

 The number of ones at the start of a word. 

### `rest`

 The word after its first ones and the zero that ends them. 

### `fld`

 The i-th number of W bits in a word. 

### `litOf`

 Five numbers from place i on, as a literal. 

### `codeOfWord`

 The word 1^W 0, then numbers of W bits: kb, lam, and 15 numbers for each clause. What is left
over at the end is not read. 

### `codeOf`

 The table with the number a: the binary digits of a, lowest first, without their first ones and
the zero after these. So every table has infinitely many numbers. 

 ### The chains: m = 2^a·(2s + 1) is place s of chain a 

### `nu`

 The number of zeros at the low end of m. 

### `pos`

 The place of m in its chain. 

### `next`

 The next number of the chain. 

### `top`

 The last place of chain a. 

### `Phi`

 The formulas. Before the last place of chain a: the formula of table a with the parameter
`next m`. At the last place: a formula that is satisfiable if and only if the formula of table a for
the first number 2^a of the chain is not.
Everywhere else, and where there is no room: the empty formula. 

 ### The language 

### `units`

 «The variables 0, 1, … have the values w.» 

### `greedy`

 The values of the first j variables in the search that sets each variable to 0 if that can still
be continued to a satisfying assignment, and to 1 if not. 

### `L0`

 The language: a word x of length m is the number i of a variable, lowest bit first; x is in the
language if the search for `Phi m` gives the variable i the value 1. 

 ### Machines 

### `unary`

 The number P in unary: 1^P 0. 

### `Outputs`

 `N`, started on the word x, halts within T steps with the word y as output. 

### `Acc`

 For some word y, `N` started on 1^P 0 y halts within T steps with the output 1. 
