---
{
  "module": "proof/variables/VariableBound/Net/Tuples.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/variables/VariableBound/Net/Tuples.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/variables/VariableBound/Net/Tuples.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # Step 3: sets of marked objects and tuples (Π₀, …, Π_r)

Step 3: «So the term is given by ξ and the sets Π₀ and Π_j of the clauses E for which E,
respectively (E, j), is marked; … Π₀ ⊆ V(ξ) and Π_j ⊆ V_j(ξ)».

A set P of positions of objects is cut into the sets `sl D 0 0 P` = Π₀ (the clauses E that are
members of P) and `sl D 1 j P` = Π_j (the clauses E whose incidence (E, j) is a member of P); `back`
puts a tuple together
again. For a fixed ξ this is a bijection between the sets P of objects with violated clauses and the
tuples with Π₀ ⊆ V(ξ) and Π_j ⊆ V_j(ξ); it keeps the numbers |Π₀|, |Π_j|, and hence the limits and
the value of the term
(`sum_sets`). Summed over ξ this is `stTuples`. `stChks`: for well-formed data, the list of checks
as sets has the numbers r, |Λ_j| and load(E) of the list of checks as lists. 

 ### The list of checks as sets 

### `mem_setD`

 A clause is in the set of a list of numbers iff its number is in the list. 

### `card_setD`

 The set of a list without repetition of numbers below m has as many members as the list. 

### `getD_chks`

 Check number j as a set is the set of check number j as a list. 

### `length_chks`

 The list of sets has r members. 

### `stChks`

 For well-formed data D (a formula Φ and a list of checks given as lists of clause numbers), the
list of sets has the numbers of the list of lists: r, |Λ_j| and load(E). 

 ### Cutting a set of objects into a tuple, and back 

### `sl`

 The clauses E such that the object (κ, E, j) is a member of P: Π₀ for (κ, j) = (0, 0), Π_j for κ = 1. 

### `back`

 The set of the objects E with E ∈ S₀ and (E, j) with E ∈ S j. 

### `mem_sl`

 E is in the part (κ, j) of P iff the object (κ, E, j) is a member of P. 

### `mem_back`

 The members of the set put together from (S₀, S) are the objects E with E ∈ S₀ and (E, j) with E
∈ S j. 

### `third_zero`

 An object of kind 0 is a triple (0, e, 0): the third entry of an object o (a place below the
number of objects) of kind 0 is 0. 

### `card_sl`

 For well-formed data and a set P of positions of objects: there are as many clauses E with (κ,
E, j) in P as members of P of kind κ with third entry j. 

### `card_kP_zero`

 |Π₀| is the number of members of P of kind 0, for well-formed data (WfD) and a set P of places
of objects. 

### `card_chP`

 |Π_j| is the number of members of P that are incidences of check j, for well-formed data (WfD)
and a set P of places of objects. 

### `card_kP_one`

 |Π₁| + … + |Π_r| is the number of members of P of kind 1, for well-formed data (WfD) and a set P
of places of objects. 

### `back_sl`

 Cutting and putting together again gives back a set P of positions of objects, for well-formed
data. 

### `sl_zero_back`

 The part Π₀ of the set put together from (S₀, S) is S₀. 

### `sl_one_back`

 The part Π_j of the set put together from (S₀, S) is S j, if S j ⊆ Λ_j. 

### `mem_tup`

 S is a tuple (Π₁, …, Π_r) of the display after Lemma 12 (the right sides for X and F) iff Π_j ⊆
Λ_j ∩ V(ξ) for all j and |Π₁| + … + |Π_r| ≤ M. 

### `mem_Vof`

 E ∈ V(ξ) iff ξ violates the clause number E. 

### `mem_vset`

 An object is in `vset` iff the assignment violates its clause. 

### `sl_subset_Vof`

 If ξ violates the clauses of all members of P, then ξ violates the clauses of every part of P. 

### `sl_one_subset`

 Π_j ⊆ Λ_j, for a set P of places of objects. 

### `back_subset_vset`

 If ξ violates all clauses of S₀ and of the S j, then ξ violates the clauses of all members of
the set put together. 

### `vset_subset`

 The members of `vset` are positions of objects. 

 ### The sum for one ξ 

### `wt_eq`

 The value of the term of P, by the numbers |Π₀| and |Π_j|, for well-formed data (WfD) and a set
P of places of objects. 

### `sum_sets`

 Step 3, «the term is given by ξ and the sets Π₀ and Π_j»: for well-formed data and one ξ, the
sum of the terms of the sets P of objects with violated clauses, within the limits, is the sum over
the tuples
(Π₀, …, Π_r) of the display after Lemma 12. 

### `stTuples`

 Step 3: for well-formed data D, the sum over ξ and the sets P of objects with violated clauses,
within the limits |Π₀| = n̄ + 1 (for F: ≤ n̄) and |Π₁| + … + |Π_r| ≤ M, is the right side of the
display after Lemma 12 (for X, resp. F). 
