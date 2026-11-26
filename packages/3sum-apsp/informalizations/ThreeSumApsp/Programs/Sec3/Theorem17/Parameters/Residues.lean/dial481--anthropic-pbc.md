---
{
  "module": "ThreeSumApsp/Programs/Sec3/Theorem17/Parameters/Residues.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Anthropic, PBC",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Programs/Sec3/Theorem17/Parameters/Residues.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Programs/Sec3/Theorem17/Parameters/Residues.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# Residues without division

"We reduce the weights modulo a prime p" (proof of Theorem 17).  The language has no division.  The
residue of a number w modulo p is found by greedy subtraction of 2^len p, …, 2p, p, which are kept
in a table.

* bitLen(U) returns the number of binary digits of U, by doubling (`bitLen_spec`).
* dblTable(dst, p, len) writes p, 2p, …, 2^len p to dst (`dblTable_spec`).
* resid(w, dbl, len) returns w mod p, for |w| < 2^len, given the table at dbl (`resid_meets`).  What
  the routine holds after i rounds is `greedyAt p len w i`: it is not negative, below 2^(len+1-i) p,
  and congruent to w (`greedyAt_inv`), so that it ends with the residue (`greedyAt_end`).
* residues(src, dst, m, dbl, len) writes the residues of the m numbers at src to dst, by one call of
  resid for each (`residues_spec`).


 ## The number of binary digits 

### `Arg`

 The local variables of bitLen: the argument U, the number of doublings, and the power of two. 

### `bitLenBody`

 bitLen(U). 

### `tBitLen`

 The time of bitLen. 

### `bitLen_spec`

 **bitLen** returns the least len with U < 2^len and changes no cell.  It forms numbers up to
2U + 1. 

 ## The table of the doubles 

### `dblList_succ`

 One more entry of the table. 

### `length_dblList`

 The table has len + 1 entries. 

### `read_dblList`

 Entry j of the table is 2^j p. 

### `Dst`

 The local variables of dblTable: the arguments dst, p, len; the exponent; the entry. 

### `dblTableBody`

 dblTable(dst, p, len). 

### `tDblTable`

 The time of dblTable. 

### `DblInv`

 The state of dblTable before round j: the entries p, …, 2^j p are written, the last of them is
in a local, and no cell outside the table has changed. 

### `dblTable_spec`

 **dblTable** writes p, 2p, …, 2^len p and changes nothing else.  It forms numbers up to
2^len p. 

 ## One residue 

### `greedyAt`

 The number that resid holds after i rounds: it starts from w + 2^len p, and round number i
subtracts 2^(len-i) p if that leaves a number that is not negative. 

### `mul_pow_modEq_zero`

 A multiple of p is congruent to 0. 

### `cast_mul_pow_succ`

 2^(j+1) p is twice 2^j p. 

### `greedyAt_inv`

 After i rounds the number is not negative, below 2^(len+1-i) p, and congruent to w. 

### `greedyAt_end`

 Greedy subtraction gives the remainder. 

### `greedyAt_lt`

 Every number that resid holds is below 2^(len+1) p. 

### `Arg`

 The local variables of resid: the arguments w, dbl, len; one more than the next exponent; the
number that is reduced. 

### `residBody`

 resid(w, dbl, len). 

### `tResid`

 The time of resid. 

### `resid_meets`

 **resid** returns w mod p and changes no cell.  It forms numbers up to 2^(len+1) p. 

 ## The residues of a list 

### `Src`

 The local variables of residues: the arguments src, dst, m, dbl, len; the counter; the
residue. 

### `residuesBody`

 residues(src, dst, m, dbl, len).  The parameter pResid is the number of the procedure resid in
the program. 

### `tResidues`

 The time of residues. 

### `ResiduesPre`

 What residues assumes: the table of the doubles of p stands at dbl, and the list l of m numbers
of absolute value at most U < 2^len at src; the m cells at dst lie in the memory and meet
neither. 

### `ResiduesInv`

 The state of residues before round i: the first i residues are written, and no cell outside dst
has changed. 

### `residList_take_succ`

 One more residue. 

### `residues_spec`

 **residues** writes the residues of a list and changes nothing else. 
