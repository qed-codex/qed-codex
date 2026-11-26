---
{
  "module": "Zeta23/PrimeSideB/Concrete.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/PrimeSideB/Concrete.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/PrimeSideB/Concrete.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

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


# The concrete prime-side data as an instance of the abstract layer
Small, dependency-light file (imports only `PrimeSideA.Basic` and `PrimeSideTemp`):

* `Params.toSetting P T = ⟨T, λ, w⟩`, `Params.localFun P T = ⟨φ̂|_ℝ, Φ|_ℝ, A_φ, g, a, b⟩(T)` and the
  `rfl` bridges (`trGtA (P.toSetting T) (P.localFun T) = P.trGtilde T`, …);
* `PrimeSide.LocalHypsEventually cϱ P` — "the taper facts `LocalHyps` hold for the concrete data for
  all large `T`" (proved in `Zeta23/PrimeSideA/Bridge.lean`);
* `PrimeSide.evBound_of_eventuallyAt` — an `EventuallyAt`-form result specialised to the concrete
  data is an `EvBound` in `T`.


### `toSetting`

 The abstract-layer parameter triple `(T, λ, w)` (`PrimeSide.Setting`). 

### `localFun`

 The concrete taper data at height `T` as an abstract `PrimeSide.LocalFun`:
`(φ̂|_ℝ, Φ|_ℝ, A_φ, g, a, b)` = `(P.phiHatR T, P.PhiR T, P.Aphi T, P.g T, P.a T, P.b T)`. 

### `GentryA_concrete`

 `GentryA` on the concrete data is `Params.Gentry` ([eq:Gdef], 2nd expression). 

### `trGtA_concrete`

 `tr G̃` of the abstract layer on the concrete data is `Params.trGtilde`. 

### `trGt2A_concrete`

 `tr G̃²` of the abstract layer on the concrete data is `Params.trGtildeSq`. 

### `LocalHypsEventually`

 The taper facts `LocalHyps` hold for the concrete data for all large `T`
(proved in `Zeta23/PrimeSideA/Bridge.lean`; here a named hypothesis). 

### `evBound_of_eventuallyAt`

 Generic bridge: an `EventuallyAt`-form result of the abstract layer, specialised to the
concrete data, is an `EvBound` in `T` (given the local hypotheses eventually and an eventually
nonnegative majorant). 
