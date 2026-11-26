---
{
  "module": "ThreeSumApsp/Programs/Sec3/Theorem17/Parameters/Sizes.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Anthropic, PBC",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Programs/Sec3/Theorem17/Parameters/Sizes.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Programs/Sec3/Theorem17/Parameters/Sizes.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# The parameters of Theorems 17 and 19, without division and without roots

The proof of Theorem 19 chooses D as "the largest power of four with D ≤ n^{1/18}"
and g := ⌈D^{1/36}⌉, or D := ⌊n^{1/18}⌋ and g := ⌈D^{0.0315}⌉; the reduction of Theorem 17 uses
⌊n²/√D⌋ and quotients rounded up.  The language has neither division nor roots, so all of these are
found by counting up.  A power is compared with a bound without forming a number above the bound
times the base.

* powLt(g, e, t), for g ≥ 1, returns 1 if g^e < t, and 0 if not (`powLt_meets`); what it holds after
  i factors is `capPow g t i`.
* rootCeil(e, t) returns the least g with g^e ≥ t (`rootCeil_meets`).
* The four parameters; 5 and 26 stand for the two routes of Theorem 19, through Theorem 5 and
  through Corollary 26.  d5(n) returns the largest power of four that is at most n^{1/18}, g5(D)
  returns ⌈D^{1/36}⌉, d26(n) returns ⌊n^{1/18}⌋, and g26(D) returns ⌈D^{0.0315}⌉; g5 and g26
  are for D ≥ 1 (`d5_spec`, `g5_spec`, `d26_spec`, `g26_spec`).
* queryCapNat(n, D) returns ⌊n²/√D⌋, and ceilDiv(a, b) returns ⌈a/b⌉ (`queryCapNat_meets`,
  `ceilDiv_meets`).

No routine touches the memory.


 ## Comparing a power with a bound 

### `capPow`

 The powers of g, as long as they are below t: the value stays as it is once it has reached
t. 

### `capPow_succ`

 One more factor. 

### `capPow_spec`

 Below t the value is the power, and a value that has reached t shows that the power has. 

### `capPow_lt_iff`

 The value is below t exactly if the power is. 

### `Base`

 The local variables of powLt: the arguments g, e, t; the number of factors so far; their
product (Acc). 

### `powLtBody`

 powLt(g, e, t). 

### `powLt_meets`

 **powLt**, for g ≥ 1, returns 1 if g^e < t and 0 if not, in at most 16 e + 14 steps.  It forms
no number above t g + e + 1. 

 ## Roots, rounded up 

### `Exp`

 The local variables of rootCeil: the arguments e, t; the candidate g; whether g^e < t. 

### `rootCeilBody`

 rootCeil(e, t), over the procedure pPow (powLt). 

### `tRootCeil`

 The time of rootCeil. 

### `rootCeil_meets`

 **rootCeil** returns the least g with g^e ≥ t, for e ≥ 1 and t ≥ 1.  It forms no number above t
times the result plus e + 1. 

### `rootCeil_succ`

 Rounding a root down is rounding the root of the next number up, minus one. 

 ## The four parameters of the proof of Theorem 19 

### `d26Body`

 d26(n), over the procedure pRoot (rootCeil): ⌊n^{1/18}⌋.  Local 0 is the argument, local 1 takes
⌈(n + 1)^{1/18}⌉. 

### `tD26`

 The time of d26. 

### `d26_spec`

 **d26** returns ⌊n^{1/18}⌋. 

### `d26_meets`

 **d26** as a procedure. 

### `d5Body`

 d5(n), over the procedure pD26: the largest power of four that is at most n^{1/18}.  Local 0 is
the argument, local 1 is ⌊n^{1/18}⌋, local 2 the power of four. 

### `tD5`

 The time of d5. 

### `four_mul_pow_le_iff`

 The test of the loop of d5: 4^(i+1) ≤ y if and only if i < ⌊log₄ y⌋. 

### `d5_spec`

 **d5** returns the largest power of four that is at most n^{1/18}. 

### `g5Body`

 g5(D), over the procedure pRoot: ⌈D^{1/36}⌉. 

### `tG5`

 The time of g5. 

### `g5_spec`

 **g5** returns ⌈D^{1/36}⌉, for D ≥ 1. 

### `g26Body`

 g26(D), over the procedure pRoot: ⌈D^{0.0315}⌉, the least g with g^2000 ≥ D^63.  Local 0 is the
argument, local 1 counts the factors, local 2 is their product. 

### `tG26`

 The time of g26. 

### `g26_spec`

 **g26** returns ⌈D^{0.0315}⌉, for D ≥ 1. 

 ## ⌊n²/√D⌋ and quotients rounded up 

### `queryCapNatBody`

 queryCapNat(n, D).  Locals 0 and 1 are the arguments, local 2 is n⁴, local 3 the candidate. 

### `tQueryCapNat`

 The time of queryCapNat. 

### `queryCapNat_test_bounds`

 The numbers that the test of queryCapNat forms for a candidate c that is at most the result
C. 

### `queryCapNat_meets`

 **queryCapNat** returns ⌊n²/√D⌋, for D ≥ 1. 

### `ceilDivBody`

 ceilDiv(a, b).  Locals 0 and 1 are the arguments, local 2 is the candidate q, local 3 is
q b. 

### `tCeilDiv`

 The time of ceilDiv. 

### `ceilDiv_meets`

 **ceilDiv** returns ⌈a/b⌉, for b ≥ 1. 
