---
{
  "module": "proof/variables/PairsToBound/FrontEnd.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/variables/PairsToBound/FrontEnd.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/variables/PairsToBound/FrontEnd.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # The front end and the test of the algorithm of Step 6

**The sentences answered** (Step 6 of Appendix D). «As in Step 5, k is the largest number of
literals in a clause, or 3 if that is larger». «In the other cases, that is, if n < K₀^17 or this k
exceeds (log n)^(1/4), the algorithm tries all assignments».

**What is proved.** `frontEndAndTestExist : FrontEndAndTestExist`: there is a polynomial-time
function that maps the code of (k, φ) to the code of (`widthOr3 φ`, φ), and for every K₀ there is a
polynomial-time test that is true on the code of (k, φ) exactly if n ≥ K₀^17 and `widthOr3 φ` ≤ (log
n)^(1/4).

**The two programs.** Both read the input with `ClauseBound.Alg.fmlOf`, which returns n in unary and
the list of clauses with natural numbers as variables. `widthN ψ` is the width of Step 6 of such a
list.
* `atWidthOr3 x` writes the formula read from x as a bit string again, by the formula of `SatM.enc`
  (`VariableBound.Rename.encN`), with `widthN` in the place of the width that x declares.
* `inMainRegime K₀ x` compares natural numbers only: K₀^17 ≤ n and 2^(k⁴) ≤ n, for k = `widthN`. For
  natural numbers k ≥ 1 and n, k⁴ ≤ log n holds exactly if 2^(k⁴) ≤ n (`pow_four_le_lg_iff`); for n =
  0 both sides are false, because Mathlib's logarithm of 0 is 0.

**Polynomial time.** The width is at most 3 plus the number of all literals written in the formula,
so it can be written in unary (`widthN_unary`); hence so can its fourth power, and the number 2^(k⁴)
has polynomially many binary digits. 

 ### The two programs 

### `widthN`

 The width of Step 6 of a formula with natural numbers as variables: the largest number of
literals in a clause, or 3 if that is larger. 

### `atWidthOr3`

 The front end: the formula written in x, written again with the width of Step 6 as its declared
width. 

### `inMainRegime`

 The test: K₀^17 ≤ n and 2^(k⁴) ≤ n, for the number n of variables written in x and the width k
of Step 6 of the formula written in x. 

 ### What they compute 

### `widthN_toN`

 Writing the variables as natural numbers does not change the width. 

### `pow_four_le_lg_iff`

 For natural numbers k ≥ 1 and n: k⁴ ≤ log n if and only if 2^(k⁴) ≤ n. 

### `atWidthOr3_rewrites`

 The front end maps the code of (k, φ) to the code of (`widthOr3 φ`, φ). 

### `inMainRegime_tests`

 The test is true on the code of (k, φ) if and only if n ≥ K₀^17 and `widthOr3 φ` is at most (log
n)^(1/4). 

 ### Polynomial time 

### `widthN_eq`

 The maximum with the start value 3 is the maximum, with the start value 0, of the list with 3
put behind it. 

### `widthN_le`

 The width is at most 3 plus the number of all literals written in the formula. 

### `widthN_polyT`

 The width is polynomial-time. 

### `widthN_unary`

 The width is polynomial-time even with its value written in unary. 

### `atWidthOr3_polyT`

 The front end is polynomial-time. 

### `both_le_polyT`

 Comparing two polynomial-time numbers with a third is polynomial-time. 

### `inMainRegime_polyT`

 The test is polynomial-time. 

### `frontEndAndTestExist`

 For every K₀ there are a polynomial-time front end and a polynomial-time test as in Step 6. 
