---
{
  "module": "proof/consequences/CircuitLowerBound/Circ/Clause.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/consequences/CircuitLowerBound/Circ/Clause.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/consequences/CircuitLowerBound/Circ/Clause.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # The circuit that computes a clause of the formula of a table from the number of the clause

`stClauseCirc : StClauseCirc`. The inputs are the nb bits of the number j of a clause, lowest first:
the position q (bq bits), the time t (bt bits), the place r in the table (rb bits). The circuit has

* two wires with the constants 0 and 1;
* for every place k of the table a chain of rb gates for «r = k»;
* for each of the three literals and each bit that the table says about a literal (two bits for the
  way the time is formed, two for the way the position is formed, the sign, the bits of the kind,
  the bits of the
  number that is added to the position) a chain of gates for the OR, over the places k whose entry
  has this bit, of «r = k»; beyond the end of the table all these wires are 0, which is the clause
  `zeroCl`;
* for each of the three literals 3 gates for every bit of the time (a chain of half adders) and 7
  gates for every bit of the position (a choice between q and P, and a chain of full adders).

Only the last group grows with L: it has 3·(3·bt + 7·bq + 12) gates, which is at most 36·(L + 1).
The size of the others depends on the table only. All numbers of wires are written in closed form. 

 ### The circuit 

### `litI`

 Literal number ι of a clause of a table. 

### `fbit`

 Bit number f of what the table says about a literal: two bits of the mode of the time, two bits
of the mode of the position, the sign, kbm bits of the kind, the bits of the number added to the
position. 

### `Ew`

 The wire «r = k»: the last wire of chain number k. 

### `selGate`

 Gate i of the chain for «r = k»: the wire before, and «bit i of r is bit i of k». 

### `selChain`

 The chain for «r = k». 

### `selG`

 The chains for «r = k», k < R. 

### `Fw`

 The wire of bit f of literal ι; nf is the number of bits of a literal. 

### `fldGate`

 Gate k of chain number a = ι·nf + f: the wire before, or «r = k» if the entry k of the table has
the bit f of literal ι. 

### `fldChain`

 Chain number a. 

### `fldG`

 The chains for the bits of the three literals. 

### `cinT`

 The carry into bit i of the time; a is the first wire of the gates of the literal. 

### `cinQ`

 The carry into bit i of the position; b is the first wire of the gates for the position, z the
wire with the constant 0. 

### `timeBit`

 The three gates for bit i of the time: «the time is used» and bit i of t; the sum with the
carry; the next carry. 

### `timeG`

 The gates for the time of a literal; m0, m1 are the wires of the mode. 

### `posBit`

 The seven gates for bit i of the position: bit i of q if q is used; or bit i of P if P is used;
then a full adder. 

### `posG`

 The gates for the position of a literal; p0, p1 are the wires of the mode, dW i the wire of bit
i of the number that is added. 

### `szL`

 The number of gates for the time and the position of a literal. 

### `offA`

 The first wire of the gates for the time and the position of literal ι. 

### `dWire`

 The wire of bit i of the number that is added to the position of literal ι. 

### `litG`

 The gates for the time and the position of literal ι. 

### `gatesC`

 All gates. 

### `outsL`

 The output wires of literal ι: the position, the time, the kind, zeros up to L wires, the sign. 

### `dSum`

 A number that is at least as large as every number that the table adds to a position. 

### `coreB`

 The circuit and its output wires, from numbers that are cut off at L where they are lengths of
lists. 

### `B`

 The circuit and its output wires. 

 ### Lengths 

 ### A gate whose function is chosen by a bit that is known when the circuit is written 

### `mod_four`

 A number modulo 4 from its two lowest bits. 

 ### The time 

### `time_val`

 The output wires for the time carry the time of the literal. 

 ### The position 

### `pos_val`

 The output wires for the position carry the position of the literal. 

 ### The place in the table 

### `sel_val`

 The wire «r = k». 

### `fld_val`

 The wire of a bit of what the table says at the place r. 

### `Fw_val`

 The wire of bit f of literal ι. 

 ### Every gate reads earlier wires 

### `outsL_lt`

 The output wires are wires of the circuit. 

 ### What the output wires carry 

### `core_val`

 The values of the output wires of literal ι, for the clause number j. 

 ### The circuit is written in polynomial time 

 ### The statement 

### `dq_le_dSum`

 No number that the table adds to a position is larger than `dSum`. 

### `stClauseCirc`

 The circuit that computes clause number j of the formula of a table from the bits of j has at
most 36·(L+1) gates and a number of gates that depends on the table only. 
