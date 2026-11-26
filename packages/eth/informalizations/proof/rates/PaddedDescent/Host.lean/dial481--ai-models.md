---
{
  "module": "proof/rates/PaddedDescent/Host.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/PaddedDescent/Host.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/PaddedDescent/Host.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 The host machine for stepped computations whose states may be large. `exists_tm'`: a stepped
computation on bit strings
whose init, step and out are polynomial-time runs on ONE of Mathlib's multi-stack machines, with ONE
constant q, such that a run
of T steps on the input x with all states of size at most S costs the machine at most
q·(T+1)·(|x|+S+1)^q steps. The machine and q
are chosen before x, T and S. The proof is that of `exists_tm`, which asks S ≤ (|x|+2)^d and lets
the constant depend on d. 

### `exists_tm'`

 A stepped computation `M` on bit strings with polynomial-time init, step and out runs on one of
Mathlib's multi-stack
machines `N` with finite alphabets. There is one number `q` such that, whenever `M` ends on `x` with
the bit `b` within `T`
steps and with all states of size at most `S`, the machine `N` started on `x` halts with output `b`
within
q · (T + 1) · (|x| + S + 1)^q steps. `N` and `q` depend on `M` only: not on `x`, `T`, `S`. 
