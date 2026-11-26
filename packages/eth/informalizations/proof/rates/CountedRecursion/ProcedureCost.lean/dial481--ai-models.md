---
{
  "module": "proof/rates/CountedRecursion/ProcedureCost.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/CountedRecursion/ProcedureCost.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/CountedRecursion/ProcedureCost.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # One entry of the callee's tables

`procedureCostFrom : ProcedureCostFrom`. Proof of Lemma 8: «an entry is a sum of at most 2^{2gP/K}
terms, each a product of at most g² values» and «answer each query by computing the entry»; proof of
Theorem A (b): «Definition 2 holds with B₁ = gB + g²(2λ)^c in the role of B and with τ =
2^{cλ}Ξ^{C₂}», «Crude bounds give L ≤ N + 1, … g(P + B₁) ≤ Ξ^{c+4}».
The procedure is `entryData` with each of its queries of Definition 2(iii) answered by the
procedures of the network (`QueryMachine.subst`). So: `EntryCostExplicit` at the price τ = (2^{cλ} +
2 + tq)·Ξ^{C₂} + 2 of a query; `BothNetworks` answers a query within τ − 2;
`QueryMachines.StSubstWithin` puts the two together; the context that is carried along is the parent
(`size_mkParent_le`);
and the clause g(P + B₁) ≤ Ξ^{c+4} of `CrudeBounds` turns (g(P + B₁))^{c₁} into a power of Ξ.
`EntryCostExplicit` asks L ≤ 2gP for the L of the call: this is had from `LabelCrude`, L ≤ N + 1 =
gP + 1 ≤ 2gP. The constant is C₂ + (c + 4)c₁ + 2c + 6. 

### `procedure_arith`

 The arithmetic: with A the price of a query one level up, G ≤ X^e, and a context of size at most
X^s. 

### `procedureCostFrom`

 **An entry of the callee's tables**, from Lemma 8 up to the call, its L and case (ii), the cost
of an entry with one constant, the procedures of the network, «L ≤ N + 1» for the L of the call,
«g(P + B₁) ≤ Ξ^{c+4}», and «answer each query by computing …». 
