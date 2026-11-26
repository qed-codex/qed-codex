---
{
  "module": "proof/networks/Eight/ViaGrouping/Table.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/networks/Eight/ViaGrouping/Table.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/networks/Eight/ViaGrouping/Table.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # Lemma 1 along the printed proof: the tables W̃_γ

This file proves two of the steps stated in proof/networks/Eight/ViaGrouping/Defs.lean, for a
network N as in Definition 2 (except that its procedures are not given B) and a grouping, given by
its number x.
* `stTable`, the first two sentences of the paragraph «Cost»: «The sum defining W̃_γ(Θ) has at most
  (2^P)^{2g/K} = 2^{2gP/K} terms, each a product of at most g² values. So |W̃_γ| < 2^{B'} with B' =
  ⌈2gP/K⌉ + g²B, and one entry costs
  2^{2gP/K}·poly(P + B)·τ operations.» The procedure is `tableM`, which calls the four procedures of
  Definition 2(iii); in particular Ψ_{a,b} inside a group costs one call, so there is no factor 2^P.
* `stValue`, the end of the paragraph «The algorithm»: «… so the value equals Z».

The order of the file:
1. a network in the sense of `IsNetworkP` gives a network in the sense of `Paper.IsNetwork`
   (`Table.isPaperNetwork`);
2. the parts z_a and θ_{a,b} that are cut out of a setting of the group and out of Θ have the
   lengths P_a and c_{a,b} (`Table.length_zA`, `Table.length_labOf`);
3. a procedure behind the test for membership in S_a (`Table.gate_runs`), and the integers that the
   factors return (`Table.f_toPaperNetwork`, `Table.psi_toPaperNetwork`, `Table.sum_valF`);
4. one factor (`Table.termP_runs`), one entry (`Table.tableM_runs`), its size
   (`Table.abs_entry_le`), one constant for K and g (`Table.tableM_runs_coarse`);
5. `stTable` and `stValue`.

The integer that `tableM` returns is `mergedVal` (proof/machines/StepMachines/Prog/NetProg.lean) for
the network `N.toPaperNetwork`: strings outside S_a give the factor 0, and on settings the procedure
for Ψ_{a,b} returns Σ_θ f_{a,b}·f_{b,a}, because (f_{a,b}, f_{b,a}) is a factorization of Ψ_{a,b}.
So that this integer is the entry of W̃_γ, and that the clique of the groups has the value Z, are
proved elsewhere (`toInst_eq_mergedVal`, `Paper.grouped_value`).

Different from the paper: 2g/K is rounded down, which (G1) allows, since the number of nodes of a
group is an integer; entries are «at most 2^{P·⌊2g/K⌋ + g²B}», as the definition of query access in
the namespace `Paper` asks; this exponent is at most the B' = ⌈2gP/K⌉ + g²B of the paper
(`Cost.le_Bp` in Main.lean). 

 ## 1. From `IsNetworkP` to `Paper.IsNetwork` 

### `isNetwork`

 A network in the sense of `IsNetworkP` is a network in the sense of Definition 2 once the
procedures are told B. 

### `isPaperNetwork`

 The network `N.toPaperNetwork` with the procedures `Np.toPaperNetwork` is a network in the sense
of `Paper.IsNetwork` with the same P and B. (These procedures do not depend on what is given for B.) 

### `cap_symm`

 The numbers c_{a,b} that are given are symmetric. 

 ## 2. The parts of a setting of a group and of Θ 

### `mem_members`

 The nodes of the group G of the grouping number x: the a < g whose digit in x is G. 

### `sum_map_le`

 A sum of numbers that are at most M is at most their number times M. 

### `natAbs_le`

 |z| ≤ 2^n, said of the natural number `z.natAbs`. 

### `stLen_le`

 «at most (2^P)^{2g/K} terms»: a setting of a group with at most m nodes has at most P·m bits,
since P_a ≤ P. 

### `length_zA`

 The part z_a of the setting number y of the group G has P_a bits. 

### `length_lAt`

 The block of the pair p in a string with at least Y_{G,G'} bits has c_p bits. 

### `mem_prs`

 A pair of a node of G and a node of G' is in the list of the pairs that have a block. 

### `length_labOf`

 «let θ_{a,b} ∈ {0,1}^{c_{a,b}} consist of the bits of Θ(χ(b)) in the block of {a, b}»: it has
c_{a,b} bits, if Y_{γ,γ'} ≤ β for all γ ≠ γ' and every Θ(γ') has β bits. 

### `size_query_le`

 The size of a well-formed query. 

 ## 3. A procedure behind the test for membership, and the integers that the factors return 

### `gate_runs`

 Test z ∈ S_a, then run M or return 0. If M takes at most t ≥ τ steps on states of size at most
S' ≥ S whenever z is a setting, then the whole takes at most 2t + 1 steps. 

### `f_toPaperNetwork`

 The factor f_{a,b}(z, θ) of `N.toPaperNetwork`, for a ≠ b and θ of c_{a,b} bits: [z ∈
S_a]·f_{a,b}(z, θ). 

### `psi_toPaperNetwork`

 The Ψ_{a,b} defined from the factors of `N.toPaperNetwork` is [z ∈ S_a][z' ∈ S_b]·Ψ_{a,b}(z,
z'). 

### `sum_valF`

 The sum over the 2^{c_{a,b}} strings θ by which `termVal` is defined inside a group is the
Ψ_{a,b} of `N.toPaperNetwork`. 

 ## 4. One factor, one entry 

### `termP_runs`

 One of the g² factors of a term of W̃_γ(Θ). The index i < g·g stands for the pair of nodes (a,
b) = (i / g, i % g). The factor is 1, or [z_a ∈ S_a]·W_a(z_a), or [z_a ∈ S_a][z_b ∈
S_b]·Ψ_{a,b}(z_a, z_b), or [z_a ∈ S_a]·f_{a,b}(z_a, θ_{a,b}).
It costs at most 4τ + 3 steps (two tests and one call, in the case of Ψ) and is at most 2^B in
absolute value. 

### `tableM_runs`

 «The sum defining W̃_γ(Θ) has at most (2^P)^{2g/K} terms, each a product of at most g² values …
and one entry costs 2^{2gP/K}·poly(P + B)·τ operations», with explicit numbers: if every group has
at most m nodes and Y_{γ,γ'} ≤ β, then `tableM` answers a well-formed
query (β bits for every other group) within 2^{Pm}·(g²(4τ + 4) + 1) steps. 

### `abs_entry_le`

 «… at most (2^P)^{2g/K} = 2^{2gP/K} terms, each a product of at most g² values. So |W̃_γ| <
2^{B'} with B' = ⌈2gP/K⌉ + g²B»: if every group has at most m nodes, an entry is at most 2^{Pm +
g²B} in absolute value. 

### `tableM_runs_coarse`

 The bounds of `tableM_runs` with one constant c₁ that depends on K and g only: «one entry costs
2^{2gP/K}·poly(P + B)·τ operations». For a grouping whose groups have at most m ≤ 2g nodes, with
Y_{γ,γ'} ≤ β ≤ 2gP: at most c₁·2^{Pm}·τ steps on states of size at most
S + c₁·(size c + P + B)^{c₁}. 

### `lbLen_eq_Y`

 Y_{γ,γ'} as the programs compute it (a sum over a list of pairs of numbers) is the Y_{γ,γ'} of
the paper. 

 ## 5. The two steps 

### `stTable`

 **«Cost», first two sentences.** «The sum defining W̃_γ(Θ) has at most (2^P)^{2g/K} = 2^{2gP/K}
terms, each a product of at most g² values. So |W̃_γ| < 2^{B'} with B' = ⌈2gP/K⌉ + g²B, and one
entry costs 2^{2gP/K}·poly(P + B)·τ operations.»
Different from the paper: ⌊2g/K⌋ nodes in a group, so P·⌊2g/K⌋ in place of 2gP/K; «at most 2^{B'}»
in place of «below 2^{B'}». 

### `stValue`

 **«… so the value equals Z»** (end of the paragraph «The algorithm»): the (K, L)-clique with the
tables W̃ has the value of the network, if Y_{γ,γ'} ≤ L. Same as in the paper, except that the value
of the (K, L)-clique is written with one string per edge (`Paper.cliqueValue`). 
