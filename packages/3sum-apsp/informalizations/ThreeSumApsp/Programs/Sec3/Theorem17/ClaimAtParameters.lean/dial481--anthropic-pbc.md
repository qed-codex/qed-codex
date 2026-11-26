---
{
  "module": "ThreeSumApsp/Programs/Sec3/Theorem17/ClaimAtParameters.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Anthropic, PBC",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Programs/Sec3/Theorem17/ClaimAtParameters.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Programs/Sec3/Theorem17/ClaimAtParameters.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# Theorem 17 for programs of the light language, with the two choices of parameters of Section 3.3

Theorem 17 reduces Exact Triangle to at most `4ng` instances of Lop-AE-SparseTri(n, D). As
a claim about programs: from every solver of Lop-AE-SparseTri there is a solver of Exact Triangle
whose time obeys the bound of the theorem, here with Strassen's algorithm for the matrix product
(`Claim.Theorem_17` with `strassen`).  The program is the host `et17`.

The host takes the procedures that compute `D` from `n` and `g` from `D` as parameters.  Here they
are the routines for the two choices of the proof of Theorem 19: "Let D be the largest power of four
with D ≤ n^{1/18} [...] and let g := ⌈D^{1/36}⌉", and "Let D := ⌊n^{1/18}⌋ and g := ⌈D^{0.0315}⌉".
The program is the solver's program, followed by the parameter routines (`paramProcs`), followed by
the procedures of the host.

1. The four routines are parameter procedures in the sense of the host (`paramProc_d5`,
   `paramProc_g5`, `paramProc_d26`, `paramProc_g26`).
2. The parameters and the numbers that the routines form are polynomially bounded
   (`polyBounded_paramD₅Nat`, `polyBounded_paramG₅Nat`, `polyBounded_wD5`, `polyBounded_wG5`,
   and the same for the second choice).  So the need of the host (word size, cells, depth of calls)
   is polynomially bounded if that of the solver is (`hostNeed_poly`).  With `et17_solves` this
   makes the host turn solvers into solvers (`host_of_paramProcs`).
3. The routines take `O(n)`, respectively `O(D)`, steps (`steps_tD5`, `steps_tG5`, `steps_tD26`,
   `steps_tG26`).  So the time of the host obeys the bound of the theorem (`obeysBound17_hostTime`).
   Together: `claim_theorem_17₅` and `claim_theorem_17₂₆`.


 ## The parameter routines 

### `paramProcs`

 The six parameter routines, placed behind a program of length `o`, at the numbers `o`, …,
`o + 5`.  The arguments are the numbers of the routines that a routine calls. 

### `wD26`

 A bound on the numbers that `d26Body` forms. 

### `wD5`

 A bound on the numbers that `d5Body` forms. 

### `wG5`

 A bound on the numbers that `g5Body` forms. 

### `wG26`

 A bound on the numbers that `g26Body` forms.  It looks for the least `g` with `g^2000 ≥ D^63`,
since `0.0315 = 63/2000`. 

### `paramProcs_get`

 The routine number `i` stands at the place `Q.length + i` of the whole program. 

### `paramProc_d26`

 `d26Body` computes `⌊n^{1/18}⌋`. 

### `paramProc_d5`

 `d5Body` computes the largest power of four that is at most `n^{1/18}`. 

### `paramProc_g5`

 `g5Body` computes `⌈D^{1/36}⌉`. 

### `paramProc_g26`

 `g26Body` computes `⌈D^{0.0315}⌉`. 

 ## The parameters and the words are polynomially bounded 

### `polyBounded_paramD₂₆Nat`

 `⌊n^{1/18}⌋ ≤ n`. 

### `polyBounded_paramD₅Nat`

 The largest power of four that is at most `n^{1/18}` is at most `⌊n^{1/18}⌋`; the `+ 1` serves
`n = 0`. 

### `polyBounded_paramG₅Nat`

 `⌈D^{1/36}⌉ ≤ D`; the `+ 1` serves `D = 0`. 

### `polyBounded_paramG₂₆Nat`

 `⌈D^{0.0315}⌉ ≤ D`; the `+ 1` serves `D = 0`. 

### `polyBounded_wD26`

 The numbers of `d26Body`. 

### `polyBounded_wD5`

 The numbers of `d5Body`. 

### `polyBounded_wG5`

 The numbers of `g5Body`. 

### `polyBounded_wG26`

 The numbers of `g26Body`. 

 ## The time of the parameter routines 

### `steps_paramD₂₆Nat`

 `⌊n^{1/18}⌋ ≤ n`. 

### `steps_tD26`

 `d26Body` takes a constant number of steps for each number up to `⌊n^{1/18}⌋ + 1`. 

### `steps_tD5`

 `d5Body` calls `d26Body` and then multiplies by four `⌊log₄ ⌊n^{1/18}⌋⌋` times. 

### `steps_tG5`

 `g5Body` takes a constant number of steps for each number up to `⌈D^{1/36}⌉ ≤ D`. 

### `steps_tG26`

 `g26Body` takes a constant number of steps for each number up to `⌈D^{0.0315}⌉ ≤ D`. 

 ## The host with parameter routines 

### `host_of_paramProcs`

 The host over two of the parameter routines, at the places `i` and `j` of `paramProcs`, turns a
solver of Lop-AE-SparseTri into a solver of Exact Triangle and keeps the need polynomial. 

### `claim_theorem_17₅`

 **Theorem 17** for programs of the light language, with D "the largest power of four with D ≤
n^{1/18}" and "g := ⌈D^{1/36}⌉". 

### `claim_theorem_17₂₆`

 **Theorem 17** for programs of the light language, with "D := ⌊n^{1/18}⌋ and g :=
⌈D^{0.0315}⌉". 
