---
{
  "module": "proof/networks/Eight/ViaGrouping/GridPsiDefs.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/networks/Eight/ViaGrouping/GridPsiDefs.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/networks/Eight/ViaGrouping/GridPsiDefs.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # Ψ_{a,a'} in the two networks of Proposition 3, as a program (definitions only)

Definition 2(iii) asks for a procedure that computes the values of Ψ_{a,b}. The row network and the
column network of ι, as Algorithm 1 runs them (`Eight.Level.netOfι`, given by the procedures
`Eight.Level.levelNet`), have procedures for W_a and f_{a,b} only.
This file has a program for Ψ, `gridPsi`. It follows the proof of Proposition 3, paragraph «Two
networks for each ι»: «Ψ_{a,a'} is the product of the factors of the g straight edges between rows a
and a' and of A_{ι(q)}(x_q, y_q, u_q, v_q) over the g(g−1)/2 rectangles q with
these two rows», and the same with rows and columns exchanged. A_i is computed by the program of the
proof of Lemma 2(a) (`Eight.aMul`); ι(q) is the digit of the number y, in base t + 1, at the number
of the rectangle q.
A setting of a row (of a column) is one word of g·g²·λ bits (the paper: g(g² − 1)λ; the λ bits more
per grid point are the dummy string of proof/networks/Eight/SecLevel_Grid.lean);
`ClauseBound.Alg.heG g g λ z i u` is the string which the grid point number i of the row keeps for
the edge to the grid point at the position u, and `ClauseBound.Alg.nodeG g tr b i'` is the position
of the grid point
number i' of the row b (proof/rates/ClauseBound/Alg/Data.lean). tr = false: rows; tr = true:
columns.
The statements `St… : Prop` at the end say that this program computes Ψ of these networks and that
it is polynomial-time. This file has no proofs. 

### `rectPsi`

 The factor of one rectangle: A_{ι(q)}(x_q, y_q, u_q, v_q) for the rectangle q on the rows a < b
and the columns i < i' (tr = true: on the columns a < b and the rows i < i'). z is the setting of a
and z' that of b. Row-wise x_q, y_q are read from z and
u_q, v_q from z'; column-wise x_q, u_q are read from z and y_q, v_q from z'. 

### `psiLt`

 Ψ_{a,b}(z, z') for a < b: 0 unless the two copies of the string agree on each of the g straight
edges between a and b; else the product of the factors of the rectangles. The product runs over all
j = i·g + i' < g², with the factor 1 unless i < i'. 

### `gridPsi`

 **Ψ_{a,a'}(z, z')** in the row network (tr = false) or the column network (tr = true) of the
function ι written by y, as a function of the query ((a, a'), (z, z')). For a > a' it is
Ψ_{a',a}(z', z). 

 ## Interface statements 

### `StGridPsi`

 The program computes Ψ of the network that Algorithm 1 runs, at all settings. 

### `StGridPsiPoly`

 The program is polynomial-time, for λ in unary (g and the direction are fixed). 
