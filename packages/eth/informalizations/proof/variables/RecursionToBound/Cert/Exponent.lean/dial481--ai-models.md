---
{
  "module": "proof/variables/RecursionToBound/Cert/Exponent.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/variables/RecursionToBound/Cert/Exponent.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/variables/RecursionToBound/Cert/Exponent.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # The exponent of the padding string is polynomial-time

`expo_polyT`: for every polynomial-time solver S, every n₁ and all polynomial-time `pick` and `num`,
the exponent `expo S n₁ pick num` of the function of Theorem D (a) along the printed Step 5
(proof/variables/RecursionToBound/Defs.lean) is polynomial-time in the input, **on all inputs**. The
file goes through the definitions in their order.

* `needWalk_polyT`: the exponent for the walk. ⌈ε·n⌉ is computed without fractions
  (`ceil_epsOf_mul`). The bound on the length of the stack has the factors (32α)^(2k), 2^k and
  (n+2)^(k+1): with k in unary these numbers have polynomially many binary digits, and only their
  number of digits enters the exponent.
* `needAtC_polyT`: the exponent for one Δ, for k, n and Δ in unary; from the certificates of the
  bounds U, P, B of Step 3 (proof/variables/VariableBound/Net/CertEv.lean), of the exponent of the
  networks (`VariableBound.CertTop.needNetC_polyT`) and of the number of profiles
  (`PaddedDescent.F.CertEval.nProf_polyT`).
* `deltas_polyT`: the list of the numbers Δ. It is cut off at n + 1, so its length is given in
  unary.
* `needOutputsC_polyT`: the maximum over Δ. The fold of the definition is rewritten as: `none` if
  one of the numbers is `none`, and otherwise the maximum of the list (`foldr_bind_max`). In the
  list, Δ is replaced by min(Δ, n + 1), which is given in unary; on the members of the list the two
  agree.
* `planAt_polyT`, `plan_polyT`, `expo_polyT`: the plan and the exponent. The width read from the
  input is at most 3 plus the number of literals written in the formula, so it is given in unary
  (`widthU_unary`); K at the index picked is given in unary because the solver is polynomial-time
  (`ClauseBound.Alg.Solver.Poly.K`), so `num` gets an argument of polynomial length (`numU_polyT`). 

 ### The walk 

### `stackLen_aux`

 The formula of the bound on the length of the walk's state is polynomial-time when every number
in it is. 

### `stackLen_polyT`

 The bound on the length of the walk's state is polynomial-time jointly in k, τ and n, if k is
given in unary. 

### `needWalk_polyT`

 The exponent for the walk is polynomial-time jointly in k, r and n, if k is given in unary. 

 ### One Δ 

### `add_two_polyT`

 Adding two polynomial-time functions of the first component to the second component is
polynomial-time. 

### `optionMap_add_two`

 Adding two polynomial-time numbers to a number that may be missing is polynomial-time. 

### `nPrMax_polyT`

 The bound on the number of profiles is polynomial-time if K, n and Δ are given in unary. 

### `needAtC_polyT`

 The exponent for one Δ, computed under a bound, is polynomial-time if the solver, the bound and
the index are and k, n and Δ are given in unary. 

 ### All Δ 

### `mem_deltas`

 The numbers Δ of the list are at least 2, at most n + 1 and at most the bound on the
occurrences. 

### `deltas_polyT`

 The list of the numbers Δ is polynomial-time jointly in k, r and n, if k and n are given in
unary. 

### `foldr_bind_max_map`

 The fold of `needOutputsC`, as a function of the list of the numbers that may be missing. 

### `maxOfOptions_polyT`

 The function whose value is `none` if one of the numbers is `none`, and otherwise the maximum of
the list, is polynomial-time. 

### `needOutputsC_polyT`

 The maximum over Δ, computed under a bound, is polynomial-time if the solver, the bound, r and
the index are and k and n are given in unary. 

 ### The plan and the exponent 

### `planAt_polyT`

 The plan is polynomial-time if the solver, the index and r are and k and n are given in unary. 

### `foldr_max_length_le`

 The largest number of literals in a clause is at most the number of all literals written in the
formula. 

### `widthOr3F_unary`

 The width of Step 5 is polynomial-time with its value written in unary. 

### `widthU_unary`

 The width read from the input is given in unary. 

### `nU_unary`

 The number of variables read from the input is given in unary. 

### `widthCut_unary`

 The width read from the input, cut off at ⌊log₂(n+1)⌋, is given in unary. 

### `powWidthCut_unary`

 2 to the width cut off is given in unary. 

### `level_polyT`

 The level picked for n and its index are polynomial-time in the input. 

### `idxU_polyT`

 The index picked for n is polynomial-time in the input. 

### `numU_polyT`

 The number in [e, 2e] for the level picked is polynomial-time in the input: its argument is (ℓ,
K_ℓ) in unary, and K is given in unary for a polynomial-time solver. 

### `plan_polyT`

 The plan is polynomial-time in the input. 

### `expo_polyT`

 The exponent of the padding string is polynomial-time in the input. 
