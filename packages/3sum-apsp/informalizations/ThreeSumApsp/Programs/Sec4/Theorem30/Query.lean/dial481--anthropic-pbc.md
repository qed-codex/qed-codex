---
{
  "module": "ThreeSumApsp/Programs/Sec4/Theorem30/Query.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Anthropic, PBC",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Programs/Sec4/Theorem30/Query.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Programs/Sec4/Theorem30/Query.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# A query, from the block that holds the data structure (proof of Theorem 30, "Query")

"Given (I, J), we find its tile from the bands of row I and column J, the subset Q of its block
product, and its output string w […], all in O(L) operations". Below, the output string is called η.
queryAt(I, J, b0) has four parts. It reads the sizes, the addresses of the tables and the bands of I
and J from the block at b0 (queryAtReads), computes the addresses of the areas of Section 4
(queryAtAreas), lets outDigits write the digits of η (queryAtOut), reads the root of the trie of the
tile from the table of roots, and lets queryCore compute the sum of Lemma 28 from the two encodings
and this trie (queryAtCore). There is one lemma for each part; for each of the two calls a record
holds the arguments (outArgs, coreArgs) and a lemma says that the block holds what the routine
assumes (outArgs_pre, coreArgs_pre). queryAt_spec puts the four parts together.


 ## The program 

### `Row`

 The local variables of queryAt: the arguments I, J, b0; the sizes L, m, t, L - m, K₀, nB, 10^L;
the addresses of the tables BAND, BLOCK, DIG3 and of the area WD; the bands of I and J; the
addresses of the areas BOX, SS, ROOTS, TR; and a local for the result of outDigits, which is not
used. 

### `queryAtReads`

 The first part of queryAt(I, J, b0): what is read from the directory and from the table BAND. 

### `queryAtAreas`

 The second part: the areas of Section 4 lie one behind the other from WD on. 

### `queryAtOut`

 The call of outDigits: the digits of the output string. 

### `queryAtCore`

 The call of queryCore: the sum of Lemma 28. The tile of (I, J) has the number bandI nB + bandJ,
and the root of its trie is read from the table of roots. 

### `queryAtBody`

 queryAt(I, J, b0) returns (XY)[I, J]: the result of a procedure is its local 0, into which the
last call stores. 

### `queryAtRead`

 What the locals hold after the first part. 

### `queryAtLocals`

 What the locals hold after the second part. 

 ## The first two parts 

### `queryAtReads_spec`

 The first part reads the sizes, the addresses of the tables, and the two bands. 

### `queryAtAreas_spec`

 The second part computes the addresses of the areas of Section 4. 

 ## The call of outDigits 

### `segN_of_segB`

 Bits as natural numbers. 

### `outArgs`

 The arguments of the call of outDigits, and the data behind them. 

### `outArgs_pre`

 The block holds what outDigits assumes. 

### `queryAtOut_spec`

 The third part writes the digits of the output string of (I, J) at WD. 

 ## The call of queryCore 

### `tileOf`

 The number of the tile of the position (I, J). 

### `coreArgs`

 The arguments of the call of queryCore, and the data behind them. 

### `abs_enc_mul_le`

 Every product of two encoded numbers fits in a word. 

### `tileOf_lt`

 The tile of the position (I, J) is one of the nB² tiles. 

### `getElem`

 It is given by the encodings of the band of I and of the band of J. 

### `coreArgs_walk`

 Every box of the query is found in the trie of the tile. 

### `coreArgs_sums`

 Every partial sum of the query fits in a word. 

### `coreArgs_value`

 What queryCore returns for the tile of (I, J) is (XY)[I, J], by Theorem 30. 

### `coreArgs_pre`

 The block, with the digits of the output string at WD, holds what queryCore assumes. 

### `queryAtCore_spec`

 The fourth part returns (XY)[I, J] and changes the scratch strings BOX and SS only. 

 ## The routine 

### `queryAt_spec`

 **queryAt** meets its specification. 
