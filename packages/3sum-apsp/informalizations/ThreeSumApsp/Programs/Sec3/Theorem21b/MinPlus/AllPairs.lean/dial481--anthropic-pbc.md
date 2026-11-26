---
{
  "module": "ThreeSumApsp/Programs/Sec3/Theorem21b/MinPlus/AllPairs.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Anthropic, PBC",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Programs/Sec3/Theorem21b/MinPlus/AllPairs.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Programs/Sec3/Theorem21b/MinPlus/AllPairs.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# All pairs with a witness, with an algorithm that finds a negative triangle

The middle step of [VW18, Theorem 4.2], one of the reductions behind Theorem 21(b).  Given three n ×
n matrices X, Y, V, the host marks all pairs (i, j) for which some k has X[i,k] + Y[k,j] < V[i,j].
It cuts the three ranges into p = ⌈n/s⌉ blocks of s = ⌈n^{1/3}⌉ indices and visits the p³ triples of
blocks.  In each round it forms the s × s × s instance of the current triple, with the weights
X[i,k], Y[k,j], and -V[i,j], or 2U + 1 if (i, j) is already marked, and asks the solver for a
negative triangle.  A triangle that comes back marks a new pair; if there is none, the host goes on
to the next triple. So there are at most p³ + n² rounds.  The last block of a range is moved back so
that it ends at n (blocks may overlap), so there are no padding vertices.

The result is isHost_pairs : IsHost findTask pairsTask pairsTime pairsNeed.  The proof goes from the
inside to the outside: the third matrix of an instance (mask_meets); one question (ask_meets, with
the instance askInst and the meaning AskPost of the answer); the parts of a round (off_spec,
mark_spec, advance_spec); what a round achieves (Progress.mark and Progress.next: less is left to
do); a round (round_spec, with the invariant PairsInv); the host (pairs_spec; when nothing is left
to do the marks are the answer, Progress.complete).


 ## The procedures 

### `Len`

 The local variables of mask: the arguments len, F (Large), ac (Mat), tmp (Flags), and the
counter q (Index). 

### `maskBody`

 mask(len, F, ac, tmp): for q < len, ac[q] := F if tmp[q] = 1, and ac[q] := -ac[q] otherwise. 

### `N`

 The local variables of ask: the arguments n, s (Side), F (Large), x, y, v, out, the offsets oI,
oK, oJ, and fr (Free); then s² (Area), and results that are not used. 

### `askBody`

 ask(n, s, F, x, y, v, out, oI, oK, oJ, fr): forms the instance of the triple of blocks at the
offsets oI, oK, oJ in the cells from fr (three matrices of s² cells; the block of marks is copied
behind them for a moment), and asks the solver for a negative triangle, with the place for the
answer at fr + 3s² and the free pointer fr + 3s² + 3.  The answer goes to local 0 and so is the
result. 

### `N`

 The local variables of allPairs: the arguments n, U, x, y, v, out, fr (Free); the side s of a
block and the number p of blocks; the numbers I, K, J of the three blocks and their offsets oI, oK,
oJ; F = 2U + 1 (Large); the address fr + 3s² of the solver's answer; the last result (Reply). 

### `offStmt`

 The offset of the block whose number is in the local src, into the local dst: I s, or n - s if
n < I s + s. 

### `advanceStmt`

 The next triple of blocks. 

### `markStmt`

 The pair that the solver has found is marked: out[(oI + a) n + (oJ + c)] := 1, where a and c
stand in the first and the third cell of the solver's answer. 

### `pairsRound`

 One round of allPairs: the offsets of the three blocks, the question, and then either a new mark
or the next triple of blocks. 

### `countStmt`

 p := ⌈n/s⌉, by counting up. 

### `pairsBody`

 allPairs(n, U, x, y, v, out, fr): s, p, F and the address of the solver's answer; no pair is
marked; then the rounds, from the first triple of blocks on. 

 ## Time and need 

### `maskTime`

 The number of steps of mask. 

### `askTime`

 The number of steps of ask, if the solver takes T. 

### `Pairs.roundTime`

 The number of steps of one round of allPairs: three offsets, the question, and a mark or the
next triple of blocks. 

### `pairsTime`

 **The number of steps of allPairs**, if the solver that finds negative triangles takes T: at
most p³ + n² rounds, with s = ⌈n^{1/3}⌉ (see cbrtLeast_eq_cbrtCeil) and p = ⌈n/s⌉, each with one
question at size s and bound 2U + 1. 

### `pairsNeed`

 **What allPairs needs**, if the solver needs r: the numbers up to 8n + 2U + 4, room for four
blocks and the solver's answer, three more levels of calls, and what the solver needs at the size
⌈n^{1/3}⌉ and the bound 2U + 1. 

### `pairsProcs`

 The procedures that the host appends to the program of a solver whose program has o procedures
and whose procedure number is p: copy, fill, subCopy, cbrtCeil, mask, ask, allPairs, with the
numbers o, …, o + 6. 

### `Ctx`

 The surroundings of allPairs: a solver that finds negative triangles, and the procedures that
the host adds. 

 ## The third matrix of an instance 

### `mask_meets`

 **mask** turns the block A of V held at ac into the third matrix of the instance, with the block
O of marks held at tmp, and changes nothing else. 

 ## One question 

### `askInst`

 The instance of the triple of blocks at the offsets oI, oK, oJ, with its three matrices at fr,
fr + s², fr + 2s² and the place for the answer behind them: the weights X[i,k], Y[k,j], and -V[i,j],
or 2U + 1 if the pair (i, j) is marked in O. 

### `askInst_pre`

 It is an instance, once its three matrices stand at their places. 

### `AskPost`

 What ask returns: 0, and in the triple of blocks every pair with a witness is marked; or 1, and
the cells res and res + 2 hold a and c such that (oI + a, oJ + c) is an unmarked pair with a
witness. 

### `askPost_of_post`

 What the answer of the solver means for the triple of blocks. 

### `ask_meets`

 **ask** asks the solver about the triple of blocks at the offsets oI, oK, oJ, and changes no
cell below the free pointer. 

 ## The parts of a round 

### `locals`

 The local variables of allPairs during the rounds, as a list. 

### `Next`

 (I', K', J') is the triple of blocks after (I, K, J); after the last triple comes (p, 0, 0). 

### `advance_spec`

 advanceStmt goes on to the next triple of blocks. 

### `off_spec`

 offStmt puts the offset of block number I into the local dst and changes nothing else.  The text
is used for three pairs of locals, so this is stated like a rule, for any list l of locals and any
Q: h says that Q holds of the state afterwards, and in a proof it is the goal that remains. 

### `mark_spec`

 markStmt marks the pair (oI + a, oJ + c), where a and c stand in the solver's answer. 

 ## The invariant 

### `Progress`

 How far the rounds have come: the marks O are right, and in the triples of blocks before
(I, K, J) every pair with a witness is marked. 

### `todo`

 What is left to do: the number of triples of blocks from (I, K, J) on, plus the number of
unmarked pairs. 

### `Progress.mark`

 A new mark on a pair with a witness: less is left to do. 

### `Progress.next`

 The current triple of blocks is done, and the next one comes: less is left to do. 

### `PairsInv`

 The state between two rounds: the marks stand at out, and below the free pointer no other cell
has changed. 

### `pairsVar`

 What is left to do, read off the state. 

### `Lim`

 What the limits have to allow for: the need of the solver behind three matrices and its answer,
two levels further down; room for four blocks; the numbers up to 8n + 2U + 4; three levels of
calls. 

 ## A round 

### `round_spec`

 One round keeps the invariant, and afterwards less is left to do. 

 ## The host 

### `count_spec`

 countStmt puts p = ⌈n/s⌉ into its local and changes nothing else.  It is stated like off_spec,
for any list l of locals and any Q. 

### `eq_pairFlags`

 The list of marks is the list of flags of the task, when it holds the right flag for every
pair. 

### `Progress.complete`

 **When no triple of blocks is left, the marks are the answer.** 

### `todo_start`

 At the beginning all p³ triples of blocks and all pairs are left. 

### `progress_start`

 At the beginning no pair is marked, and no triple of blocks has been visited. 

### `lim_of_ok`

 What allPairs needs covers what the rounds need. 

### `roundTime_le`

 A round, with the test of the loop (4 steps). 

### `time_le`

 The steps of allPairs add up to at most pairsTime: cbrtCeil takes 12 s steps, countStmt 10 p,
fill 13 n², the other statements before the rounds 56 in all, and there are at most p³ + n² rounds,
each with the test of the loop. 

### `pairs_spec`

 **allPairs** solves the task. 

 ## The need 

### `polyNeed_pairs`

 The need of allPairs is polynomially bounded if the need of the solver is. 

### `isHost_pairs`

 **The middle step of [VW18, Theorem 4.2]: all pairs with a witness, from finding a negative
triangle.** 
