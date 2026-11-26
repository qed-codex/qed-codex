---
{
  "module": "proof/rates/PaddedDescent/BrutePad.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/PaddedDescent/BrutePad.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/PaddedDescent/BrutePad.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 Plain exhaustive search for 3-SAT as a polynomial-time function of the padded input:
`bruteA (x, pad)` decodes the formula written
in x and tries the assignments number 0, 1, …, (length of the pad) − 1, where assignment number y
gives the variable i the i-th binary
digit of y. With a pad of length 2^n that is every assignment. It is polynomial-time in the sense of
`PolyT` (`bruteA_polyT`), and with a pad of length
at least 2^n it finds a satisfying assignment exactly if there is one (`bruteA_enc_of_le`).
`withBrute` in proof/rates/PaddedDescent/Reduce.lean uses it for those n
where `sOf n` is small. 

### `nOf`

 The number of variables written in the bit string x. 

### `satAt`

 Does assignment number y (variable i gets the i-th binary digit of y) make a literal of every
clause of ψ true? 

### `bruteA`

 Exhaustive search with fuel: try the assignments number 0, …, (length of the pad) − 1 on the
formula written in the bit string. 

### `bruteA_enc_of_le`

 With a pad of length at least 2^n, exhaustive search finds a satisfying assignment exactly if
there is one. 
