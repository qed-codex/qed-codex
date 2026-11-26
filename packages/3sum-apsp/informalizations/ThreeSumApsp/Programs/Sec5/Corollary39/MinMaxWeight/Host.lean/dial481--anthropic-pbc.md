---
{
  "module": "ThreeSumApsp/Programs/Sec5/Corollary39/MinMaxWeight/Host.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Anthropic, PBC",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Programs/Sec5/Corollary39/MinMaxWeight/Host.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Programs/Sec5/Corollary39/MinMaxWeight/Host.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# Corollary 39, minimum and maximum weight: the host

Proof of Corollary 39: "We enumerate the n^t ways of fixing one vertex in each of the first
t parts, and for each of them we build H as above from the remaining 3⌊k/3⌋ parts; now the triangles
of H correspond to the k-cliques through the t fixed vertices."  And: "We give H edge weights so
that a triangle and its k-clique have the same weight."  So a best triangle over the n^t graphs H
gives a best k-clique (`opt_of_best`, from `Corollary39.S_graphH_eq_cliqueWeight`).

This file has the reduction from Max-Weight (Min-Weight) k-Clique to Max-Weight (Min-Weight)
Triangle, as a procedure that calls an arbitrary solver of the triangle problem (`isHost_maxKc`,
`isHost_minKc`).  Where such a solver comes from ([VW13, Theorem 3.3], and the negated weights for
the minimum) is not the subject of this file.  The two hosts are one program with a flag mx, true
for the maximum and false for the minimum; the host for the minimum calls a solver of Min-Weight
Triangle.

The route.
* Set-up: `hostSetup`, the free pointer for the solver, and a weight that every triangle beats.
* A round takes the invariant `OptInv` from F to F + 1 (`optRound_spec`): `buildH` writes H; the
  solver writes a best triangle of H to three cells (`triangleAt_of_answer`); `readTriangle` adds up
  its weight; `keepBetter` compares it with the best weight of the earlier rounds (`BestSo.keep`,
  `BestSo.replace`); `nextChoice` goes on (`endOfRound_spec`).
* The end (`optDecode_spec`).  The paper does not speak of this step: the solver returns vertices of
  H as numbers below N, and the k vertices of the clique are their digits in base n.  The host
  writes them by counting up with odometers (`countUp_spec`, `decode_spec`), in O(k (n^t + N))
  steps, against more than n^t N² steps for the rounds.
`opt_spec` puts the three together.

The names of the local variables that both hosts for k-Clique use are in the namespace `KC`, those
of this host in `OptKc`, and `optLocals` lists all of them with their values before a round.

In the texts of programs the number of parts is called kk, because k is the constant of the
language.


 ## The local variables 

### `Dest`

 The address of the k cells for the clique. 

### `Free`

 The free pointer, at the start of the host.  `hostSetup` uses the same local as `Side`. 

### `Count`

 The counter of `countUp`.  `fillMat` uses the same local as `Row`. 

### `BestWeight`

 The weight of the best triangle so far. 

### `BestRound`

 The number of the round of the best triangle so far. 

### `BestA`

 The first vertex of the best triangle so far. 

### `BestB`

 The second vertex of the best triangle so far. 

### `BestC`

 The third vertex of the best triangle so far. 

### `SolverFree`

 The free pointer for the solver. 

### `TriA`

 The first vertex of the triangle of this round. 

### `TriB`

 The second vertex of the triangle of this round. 

### `TriC`

 The third vertex of the triangle of this round. 

### `TriWeight`

 The weight of the triangle of this round. 

 ## Counting up 

### `countUp`

 The odometer of len digits at base + j (base is local vb) is moved on as many times as local vt
says. 

### `countUp_assigns`

 `countUp` assigns only `Count`. 

### `countUp_spec`

 **countUp** turns zeros into the digits of the number in local vt; val (14 len + 13) + 6 steps.


 ## Comparing weights 

### `better_trans`

 Being at least as good is transitive. 

### `better_of_not`

 Of two weights one is at least as good as the other. 

### `cmpE`

 The weight of the triangle of this round is strictly better than the best weight so far. 

### `cmpE_cost`

 The test costs three steps. 

### `cmpE_safe`

 The test is safe. 

### `cmpE_holds`

 The test holds if and only if the best weight so far is not at least as good as the weight of
this round. 

### `sentinel`

 A weight that is worse than the weight of every triangle of H. 

### `sentinelE`

 The expression whose value is `sentinel kk U mx`. 

### `sentinelE_cost_le`

 The expression costs at most seven steps. 

### `sentinelE_safe_val`

 The expression is safe and has the value sentinel kk U mx. 

### `not_better_sentinel`

 No weight of a triangle of H is beaten or matched by the sentinel. 

 ## The program 

### `readTriangle`

 Read the triangle that the solver has found from the three cells behind the matrices of H, and
add up its weight from the three matrices. 

### `keepBetter`

 Keep the triangle of this round if it is strictly better than the best so far. 

### `endOfRound`

 The end of a round. 

### `optRound`

 One choice of the fixed vertices: build H, let the solver (procedure pe) find a best triangle,
then endOfRound. 

### `decodeStmt`

 The number of the best round and the three vertices of the best triangle are turned into their
digits in base n, in the kk cells for the clique. 

### `optBody`

 optKc(n, U, g, res, fr). 

### `optRoundT`

 The time of one round: the three matrices of H, the solver, and the end of the round. 

### `optTime`

 The time of the host: n^t rounds, each with the test of the loop; the decoding, at most n^t + 3
N steps of an odometer; the set-up. 

### `optNeed`

 What the host needs.  Words: what the solver needs, three times the largest weight of H and one
more (the sentinel), and the sizes.  Cells: the k chosen vertices, the three matrices, the three
cells for the triangle, and what the solver needs.  Depth of calls: one more than the solver. 

 ## The best triangle so far 

### `Best`

 What the host holds in `BestWeight` to `BestC`: the weight of a triangle, the number of its
round, and its three vertices. 

### `bestOf`

 The triangle (a, b, c) of the graph H of the choice number Fb, as the host holds it. 

### `Beats`

 The weight w is at least as good as that of every triangle of the choices number 0, …, F - 1. 

### `BestSo`

 What the host holds before round F: before the first round the weight is the sentinel; later it
holds a triangle that is at least as good as all triangles of the earlier rounds. 

### `Beats.succ`

 A weight that is at least as good as all triangles of the choices below F and of the choice
number F is at least as good as all triangles of the choices below F + 1. 

### `BestSo.keep`

 **The old triangle stays** if it is at least as good as a best triangle (a, b, c) of round F. 

### `BestSo.replace`

 **A best triangle (a, b, c) of round F takes the place of the old one** if the old one is not at
least as good: it beats the old one, and so all that the old one beat. 

 ## The answer of the solver 

### `TriangleAt`

 **The answer of the solver in the memory.**  The triangle (a, b, c) stands in the three cells
behind the matrices of H.  The matrices hold the weights of the graph G, and the three weights of
the triangle are at most L in absolute value. 

### `TriangleAt.abs_S_le`

 The weight of the triangle is at most 3 L in absolute value. 

### `findPre_of_triPre`

 Three cells behind an instance of a triangle problem are a place for the answer. 

### `triangleAt_of_answer`

 **What the answer of the solver means.**  The solver was asked in the memory μ and has left the
memory μ', with the triangle (a, b, c) in the three cells behind the matrices of H.  Then μ' holds
the answer, for the graph whose matrices stand in μ. 

 ## The locals of the host 

### `optLocals`

 The locals of the host before round F, with the best triangle so far. 

### `optScratch`

 The locals of the host whose values do not matter between two rounds. 

### `OptInv`

 Before round F of the host: the locals, with the best triangle of the earlier rounds; the cells
below fr are as at the start; and the fixed vertices are those of the choice number F. 

 ## The end of a round 

### `toNat_entry`

 The place of an entry of a matrix, as the program computes it. 

### `readTriangle_spec`

 **readTriangle** puts a, b, c and the weight of the triangle into `TriA` to `TriWeight`. 

### `keepBetter_spec`

 **keepBetter** copies the weight, the number of the round and the triangle of this round into
`BestWeight` to `BestC` if the weight is strictly better than the best so far, and changes nothing
if not. 

### `optNext_spec`

 **nextChoice** leads to the invariant for round F + 1, if the best triangle of the rounds up to
F is in its place. 

### `endOfRound_spec`

 **endOfRound** reads the answer of the solver, a best triangle (a, b, c) of round F, keeps it if
it is strictly better than the best so far, and goes to the choice number F + 1. 

 ## A round 

### `optRound_spec`

 **One round of the host** takes the invariant from F to F + 1. 

 ## Decoding 

### `DecodedTo`

 The first j of the kk cells at res hold the vertices vf, the others hold 0. 

### `DecodeOk`

 What the decoding needs of the limits. 

### `countUp_decoded`

 **One odometer of the decoding.**  If the next len vertices are the digits of the number val in
local vt, countUp writes them. 

### `vtx_digits`

 The vertices of the clique in the fixed parts and in the three groups are digits of the four
numbers. 

### `decode_spec`

 **decodeStmt** writes the clique that is given by the number Fb of the best round and the best
triangle (a, b, c). 

### `opt_of_best`

 The clique that belongs to the best triangle is a best clique. 

 ## The host 

### `optDecode_spec`

 **After the last round** decodeStmt writes a best clique. 

### `opt_spec`

 **The host finds a k-clique of maximum (minimum) total weight.** 

 ## The host as a reduction between tasks 

### `polyNeed_optNeed`

 The need of the host is polynomially bounded if the need of the solver is. 

### `isHost_opt`

 **Max-Weight (Min-Weight) k-Clique from Max-Weight (Min-Weight) Triangle** (Corollary 39). 

### `isHost_maxKc`

 **Max-Weight k-Clique from Max-Weight Triangle** (Corollary 39). 

### `isHost_minKc`

 **Min-Weight k-Clique from Min-Weight Triangle** (Corollary 39). 
