---
{
  "module": "Nc/Price/BorderSum.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/vp-vnp/Nc/Price/BorderSum.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/vp-vnp/Nc/Price/BorderSum.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# Sums up to ε: powers, extraction of a coefficient, restrictions

The helpers of the lemma `few`. A local map with entries in `K[ε]` is a family of matrices of polynomials;
`polyApp` is the array that it makes of a tensor.


### `polyApp`

 The array over `K[ε]` that local maps with polynomial entries make of a tensor. 

### `polyApp_prod`

 A product of images of tensors is the image of the product of the tensors. 

### `coeff_sum_words`

 **Paper: Lemma few, powers of a sum up to ε, the words.** If the images of the b k have the sum
ε ^ D * t up to higher powers, then the products of N images, over all words, have the sum
ε ^ (N * D) * t^N up to higher powers. 

### `coeff_prod_choices`

 The coefficient of ε ^ D of a product of polynomials, as a sum over the choices of the exponents. 

### `le_coeff`

 **Paper: Lemma few, extraction of a coefficient.** The coefficient of ε ^ D of the image of a tensor z under
local maps with polynomial entries is a sum of at most (D + 1) ^ #parties restrictions of z, so a spectral point
is at most that many times its value at z. 
