---
{
  "module": "proof/variables/VariableBound/Net/Val.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/variables/VariableBound/Net/Val.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/variables/VariableBound/Net/Val.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # Step 3: the value of the network of one profile

The plain functions `netD` present the network `netDN` (StPresents). The value of the network of the
profile y is the sum, over the pairs (ξ, P) of an assignment ξ and a set P of objects whose clauses
ξ violates, such that
P belongs to the profile y, of ∏_j σ_(|Π_j|), for F times (−1)^|Π₀| (StVal). This is the sentence of
Appendix D, Step 3, of the paper: «Hence the nonzero terms are the tuples (ξ, Π₀, …, Π_r), each
once, with the values in (65)». The steps: if the settings of two
nodes belong to the profile, Ψ is 1 if they give the same marks to every object with the test {a, b}
and 0 otherwise, because the position of a string determines it (StLab); «in a nonzero term the
marks of an object agree at
all nodes that it touches, because its tests form a path», so the settings at which all weights are
nonzero and all marks agree are exactly the settings of the pairs (ξ, P); «h(j) sees |Π_j|», because
every incidence of
check j touches h(j); and every marked clause is counted in the sign by its owner alone. 

 ### The lists of objects 

### `mem_tch`

 The list `tch g n D a` holds the places of the objects that touch the node a. 

### `nodup_tch`

 No object occurs twice in the list of the objects that touch a. 

### `linkB_iff`

 {a, b} with a < b is a test of the object e iff e touches a and b and no node between them. 

### `ownB_iff`

 The node a owns the object e iff e touches a and no smaller node. 

### `mem_tst`

 The list `tst g n D a b i` holds the places of the objects of kind i with the test {a, b}. 

### `nodup_tst`

 No object occurs twice in the list of the objects with the test {a, b}. 

### `tst_comm`

 The objects with the test {a, b} are those with the test {b, a}. 

### `mem_tch_of_mem_tst`

 An object with the test {a, b} touches a. 

 ### The settings of a pair (σ, P) 

### `st`

 The setting of the node a: the values of its variables, then the marks of the objects that touch
it. 

### `length_st`

 The setting of the node a has ⌈n/g⌉ value bits and one mark bit for each object that touches a. 

### `getD_st_lt`

 The value bit number r < ⌈n/g⌉ of the setting of the node a is the value of the variable a·⌈n/g⌉ +
r. 

### `mark_st`

 The setting of (σ, P) at the node a marks an object e that touches a iff e is a member of P. 

 ### The weight without the profile 

### `base`

 The value bits of variables numbered n or more are 0, and a marked object has all its literals
at a false. 

### `ownC`

 The number of marked objects of kind i that the node a owns, in the setting z. 

### `prof`

 The setting z of the node a has the numbers that the profile y prescribes. 

### `wz`

 ∏_(j : h(j) = a) σ_(q_j), times, for F only, (−1)^q, where q is the number of marked clauses
owned by a. 

### `WD_eq`

 The weight is `wz` if the setting is consistent and has the profile, and 0 otherwise. 

### `prof_iff`

 What `prof` says: for both kinds i, the node a owns μ_(a,i) marked objects, and for every other
node a' < g the string of the marks of the objects with the test {a, a'} has μ_(a,a',i) ones. 

 ### The network of one profile 

### `netDN_W`

 The weight W_a of the network of the profile y is `WD`. 

### `netDN_f`

 The factor f_(a,a')(z, θ) of the network of the profile y is 1 if θ is the label that z shows to
a', and 0 otherwise. 

### `netDN_S`

 The set S_a of the network of the profile y is the set of all words of ⌈n/g⌉ + (number of
objects that touch a) bits. 

### `mu_comm`

 μ_(a,a',i) = μ_(a',a,i). 

### `capD_comm`

 c_(a,a') = c_(a',a). 

### `netDN_lab`

 The labels of the pair {a, a'} in the network of the profile y are all words of c_(a,a') bits. 

### `sum_words_eq`

 The sum over all labels of length c of «A is the label and B is the label». 

### `Ψ_eq`

 Ψ_(a,a') for two different nodes whose settings z, z' belong to the profile y: 1 if they give
the same mark to every object with the test {a, a'}, and 0 otherwise. Needs that the labels
determine the strings (StLab). 

 ### The quantities of the profile at the settings of (σ, P) 

### `length_filter_eq_card`

 The length of a filtered list without repetitions is the number of elements of the set that it
lists. 

### `str_st`

 The string of the marks that the setting of (σ, P) at a gives to the objects of kind i with the
test {a, a'}: the bit of an object says whether it is a member of P. 

### `count_str_st`

 That string has as many ones as P has members of kind i with the test {a, a'}. 

### `ownC_st`

 In the setting of (σ, P), for a set P of places of objects, the number of marked objects of kind
i that a owns is the number of members of P of kind i that a owns. 

### `qj_st`

 «h(j) sees |Π_j|»: at the home of check j, the number of marked incidences of check j in the
setting of (σ, P) is the number of members of P that are incidences of check j, for a set P of
places of objects. 

### `prof_st_iff`

 For a set P of places of objects: the settings of (σ, P) at all nodes have the numbers of the
profile y exactly if P belongs to y. 

 ### Every object has one owner 

### `exists_owner`

 Every object has an owner, if g > 0 and the data are well formed (WfD). 

### `owner_unique`

 An object has at most one owner among the nodes below g. 

### `sum_owner`

 Counting the members of P with a property p owner by owner counts each once, if g > 0, the data
are well formed (WfD) and P is a set of places of objects. 

### `prod_wz_st`

 The weights of the nodes at the settings of (σ, P) multiply to the value of the term of P in
display (65), if g > 0, the data are well formed (WfD) and P is a set of places of objects. 

 ### Good settings are the settings of the pairs (σ, P) 

### `base_iff`

 What `base` says: a value bit of a variable with a number ≥ n is 0, and every object that
touches a is unmarked or has all its literals at a false. 

### `vio_iff`

 σ violates the clause C iff it makes all literals of C false. 

### `Gd`

 The family z of settings is good: at every node `base` holds (the value bits of variables
numbered n or more are 0, no marked object has a true literal there), and any two nodes a < a' give
the same marks to the objects with the test {a, a'}. 

### `qv_pos`

 A node holds at least one variable, if there is a node and a variable: ⌈n/g⌉ > 0 for g > 0 and n > 0. 

### `lit_lt`

 For well-formed data (WfD), the variables of the clause of an object are below n. 

### `exists_lit`

 For well-formed data (WfD), the clause of an object has a literal. 

### `st_good`

 The settings of (σ, P) are good if g > 0, the data are well formed (WfD), σ is false at all
numbers ≥ n, and σ violates the clauses of all members of P. 

### `ext_of_lt`

 The assignment σ of the n variables, continued to all numbers: at x < n it is σ. 

### `ext_of_le`

 The assignment σ of the n variables, continued to all numbers: at x ≥ n it is false. 

### `st_inj`

 The settings determine σ and P: «each once». Needs g > 0, well-formed data (WfD), and that P and
P' are sets of places of objects. 

### `mark_eq`

 «In a nonzero term the marks of an object agree at all nodes that it touches, because its tests
form a path»: in a good family z of settings, an object e has the same mark at any two nodes that it
touches. 

### `ext_getD`

 Two words of the same length with the same bits are equal. 

### `getD_st_ge`

 The mark bit number t of the setting of (σ, P) at a says whether the object number t in the list
of the objects that touch a is a member of P. 

### `mark_getElem`

 The mark of the object number t in the list of the objects that touch a is the bit number ⌈n/g⌉ +
t of the setting. 

### `st_surj`

 Every good family of settings of the right lengths is the family of the settings of some (σ, P),
and σ violates the clauses of all members of P: «all literals of a marked clause are false, so Π₀ ⊆
V(ξ) and Π_j ⊆ V_j(ξ)». Needs g > 0 and well-formed data (WfD). 

### `sum_good`

 A sum over the good families of settings is a sum over the pairs (σ, P) of an assignment and a
set of objects whose clauses it violates, if g > 0 and the data are well formed (WfD). 

 ### The value of the network of one profile 

### `term_eq`

 One term of the value: the product of the weights at a good family of settings that has the
numbers of the profile, and 0 at every other family. Needs that the labels determine the strings
(StLab). 

### `netVal`

 The value of the network of the profile y is the sum, over the assignments σ and the sets P of
objects whose clauses σ violates, of the term of P if P belongs to y. Needs that the labels
determine the strings (StLab), g > 0 and well-formed data (WfD). 

### `stVal`

 Step 3: «Hence the nonzero terms are the tuples (ξ, Π₀, …, Π_r), each once, with the values in
(65)», for the network of one profile y, admissible or not. Hypotheses: g > 0; ψ has clauses of 1 to
k literals on variables
below n and the checks are lists without repetition of numbers of clauses (WfD); the labels
determine the strings (StLab). 

### `stPresents`

 The plain functions `netD` present the network `netDN`, in every context. 
