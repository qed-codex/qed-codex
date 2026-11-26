---
{
  "module": "Zeta23/ThmE/TracesChi.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/ThmE/TracesChi.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/zeta23/Zeta23/ThmE/TracesChi.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

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


# [thm:traces] for L(s,chi) — the E3 assembly

Mirror of Zeta23/PrimeSideB.lean (abstract Facts → TracesBounds assembly) and
Zeta23/PrimeSideB/Traces.lean (concrete instantiation) for a Dirichlet character:
ell1 ↦ ell1q q, nu_X ↦ nu_{X,chi} = mu_{kappa,q} + P_{X,c} (no pole term: [eq:Msplit] has three
terms), [prop:PP] main sum ↦ sumA2gCoprime.  The real-variable pointwise lemmas tr2_pointwise and
ratio_pointwise (PrimeSideB.lean) are reused verbatim — they take the density-log as a free real,
and ell1q slots in (l ≤ ell1q for q ≥ 1).  Constants may depend on q (q fixed in [thm:E]; the
q-uniformity question for [rem:otherL](i) is not addressed in this file).

Inputs: prop_trace_chi, eq_Msplit_chi (PrimeSideChi.lean);
prop_mumu_chi (MuMuChi.lean); prop_cross_muP_chi_proved (CrossMuPChi.lean);
prop_PP_chi + sumA2gCoprime sandwich (PPChi.lean);
lem_ends_chi (via the nu-generic lem:ends).


### `l_le_ell1q`

 l ≤ ell1q q T for q ≥ 1, T > 0. 

### `DataChi`

 The data of the chi-[thm:traces] assembly (mirror of PrimeSide.Data; no Pi-terms). 

### `FactsChi`

 Hypotheses of the chi-assembly = conclusions of the §5-chi sub-results (mirror of
PrimeSide.Facts; [thm:E] proof (iii)). 

### `tr2_first_chi`

 [eq:tr2] first form for chi (three-term Msplit). 

### `tr2_chi`

 [eq:tr2], second form for chi. 

### `ratio_chi`

 [eq:ratio] for chi. 

### `tracesBoundsChi_of_factsChi`

 [thm:traces] for chi, assembled. 

 ## Concrete instantiation 

### `GentryChiA_concrete`

 rfl-bridges between the abstract-taper chi-quantities and the concrete ones. 

### `concreteDataChi`

 The concrete chi-data. 

### `rvm_evBound_chi`

 H-RvM(chi) in the l-majorant form. 

### `concreteFactsChi`

 FactsChi for the concrete data, from the chi-inputs together with the taper facts
(including lem_ends_chi). 

### `thm_traces_chi`

 **[thm:traces] for L(s,χ), concrete.** 
