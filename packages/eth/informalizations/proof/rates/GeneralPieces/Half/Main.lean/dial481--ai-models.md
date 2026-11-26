---
{
  "module": "proof/rates/GeneralPieces/Half/Main.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/GeneralPieces/Half/Main.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/GeneralPieces/Half/Main.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # The theorem on pieces with ρ = 1/√2, with the running time

`AppRunningTime.ThmHalfPieces`: the programs `halfF c₀ c` are pieces with parameters (1/√2, c') in
the sense of the definition in Appendix A, for the constant c' = `max (c + 1) (2 * (halfF c₀ c).m)`
of the proof below, and they are the pieces of the proof in Appendix B: h is the least number ≥ 2
with p(h) ≥ 2^λ, μ(x) is the partition of h with number x in the lexicographic list, 𝓘 = {−2h, …,
2h} is numbered from 0 to 4h, d = h!, A_s is the coefficient of t^{μ(u)} in
Q_s(a^{μ(x)}, b^{μ(v)})·t^{μ(y)}, and the numbers of bits are ⌈log R^row_s⌉ and ⌈log R^col_s⌉. The
statements about the ring, `AppHalfPieces.PieceFacts`, are a hypothesis. The cut-offs in the
programs
(the search for h up to c₀·λ², the number of a piece at 4h, the numbers of bits at 2cλ) are not
active for the constants that are chosen. The running times of the proof's last paragraph are those
of the programs `halfF`: they are functions of an input and of a padding input,
run in polynomial time, and give the right values once the padding input has 2^{cλ} units, which
stands for the bound of 2^{cλ} operations in part (c) of that definition; they are not restated
sentence by sentence. 

### `thmHalfPieces`

 The theorem on pieces with ρ = 1/√2, with the running time, for the functions of its proof,
given the statements about the ring (`AppHalfPieces.PieceFacts`, proved in
`proof/rates/GeneralPieces/Main.lean`). 
