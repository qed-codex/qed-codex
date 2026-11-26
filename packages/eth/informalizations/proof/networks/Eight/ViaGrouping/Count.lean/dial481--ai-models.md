---
{
  "module": "proof/networks/Eight/ViaGrouping/Count.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/networks/Eight/ViaGrouping/Count.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/networks/Eight/ViaGrouping/Count.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # Section 6, «Cost», for an algorithm that is given networks as Definition 2 prints them

Here «So … Z is computed in time O(2^{δ'm})» is proved for an algorithm `NA : SecNetworks.NetAlg`,
which is given P and the four procedures of Definition 2(iii),
and which obeys the bound of Lemma 1 (`ViaGrouping.Correct`). The machine is
`NA.app (satProcs g 3)`: NA on the procedures of the network of Φ, with the procedure for Ψ of
proof/networks/Eight/ViaGrouping/SatPsiDefs.lean.
* Lemma 1 applied to the network of Φ: `Correct.onFormula`; the steps of the machine take polynomial
  time: `count_isPolyT`;
* «Cost», in the order of the sentences of the paper: `count_cost_of`, `count_cost_pos_of`.
The sentences on the network itself (what Z is, U < 6m, the exponent, the remaining factor) are
those of proof/networks/Eight/SecProof_Network.lean. 

### `Correct.onFormula`

 **Lemma 1, applied to the network of Φ.** If NA obeys the bound of Lemma 1 with the exponent ε·U +
b·gP/K, then on the procedures of the network of Φ it returns the value Z of that network within
C₁·2^{εU + b·gP/K}·(P + 1)^{C₁} steps: B = 1 and τ = 1. 

### `count_isPolyT`

 The machine has polynomial-time steps if the algorithm has them whenever the procedures have and
P is given in unary. 

### `size_bound`

 The sizes of the states: a polynomial in the size s of Φ. Here μ = m̄ ≤ m < s and P ≤ 2kμ + 1. 

### `mul_satPf_le`

 gP = 2k·g⌈m/g⌉ ≤ 2k(m + g), for P = max{1, 2k·m̄} and k ≥ 1 (for k = 3 the paper's «gP = 6g⌈m/g⌉
≤ 6(m + g)»). 

 ## «Cost» 

### `count_cost_of`

 **Section 6, «Cost», for a named algorithm.** «So … Z is computed in time O(2^{δ'm})», and «Z is
the number of assignments of the variables occurring in Φ that satisfy Φ». If `NA` evaluates the
networks on [g], given as Definition 2 prints them, within the bound of
Lemma 1 with e = δ'/12 and K ≥ 72/δ', the constants of the paper, then `NA` on the network of Φ
(procedure COUNT of Algorithm 1) returns that number within A·2^{δ'm} steps, on states of polynomial
size. The proof goes through the sentences of the paper in their order:
Definition 2 holds, with P = 6m̄ and B = 1 (`satNet_isNetworkP`, inside `Correct.onFormula`); what Z
is (`network_value_eq`); U < 6m (`network_total_lt`) and gP ≤ 6(m + g); the exponent
(`network_exponent_lt'`); the remaining factor (`remaining_factor`).
Different from the paper: the case m = 0, which the paper sets apart, is run through the same
machine (then U = 0, P = 1, P + B = 2 ≤ 2(6m̄ + 1), which costs the constant factor 2^{C₁}, and the
exponent is at most δ'g); only steps are counted here (they take polynomial time when those of `NA`
do: `satProcs_keepsP`), so τ = 1 and there
is no «preparation in time polynomial in n». 

### `count_cost_pos_of`

 The same in the form that the reduction to sparse formulas takes («… and Φ is satisfiable if and
only if Z > 0»): the machine returns an integer that is positive exactly if Φ is satisfiable. 
