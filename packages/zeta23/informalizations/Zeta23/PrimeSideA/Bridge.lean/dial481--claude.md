---
{
  "module": "Zeta23/PrimeSideA/Bridge.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/PrimeSideA/Bridge.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/PrimeSideA/Bridge.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

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


# Bridge: the concrete taper data satisfy the abstract prime-side hypotheses `LocalHyps`

The §5 layer (`Zeta23/PrimeSideA.lean`) is proved for abstract data
`p : Setting = (T, λ, w)`, `F : LocalFun = (φ̂, Φ, A_φ, g, a, b)` under `LocalHyps cϱ p F` — the list
of test-family facts [eq:psidef], [eq:psiints], [eq:abdef], [eq:gbounds], [eq:PhigA], [eq:Phi2FT],
[lem:poisson], [eq:PiPfacts] used in §5.  Here:

* `localHyps_concrete` — every `LocalHyps` field for the concrete data, from `Taper.lean`,
  `Poisson.lean` ([lem:poisson]) and `PiFacts.lean`, with
  `cϱ := P.crho = c_ϱ` [eq:phinorms]; hence `localHypsEventually : LocalHypsEventually P.crho P`;
(The instantiation `Params.toSetting / localFun` itself lives in `Zeta23/PrimeSideB/Concrete.lean`.)


 ## The concrete data satisfy `LocalHyps` 

### `psiA_concrete`

 The guarded majorant `psiA` [eq:psidef] on the concrete data is Taper's `P.psi' T`
(= Defs' `P.psi T`). 

### `localHyps_concrete`

 **All of `LocalHyps` for the concrete taper data**, at any height `T` with `8w ≤ L`
([eq:wrange]), `l ≥ 1` and `X ≥ 1`.  Field-by-field from Taper.lean / Poisson.lean / PiFacts.lean. 

### `localHypsEventually`

 The concrete data satisfy `LocalHyps P.crho` for all large `T`. 
