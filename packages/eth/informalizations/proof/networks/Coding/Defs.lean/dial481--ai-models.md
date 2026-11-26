---
{
  "module": "proof/networks/Coding/Defs.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/networks/Coding/Defs.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/networks/Coding/Defs.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # The printed objects, and Lean's as these with padding (definitions and statements only)

Section 6: «A setting z_a of node a is a bit string with one bit z_a[o] for each occurrence o in
cluster a, and S_a is the set of all these bit strings.» In the network on which the machines run
(`Eight.ViaGrouping.satNet`, on `Groundwork.Prog.Count.wordNet`) a setting has one bit for each
PLACE of a literal, 3 places per clause and m̄ clauses per cluster, and
W_a has one condition more: the bit at a place without a literal is 0. And: «a clause is a nonempty
set of literals, and a 3-CNF is a finite set of clauses with at most 3 literals each», where Lean's
end statement has lists (`Sat3.CNF`, `Sat3.Is3CNF`).
This file defines the printed objects in the words of the paper, without reference to Lean's, and
states that Lean's are these up to padding:
* `PaddingOf N₀ N pad`: the network N is the network N₀ with each setting z of a node a written as
  the string pad a z; on the settings of N that write no setting of N₀, W is 0; W, Ψ, f and the
  numbers c_{a,b} are carried over. Then both have the same value and the same total
  (`StPaddingValue`).
* `occNet g Φ`: the network of Φ with one bit per occurrence; `StOccNet`: `satNet g 3 Φ` is
  `occNet g Φ` with padding; `StOccNetCounts`: so its value is the number of satisfying assignments
  of the variables that occur.
* `ThreeCNF n`: a 3-CNF as a set of sets; `StSetForm`: Theorem 2 for these, whichever way the set is
  written as a list.
No proof of the main theorems uses this file: their machines run on the padded network.
Three choices that the paper leaves open are fixed here as in Lean's network: the clusters are
blocks of m̄ consecutive clauses; the occurrences of a variable are listed in reading order (by
clause, then by position in the clause); the tests between two clusters are listed in reading order
of their earlier occurrence.
(proof/networks/Eight/SecProof_NetworkDefs.lean has another definition called tests, a set of pairs
of places; `Coding.tests` is a list of pairs of occurrences.)
This file has no proofs. 

 ## Padding 

### `PaddingOf`

 The network N is the network N₀ with padded settings. 

### `PaddingOf.maps`

 a setting of N₀ is written by a setting of N, and different settings by different ones 

### `PaddingOf.off`

 a setting of N that writes no setting of N₀ has W = 0 

### `StPaddingValue`

 Padding changes neither the value nor the total. 

 ## The network of Φ, one bit per occurrence 

### `occIn`

 «An occurrence is a pair o = (E, ω) of a clause E ∈ Φ and a literal ω ∈ E, that is, one position
of one clause»: (number of the clause, position in the clause). For a clause that lists no literal
twice, positions and literals correspond; a clause of a list that repeats a literal has two
occurrences of it, which the paper's sets never have. All occurrences in the clauses number e₀, …,
e₀ + r − 1, in reading order. 

### `occOf`

 The occurrences in cluster a: the cluster holds the clauses number a·m̄, …, a·m̄ + m̄ − 1 (those
that exist), m̄ = ⌈m/g⌉. 

### `occAll`

 All occurrences in Φ. 

### `litOf`

 The literal at an occurrence. 

### `clusterOf`

 The cluster in which an occurrence lies. 

### `tests`

 «For each variable, list all its occurrences in Φ, across all clusters, in some order o₁, …, o_d
(any order will do); the pairs {o₁,o₂}, {o₂,o₃}, … of consecutive occurrences are the equality
tests»: (o, o') is a test if o' is the next occurrence of the variable of o in reading order. All
tests, in reading order of (o, o'). 

### `testsBetween`

 The tests with one occurrence in cluster a and the other in cluster b, in their order. For a =
b: the tests with both occurrences in cluster a. 

### `bitAt`

 z_a[o]: the bit of the setting z of cluster a at the occurrence o. 

### `isTrue`

 «call o = (E, ω) true if ω is positive and z_a[o] = 1, or ω is negative and z_a[o] = 0». 

### `restrict`

 z_a|_b: «the bits of z_a at their occurrences in cluster a», for the tests between the clusters
a and b, in the order of these tests. 

### `occNet`

 **The network of Φ** on [g], as printed: a setting of node a has one bit for each occurrence in
cluster a, and S_a is the set of all these strings; W_a is 1 exactly if every clause of cluster a
has a true occurrence and z_a[o] = z_a[o'] for every test with both occurrences in cluster a;
c_{a,b} is the number of tests between the clusters a and b;
Ψ_{a,b}(z_a, z_b) = [z_a|_b = z_b|_a], f_{a,b}(z_a, θ) = [z_a|_b = θ]. 

### `padOcc`

 The padding: the string of 3·m̄ bits with the bit z_a[o] at the place of the occurrence o =
(a·m̄ + r, j), which is place 3r + j, and 0 at the places without a literal. 

### `StOccNet`

 **Lean's network of Φ is the printed one with padding**, for g ≥ 1 clusters and clauses of at
most 3 literals. 

### `StOccNetIs`

 «The network of Φ is the following network on [g] with P = 6m̄ and B = 1 … Definition 2 holds:
Σ_{b ≠ a} c_{a,b} ≤ 2·3m̄ = P»: the printed network satisfies Definition 2 (all but (iii)) with the
printed parameters, for m ≥ 1. 

### `StOccNetSmall`

 «Their length is at most 3m̄ ≤ P» and «all values are 0 or 1». 

### `StOccNetCounts`

 **«Hence Z is the number of assignments of the variables occurring in Φ **«Hence Z is the number
of assignments of the variables occurring in Φ that satisfy Φ»**, and so Φ is satisfiable if and
only if Z &gt; 0, for the printed network. if and only if Z > 0**, for the printed network. 

### `StOccNetCountsOf`

 The count for the printed network is carried over from Lean's network, for which this
development proves it along the printed sentences («Every term of the value Z is 0 or 1. Each test
is checked exactly once … so a term is 1 exactly if all occurrences of each variable carry the same
bit and every clause has a true occurrence»: `Eight.network_value_eq`,
proof/networks/Eight/SecProof_Network.lean): padding does not change the value. These sentences are
not proved a second time for the printed network. 

### `StTests`

 «An occurrence lies in at most two tests. The total number of tests is the number of occurrences
minus the number of variables that occur, hence at most 3m − 1» (m ≥ 1, nonempty clauses of at most
3 literals). 

### `sixExample`

 Three clauses on three variables, each variable in all three clauses; with g = 3 every cluster
is one clause (m̄ = 1), and each of the three occurrences in the middle clause lies in two tests,
one to each of the other clusters. 

### `StRowSumReached`

 The footnote to «Their length is at most 3m̄ ≤ P»: «P is taken as large as 6m̄ because Σ_{b ≠ a}
c_{a,b} can reach 6m̄». An example in which it does, in the printed network and in Lean's. 

 ## Sets for lists 

### `ThreeCNF`

 «a clause is a nonempty set of literals, and a 3-CNF is a finite set of clauses with at most 3
literals each», on the variables x₀, …, xₙ₋₁. A literal is a variable with the value that makes it
true (`Sat3.Lit`). 

### `ThreeCNF.Satisfiable`

 Some assignment makes a literal of every clause true. 

### `Writes`

 The list of lists φ writes the set of sets Φ: every clause of Φ is written exactly once, in some
order of the clauses, with its literals in some order, each once. 

### `StWrites`

 Every 3-CNF can be written; and whatever writes it is an instance in the sense of the end
statement, has as many clauses, has no empty clause, and is satisfiable exactly if the 3-CNF is. 

### `StSetForm`

 **Theorem 2 in its decision form for 3-CNFs as sets**: for every δ > 0 there are one machine and
one constant such that for every 3-CNF Φ on n variables, in whichever way it is written on the tape,
the machine halts after at most c·2^{δn} steps and outputs whether Φ is satisfiable. 

### `StSetFormOf`

 It follows from Theorem 2 for lists. 

### `StCubic`

 Section 3, Conventions: «a 3-CNF is a set of clauses (Section 6), so m = O(n³)»: a 3-CNF on n
variables has at most 14n³ clauses. 
