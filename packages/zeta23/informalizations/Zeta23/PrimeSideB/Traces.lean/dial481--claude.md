---
{
  "module": "Zeta23/PrimeSideB/Traces.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/PrimeSideB/Traces.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/PrimeSideB/Traces.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/

/-
  Part of the Zeta23 formalization of the paper
  "More than two thirds of the zeros of the Riemann zeta function lie on the critical line".
-/
```


# [thm:traces] for the concrete data — instantiating the abstract assembly
`Zeta23/PrimeSideB.lean` proves [thm:traces] for abstract real functions of `T`
(`PrimeSide.Facts D → TracesBounds …`).  This file plugs in the concrete objects:

* `Params.toSetting P T = ⟨T, λ, w⟩` and `Params.localFun P T = ⟨φ̂, Φ, A_φ, g, a, b⟩(T)` turn
  (`P : Params`, `T`) into the abstract prime-side layer (`Setting`, `LocalFun`), and
  `trGtA (P.toSetting T) (P.localFun T) = P.trGtilde T` etc. hold by `rfl`;
* `PrimeSide.concreteData P Z` is the `Data P` record of the actual traces / 𝓜-terms / ∫μ² / Σa_n²g;
* `PrimeSide.concreteFacts` derives `Facts (concreteData P Z)` from `P.Valid`, `PaperInputs Z`
  (H-RvM, H-Γ, H-cheb, H-MV), [prop:trace]/[lem:ends]/[eq:Msplit]/[prop:mumu]/[prop:cross],
  [prop:PP] + sandwich, and `LocalHypsEventually cϱ P` (the taper facts [eq:psidef],
  [eq:abdef], [eq:gbounds], [eq:Phi2FT], [lem:poisson] … for the concrete φ — proved in
  `Zeta23/PrimeSideA/Bridge.lean` from Taper.lean / Poisson.lean);
* `thm_traces_of_localHyps : … → ThmTracesHyp P Z`.


### `concreteData`

 The concrete `Data P`: the actual prime-side traces, 𝓜-terms, `∫_T^{2T} μ²` and
`Σ_{n≤X} Λ(n)²/n g(log n)`, and `N(T,2T)` of the zero configuration `Z`. 

### `rvm_evBound`

 From H-RvM (`C log T` form) to the `l`-form used by the assembly: `log T ≤ 2 l` eventually. 

### `concreteFacts`

 **`Facts` for the concrete data.**  Inputs: `P.Valid`; `PaperInputs Z` (only H-RvM, H-Γ,
H-cheb, H-MV are used); the taper facts eventually (`LocalHypsEventually`).  The §5 sub-results are
proved elsewhere in the repository. 

### `thm_traces_of_localHyps`

 **[thm:traces] for the concrete prime-side data**: the hypothesis `ThmTracesHyp P Z` of
`PrimeSideTemp.lean` follows from `P.Valid`, the published inputs `PaperInputs Z`, and the taper
facts for the concrete φ. 
