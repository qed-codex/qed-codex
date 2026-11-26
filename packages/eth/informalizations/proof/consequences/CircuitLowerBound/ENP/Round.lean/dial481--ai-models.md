---
{
  "module": "proof/consequences/CircuitLowerBound/ENP/Round.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/consequences/CircuitLowerBound/ENP/Round.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/consequences/CircuitLowerBound/ENP/Round.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # The circuit lower bound for E^NP (Section 7): one round of the prefix search for the language L0

The language `L0` is decided by a prefix search with queries to SAT. In the restart form of E^NP an
ordinary machine is started on x and the answers so far (`ENP.roundInput`). This file has the
function `roundF` that such a
machine computes, as a function of its input word and a pad. With m = |x| and i the number that x
writes: as long as there are at most i answers, it returns the query «is `Phi m`, together with the
values found so far and 0 for the next
variable, satisfiable?»; after that it returns the result, the negation of answer number i.
The file proves: the input word is read correctly (`mL_roundInput`, `xW_roundInput`,
`aW_roundInput`); the code of formulas is one-to-one, so that a query asks what it is meant to ask
(`sat_encCnf`); with a pad of 2^(2m+4) units
nothing is cut off (`roundF_roundInput`); and `roundF` is polynomial-time in its input and the pad
(`roundF_polyT`). The functions G and fb are those of the interface statements `StCertTabF` and
`StFlip`. 

 ### The function 

### `mL`

 The numbers 0, …, m − 1, where m is the number of pairs 1b at the start of the word. 

### `mU`

 m in unary. 

### `xW`

 The word x. 

### `aW`

 The answers so far. 

### `eW`

 The logarithm of the length of the pad. 

### `PhiF`

 `Phi m`, for m in unary, written under a pad. 

### `encF`

 The code of a formula, with the variables cut off at the length of the pad. 

### `roundF`

 One round: the next query, or the result. 

 ### Reading the input word 

### `takeWhile_range`

 The first numbers that pass a test, if the test holds below m, fails at m, and m is in the
range. 

 ### The code of formulas is one-to-one 

### `sat_encCnf`

 The code of a formula is in SAT if and only if the formula is satisfiable. 

### `encF_eq`

 Under a pad that is at least as long as every variable is large, the code is not cut off. 

 ### Sizes 

### `length_tab_codeOf_le`

 The table number a has at most a clauses. 

### `nb_le`

 The number of a clause of the formula of the table of m, for variables of m bits, has at most 2m
bits. 

### `var_Phi_lt`

 The variables of `Phi m` have m bits. 

### `var_units_lt`

 The variables of `units w` are below the length of w. 

 ### Nothing is cut off 

### `PhiF_eq`

 With a pad of at least 2^(2m) units, `PhiF` writes `Phi m`. 

### `roundF_roundInput`

 What a round returns on x and at most 2^m answers, with a pad of at least 2^(2m+4) units, m = |x|. 

 ### Polynomial time 

### `roundF_polyT`

 One round is polynomial-time in the input word and the pad. 
