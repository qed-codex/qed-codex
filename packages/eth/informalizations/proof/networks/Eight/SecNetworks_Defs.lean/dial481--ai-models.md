---
{
  "module": "proof/networks/Eight/SecNetworks_Defs.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/networks/Eight/SecNetworks_Defs.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/networks/Eight/SecNetworks_Defs.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # Section 3 «Networks»: Definitions 2 and 3, and the counts of «A good grouping exists» (definitions and statements only)

The file proof/networks/Paper/SecNetworks_Networks.lean states Definitions 2 to 4 in the model of
the algorithms of this development: Ψ is defined from its factorization, S_a is all of {0,1}^{P_a},
values are «at most 2^B», a query costs t steps.
This file states Definitions 2 and 3 as the paper prints them: a network has the sets S_a, the
functions W_a and Ψ_{a,b}, the numbers c_{a,b} and the factorizations (f_{a,b}, f_{b,a}) as separate
data; S_a is a subset of {0,1}^{P_a}; values are
«below 2^B»; four procedures decide membership in S_a and compute W_a, Ψ_{a,b}, f_{a,b}; the (K,
λ)-clique is such a network.

What remains of the model of this development, here too: the node set is Fin g (the paper: [g]);
«operations» are steps of step machines (`Paper.StepMachine`); a bound S on the size of the states
is carried along; procedures get a context c, which
stands for whatever the calling algorithm holds in memory. This file has no proofs. 

 ## Definition 2: a network with parameters P, B, τ 

### `Net`

 The data of a network on the node set [g] (Definition 2): for each node a the length P_a of its
settings, the set S_a of its settings and the function W_a; for each pair of nodes the function
Ψ_{a,b}, the number c_{a,b} of shared bits, and the functions f_{a,b}, f_{b,a} of a factorization.
Settings and indices θ are bit strings, written as lists. 

### `value`

 The value Z = Σ_z ∏_a W_a(z_a) ∏_{{a,b}} Ψ_{a,b}(z_a, z_b); z runs through all choices of one
setting z_a ∈ S_a for each node, the second product through the pairs a < b. 

### `U`

 The total U = Σ_{(a,b) : a ≠ b} c_{a,b}, a sum over ordered pairs. 

### `Is`

 **Definition 2**, all but (iii): N is a network on [g] with parameters P, B. 

### `Is.len_S`

 the settings of a are bit strings of one fixed length P_a ≤ P 

### `Is.Ψ_symm`

 Ψ_{b,a}(z_b, z_a) = Ψ_{a,b}(z_a, z_b) 

### `Is.fact`

 (f_{a,b}, f_{b,a}) is a factorization of Ψ_{a,b} through c_{a,b} bits 

### `Is.i`

 (i) 

### `Is.ii_W`

 (ii) 

### `PsiQ`

 A query for a value of Ψ: ((a, b), (z, z')). 

### `Procs`

 What an algorithm is given of a network (Definition 2(iii)): the numbers P, B, P_a, c_{a,b}, and
four procedures: membership in S_a, W_a, Ψ_{a,b}, f_{a,b}. All may depend on a context c. 

### `Procs.Give`

 **Definition 2(iii)**: in the context c the procedures give the numbers P, B, P_a, c_{a,b} of N,
decide membership in S_a for strings of P_a bits, and compute every value of W_a, Ψ_{a,b}, f_{a,b},
each within τ steps on states of size at most S. 

### `IsNetwork`

 **Definition 2.** N is a network on [g] with parameters P, B, τ, given by the procedures Np in
the context c. 

### `NetAlg`

 An algorithm for networks in this form: from the procedures a computation on contexts. 

### `Procs.Keeps`

 The lengths P_a and c_{a,b} are given in unary and the four procedures have polynomial-time
steps. 

 ## Definition 3: the (K, λ)-clique as a network 

### `place`

 The place of the node w' among the K − 1 nodes other than w. 

### `copyAt`

 z_w(w'): the copy, held at w, of the string on the edge {w, w'}; a setting z_w is the
concatenation of its K − 1 strings of λ bits. 

### `clique`

 **Definition 3.** The (K, λ)-clique with tables W_1, …, W_K: S_w = ({0,1}^λ)^{K−1}, encoded by
concatenation, so P_w = (K − 1)λ; c_{w,w'} = λ; Ψ_{w,w'}(z_w, z_{w'}) = [z_w(w') = z_{w'}(w)];
f_{w,w'}(z_w, θ) = [z_w(w') = θ]. 

 ## «A good grouping exists», with the numbers of the proof, as counts over all K^g groupings 

### `Y`

 Y_{γ,γ'} for numbers c_{a,b}: the sum of c_{a,b} over a ∈ G_γ, b ∈ G_{γ'}. 

### `Good`

 A grouping is good: (G1) every group has at most 2g/K nodes; (G2) Y_{γ,γ'} ≤ (U + gP/K)/K² for
all γ ≠ γ' (multiplied by K³). 

### `GroupingFacts`

 The steps of the paragraph «A good grouping exists», for g = 3K⁸, K ≥ 2, c symmetric with (i). A
probability p of an event is written as: the number of groupings in the event is at most p·K^g. 

### `GroupingFacts.cheb`

 by Chebyshev, Pr(Y_{γ,γ'} > U/K² + gP/K³) ≤ 4K⁶/g = 4/(3K²) 

### `GroupingFacts.pairs`

 some pair violates this bound with probability less than 2/3 

### `GroupingFacts.group`

 a group exceeds 2g/K with probability at most K/g 

### `GroupingFacts.groups`

 some group does so with probability less than 1/3 (the paper: at most K²/g < 1/3) 

### `GroupingFacts.exists_good`

 so a good grouping exists 
