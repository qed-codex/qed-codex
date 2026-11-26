---
{
  "module": "Zeta23/Taper.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/Taper.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/Taper.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/

/-
Zeta23/Taper.lean — the test family [subsec:family] of the paper §2.2 and its
elementary facts: text after [eq:phidef], [eq:phinorms], [eq:abdef], the facts after [eq:PhigA]
(incl. [eq:Phi2FT]), [eq:gbounds], [eq:psidef], [eq:psiints], and [eq:hfbound] specialized to φ.
([eq:hfbound] for general f is in `Zeta23.Poisson.PaperFT`.)

SUB-FILES: Zeta23/Taper/Basic.lean (defs + [eq:phidef] facts),
Norms.lean ([eq:phinorms], [eq:abdef]), Strip.lean ([eq:hfbound] for φ),
Decay.lean ([eq:gbounds], [eq:psidef], [eq:psiints]),
Fourier.lean ([eq:PhigA]-line facts, Plancherel, [eq:Phi2FT]).  This umbrella file
holds the consumer-facing `Params` layer, part 2 (φ̂/Φ/ψ/g/A_φ facts); part 1 (φ, a, b, C₁,
hfbound — depends only on Basic/Norms/Strip) is Zeta23/Taper/Params.lean, importable on its own.

ORGANIZATION.  Namespace `Zeta23.Taper`: generic parameters `(ϱ : ℝ → ℝ) (L w : ℝ)` — pure
one-variable calculus, no `T`.  Namespace `Zeta23.Params` (last section): the same facts for
`P : Params`, `T : ℝ` of Zeta23/Defs.lean (`L = P.L T`, `w = P.w`, `ϱ = P.ϱ`); the bridges
`P.phi T = Taper.phi P.ϱ (P.L T) P.w` etc. are `rfl`.  Consumers use the `Params` versions.

Side conditions: the paper fixes `1 ≤ w ≤ L/8` [eq:wrange].  Generic lemmas carry the minimal
hypothesis they need (`0 < w`, `2w ≤ L`, …); the `Params` versions uniformly assume
`hP : P.Valid` (gives `1 ≤ w`, `TaperProfile ϱ`) and `hwL : 8 * P.w ≤ P.L T` ([eq:wrange]).
-/
```

 ## Instantiation for `P : Params`, `T : ℝ` (Zeta23/Defs.lean).
Consumer-facing names.  Hypotheses: `hP : P.Valid`, `hwL : 8 * P.w ≤ P.L T` ([eq:wrange]). 

 #### hypothesis-free facts 

 #### φ̂, Φ real/even/continuous; conj symmetry 

 #### [eq:PhigA]-line facts 

 #### [eq:gbounds] 

 #### [eq:psidef] division-free, and ψ form 

 #### [eq:psiints] 
