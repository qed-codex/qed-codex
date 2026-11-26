---
{
  "module": "ThreeSumApsp/Programs/Sec2/Theorem5/Encode/AllBands.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Anthropic, PBC",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Programs/Sec2/Theorem5/Encode/AllBands.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Programs/Sec2/Theorem5/Encode/AllBands.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# The encodings of all bands of one matrix (Section 2.4.1)

Section 2.4.1: "We compute the encodings of the input arrays of all row bands and all column bands
[...], and every tile reads its two encodings from these."  encodeBands does this for one of the two
matrices: for each band β it calls bandArray, which forms the input array of the band at arr, and
encode, which leaves its encoding in the T = 10^L cells from enc + β T.

The loop is treated once, for callees that are described by what they do here (`encodeBands_proc`).
The two entries, for the row bands of X and for the column bands of Y, put in the specifications of
bandArray and encode for their side.


### `Levels`

 The local variables of `encodeBands`.  The arguments: `Levels` = L, `Size` = m, `Rows` = N,
`Cols` = D, `NumBlocks` = K0, `Width` = N0, `Cells` = S7 = 7^L, `Leaves` = T = 10^L and `NumBands` =
nB are the sizes of the layout; `Side` says which of the two matrices stands at `Source`, with the
steps `StepRow` and `StepCol`; `MaskTable`, `Digits3` and `Digits4` are the tables that
`bandArray` reads, `Table`, `Pow7` and `Pow10` those that `encode` reads; `Arr` and `Scratch` are
scratch areas, and the encodings are written from `Enc` on.  Then `BandNo` = β, and `Res` takes the
results of the calls. 

### `encodeBandsBody`

 encodeBands(L, m, N, D, K0, N0, S7, T, nB, side, aA, sI, sK, mask, dig3, dig4, arr, zs, tab, p7,
p10, enc): for each band, the input array is formed at arr and encoded into the T cells from
enc + β T. 

### `encodeBands_time`

 The time of the loop is at most the constant cB + cE + 50 times the shape of the entries. 

 ## The arguments, and what is assumed about them 

### `BandsArgs`

 The addresses that encodeBands gets besides that of the matrix.  mask, dig3 and dig4 are the
tables that bandArray reads, tab, p7 and p10 those that encode reads.  arr and zs are scratch, and
the encodings are written from enc on. 

### `BandsArgs.vals`

 The arguments of encodeBands at the sizes of p, for the matrix at aA with the strides sI and
sK. 

### `BandsPre`

 What encodeBands assumes besides the matrix.  Everything that is read lies below enc: the tables
of bandArray, the 70 coefficients coefs of the side, and the powers of 7 and of 10.  From enc on
follow the encodings and the two scratch areas.  V bounds the entries of the matrix. 

### `encodeBands_proc`

 **encodeBands**, at the sizes of `p`, for callees described by what they do here: `HB` says that
`bandArray` leaves the list `A β` at `arr`, within `cB bandArrayShape` steps, `HE` that `encode`
turns it into the list `E β` at `enc + β T`, within `cE 10^L` steps; both in any memory that agrees
with `μ` below `enc`.  Then the lists `E β` stand from `enc` on. 

 ## What is read does not change 

### `BandTables.congr_below`

 The tables that bandArray reads, in a memory that agrees below their bound. 

### `BandTables.mono`

 The tables also lie below every larger bound. 

### `BandsPre.encodePlaces`

 The places of the call of encode for the band β, in a memory that agrees with μ below enc. 

 ## The two entries 

### `EncodeBandsLSpec`

 encodeBands for the row bands of X: side = 0, the coefficients φ at tab. 

### `encodeBandsL_entry`

 **encodeBands** meets this entry, with every constant from cB + cE + 50 on. 

### `EncodeBandsRSpec`

 encodeBands for the column bands of Y: side = 1, the coefficients ψ at tab. 

### `encodeBandsR_entry`

 **encodeBands** meets this entry, with every constant from cB + cE + 50 on. 
