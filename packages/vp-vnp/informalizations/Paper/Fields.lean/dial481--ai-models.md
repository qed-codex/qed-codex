---
{
  "module": "Paper/Fields.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/vp-vnp/Paper/Fields.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/vp-vnp/Paper/Fields.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# The paper, appendix "All fields and the Hamiltonian cycle polynomial"


### `permInt`

 The permanent with integer coefficients. 

### `exists_closed`

 KK, "the algebraic closure of the prime field of characteristic p". 

### `two_ne_zero_of_char`

 2 is not 0 in characteristic other than 2. 

### `flat_rate_hc`

 The flat case for HC, in every characteristic. 

### `contracting_hc`

 The contracting case for HC, in every characteristic. 

### `thm_allfields_exceeds`

 "The bound of the contracting case, although its constant depends on p, exceeds that of the flat case for large m." 

### `beyond_of_rate`

 The bound 2^((log m)^(4/3)/1600²) in the form of the main theorems. 

### `thm_allfields`

 **Paper: Theorem thm:allfields.** "There is an absolute constant c > 0 such that for every p, zero or prime,
there is m₀: over every field of characteristic p and for every m ≥ m₀ every circuit for HC_m, and for PERM_m if p ≠ 2,
has more than m^(c(log m)^(1/3)) gates." 

### `exists_beyond_poly`

 A bound m^(c(log m)^(1/3)) is beyond every polynomial. 

### `hc_mem_VNP`

 "(HC_m) is in VNP." 

### `cor_allclasses`

 **Paper: Corollary cor:allclasses.** "Over every field, VP is a proper subset of VNP." 
