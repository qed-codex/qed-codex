---
{
  "module": "ThreeSumApsp/Programs/Sec5/Corollary39/ZeroWeight/Host.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Anthropic, PBC",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Programs/Sec5/Corollary39/ZeroWeight/Host.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Programs/Sec5/Corollary39/ZeroWeight/Host.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# Corollary 39, weight zero, in the light language: the host

Proof of Corollary 39: "We enumerate the n^t ways of fixing one vertex in each of the first t parts,
and for each of them we build H", and ask an arbitrary solver of Exact Triangle whether H has a
triangle of weight zero.  The number k of parts is fixed before the program is written.

kc(n, U, g, fr): the weights stand at g; the result is 1 if some k-clique has total weight zero, and
0 if not (`kcTask`).  `kcRound_spec` is one round: build H (`buildH_spec`), ask the solver, note the
answer and go to the next choice (`noteAnswer_spec`); `kc_spec` is the loop over the n^t choices,
with the invariant `KcInv`; `isHost_kc` puts it in the form of a host, with the time `kcTime` and
the need `kcNeed`.

Only weight zero is treated here; minimum and maximum weight have a host of their own.  The running
time n^{k - ε⌊k/3⌋} is derived from `kcTime` where the host is put together with the solver of
Theorem 19.

The names of the local variables that both hosts for k-Clique use are in the namespace `KC`, those
of this host in `ZeroKc`; `kcLocals` lists the locals of this host with their values before a round.


 ## The program 

### `Result`

 The result of the host: a procedure returns what local 0 holds at its end. 

### `Free`

 The free pointer. 

### `Found`

 1 if a triangle of weight zero has been found, 0 if not. 

### `noteAnswer`

 The result becomes 1 if the answer of the solver is 1; then the next choice. 

### `kcRound`

 One choice of the fixed vertices: build H, ask the solver (procedure pe), note the answer, go to
the next choice. 

### `kcBody`

 kc(n, U, g, fr). 

### `roundT`

 The time of one round. 

### `kcTime`

 The time of the host. 

### `kcNeed`

 What the host needs.  Words: what the solver needs, the largest weight of H, and the sizes.
Cells: the k chosen vertices, the three matrices, and what the solver needs.  Depth of calls: one
more than the solver. 

 ## The host is correct 

### `ZeroAt`

 The graph H of the choice number F has a triangle of weight zero. 

### `hasZeroClique_iff`

 Some k-clique has weight zero exactly if for some choice of the fixed vertices the graph H has a
triangle of weight zero. 

### `kcLocals`

 The locals of the host before the round for the choice number F of the fixed vertices.  `found`
is the result so far. 

### `kcScratch`

 The locals of the host whose values do not matter between two rounds. 

### `KcInv`

 The state before the round for the choice number F of the fixed vertices: the locals of the
host, with a result that tells whether an earlier choice had a triangle of weight zero; the input;
and the chosen vertices. 

### `flag_exists_lt_succ_of_not`

 The result after one more choice, if this choice has no triangle of weight zero. 

### `noteAnswer_spec`

 **The answer is noted**, and the next choice is made. 

### `kcRound_spec`

 **One round of the host**: H is built for the choice number F, the solver is asked, the result
becomes 1 if the answer is yes, and the next choice is made. 

### `kc_spec`

 **The host solves Zero-Weight k-Clique.** 

 ## The host, in the form that all hosts have 

### `polyNeed_kcNeed`

 The need of the host is polynomially bounded if the need of the solver is. 

### `isHost_kc`

 **Zero-Weight k-Clique from Exact Triangle** (Corollary 39): the host makes a solver of
Zero-Weight k-Clique from every solver of Exact Triangle. 
