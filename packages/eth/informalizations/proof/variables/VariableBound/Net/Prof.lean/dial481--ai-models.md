---
{
  "module": "proof/variables/VariableBound/Net/Prof.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/variables/VariableBound/Net/Prof.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/variables/VariableBound/Net/Prof.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # Step 3, «Profiles»: every set of marked objects has exactly one profile

A set P of (positions of) objects stands for a tuple (Π₀, …, Π_r). It determines, for each kind κ,
how many of its members each node owns (`oc`) and how many lie among the objects with the test {a,
b}
(`pw`). These numbers are the digits of exactly one number y below `nPr` whose unused places are 0
(`adm_match_iff`, with `Mark.Prof.sum_digit_eq` of proof/rates/PaddedDescent/F/MarkProf.lean).

The sentence of the text «Every nonzero term belongs to exactly one profile, which has Σ_a μ_(a,0) = |Π₀|,
Σ_a μ_(a,1) = Σ_j |Π_j|, μ_(a,b,κ) ≤ t_(a,b,κ) and Σ_({a,b}) μ_(a,b,κ) ≤ (k − 1 + κ)·Σ_a μ_(a,κ)» is
proved, with Σ_j |Π_j| read as the number of marked incidences,
in two forms: for the numbers of P (`sum_oc`, `pw_le_length`, `sum_pw_le`) and for a profile y to
which P belongs (`tot_of_match`, `mu_le_of_match`, `totP_le_of_match`). An object has one owner; an
object of kind κ touches at
most k + κ nodes and so has at most k − 1 + κ tests (`card_links_le`). So the profile of P is
admissible iff |Π₀| = n̄ + 1 (for F: ≤ n̄) and Σ_j |Π_j| ≤ M: this is `stProf`, the interface
statement `StProf`. The number of
profiles is `stNPr`. No setting of the network occurs in this file.

Twin of proof/rates/PaddedDescent/F/MarkProf.lean (layers of clauses in place of kinds of objects;
there every clause has at most k − 1 tests and every layer has the same cap). 

 ### Digits 

### `mu_comm`

 The number that the profile prescribes for two nodes does not depend on their order: μ_(a,b,κ) =
μ_(b,a,κ). 

### `mu_of_le`

 For a ≤ b the number that the profile prescribes is the digit at the place (a·g + b)·2 + κ. 

### `pw_comm`

 The number of members of P with the test {a, b} does not depend on the order of a and b. 

### `tot_eq`

 `tot` is Σ_a μ_(a,κ), as a sum over a finite set. 

### `totP_eq`

 `totP` is Σ_({a,b}) μ_(a,b,κ), as a sum over the pairs a < b < g. 

 ### Touched nodes, owners, tests 

### `tset`

 The nodes below g that the object o touches. 

### `mem_tset`

 Membership in `tset`. 

### `tset_nonempty`

 If 0 < g and the data are well formed, an object o (o below the number of objects) touches some
node below g. 

### `card_tset_le`

 If the data are well formed, an object o (o below the number of objects) of kind κ touches at
most k + κ nodes. 

### `ownB_iff`

 What `ownB` says: a is touched, and no smaller node is. 

### `linkB_iff`

 What `linkB` says: a < b are touched, and no node between them is. 

### `card_owner`

 If 0 < g and the data are well formed, exactly one node below g owns an object o (o below the
number of objects). 

### `card_links_le`

 Step 3: «an object of kind κ ∈ {0, 1} has at most k − 1 + κ tests», for an object o (o below the
number of objects), if 0 < g and the data are well formed. 

 ### The facts of the text, for the numbers of a set P of objects 

### `sum_oc`

 Step 3, «Profiles»: Σ_a μ_(a,κ) is the number of marked objects of kind κ, that is |Π₀| for κ =
0 and the number of marked incidences for κ = 1. Here for the numbers of P: the members of kind κ
that the nodes
own add up to the members of kind κ. Needs 0 < g, well-formed data, and that P is a set of positions
of objects. 

### `mem_tst`

 Membership in `tst` for a < b. 

### `sum_pw_le`

 Step 3, «Profiles»: Σ_({a,b}) μ_(a,b,κ) ≤ (k − 1 + κ)·Σ_a μ_(a,κ). Here for the numbers of P:
the members of kind κ with the test {a, b}, summed over the pairs a < b < g, are at most k − 1 + κ
times the
members of kind κ. Needs 0 < g, well-formed data, and that P is a set of positions of objects. 

### `pw_le_length`

 Step 3, «Profiles»: μ_(a,b,κ) ≤ t_(a,b,κ). Here for the numbers of P: at most as many members of
P have the test {a, b} as there are objects of kind κ with this test. 

 ### The facts of the text, for a profile to which P belongs 

### `tot_of_match`

 Step 3, «Profiles»: the profile y of a term has Σ_a μ_(a,κ) equal to the number of members of P
of kind κ, that is |Π₀| for κ = 0 and the number of marked incidences for κ = 1. Needs 0 < g,
well-formed data, that P is a set of positions of objects,
κ < 2, and that P belongs to y. 

### `mu_le_of_match`

 Step 3, «Profiles»: the profile y of a term has μ_(a,b,κ) ≤ t_(a,b,κ), for nodes a ≠ b below g
and κ < 2, if P belongs to y. 

### `totP_le_of_match`

 Step 3, «Profiles»: the profile y of a term has Σ_({a,b}) μ_(a,b,κ) ≤ (k − 1 + κ)·Σ_a μ_(a,κ).
Needs 0 < g, well-formed data, that P is a set of positions of objects, κ < 2, and that P belongs to
y. 

 ### The profile of a set of objects 

### `adm_iff`

 What `admD` says. 

### `tgt`

 The digit that the profile of P has at the place q. 

### `tgt_place`

 The digit of P at the place (a·g + b)·2 + κ, for b < g and κ < 2. 

### `tgt_le`

 The digits of a set P of positions of objects are at most the number I + m of objects. 

### `adm_match_iff`

 If 0 < g, the data are well formed and P is a set of positions of objects: y is an admissible
profile to which P belongs iff |Π₀| = n̄ + 1 (for F: ≤ n̄), Σ_j |Π_j| ≤ M, and y has the digits of
P. 

### `stProf`

 `StProf`. Step 3, «Profiles»: «every nonzero term belongs to exactly one profile», and that
profile is admissible iff |Π₀| = n̄ + 1 (for F: ≤ n̄) and Σ_j |Π_j| ≤ M. In Lean: for g > 0,
well-formed data (WfD) and a set P of places of objects, the number of admissible profiles y < `nPr`
to which P belongs is 1 if P is within these limits, and 0 otherwise. 

 ### The number of profiles 

### `length_objs_le`

 Step 3: «there are I ≤ r·s̄ incidences»: if every check has at most s clauses, there are at most
r·s + m objects. 

### `stNPr`

 `StNPr`. Step 3, «Profiles»: «of which there are at most (I + m + 1)^(2(g² + g))»: the number
`nPr` of the numbers y that are tried as profiles, the admissible ones among them, is at most this;
and I + m ≤ r·s + m. Needs that every check has at most s clauses. 
