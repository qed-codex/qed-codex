---
{
  "module": "proof/networks/Groundwork/Net/Defs.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/networks/Groundwork/Net/Defs.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/networks/Groundwork/Net/Defs.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 Instances and their value Z (a sum, over all labellings of the edges of a complete graph, of a
product of one tensor per node), networks and their value, merging the nodes of a
network into classes, and the passage from a network to an instance.
Definitions only; the theorems are in Groundwork.Net.Calculus and Groundwork.Net.Net.

Conventions. Nodes: a finite linearly ordered type J. An unordered pair {a,b} of distinct nodes is
named by the
ordered pair (min a b, max a b), written pr a b. Tuples indexed by a subset of an index type are
total functions
that take a fixed default value off the subset, so that all index sets are Finsets of plain function
types. 

### `pairs`

 The pairs a < b. 

### `pr`

 The name of the unordered pair {a,b}. 

### `tuples`

 Tuples (t i) with t i ∈ T i where P i holds and t i = d elsewhere. 

 ### Instances 

### `Inst`

 A (J,A)-instance: R v reads the labels of the edges at v, as a function w ↦ label of {v,w};
at w = v it is always handed the default label (see Z). The problem on K nodes with λ-bit labels on
the edges (the (K,λ)-clique of
Definition 3 in the paper): J = Fin K, card A = 2^λ, and R v is the tensor W_v. 

### `labellings`

 The labellings of the edges of the complete graph on J: functions on J × J, free at a < b, equal
to d elsewhere. 

### `star`

 Λ_v: the labelling Λ on the edges at v. 

### `Inst.Z`

 Z(R) = Σ_Λ ∏_v R_v(Λ_v). 

### `Inst.pad`

 Padding to a larger alphabet: labels in A' are read through dec on the set D, and the value is 0
if a label at v lies
outside D. 

 ### Networks 

### `Network`

 A network on J with states in σ and labels in τ. Only Θ a b with a < b is used (see lab); f a b
is the factor on
a's side of the pair {a,b}. The interaction is defined by its factorisation (see Ψ). c is the table
of capacities: plain
numbers, which `value` does not read and on which the structure puts no condition; `U` reads only c,
and `Shaped.card_lab`
asks for at most 2^c labels. 

### `lab`

 The label set of the unordered pair {a,b}. 

### `Ψ`

 Ψ_ab(z,z') = Σ_θ f_ab(z,θ) f_ba(z',θ). 

### `value`

 Z = Σ_z ∏_a W_a(z_a) ∏_{a<b} Ψ_ab(z_a,z_b). 

### `U`

 U = Σ_{a≠b} c_ab, over ordered pairs. 

### `Shaped`

 The shape of a network «of size P»: few states, symmetric capacities that sum to at most P at
every node,
and at most 2^c labels on a pair of capacity c. No bound on the values. 

### `Sized`

 «Network of size P» all of whose values are bounded by 2^B. 

### `merge`

 Merging along χ : J → J'. A state of the class G is a function on J: a state of a at the members
a of G, s₀ elsewhere.
A label of the classes G < G' is a function on J × J: a label of {a,b} at (a,b) with a in G and b in
G', t₀ elsewhere. 

### `toInst`

 From a network to an instance over A, padding of the label sets included: a label x ∈ A of the
pair {a,b} stands for the label
dec (min a b) (max a b) x of the network if x ∈ D (min a b) (max a b), and the factors vanish at all
other x.
N_a(θ) = Σ_z W_a(z) ∏_{b≠a} f_ab(z,θ_b). 
