---
{
  "module": "proof/threesat/Printed/GroupingPoly.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/threesat/Printed/GroupingPoly.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/threesat/Printed/GroupingPoly.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # The machine of Lemma 1 has polynomial-time steps

The model is proof/networks/Eight/ViaGrouping/Keeps.lean: the plain functions are those defined
there and their certificates are taken from there; the machines are put together with the
certificates of proof/machines/QueryMachines/Poly.lean.
* `asked_keepsP`: the numbers P, P_a, c_{a,b} are read off the input, where they stand in unary;
  each of the four procedures is one query;
* `tableQ_poly`: one entry W̃_γ(Θ);
* `stGroupingPoly`: the search (`Exits.IsPolyT.firstUntil`), L and B' in unary, the machine M with
  its queries answered by `tableQ` (`QueryMachines.stPolySubst`). 

### `asked_mem_poly`

 «Is z ∈ S_a?», asked. 

### `asked_W_poly`

 W_a(z), asked. 

### `asked_Ψ_poly`

 Ψ_{a,b}(z, z'), asked. 

### `asked_f_poly`

 f_{a,b}(z, θ), asked. 

### `asked_keepsP`

 The numbers of Definition 2(iii) stand in the input in unary, and the step machines under the
four procedures have polynomial-time steps. 

### `tableQ_poly`

 One entry W̃_γ(Θ) has polynomial-time steps, if the four procedures have and P_a, c_{a,b} are
given in unary. 

### `bitsOut_unary`

 B' in unary is computed in polynomial time from the input. 

### `toLists_polyT`

 Cutting a setting z_w into its K − 1 strings of λ bits is computed in polynomial time. 

### `stGroupingPoly`

 **The machine of Lemma 1 has polynomial-time steps if M has.** 
