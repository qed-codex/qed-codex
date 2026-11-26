---
{
  "module": "ThreeSumApsp/Programs/Sec3/Theorem17/Host/Text.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Anthropic, PBC",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Programs/Sec3/Theorem17/Host/Text.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Programs/Sec3/Theorem17/Host/Text.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# The host of Theorem 17: the top procedure

The host procedure et17(n, U, ab, bc, ac, fr) decides Exact Triangle with the help of an arbitrary
solver of Lop-AE-SparseTri (proof of Theorem 17).  It computes the parameters `D` and `g` by two
procedures that are parameters of the construction, and `s = ⌊√D⌋`.  For small `n`
(`D < 16`, `n < D`, `g < 1` or `s < g`) it runs the brute force.  Otherwise it chooses the prime,
computes the largest number of query pairs, the number of vertices of a piece and the number of
pieces, lays out its arrays from the free pointer on, computes the residues of the weights, sorts
the pairs `(a, b)` into classes, cuts the classes into chunks, and runs the loop over the instances.

This file holds the program (`et17Body`), its time and its need (`hostTime`, `hostNeed`), what it
assumes about the program around it (`Et17Ctx`), and the data, the addresses and the local variables
of a run.

**The way through the files on the host**, each named by its main result.

1. The instances as data, with no program in sight: what the host writes, what the solver answers
   and which scans succeed (`HostData`); a zero triangle is found if and only if there is one
   (`HostData.found_m`); a failed scan belongs to a false positive of its own
   (`HostData.sum_fails_le`); there are at most 4ng instances (`HostData.m_le`).
2. The loop over the instances (`hostLoop_spec`).
3. The text of the top procedure (this file), in three parts and the small case.
4. The parts: the parameters and the small case (`et17Params_spec`, `et17Small_spec`); the prime,
   the sizes and the addresses (`et17Sizes_spec`, `et17Addr_spec`); the arrays and the call of the
   loop (`et17Tables_spec`).
5. What the parts need: the limits cover what the called procedures ask for (`choosePre_of_ok`,
   `hostLim_of_ok`), and the time of a run is within the worst case (`hostRunTime_le`).
6. The parts together: et17 decides Exact Triangle (`et17_spec`).
7. The list of the procedures with their numbers; with a solver it is a solver (`et17Procs`,
   `et17_solves`).
8. For the claim: the need is polynomially bounded (`hostNeed_poly`), the time obeys the bound of
   Theorem 17 (`obeysBound17_hostTime`), and so the claim holds for programs of the light language
   (`claim17_of_host`, `claim_theorem_17₅`, `claim_theorem_17₂₆`).

The layout, from the free pointer `fr` on: the table of doubles (`len + 1` cells, where
`len = bitLen U` is the number of binary digits of `U`; cell `j` holds `2^j p`, for residues without
division); the residues of `w(a,b)`, `w(b,c)`, `w(a,c)` (`n²` each); the starts of the classes
(`p + 1`); running places (`p`; while the pairs are sorted, cell `ϱ` holds the next free place of
the class `ϱ`); rows and columns of the sorted pairs (`n²` each); the three components of the table
of chunks (`n² + p` each); `X` (`n D`); `Y` (`D n`); the answers (`cap`); the solver's free pointer.

Notation: `κ` is the exponent in `|w(e)| ≤ n^κ`, the paper's ν; as in the paper, `F(p)` is the
number of false positives of `p`, that is, of triples with `S(a,b,c) = w(a,b) + w(b,c) + w(a,c) ≠ 0`
and `p ∣ S(a,b,c)`.


 ## The procedure 

### `Et17Nums`

 The numbers of the procedures that et17 calls, directly or through the procedures that it
calls: the two parameter procedures, sqrt, brute, scan, choosePrime, queryCapNat, ceilDiv, bitLen,
dblTable, resid, residues, classes, chunks, hostLoop, the solver, writeX, writeY, scanPairs, and
the procedures below choosePrime. 

### `Size`

 The locals of `et17`.  The arguments: `n`, `U`, the addresses of the three arrays of weights,
and the free pointer (the table of doubles is there).  Then `D`, `g`, `s = ⌊√D⌋`, the prime `p`,
`cap`, the number `q` of vertices of a piece, the number `h` of pieces, `len = bitLen U`, and `n²`.
Then the addresses of the residues of `w(a,b)`, `w(b,c)`, `w(a,c)`, of the starts of the classes,
the running places, the rows and the columns of the sorted pairs, the three components of the table
of chunks, `X`, `Y`, the answers, and the solver's free pointer.  Then `n² + p`, the number of
chunks, the number of instances, a flag (also the place for results that are not used), and `n D`.


### `et17Params`

 The first part of et17: `D`, `g`, `s`, and the flag that says whether `n` is small. 

### `et17Addr`

 The end of the second part: the sizes n², nD, n² + p, and the addresses of the arrays. 

### `et17Sizes`

 The second part: the prime, the sizes, and the addresses of the arrays. 

### `et17Tables`

 The third part: the residues, the classes, the chunks, and the loop over the instances. 

### `et17Body`

 et17(n, U, ab, bc, ac, fr). 

 ## Time and need

The additive constants in the time functions are upper bounds for the cost of evaluating arguments,
of calls and of tests.  They are not meant to be tight. 

### `SmallCase`

 n is small for the parameters D and g: the host runs the brute force. 

### `supTime`

 The largest time of the solver on an instance with at most cap query pairs. 

### `supNeed`

 The largest need of the solver on an instance with at most cap query pairs. 

### `falsePositiveBound`

 Proof of Theorem 17: "F(p) = O(n³ log(3n^ν)/√D) = O(ν n³ log n/√D)" for the selected prime.
Here the second form, with the constant `Hashing.falsePositiveConst` and with κ = kappaOf n U =
max(1, log U / log n), so that U ≤ n^κ. 

### `hostSetup`

 The time of the parameter procedures, of the square root and of the tests. 

### `hostLoopBound`

 A bound on the time of the loop over the instances: at most 4ng instances, with pieces of at
most q vertices and at most cap query pairs, and at most falsePositiveBound + 1 scans. 

### `hostMain`

 The time of et17 after the tests, if n is not small. 

### `hostTime`

 **A bound on the time of the host in the worst case**, for the parameter functions Dfun, Gfun
with the times tD, tG, over a solver with the time Tn. 

### `hostLayout`

 The cells of the arrays of et17, with s in place of the prime. 

### `hostWord`

 The largest number that et17 and the procedures below it form, apart from the solver; a and b
bound the numbers that the two parameter procedures form. 

### `hostNeedAt`

 The need of the host for given parameters D and g. 

### `hostNeed`

 **The need of the host**, over a solver with the need `need`; wD and wG bound the numbers that
the parameter procedures form. 

 ## The context 

### `ParamProc`

 A procedure that computes a function of one number and changes no cell; t is its time, w bounds
the numbers it forms, and it nests calls at most three deep. 

### `Et17Ctx`

 The context of et17: the solver and what hostLoop calls; the procedures of the host; the
two parameter procedures. 

 ## The data, the addresses and the local variables of a run 

### `hostData`

 The data of the loop over the instances, for the parameters D and g. 

### `aRab`

 The address of the residues of `w(a,b)`; the table of doubles is at fr. 

### `aRbc`

 The address of the residues of `w(b,c)`. 

### `aRac`

 The address of the residues of `w(a,c)`. 

### `aCls`

 The address of the starts of the classes. 

### `aCur`

 The address of the running places. 

### `aQi`

 The address of the rows of the sorted pairs. 

### `aQj`

 The address of the columns of the sorted pairs. 

### `aCr`

 The address of the residues of the chunks. 

### `aCl`

 The address of the starts of the chunks. 

### `aCw`

 The address of the lengths of the chunks. 

### `aX`

 The address of the matrix `matX` of an instance. 

### `aY`

 The address of the matrix `matY` of an instance. 

### `aOut`

 The address of the answers. 

### `aFr`

 The free pointer that is handed to the solver. 

### `host_places`

 The arrays of the host stand one after the other. 

### `hostAddr`

 The addresses that hostLoop gets. 

### `et17Loc0`

 The locals at the start: the arguments, then zeros. 

### `et17LocA`

 The locals after the first part. 

### `Et17.locals`

 The locals of the third part, for the data X of the loop: those after the second part, with the
number of chunks in NumChunks and the result of the last call in Small.  ParG and RootD are not
read. 

### `et17LocB`

 The locals after the second part (n is not small, so the flag is 0). 

### `hostRunTime`

 The time of the third part in a run: it depends on the data. 
