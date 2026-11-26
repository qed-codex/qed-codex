---
{
  "module": "ThreeSumApsp/Programs/Sec3/Theorem21b/MinPlus/FindNegativeTriangle.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Anthropic, PBC",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Programs/Sec3/Theorem21b/MinPlus/FindNegativeTriangle.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Programs/Sec3/Theorem21b/MinPlus/FindNegativeTriangle.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# Finding a negative triangle with an algorithm that decides whether there is one

[VW18, Lemma 4.1], a step of [VW18, Theorem 4.2], one of the reductions behind Theorem 21(b).
The host asks the solver of Negative Triangle about the whole instance.  If the answer is yes, it
keeps three offsets and a side length h such that the h × h × h sub-instance at these offsets has a
negative triangle.  While h > 1 it puts h' = ⌈h/2⌉, asks about the eight sub-instances of side h'
made of the lower half [o, o + h') or the upper half [o + h - h', o + h) of each of the three
ranges, and goes on with one for which the answer is yes.  All eight questions are asked, and the
last yes counts.

The result is isHost_find : IsHost ntTask findTask findTime findNeed.  The proof goes from the
inside to the outside: one question (probe_meets: three calls of subCopy, one of the solver); the
questions of a round (try_spec and tries_spec, with the invariant TryInv); a round (round_spec; that
one of the eight answers is yes is NegAt.split); the rounds (loop_spec, with the invariant LoopInv);
the search and the host (search_spec, find_spec).


 ## The procedures 

### `N`

 The local variables of probe: the arguments n, U, ab, bc, ac, the offsets a0, b0, c0, the side
h and fr (Free); then h² (Area), and the results of subCopy, which are not used. 

### `probeBody`

 probe(n, U, ab, bc, ac, a0, b0, c0, h, fr): copies the three h × h blocks of the sub-instance at
the offsets a0, b0, c0 to fr, fr + h², fr + 2h², and asks the solver of Negative Triangle about
them, with the free pointer fr + 3h².  The answer goes to local 0 and so is the result. 

### `N`

 The local variables of find: the arguments n, U, ab, bc, ac, res (Answer), fr (Free); the
offsets a0, b0, c0 and the side length h of the current sub-instance; the next side length h' (Half)
and δ = h - h' (Shift); the offsets na, nb, nc of the last sub-instance with the answer yes; the
last answer of probe or of the solver (Reply). 

### `tryStmt`

 One question of a round of find: about the sub-instance of side h' whose offsets are those of
the round, moved by δ where the triple t has a 1.  If the answer is yes, the offsets are noted in
na, nb, nc. 

### `triesStmt`

 The questions for a list of triples, one after the other. 

### `halfStmt`

 h' := ⌈h/2⌉, by counting up. 

### `roundStmt`

 One round of find: h' = ⌈h/2⌉, δ = h - h', the eight questions, the new offsets and the new
side length. 

### `searchStmt`

 The search of find, once it is known that there is a negative triangle: rounds until the side
length is 1; then the offsets are the triangle, and the result is 1. 

### `findBody`

 find(n, U, ab, bc, ac, res, fr): asks about the whole instance; the result is 0 if the answer is
no, and else the search begins. 

 ## Time and need 

### `probeTime`

 The number of steps of probe, if the solver takes T. 

### `tryTime`

 The number of steps of one question of a round, with the test of the answer. 

### `roundBound`

 A bound on the number of steps of the round that goes to the side length h: eight questions,
each with the copying of three blocks. 

### `findTime`

 **The number of steps of find**, if the solver of Negative Triangle takes T: one question at
size n, and one round for each side length of the chain ⌈n/2⌉, ⌈⌈n/2⌉/2⌉, …, 1. 

### `findNeed`

 **What find needs**, if the solver needs r: room for three blocks, three more levels of calls,
and what the solver needs at any size up to n. 

### `findProcs`

 The procedures that the host appends to the program of a solver whose program has o procedures
and whose procedure number is p: copy, subCopy, probe, find, with the numbers o, o + 1, o + 2,
o + 3. 

 ## The surroundings 

### `Ctx`

 The surroundings of find: a solver of Negative Triangle, and the procedures probe, subCopy, copy
in the program. 

### `ok_sub`

 What find needs covers what the solver needs at a size h ≤ n, behind three blocks and up to
three levels further down. 

### `word_depth_of_ok`

 What find needs covers the numbers up to n + 2 and three levels of calls. 

 ## One question 

### `subInst`

 The sub-instance of side h at the offsets a0, b0, c0, with its three blocks at fr, fr + h² and
fr + 2h². 

### `subInst_pre`

 The sub-instance is an instance, once its three blocks stand at their places. 

### `probe_meets`

 **probe** returns 1 if the sub-instance of side h at the offsets a0, b0, c0 has a negative
triangle, and 0 if not, and changes no cell below the free pointer. 

 ## The questions of a round 

### `TryInv`

 The state during the questions of a round: na, nb, nc are offsets of a sub-instance of side h',
and if Done holds (one of the questions asked so far had the answer yes), that sub-instance has a
negative triangle.  No cell below the free pointer has changed. 

### `NegOct`

 The sub-instance that the triple t stands for has a negative triangle. 

### `try_spec`

 **One question** keeps the invariant, and notes the offsets of its sub-instance if the answer is
yes. 

### `tries_spec`

 The questions for a list of triples keep the invariant: afterwards na, nb, nc are the offsets of
a sub-instance with a negative triangle, if one of the triples stands for such a sub-instance. 

 ## A round, and the search 

### `LoopInv`

 The state between two rounds: the sub-instance of side h at the offsets a0, b0, c0 has a
negative triangle, and no cell below the free pointer has changed.  The six locals that a round uses
hold anything. 

### `half_spec`

 halfStmt puts ⌈h/2⌉ into h' and changes nothing else. 

### `roundTime`

 The number of steps of the round that goes to the side length h'. 

### `round_spec`

 **One round** goes from a sub-instance of side h ≥ 2 with a negative triangle to one of side
⌈h/2⌉. 

### `loopTime`

 The number of steps of the search from the side length h on. 

### `loop_spec`

 The rounds end with a sub-instance of side 1 that has a negative triangle. 

 ## The host 

### `search_spec`

 **The search** finds a negative triangle if there is one. 

### `find_spec`

 **find** returns 1 and writes a negative triangle to the cells from `res` if there is one, and
returns 0 if there is none (`findTask`), within `findTime` steps. 

 ## The need 

### `polyNeed_find`

 The need of find is polynomially bounded if the need of the solver is. 

### `isHost_find`

 **[VW18, Lemma 4.1]: finding a negative triangle from deciding whether there is one.** 
