---
{
  "module": "ThreeSumApsp/Programs/Sec2/Theorem5/Contracts.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Anthropic, PBC",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Programs/Sec2/Theorem5/Contracts.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Programs/Sec2/Theorem5/Contracts.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# Theorem 5 in the light language: the map

One file that fixes everything on which two routines have to agree, besides the sizes and the places
of the arrays: the numbers of the procedures, and for every procedure its arguments, what it needs,
what it leaves behind, which cells it may change, and the shape of its running time. A routine is
proved against its own entry; a caller assumes the entries of the routines it calls. So the proof of
a routine does not depend on the proofs of the routines that it calls.

* Routines never contain an address.  They receive scalars and base addresses as arguments.  Only
  the two main routines (Theorem 5 here, the data structure of Section 4) know the places.
* The stages up to the encodings of all bands are shared with Section 4: procedure pShared fills the
  shared block, which starts at an address b0 above the input and the output of the program that
  calls it (the free pointer).
* An entry XSpec lim P c says: in the program P, within the limits lim, procedure number pX does its
  job within c times the shape of its running time (Meets).  The theorem on a routine proves its
  entry for every c from the constant of the routine on, so a caller can assume several entries at
  one constant.
* The entries of encStep, encodeBands, countSort, copy, runTiles and report stand with these
  routines.
* Strings are numbers: a string over an alphabet of b symbols is its code in base b, level 1 most
  significant (namespace Spec).


 ## Vocabulary 

### `SegB`

 The cells from a on hold a list of bits, as 1 and 0. 

### `SegB.get`

 A cell of a segment of bits. 

 ## The numbers of the procedures

Number 0 is empty.  1 to 25: the shared routines and those of Theorem 5.  26 to 28: the test of the
regime, the brute force, and the solver for all instances.  29 to 39 are not used.  From 40 on:
Section 4. 

### `pShared`

 The number of shared. 

### `pPow`

 The number of pow. 

### `pBinom`

 The number of binom. 

### `pSqrt`

 The number of sqrt. 

### `pSubsets`

 The number of subsets. 

### `pCounters`

 The number of counters. 

### `pDigits`

 The number of digits. 

### `pCoef`

 The number of coef. 

### `pBandArray`

 The number of bandArray. 

### `pEncStep`

 The number of encStep. 

### `pEncode`

 The number of encode. 

### `pEncodeBands`

 The number of encodeBands. 

### `pWanted`

 The number of wanted. 

### `pCountSort`

 The number of countSort. 

### `pSortWanted`

 The number of sortWanted. 

### `pSegBounds`

 The number of segBounds. 

### `pUnion`

 The number of union. 

### `pPick`

 The number of pick. 

### `pPruned`

 The number of pruned. 

### `pRunTiles`

 The number of runTiles. 

### `pReport`

 The number of report. 

### `pFill`

 The number of fill. 

### `pCopy`

 The number of copy. 

### `pGather`

 The number of gather. 

### `pThm5`

 The number of the solver of Theorem 5. 

### `pRegime`

 The number of the test of the regime. 

### `pThinBrute`

 The number of the brute force. 

### `pThin`

 The number of the solver for all instances. 

 ## The entries of the shared routines 

### `PowSpec`

 pow(b, n, dst): writes b^0, …, b^n to dst. 

### `BinomSpec`

 binom(L, m, pas): returns binom(L, m), by Pascal's triangle in the L + 2 cells from pas. 

### `SqrtSpec`

 sqrt(K): returns ⌊√K⌋, by counting up.  Changes no cell. 

### `SubsetsSpec`

 subsets(L, m, KK, mask): writes the first KK subsets of size m of the L levels, as rows of L
bits, in the order of Spec.unrank. 

### `CountersSpec`

 counters(N, K0, N0, band): for every row I < N writes its band I / (K0 N0) to band + I and its
block I / N0 % K0 to band + N + I, by counting. 

### `DigitsSpec`

 digits(n, b, len, dst): for every x < n writes the len digits of x % b^len in base b, most
significant first, to dst + x len, by an odometer. 

### `CoefSpec`

 coef(phi): writes the 70 coefficients φ_λ(s) to phi and the 70 coefficients ψ_λ(t) to phi + 70.


### `BandTables`

 What bandArray reads, apart from the matrix: the table of subsets and the two tables of digits,
all below the array it writes. 

### `bandArrayShape`

 The shape of the running time of bandArray: clear 7^L cells, then one entry in O(L) steps for
each subset of the table, each row of a block and each column. 

### `BandArrayLSpec`

 bandArray(L, m, N, D, K0, N0, S7, β, side, aA, sI, sK, mask, dig3, dig4, arr), for the left
side: side = 0, aA the address of X, sI = D, sK = 1 (sI and sK are the strides of the index I of the
band and of the inner index k: the entry is at aA + I sI + k sK).  Writes the input array of the row
band β (Section 2.3.4), in the order of the codes, to arr. 

### `BandArrayRSpec`

 The same procedure for the right side: side = 1, aA the address of Y, sI = 1, sK = N. Writes the
input array of the column band β. 

### `EncodePlaces`

 Where encode finds its tables and its areas: the tables lie below dst, the 10^n cells of dst
below src, the 7^n cells of src below scr, and scr has 7^n cells. 

### `EncodeLSpec`

 encode(n, src, dst, scr, tab, p7, p10), the procedure of Section 2.4.1, recursive as
printed, with the coefficients φ: from the array a at src it computes the encoding of a at dst. 

### `EncodeRSpec`

 The same procedure with the coefficients ψ. 

 ## The shared stage 

### `PowTables`

 The tables of the powers of 3, 4, 7 and 10 in the shared block. 

### `RowTables`

 The other tables of the shared block: the coefficients, the subsets, the band and the block of
every row, and the digits of the offsets and of the inner indices. 

### `SharedTables`

 The tables of the shared block, all in one memory. 

### `SharedReady`

 What the shared stage leaves behind: the tables, the directory, and the encodings of all bands.
(Cell 31 of the directory is not used by it.) 

### `sharedShape`

 The shape of the running time of the shared stage. 

### `SharedPre`

 What the shared stage assumes: the shared block fits in the memory, X and Y stand below it, V
bounds their entries, and the encoded numbers and the powers of ten fit in a word. 

### `SharedSpec`

 shared(L, m, N, D, aX, aY, b0): fills the shared block. 

 ## Theorem 5 

### `WantedTables`

 What wanted reads, apart from the positions: all of it lies below the area it writes. 

### `Wanted.WantedPre`

 What wanted assumes. 

### `WantedSpec`

 wanted(w, L, Lo, N, K0, nB, aWI, aWJ, band, dig3, mask, tid): "locate the output strings"
(Section 2.4.4). For the i-th wanted position (I, J) it writes the number of its tile to tid + i,
the code of its output string to tid + w + i, and the L digits of that code to tid + 2 w + i L. 

### `Args`

 The arguments of sortWanted. 

### `Args.w`

 the number of positions 

### `Args.L`

 the number of digits of a code 

### `Args.nT`

 the number of tiles 

### `Args.tid`

 where the numbers of the tiles stand 

### `Args.dgt`

 where the digits of the codes stand 

### `Args.perm`

 where the sorted list goes 

### `Args.room`

 The number of cells from perm on that may change. 

### `Args.room_eq`

 The number of cells, written out. 

### `SwPre`

 What sortWanted assumes: t i and x i are the tile and the code of position i, and they stand
before the cells that may change. 

### `SortWantedSpec`

 sortWanted(w, L, nT, tid, dgt, perm): "sort the sets W_T" (Section 2.4.4), by a radix sort: L
stable counting sorts on the digits of the codes, the last digit first, then one on the numbers of
the tiles. t i and x i are the tile and the code of position i. It writes the sorting permutation to
perm and, for every s ≤ nT, the number of positions in tiles below s to perm + 2 w + nT + 11 + s.
The cells from perm + w to perm + 2 w + nT + 11 are scratch. 

### `FillSpec`

 fill(dst, n, x): dst[i] := x for i < n. 

### `segStart`

 The number of codes of an increasing list whose first digit (of n + 1) is below z. 

### `SegBoundsSpec`

 segBounds(l, len, pw, bnd), with pw = 10^n: one pass over an increasing list of codes of n + 1
digits. For z ≤ 10 it writes the number of codes with first digit below z to bnd + z, and it writes
the codes without their first digits to the len cells from bnd + 11. So the slice at z (Section
2.4.2), Spec.sliceList n z codes, is the segment that starts at bnd + 11 + segStart n codes z. 

### `UnionSpec`

 union(pa, na, pb, nb, pc): writes the merge of two lists, a number that heads both being taken
once, to pc, and returns its length. 

### `PickArgs`

 The arguments of pick but for the mode, with the data behind them: the list small stands at
pSub, the list big at pU, the list values at pVal, and pDst is the destination. 

### `PickArgs.vals`

 The values of the arguments of pick. 

### `PickPre`

 What pick assumes: big is an increasing list, values has a value for each of its numbers, and
small is an increasing list of numbers of big; all of it lies above the cells that pick writes. 

### `PickSetSpec`

 pick(pSub, nSub, pU, nU, pVal, pDst, 0): restriction of an array on a set to a subset (step (4)
of Pruned), in one walk through both lists: writes the values of the numbers of small to pDst. 

### `PickAddSpec`

 pick(pSub, nSub, pU, nU, pVal, pDst, 1): the same, but the values are added to the cells from
pDst on, which hold the list acc. 

### `PrunedArgs`

 The arguments of pruned but for the number n of levels that are left, with the data behind them.
The two encodings are the lists EA at aEA and EB at aEB, and the parts of them below the current
vertex begin at the position base.  The list codes stands at l, the values are written to out, the
stack begins at sp, and the powers of ten up to 10^Lmax stand at p10.  A and B bound the numbers in
the two encodings. 

### `PrunedArgs.vals`

 The values of the arguments of pruned. 

### `PrunedPre`

 What a call of pruned with n levels left assumes.  The list codes is an increasing list of
output strings, as numbers below 10^n.  The two encodings and the powers of ten lie below that list;
then come the cells of out, one for each code; then, from sp on, the stack, n frames of 3 len + 11
cells.  Sums of 10^n products of a number of EA and a number of EB fit in a word. 

### `PrunedSpec`

 pruned(n, ea, eb, l, len, out, sp, p10), the procedure Pruned of Section 2.4.2, recursive as
printed, on increasing lists of codes: a slice is a segment and a union of slices is a merge
(Section 2.4.4). ea = aEA + base and eb = aEB + base are the addresses at which the parts of the two
encodings below the current vertex begin. It writes the values, in the order of the list, to out,
and changes no other cell but those of its stack.
Time: c for each call and for each code passed to a call. 

### `GatherSpec`

 gather(w, perm, src, dst): dst[i] := src[perm[i]] for i < w. 

### `thm5Shape`

 The shape of the running time of Theorem 5's program; work is the sum over the tiles of the work
of the pruned recursions. 
