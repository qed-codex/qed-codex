---
{
  "module": "proof/networks/Eight/SecNetworks_LemGrouping.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/networks/Eight/SecNetworks_LemGrouping.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/networks/Eight/SecNetworks_LemGrouping.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # Section 3 «Networks»: from a network as Definition 2 prints it to the form of proof/networks/Paper

This file passes from a network as Definition 2 prints it (file SecNetworks_Defs: sets S_a ⊆
{0,1}^{P_a}, functions W_a, Ψ_{a,b}, f_{a,b} with values below 2^B, and four procedures) to the form
of the namespace `Paper`, in two steps.
1. `Net.toPaperNetwork`: a network in the printed form gives a `Paper.Network`
   (proof/networks/Paper/SecNetworks_Networks.lean). A node's settings become all strings of P_a
   bits, and W_a and f_{a,b} are set to 0 at strings outside S_a.
   It has the same value (`value_toPaperNetwork`) and the same total U, and satisfies the size
   conditions of proof/networks/Paper with the same P and B (`sized_toPaperNetwork`).
2. `Procs.toPaperNetwork`: the procedures for it. Each first runs the membership test, and then runs
   the procedure for W_a (or f_{a,b}) or returns 0. They answer within 2τ + 1 steps
   (`presents_toPaperNetwork`) and have polynomial-time steps (`keeps_toPaperNetwork`).

`Paper.Network` has no Ψ of its own and `Paper.NetworkProcedures` no procedure for Ψ: Ψ_{a,b} is
defined from f_{a,b} and f_{b,a}, and the procedure for Ψ and the numbers P and B are not passed on.

The last section has three inequalities that the text uses, in the paper's numbers: U ≤ gP, L ≤ 2gP
and K²L ≤ K² + U + gP/K. 

 ## A procedure behind a test 

### `gated`

 Run the test M; if it says yes, run N on the same input; if it says no, return 0. 

### `gated_runs`

 If the test and the procedure each take at most τ steps on states of size at most S, then
`gated` takes at most 2τ + 1 steps on states of size at most S + 4 + the size of the input. The
procedure needs to work only where the test says yes. 

### `gated_isPolyT`

 `gated` has polynomial-time steps if the test and the procedure have. 

### `size_bits`

 The size of a bit string of length n is 2n + 1. 

 ## From the printed form of a network to the form of proof/networks/Paper 

### `toPaperNetwork`

 The network of proof/networks/Paper (`Paper.Network`) that belongs to N: the settings of a are
all strings of P_a bits; W_a is 0 outside S_a; f_{a,b}(z, θ) is 0 unless a ≠ b, z ∈ S_a and θ has
c_{a,b} bits; θ ranges over {0,1}^{c_{a,b}}.
`Paper.Network` has no Ψ of its own: it defines Ψ_{a,b} from f_{a,b} and f_{b,a}. 

### `lab_toPaperNetwork`

 In the network of proof/networks/Paper, θ ranges over {0,1}^{c_{a,b}} for the pair {a, b}, in
either order. 

### `Ψ_toPaperNetwork`

 On S_a × S_b, the Ψ_{a,b} that proof/networks/Paper defines from the factors is the Ψ_{a,b} of
N, because (f_{a,b}, f_{b,a}) is a factorization of Ψ_{a,b} (Definition 2). 

### `Ψ_toPaperNetwork_eq_zero`

 Off S_a × S_b, the Ψ_{a,b} that proof/networks/Paper defines from the factors is 0. 

### `value_toPaperNetwork`

 The value Z is the same: a choice z with some z_a outside S_a contributes 0, since W_a is 0
there, and the other choices contribute what they contribute in N. 

### `sized_toPaperNetwork`

 The network of proof/networks/Paper satisfies the size conditions of proof/networks/Paper with
the same P and B: |S_a| ≤ 2^P, c symmetric, (i), 2^{c_{a,b}} strings θ, and all values at most 2^B
in absolute value («below 2^B» gives «at most 2^B»). 

### `c_le`

 c_{a,b} ≤ P, by (i). 

 ## The procedures 

### `memOfF`

 From a query ((a, b), (z, θ)) for a value of f to the query (a, z) for membership. 

### `Procs.toPaperNetwork`

 The procedures of proof/networks/Paper that belong to the four procedures of Definition 2(iii).
For W_a(z): test z ∈ S_a, then run the procedure for W_a or return 0. For f_{a,b}(z, θ): test z ∈
S_a, then run the procedure for f_{a,b} or return 0.
`Paper.NetworkProcedures` has no procedure for Ψ, so the procedure for Ψ and the numbers P and B are
not passed on. 

### `presents_toPaperNetwork`

 If the four procedures give N within τ steps on states of size at most S (Definition 2(iii)),
then the procedures of proof/networks/Paper give `N.toPaperNetwork` within 2τ + 1 steps on states of
size at most S + (size of c) + 2·(size of g) + 4P + 6. 

### `keeps_toPaperNetwork`

 The procedures of proof/networks/Paper have polynomial-time steps if those of Definition 2(iii)
have. The certificate for the procedure for Ψ is not used. 

 ## Three inequalities of the text, in the paper's numbers 

### `U_le`

 «U ≤ |J|·P by (i)» (after Definition 2). 

### `K2L_le`

 «K²L ≤ K² + U + gP/K» (end of the proof of Lemma 1), multiplied by K, for L = max{1, ⌊(U +
gP/K)/K²⌋}. 

### `L_le`

 «L ≤ 2gP» (end of the proof of Lemma 1), for L = max{1, ⌊(U + gP/K)/K²⌋} and U ≤ gP. 
