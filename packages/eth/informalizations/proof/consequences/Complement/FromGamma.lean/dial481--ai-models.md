---
{
  "module": "proof/consequences/Complement/FromGamma.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/consequences/Complement/FromGamma.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/consequences/Complement/FromGamma.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # Section 7, proof of Corollary 7: the route from end to end, counted in steps

`stFromGamma` is `stFromGamma_of` (proof/consequences/Complement/Readers.lean) applied to
`SizeCircuit.stSizedBy` from proof/consequences/SizeCircuit/Sized.lean; so this file builds only
with the proofs of proof/consequences/SizeCircuit/. 

### `stFromGamma`

 **The route from end to end, counted in steps**: for every family of circuits that tests the
size, every δ > 0 and every procedure E for #3-SAT whose exponent is small enough, the machine «Γ
beside the formula, then E», put after the reader of the formula for independent sets, after
`readClique` and after `readCover`, returns the numbers of independent sets, cliques and vertex
covers of size s ≤ n within c'·2^{δn} steps. 
