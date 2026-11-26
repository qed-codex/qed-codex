---
{
  "module": "proof/networks/Eight/ViaGrouping/LevelNet.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/networks/Eight/ViaGrouping/LevelNet.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/networks/Eight/ViaGrouping/LevelNet.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # Proof of Proposition 3: «Both networks satisfy Definition 2»

The sentence of the paper (Section 5, proof of Proposition 3, paragraph «Two networks for each ι»):
«Both networks satisfy Definition 2 with P = g³λ (so gP = N), with B₁ = gB + g²λ + 1 in the role of
B, and with τ = poly(B + λ): indeed
∑_{a' ∈ [g]∖{a}} c_{a,a'} ≤ g³λ, |W_a| < 2^{gB}, and Ψ_{a,a'} and the functions of its factorization
are products of indicators and of g(g−1)/2 numbers of absolute value at most 2^t ≤ 2^λ.»
Here it is a statement about the objects that Algorithm 1 runs: the network `levelNetP g tr λ y W`
(tr = false: rows, tr = true: columns; y is the number of ι in base t + 1; W are the tables of the
clique on g² nodes), which is `Eight.Level.netOfι` read as
the data of Definition 2 (proof/networks/Eight/ViaGrouping/LevelDefs.lean), and the procedures
`levelProcs g tr psi lam R` that CLIQUE hands to NETWORK, for any function psi that computes
Ψ_{a,a'} on settings (`StPsiOK`). `levelNetP_isNetworkP_of` has gB + g²t + 1, t = ⌈λ/3⌉, in the role
of B, which is what the reason given in the sentence yields; `levelNetP_isNetworkP_printed_of` has
the printed B₁. The paragraph «Cost» of the proof applies Lemma 1 to `levelNetP` by the first.
The parts: (i), (ii) and the number of settings are in proof/networks/Eight/SecLevel_GridWords.lean
(`netOfι_sized_t`); that the procedures for W_a and f_{a,a'} present the networks is a hypothesis
here (`Eight.Level.StPresents`); the run of
the procedure for Ψ_{a,a'} is `lvlPsi_netOfι_runs` below; the passage to the printed form of
Definition 2 is in proof/networks/Eight/ViaGrouping/Bridge.lean.

Different from the paper: τ is explicit, a·(B + λ)^a·t₀ with a constant a that depends on g only and
t₀ the cost of a query to the tables of the clique; the tables satisfy |W_w| ≤ 2^B where the paper
has < 2^B; a bound on the sizes of the states is
carried along; «B is given» is not part of the statement (`IsNetworkP`); a setting of a row has g³λ
bits, one dummy string of λ bits per grid point for the grid point itself, where the paper encodes
it in g(g² − 1)λ bits, so P_a = P = g³λ (proof/networks/Eight/SecLevel_GridWords.lean). 

### `is_mono_B`

 In Definition 2 without (iii), the bound B on the values may be raised. 

### `isNetworkP_mono_B`

 The same for Definition 2 with its procedures. 

### `value_levelNetP`

 «The value is Z_ι», for the network in the printed form. 

### `U_levelNetP`

 The total is the number that the algorithm compares (`useRowP`). 

 ## The procedure for Ψ 

### `lvlPsiSize`

 A number, depending on g only, for the size of a query for Ψ and of its answer. 

### `lvlPsi_runs`

 A plain function run as a procedure for Ψ: one step; the states are the query and the answer. 

### `lvlPsiSize_le`

 The sizes of a query for Ψ and of its answer add up to at most `lvlPsiSize g`·(size of c + B +
λ). 

### `lvlPsi_netOfι_runs`

 Definition 2(iii) for Ψ: the function for Ψ, run as a procedure, answers every query on settings
of the network of ι in one step, on states of size at most `lvlPsiSize g`·(size of c + B + λ). 

 ## The sentence 

### `levelNetP_isNetworkP_of`

 «Both networks satisfy Definition 2 with P = g³λ …», with gB + g²t + 1, t = ⌈λ/3⌉, in the role
of B. For every g ≥ 1 there is a constant a ≥ 1 such that, for every function psi that computes
Ψ_{a,a'} on settings, λ = lam c ≥ 1, every y < (t + 1)^{|ℛ|}, and tables W
of the clique on g² nodes with |W_w| ≤ 2^B that the procedure R answers within t₀ ≥ 1 steps on
states of size at most S: the procedures that CLIQUE hands to NETWORK give, in the context (c, y),
the network `levelNetP g tr λ y W`, and it is a network in the
sense of Definition 2 with the parameters P = g³λ, gB + g²t + 1 and τ = a·(B + λ)^a·t₀. 

### `levelNetP_isNetworkP_printed_of`

 **«Both networks satisfy Definition 2 with P = g³λ (so gP = N), with B₁ = gB + g²λ + 1 in the
role of B, and with τ = poly(B + λ)»** (proof of Proposition 3). As `levelNetP_isNetworkP_of`, with
the printed B₁; t ≤ λ. Different from the paper: τ is written
out as a·(B + λ)^a·t₀, with t₀ the cost of a query to the tables of the clique; |W_w| ≤ 2^B in place
of < 2^B; the sizes of the states are bounded too; the procedures do not give B₁; a setting of a row
has g³λ bits, one dummy string of λ bits per grid point for the grid point itself, where the paper
encodes it in g(g² − 1)λ bits, so P_a = P = g³λ (proof/networks/Eight/SecLevel_GridWords.lean). 
