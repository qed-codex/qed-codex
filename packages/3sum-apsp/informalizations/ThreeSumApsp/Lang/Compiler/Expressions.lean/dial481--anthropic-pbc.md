---
{
  "module": "ThreeSumApsp/Lang/Compiler/Expressions.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Anthropic, PBC",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Lang/Compiler/Expressions.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Lang/Compiler/Expressions.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# The compiler is correct on expressions

The code of an expression e, compiled for the temporary T_k, only changes the memory
(`straight_compileExpr`).  Run in a memory that represents the state σ, it leaves the value of e in
T_k and changes nothing but ADDR and the temporaries from T_k on.  That is `effects_compileExpr`,
for an expression that needs no more temporaries than there are from T_k on, and
`effects_compileExpr_of_width`, the form that the other files use, for an expression of width at
most F.

The proof is an induction on e; in each case the instructions are run one after the other.  A
constant is built from its binary digits (`effects_digitsCode`).  For an operation, the value of the
left side waits in T_k while the right side is evaluated into T_{k+1}, which does not touch T_k.


### `_root_.Light.Expr.height_pos`

 Every expression uses at least one temporary. 

### `cT_mem_temps_of_height`

 The temporary that receives the value of an expression is one of those that its code may
change. 

 ## Constants 

### `effects_digitsCode`

 The code for a constant: the cell c receives the number with the given binary digits, and
nothing else changes. 

 ## Expressions 

### `straight_compileExpr`

 The code of an expression only changes the memory. 

### `effect_instr`

 The instruction of an operation, on cells that hold known numbers. 

### `effects_compileExpr`

 The code of an expression leaves its value in T_k and changes nothing but ADDR and the
temporaries from T_k on. 

### `effects_compileExpr_of_width`

 The code of an expression of width at most F, when there are F temporaries from T_k on, leaves
its value in T_k and changes nothing but ADDR and the temporaries from T_k on. 
