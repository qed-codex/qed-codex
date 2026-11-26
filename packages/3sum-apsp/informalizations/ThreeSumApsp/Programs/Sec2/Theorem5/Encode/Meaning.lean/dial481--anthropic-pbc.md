---
{
  "module": "ThreeSumApsp/Programs/Sec2/Theorem5/Encode/Meaning.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Anthropic, PBC",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Programs/Sec2/Theorem5/Encode/Meaning.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Programs/Sec2/Theorem5/Encode/Meaning.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# What encode computes, in the paper's terms

The result of encode is described by a recursion on positions in arrays (`encIdx`).  Here this is
linked with the definitions of the paper (Section 2.4.1) through arrays on strings as lists: if the
source holds an array on strings and the table holds the coefficients of the linear forms, then the
output holds the encoding of the array.

Both sides are treated at once, for an alphabet of seven variables with any coefficients:
`computeEncoding` is the procedure of Section 2.4.1 for such an alphabet,
`encIdx_eq_computeEncoding` says that the recursion on positions computes it, and `encode_str` is
the specification of encode in these terms. For the two alphabets of the paper the procedure gives
the two encodings (`computeEncoding_phi`, `computeEncoding_psi`).


 ## From positions to strings 

### `encIdx_eq_computeEncoding`

 The recursion on positions computes the procedure of Section 2.4.1, if the array and the table
of coefficients are stored by digits. 

 ## The specification of encode, on lists 

### `EncodePre.of_seg`

 The hypotheses of encode hold if the source, the table of coefficients and the two tables of
powers are in their places and the numbers obey the bounds. 

### `encode_str`

 **The encoding of an array on strings** (Section 2.4.1), for both alphabets at once.  If the
source holds the array A on the strings of length L, the table holds the coefficients, the tables of
powers are in their places and the numbers obey the bounds, then encode ends within `cEncode · 10^L`
steps, the output holds what the procedure of Section 2.4.1 computes, and only the output and the
scratch area have changed. 
