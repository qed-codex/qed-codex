---
{
  "module": "proof/networks/Groundwork/Net/Colouring.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/networks/Groundwork/Net/Colouring.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/networks/Groundwork/Net/Colouring.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# The colouring lemma

The Chebyshev step in the proof of Lemma 1 of the paper (a good grouping exists): g ≥ 3K^8 points
carry symmetric capacities c(a,b) that sum to at
most P at every point; then some colouring with K colours has all classes of size < 2g/K and,
between any two classes,
capacity at most (U + gP/K)/K², where U is the sum of all capacities over ordered pairs.
Second-moment argument over the finite type of all colourings, written with finite sums.
Main results: Groundwork.Colouring.exists_colouring, Groundwork.Colouring.exists_colouring_beta.


### `card_prescribed`

 The number of colourings with prescribed values on S is K^(g-#S). 

### `card_one`

 A fraction 1/K of the colourings gives one point a prescribed colour. 

### `card_two`

 A fraction 1/K² of the colourings gives two points prescribed colours. 

### `card_four`

 A fraction 1/K⁴ of the colourings gives four points prescribed colours. 

### `cheb`

 Chebyshev, as a count. 

### `cheb_nat`

 Chebyshev from the first two moments, in natural numbers with denominators cleared. 

 ### Class sizes 

### `Zs`

 The size of the class of colour γ, as a sum of indicators. 

### `Zs_eq`

 The sum of indicators is the size of the class. 

### `sum_Zs`

 First moment of the class size: its mean is g/K. 

### `sum_Zs_sq`

 Second moment of the class size: at most (g/K)² + g/K. 

### `card_badZ`

 The number of colourings whose class γ is too large, times g, is at most K·K^g. 

 ### Capacities between classes 

### `Ys`

 The capacity from class γ to class γ'. 

### `Us`

 The total capacity, over ordered pairs. 

### `Ys_le_Us`

 The capacity between two classes is at most the total capacity. 

### `Us_le`

 The total capacity is at most g·P. 

### `sum_Ys`

 First moment of the capacity between two classes: its mean is U/K². 

### `meet`

 How often the ordered pair q meets the ordered pair p. 

### `card_pairs_le`

 The fraction of colourings that send two ordered pairs from γ to γ' is at most 1/K⁴, plus 1/K²
for every time the pairs
meet. 

### `sum_meet`

 The capacities of the pairs that meet a given pair sum to at most 4P. 

### `sum_Ys_sq`

 Second moment of the capacity between two classes: at most (U/K²)² + 4PU/K². 

### `card_badY`

 The number of colourings for which the capacity from γ to γ' is too large, times g, is at most
4K⁴·K^g. 

### `exists_colouring_core`

 Core form: zero diagonal, general finite index and colour types. 

### `exists_colouring_fintype`

 The colouring lemma for finite types: K colours, g points, g ≥ 3K^8. The diagonal of c is
ignored. 

### `exists_colouring`

 The colouring lemma: K ≥ 2 colours, g ≥ 3K^8 points (Lemma 1 of the paper has g = 3K^8). 

### `beta`

 The label length after merging: max 1 ⌊(U + gP/K)/K²⌋, written as max 1 ⌊(KU + gP)/K³⌋. 

### `one_le_beta`

 The label length is at least 1. 

### `beta_le`

 K²β ≤ K² + U + gP/K, multiplied by K. 

### `le_beta`

 What a class-pair capacity needs in order to be at most β. 

### `exists_colouring_beta`

 The colouring lemma with β: small classes, every class-pair capacity at most β. 
