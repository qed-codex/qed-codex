---
{
  "module": "proof/machines/Wrap/FrontEnd.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/machines/Wrap/FrontEnd.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/machines/Wrap/FrontEnd.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # The front end for 3-SAT

Three results.
* `pad4KeepsSatAndMeetsSideConditions`: the formula `pad4 φ` (φ with four more variables, each
  forced to be true by a unit clause) is a 3-CNF without repeated clauses, has four clauses more
  than φ, between 4 and n + 4 variables occur in it, and it is satisfiable if and only if φ is.
* `frontEndExists`: the function `frontEnd` on bit strings is polynomial-time and maps the plain
  code `Sat3.enc φ` to the compact code `MainTheoremForms.encC 3 (pad4 φ)`. It decodes the plain
  code to the number n and the list of clauses, with natural numbers as
  variables; puts the four unit clauses behind them; and writes the compact code by its formula,
  with the number of bits of a slot computed from n + 4.
* `length_encC_pad4_le`: both codes have at most a·(n + 2)^d bits, for some a and d; the proof takes
  a = 100 and d = 4. 

 ### The padded formula 

### `castLit_injective`

 The map on literals inside `pad4`, which keeps the number of the variable and the sign, is
injective. 

### `mem_pad4`

 A clause is in `pad4 φ` if and only if it is a clause of φ with its variables carried over, or
one of the four unit clauses. 

### `numOcc_le`

 At most N variables occur in a formula over N names. 

### `occurs_pad4`

 Each of the four new variables occurs in `pad4 φ`. 

### `pad4KeepsSatAndMeetsSideConditions`

 The facts on the padded formula: it is a 3-CNF without repeated clauses, has four clauses more,
between 4 and n + 4 variables occur in it, and it is satisfiable if and only if φ is. 

 ### The front end as a function on bit strings 

### `slotNat`

 A slot of a clause as a number, as `Sat3.slot`, with natural numbers as variables: 0 = no
literal, 2i+1 = ¬xᵢ, 2i+2 = xᵢ. 

### `addFour`

 The clauses of the padded formula, from the number n of variables and the clauses of φ, with
natural numbers as variables. 

### `encUnary`

 The compact code at width 3, from the number w of bits of a slot, in unary, and the clauses: 1³
0, then 1ʷ 0, then 3 slots per clause, w bits per slot, low bit first. 

### `slotBits`

 The number of bits of a slot of the padded formula, from the plain code: ⌊log₂(2(n + 4))⌋ + 1,
where n is the number of ones at the beginning. 

### `frontEnd`

 The front end: decode the plain code to n and the clauses, add the four unit clauses, write the
compact code for n + 4 names. 

### `slotNat_map`

 The number of a slot, with natural numbers as variables, is that of `Sat3.slot`. 

### `encUnary_toN`

 On w = ⌊log₂(2N)⌋ + 1 in unary and a formula over N names, with natural numbers as variables,
`encUnary` is the compact code at width 3. 

### `toN_pad4`

 The padded formula, with natural numbers as variables, is φ with natural numbers as variables
and the four unit clauses on n, …, n + 3 behind it. 

### `frontEnd_enc`

 The front end maps the plain code of φ to the compact code of (3, `pad4 φ`), if every clause of
φ has at most 3 literals. 

### `slotBits_unary`

 The number of bits of a slot is polynomial-time in unary: it is at most 2·(|x| + 4) + 1. 

### `slotNat_polyT`

 The number of a slot is polynomial-time. 

### `addFour_polyT`

 Adding the four unit clauses is polynomial-time. 

### `encUnary_polyT`

 Writing the compact code at width 3 is polynomial-time, with the number of bits of a slot in
unary. 

### `frontEnd_polyT`

 The front end is polynomial-time. 

### `frontEndExists`

 There is a front end: `frontEnd`. 

 ### The lengths of the two codes 

### `length_encC`

 The length of the compact code: k + w + 2 + m·k·w with w = ⌊log₂(2N)⌋ + 1. 

### `length_encC_pad4_le`

 Both codes are polynomially long in n: the compact code of the padded formula and the plain code
of φ have at most a·(n + 2)^d bits, for every 3-CNF φ on n variables without repeated clauses. The
proof takes a = 100 and d = 4. 
