---
{
  "module": "ThreeSumApsp/Programs/Sec2/Theorem5/Encode/Contract.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Anthropic, PBC",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Programs/Sec2/Theorem5/Encode/Contract.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/3sum-apsp/ThreeSumApsp/Programs/Sec2/Theorem5/Encode/Contract.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# What the callers of encode assume

The callers of encode (Section 2.4.1) assume a specification of the procedure that does not name its
body: `EncodeLSpec` for the array a and the forms φ_λ, `EncodeRSpec` for b and ψ_λ.  Both hold for
every program that has encStep and encode at their numbers.  The places that the callers provide are
a layout for encode (`EncodePlaces.layout`), so the specification of encode on lists applies
(`encode_entry`, for any alphabet of seven variables); the two specifications are its cases for the
left variables with the forms φ_λ and for the right variables with the forms ψ_λ.


### `scrSize_le`

 The scratch area of encode has fewer than 7^L cells. 

### `EncodePlaces.layout`

 The places that the callers provide are a layout for encode. 

### `pow_of_seg`

 A cell of a table of powers. 

### `encode_entry`

 **The specification that the callers of encode assume**, for any alphabet of seven variables.
The callers allow `7^n` cells of scratch area, more than the `scrSize n` that `encode` uses. 

### `encodeL_entry`

 **The specification that the callers of encode assume, for the array a.** 

### `encodeR_entry`

 **The specification that the callers of encode assume, for the array b.** 
