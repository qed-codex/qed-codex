---
{
  "module": "ThreeSumApsp/Programs/Sec3/Theorem21b/NegativeTriangle/Host.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Anthropic, PBC",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Programs/Sec3/Theorem21b/NegativeTriangle/Host.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Programs/Sec3/Theorem21b/NegativeTriangle/Host.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# Negative Triangle from Exact Triangle, as a host

[VW13, Theorem 3.3] in the form needed for Theorem 21(b): whether an instance with weights in
[−U, U] has a negative triangle is decided by asking O(log U) times whether there is a zero
triangle, each time after changing the weights, edge by edge, to numbers of absolute value O(U).

nt(n, U, ab, bc, ac, fr) computes L, the least number with 2^L > 6U, writes the shifted and doubled
weights 2(w(a,b) + U), 2(w(b,c) + U), 2(2U − w(a,c)) into an array r of 3n² cells, and zeros into an
array q of 3n² cells.  Then it makes L rounds.  A round moves one more bit of every number from r to
q (prefDown), so that q holds the prefixes of the level ℓ = L − 1, L − 2, …, 0; then, for e = 2 and
for e = 3, it writes e minus the prefixes of the third matrix to an array of n² cells and asks the
solver of Exact Triangle.  The answer is 1 if one of the 2L answers is 1.

The text is cut into parts, and each part has its lemma: `NegHost.init_spec`, `pow_spec`,
`fill_spec`, `probe_spec` (one question), `round_spec`, `rounds_spec`; `NegHost.nt_spec` puts them
together, and `isHost_nt` is the result.


 ## The text 

### `Verts`

 The number n of vertices. 

### `Bound`

 The bound U on the weights. 

### `MatAB`

 The address of the first matrix. 

### `MatBC`

 The address of the second matrix. 

### `MatAC`

 The address of the third matrix. 

### `PreAB`

 The free pointer, where the array q begins: its first part. 

### `Cells`

 n². 

### `Power`

 2^L. 

### `Levels`

 The number L of levels. 

### `Round`

 The number of the round. 

### `Ans`

 The answer so far. 

### `Res`

 The result of a call. 

### `Bound6`

 6U. 

### `RestAB`

 The first part of the array r. 

### `Third`

 The array for the third matrix of a question. 

### `SolverFree`

 The free pointer for the solver. 

### `PreAC`

 The third part of the array q. 

### `PreBC`

 The second part of the array q. 

### `Cells3`

 3n². 

### `RestBC`

 The second part of the array r. 

### `RestAC`

 The third part of the array r. 

### `ntInit`

 The beginning of nt: sizes and addresses. 

### `ntPow`

 The number of levels L and the power 2^L, by doubling. 

### `ntFill`

 The arrays r and q at the top level. 

### `ntProbe`

 One question to the solver of Exact Triangle: the third matrix for the exact value e, the call,
and the note of a positive answer. 

### `ntRound`

 One round: the next level, and its two questions. 

### `ntRounds`

 The L rounds. 

### `ntBody`

 nt(n, U, ab, bc, ac, fr). 

### `ntLevels`

 The number of levels: for U ≥ 1, the least L with 2^L > 6U. 

### `ntTime`

 The time of nt, if the solver of Exact Triangle takes T n U steps. 

### `ntNeed`

 The need of nt, if the solver of Exact Triangle needs r n U. 

 ## The local variables and the hypotheses 

### `locals`

 The locals of nt after its beginning.  The last five arguments are those that change later: the
power of two, the number of levels, the number of the round, the answer so far and the result of the
last call.  Local 13 is not used and stays 0. 

### `Ctx`

 The program has the solver and the two loops over arrays, the instance is as the task
prescribes, and the limits allow for the need of nt. 

### `Ctx.places`

 The arithmetic facts of the hypotheses as one conjunction: what the limits allow, and that the
three matrices have n² ≥ 1 entries each and lie below the free pointer. 

### `Ctx.affine_meets`

 **affine** as a procedure, for a source and a destination that lie apart, below the free pointer
of the solver. 

 ## The beginning 

### `init_spec`

 **The beginning of nt** sets the sizes and the addresses. 

### `PowInv`

 The state of the loop that doubles after i rounds: Power = 2^i and Levels = i. 

### `pow_spec`

 **The loop that doubles** computes the number L of levels and 2^L. 

 ## The memory 

### `NtMem`

 The memory of nt at the level ℓ: the array q holds the prefixes, the array r the rests, and
nothing below the free pointer has changed. 

### `negStart_range`

 The numbers at the start are between 0 and 6U, and below 2^L. 

### `seg_negStart`

 The three shifted and doubled matrices, one after the other, are the array r at the start. 

### `fits_of_absLe`

 The products and the sums that are formed in the first three calls of affine fit in a word. 

### `fill_spec`

 **The four calls of affine** fill the arrays r and q for the top level. 

 ## One question 

### `question`

 The instance of Exact Triangle for the level ℓ and the exact value e, as it lies in the arrays
of nt. 

### `NtYes`

 The instance of Exact Triangle for the level ℓ and the exact value e has a zero triangle. 

### `prefQ_range`

 The prefixes are between 0 and 6U. 

### `seg_parts`

 The three parts of the array q. 

### `question_pre`

 The question is an instance of Exact Triangle as the task prescribes. 

### `St`

 The state of nt between two steps of a round: the locals, with some result of the last call,
and the memory at the level ℓ. 

### `ntMem_of_question`

 The arrays q and r and the cells below the free pointer survive a question. 

### `probe_spec`

 **One question** leaves the arrays as they are, and sets Ans to 1 if the instance for the level
ℓ and the exact value e has a zero triangle. 

 ## The rounds 

### `NtFound`

 One of the questions at the levels from ℓ₀ on has the answer yes. 

### `St.round`

 The number of the round can be read and changed. 

### `down_pre`

 What prefDown needs holds at every level above 0. 

### `round_spec`

 **One round**: from the level ℓ + 1 to the level ℓ, and the two questions at the level ℓ. 

### `rounds_spec`

 **The L rounds**: in the end Ans says whether one of the questions at the levels below L was
answered yes. 

 ## The procedure 

### `nt_spec`

 **nt is correct**, in every program that begins with the solver's program and has the two loops
over arrays. 

### `polyNeed_ntNeed`

 The need of nt is polynomially bounded if the need of the solver is. 

### `isHost_nt`

 **Negative Triangle from Exact Triangle**: from every solver of Exact Triangle, the three
procedures affine, prefDown, nt make a solver of Negative Triangle. 
