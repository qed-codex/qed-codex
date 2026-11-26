---
{
  "module": "ThreeSumApsp/Programs/Sec3/Theorem17/Hashing/Strassen.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Anthropic, PBC",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Programs/Sec3/Theorem17/Hashing/Strassen.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Programs/Sec3/Theorem17/Hashing/Strassen.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# Strassen's algorithm for matrices over ℤ[x]/(x^p - 1) in Z-order

"Computing PQ takes […] O(n^{log₂ 7}) with Strassen's algorithm" (proof of Theorem 17).

strassen(dst, a, b, j, szt, p, scr): dst := a · b for 2^j × 2^j matrices whose entries are vectors
of p numbers, stored in Z-order, so that the four quadrants of a matrix are the four quarters of its
segment.  szt is the address of the table of the sizes 4^i p, and scr is scratch space.

* At level 0 the product is one product in the ring (`strassen_zero`).
* At level j + 1 the routine clears dst and runs seven phases (`strassen_succ`).  phase(a1, a2, sA,
  b1, b2, sB, c1, s1, c2, s2, j, szt, p, scr, q) forms S = a1 + sA a2 and T = b1 + sB b2 in the
  scratch space, M = S · T by a recursive call, and adds s1 M to c1 and s2 M to c2 (`phase_meets`).
* Between two phases the four quarters of dst hold four lists, and the operands and the table are in
  place (`StrInv`); a phase changes two of the lists (`phase_step`).  After the seven phases the
  four lists are the four quadrants of the product (`sevenPhases_spec`).
* `strassen_spec` is the induction on the level: the product stands at dst after at most
  `strSteps p j` steps, and nothing has changed outside dst and `strScr p j` cells of scratch space.
  The recursion `strSteps` is bounded where the running times are added up.


 ## The program 

### `StrNums`

 The numbers of the procedures that Strassen's algorithm consists of. 

### `OpA1`

 The local variables of phase: the arguments a1, a2, sA, b1, b2, sB, c1, s1, c2, s2, j, szt, p,
scr, q, and a local that takes the results of the calls. 

### `phaseOpnds`

 The operands of a phase: S := a1 + sA a2 at scr, and T := b1 + sB b2 at scr + q. 

### `phaseAccum`

 The end of a phase: c1 := c1 + s1 M and c2 := c2 + s2 M, where M stands at scr + 2 q. 

### `phaseBody`

 phase(a1, a2, sA, b1, b2, sB, c1, s1, c2, s2, j, szt, p, scr, q): the operands; M := S · T at
scr + 2 q, with the scratch space from scr + 3 q on; the end. 

### `Dst`

 The local variables of strassen: the arguments dst, a, b, j, szt, p, scr; the numbers q, 2q, 3q,
where q is the size of a quarter; j - 1; a local that is not used; a local that takes the results of
the calls. 

### `qAddr`

 The address of the quarter number t of the segment whose address is in local x. 

### `sPos`

 The sign 1. 

### `sNil`

 The sign 0. 

### `sNeg`

 The sign -1. 

### `phaseCall`

 A call of phase from the body of strassen: the operands are the quarters number a1, a2 of a and
b1, b2 of b, and the results go to the quarters number c1, c2 of dst. 

### `sevenPhases`

 The seven phases. 

### `strBody`

 strassen(dst, a, b, j, szt, p, scr). 

### `StrProg`

 The procedures of Strassen's algorithm stand in the program at their numbers. 

 ## The specification 

### `strScr`

 The scratch space of strassen at level j. 

### `strSteps`

 The steps of strassen at level j.  At level j + 1, with q = 4^j p: seven phases, each with a
recursive call and 92 q further steps, and the clearing of 4 q cells in 13 steps each, so that
696 = 7 · 92 + 4 · 13; the 900 covers the steps that do not depend on q. 

### `StrArgs`

 The arguments of strassen other than the level, with the data behind them: the operands `A` and
`B` have `len` numbers each, bounded by `α` and `β`, and the table of sizes reaches level `J`. 

### `StrArgs.vals`

 The values of the arguments of strassen at level j. 

### `StrPre`

 What strassen assumes at level j.  The operands have len = 4^j p numbers each.  They and the
table of sizes lie below dst, and dst lies below the scratch space. 

### `StrPre.keep`

 What strassen assumes still holds when no cell below dst has changed. 

### `StrSpec`

 What strassen does at level j, in the program P: it writes the product to dst and changes
nothing else but the scratch space. 

 ## A phase 

### `PhaseArgs`

 The arguments of phase other than the level, with the data behind them: the six lists that stand
at the six addresses, the bounds `α` and `β` on the operands, and the level `J` that the table of
sizes reaches. 

### `vals`

 The values of the arguments of phase at level j. 

### `S`

 The first operand of the product of the phase, S = A1 + sA A2. 

### `T`

 The second operand of the product of the phase, T = B1 + sB B2. 

### `prod`

 The product of the phase, M = S · T. 

### `inner`

 The arguments of the recursive call: S stands at scr, T at scr + q, the product goes to
scr + 2 q, and the scratch space begins at scr + 3 q. 

### `PhasePre`

 What a phase assumes at level j + 1.  The six lists have q = 4^j p numbers each.  All of them
and the table of sizes lie below the scratch space, and the two results do not meet. 

### `PhasePost`

 What a phase promises: s1 M has been added to the list at c1 and s2 M to the list at c2, and
nothing else has changed but the scratch space. 

### `length_prod`

 The product of a phase has q numbers. 

### `bound_nonneg`

 The bound of level j for operands that are sums of two is not negative. 

### `absLe_prod`

 The product of a phase is bounded by strassenBound p j (2 α) (2 β). 

### `space_inner`

 The scratch space of level j + 1: three lists of q numbers, and the scratch space of level j. 

### `keep`

 What a phase assumes still holds when no cell below scr has changed. 

### `inner`

 What the recursive call of a phase assumes, once the two operands stand in the scratch space. 

### `phaseOpnds_spec`

 **The operands of a phase.** 

### `phaseAccum_spec`

 **The end of a phase.** 

### `phase_meets`

 **A phase** adds s1 M to c1 and s2 M to c2, where M = (a1 + sA a2) · (b1 + sB b2), and changes
nothing else but the scratch space. 

 ## Between two phases 

### `PhaseRow`

 A row of the table of Strassen's seven products.  With a[t], b[t] and c[t] for the quarters
number t of the operands and of the result, the product is
M = (a[a1] + sA a[a2]) · (b[b1] + sB b[b2]), and s1 M is added to c[c1] and s2 M to c[c2]. 

### `PhaseRow.Ok`

 The entries of a row are numbers of quarters and signs, and the two results are different
quarters. 

### `StrArgs.phase`

 The arguments of the phase of a row, called from strassen with the arguments x, when a
quarter has q numbers and the four quarters of dst hold the lists L 0, …, L 3. 

### `StrArgs.after`

 The four lists after the phase of a row. 

### `StrInv`

 The state of strassen at level j + 1 after κ phases: what strassen assumes still holds, and the
four quarters of dst hold the lists L 0, …, L 3, of q = 4^j p numbers each, bounded by κ times the
bound on a product. 

### `quarter_apart`

 Two different quarters do not meet. 

### `forall_update_update`

 A property of the four lists after two of them have been replaced. 

### `size_eq`

 An operand has four quarters. 

### `phasePre`

 What the phase of a row assumes holds between two phases. 

### `step`

 The state after a phase: two of the four lists are replaced, the rest is as before. 

### `phase_step`

 **A phase, called from the body of strassen**: with M the product of the row, s1 M is added to
the list number c1 and s2 M to the list number c2. 

### `seg_of_quarters`

 Four lists of q numbers in the four quarters of a segment are one list. 

### `seg_zeros_quarter`

 A quarter of a cleared segment is cleared. 

 ## The seven phases 

### `sevenPhases_spec`

 **The seven phases** turn four cleared quarters into the product. 

 ## The two cases and the induction 

### `strassen_zero`

 **Level 0**: one product in the ring. 

### `strassen_succ`

 **Level j + 1**: clear the result, then the seven phases. 

### `strassen_spec`

 **Strassen's algorithm**, at every level. 
