---
{
  "module": "proof/rates/ClauseBound/Inst/RecArith.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/ClauseBound/Inst/RecArith.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/ClauseBound/Inst/RecArith.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # The arithmetic of the recombined pieces as programs

The coefficients of the recombined pieces are sums of binomial coefficients with an integer on top.
This file writes them as programs made of loops over ranges, proves that `chooseZ` is the binomial
coefficient
and that `nbF` and `muF` are the block sizes and the number μ of `Pieces`, and proves that the
programs are polynomial-time when the lengths of the loops are given in unary:

* `chooseZ a k` is the binomial coefficient C(a, k) for an integer a, `phiF` is φ_{a,w}(j), `qqF` is
  the coefficient of ψ_β(x,y)·ψ_β(u,v) in Â_t;
* `ccF` is the coefficient of ψ_β(x,u)·ψ_β(y,v) in Â_t, computed from the few numbers through which
  it depends on β: all blocks but the last have the same number of positions, so the
  polynomial of β is a power of one linear factor times at most one other, and the binomial theorem
  gives its coefficients;
* `muF` is μ, by the closed form with the common denominator 2^(λ+1);
* the number of blocks (`nblk`), the block sizes and μ can be written in unary. 

 ### The programs 

### `powZ`

 b^k. 

### `fallZ`

 a(a − 1)⋯(a − k + 1). 

### `factN`

 k!. 

### `chooseZ`

 The binomial coefficient C(a, k) for an integer a: the falling product divided by k!, sign and
absolute value apart. 

### `sumR`

 Σ_{k<w} f k. 

### `sgnZ`

 (−1)^a. 

### `phiF`

 φ_{a,w}(j). 

### `qqF`

 The coefficient of ψ_β(x,y)·ψ_β(u,v) in Â_t, for odd(β) = j. 

### `linF`

 The functional with parameters a and w at the polynomial σ·T^ν·(2^{n₀} − (2^{n₀} − 1)·T)^z,
times 2^r − (2^r − 1)·T if ε. 

### `ccF`

 The coefficient of ψ_β(x,u)·ψ_β(y,v) in Â_t, for a label β whose polynomial is σ·T^ν·(2^{n₀} −
(2^{n₀} − 1)·T)^z, times 2^r − (2^r − 1)·T if ε. 

### `nbF`

 The number of positions of block b. 

### `muF`

 μ: the sum of (2^{n_b} − 1)·2^{λ − n_b} over the blocks, divided by 2^{λ+1}. 

 ### What some of the programs compute 

### `countP_range`

 Counting in a list of the numbers below n is counting in the finite set. 

### `muF_eq`

 μ, for all λ and h. 

### `nblk_le_all`

 There are at most λ blocks. 

### `muF_le`

 μ ≤ λ. 

### `clog_two_eq`

 ⌈log₂ n⌉ is the number of binary digits of n − 1. 

 ### The certificates 
