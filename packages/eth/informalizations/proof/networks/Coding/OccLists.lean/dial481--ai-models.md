---
{
  "module": "proof/networks/Coding/OccLists.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/networks/Coding/OccLists.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/networks/Coding/OccLists.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # Occurrences and places

Section 6: «An occurrence is a pair o = (E, ω) of a clause E ∈ Φ and a literal ω ∈ E, that is, one
position of one clause.» Lean's network (`Groundwork.Prog.Count.wordNet`) numbers PLACES: 3 for each
clause, whether or not a literal stands there. The occurrence (e, j) stands at the place 3e + j
(`place`).
For clauses of at most 3 literals this map is increasing for the reading order and goes onto the
places with a literal. So it carries «the pairs {o₁,o₂}, {o₂,o₃}, … of consecutive occurrences are
the equality tests» (`Coding.tests`) to Lean's links (`linkB`): `mem_tests_iff`.
The file begins with five small facts: a product of increasing lists is increasing in the order of
the dictionary; two increasing lists with the same members are equal; in an increasing list the
order of the positions is the order of the values; two bit strings with the same bits are equal; and
e / μ = a exactly if e lies in the a-th block of μ numbers. `import all StepMachines.Prog.CountNet`
gives access to `slotsOf_eq`, which is not public. 

 ### Lists 

### `lexLt`

 The order of the dictionary on pairs of numbers. 

### `pairwise_product`

 The product of two lists that are increasing for r₁ and r₂ is increasing for the order of the
dictionary. 

### `eq_of_lex`

 Two lists of pairs of numbers that are increasing in the order of the dictionary and have the
same members are equal. 

### `idxOf_lt_iff`

 In a list along which f increases, the order of the positions is the order of the values of f. 

### `ext_getD`

 Two bit strings of the same length with the same bits are equal. 

### `div_eq_iff_block`

 e lies in the a-th block of μ numbers. 

 ### Occurrences 

### `place`

 The place of an occurrence: 3 places for each clause. 

### `place_div_mod`

 The place of the pair (i / 3, i % 3) is i. 

### `getD_nil_of_le`

 Beyond the last clause, Φ.getD e [] is the empty list. 

### `length_getD_le`

 Every clause, and the empty list beyond the last clause, has at most 3 literals. 

### `mem_occIn`

 (e, j) is an occurrence in the clauses number e₀, …, e₀ + r − 1 if e is one of these numbers and
j is a position of clause e. 

### `mem_occAll`

 (e, j) is an occurrence in Φ if j is a position of clause e. 

### `fst_lt_of_mem_occAll`

 The clause of an occurrence is one of the clauses of Φ. 

### `pairwise_occIn`

 The reading order of the occurrences is the order of their places. 

### `nodup_occIn`

 No occurrence is listed twice. 

 ### Literals at places 

### `litAt_eq`

 What stands at place i: the literal of the occurrence (i / 3, i % 3), if this is one. 

### `litAt_place`

 At the place of an occurrence stands its literal. 

### `varAt_place`

 At the place of an occurrence stands the variable of its literal. 

### `mem_occAll_of_varAt`

 A place with a variable is the place of an occurrence. 

### `place_lt`

 The place of an occurrence is one of the 3m places of Φ. 

 ### Tests and links 

### `linkB_iff_places`

 Lean's link between two places, in words. 

### `mem_tests_iff`

 «the pairs {o₁,o₂}, {o₂,o₃}, … of consecutive occurrences are the equality tests» (Section 6):
(o, o') is a test exactly if Lean's network has a link from the place of o to the place of o'. 
