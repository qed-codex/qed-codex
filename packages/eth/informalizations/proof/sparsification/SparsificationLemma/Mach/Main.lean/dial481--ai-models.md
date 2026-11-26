---
{
  "module": "proof/sparsification/SparsificationLemma/Mach/Main.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/sparsification/SparsificationLemma/Mach/Main.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/sparsification/SparsificationLemma/Mach/Main.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # One machine prints the outputs of the sparsification

`prints : Prints` (proof/sparsification/SparsificationLemma/Mach/Defs.lean): one multi-stack Turing
machine of Mathlib with finite alphabets and one constant C, for all widths k ≥ 1 and all precisions
s ≥ `s0U k`, and every k-CNF φ without an empty clause. Started on 1^s 0 1^k 0 code(φ), it halts
with
the code of the list of outputs of the sparsification run with its parameter τ = 2^(4s+17), as in
`Prints` (this τ is not the τ of Definition 2), within C·(length of the input + 2^k)^C·2^(C·⌊n/2^s⌋)
steps, where n is the number of variables of φ.
The machine is the padding machine `CountKSatRate.stPaddedW` for the function `BL` of (input, pad)
and the exponent `eL` (proof/sparsification/SparsificationLemma/Mach/Walk.lean). Both are
polynomial-time (proof/sparsification/SparsificationLemma/Mach/Cert.lean), and `BL` writes the
outputs (proof/sparsification/SparsificationLemma/Mach/Len.lean). The machine takes at most q·(|x| +
2^(eL x) + 1)^q steps; `time_le` compares this with the bound: 2^(eL x) = 2^⌊n/2^s⌋·2^k·(2^b)³·512,
where b is the number of binary digits of |x|, and 2^b ≤ 2|x|. 

### `two_pow_size_le`

 2 to the number of binary digits of N ≥ 1 is at most 2N. 

### `time_le`

 The time of the padding machine is within the bound of the statement, with C = q·4097^q + 4q. 

### `prints`

 **One machine prints the outputs.** One machine and one constant C for all widths k ≥ 1 and all
precisions s ≥ `s0U k`, and every k-CNF φ without an empty clause: on 1^s 0 1^k 0 code(φ) it halts
with the code of the list of outputs of the sparsification
run with its parameter τ = 2^(4s+17) (as in `Prints`; not the τ of Definition 2) within C·(length of
the input + 2^k)^C·2^(C·⌊n/2^s⌋) steps, where n is the number of variables of φ. 
