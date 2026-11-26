---
{
  "module": "proof/rates/ClauseBound/Alg/Top.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/ClauseBound/Alg/Top.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/ClauseBound/Alg/Top.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # The definitions, part 3, and the interface lemmas of the top level in m

From a clique solver with a sequence of indices to ONE function of (input, pad) and ONE exponent
function of the input, with the statements on their correctness, on their polynomial cost and on the
size of the exponent. 

### `kOf`

 k in unary: the leading 1s of the input. 

### `restOf`

 The input after 1ᵏ 0. 

### `fmlOf`

 (n in unary, the formula). 

### `root9`

 ⌊m^{1/9}⌋ in unary. 

### `PtopK`

 P of the network of a k-CNF with m clauses on g nodes. 

### `lamTopK`

 An upper bound for the label length of the top instance (U ≤ 2km). 

### `countG`

 The value of the network of ψ on 3K⁸ nodes: rebalanced to K nodes with labels of exactly
`lamTopK` bits, then the solver at the index i. 

### `needTop`

 The exponent of a pad that suffices for a k-CNF with m clauses at the index i. 

### `needTopC`

 `needTop` computed under the bound b; `none` if it is larger. 

### `planM`

 The exponent of the clique algorithm at the level picked for m, if it is at most n; `none` if
exhaustive counting is at least as good. 

### `eM`

 THE exponent function: the smaller of n and the exponent of the clique algorithm. 

### `AM`

 THE function: the number of satisfying assignments of the formula written in p.1, in n + 1 bits,
when the pad p.2 is long enough. 

 ### Decoding the input 

 ### The value of the top instance 

### `StCountG`

 The solver at the index i, fed with the rebalanced network of ψ, returns the value of that
network. 

### `StCorrectM`

 Correctness of `AM`: on the code of a k-CNF with at least one clause in which all n variables
occur, and a pad of at least 2^(`eM`) units, it returns the number of satisfying assignments in n +
1 bits. 

 ### Polynomial-time bounds 

 ### The exponent is O(k·m·e) 

### `StTopArith`

 Part (c) of the theorems, as an inequality: with l the level picked for m, the exponent is at
most A·k·m·e_l. 
