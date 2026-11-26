---
{
  "module": "Nc/Price/Basic.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/vp-vnp/Nc/Price/Basic.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/vp-vnp/Nc/Price/Basic.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# Prices of wires: the definition

For a field K and a finite set V of parties, `Prices K V` is the closure (for pointwise limits) of the
multiples c·d_F, c ≥ 0, of the metrics d_F(u,v) = F.e u v of the spectral points F over V. A function w
on pairs of any set Y is a price (`IsPrice K w`) if its pull-backs to finite sets are in `Prices`.
That prices are pseudometrics, closed under pull-backs, multiples and limits, and compact below a bound is
in `Paper/Prices.lean`. At the end there are two lemmas on the entries of a wire, for the files that compute with them.


### `specCone`

 The multiples of the metrics of spectral points. 

### `Prices`

 The prices of a finite set of parties. 

### `prices_induction`

 A closed property of the metrics of spectral points that is kept by multiples holds for
prices. 

### `IsPrice`

 A function w on pairs of a set Y is a price if all its pull-backs to finite sets are. 

### `isPrice_spec`

 The metric of a spectral point is a price. 

### `isPrice_of_finset`

 A function is a price if its restrictions to finite subsets are. 

### `IsPrice.exists_spec`

 Approximation by the metric of a spectral point. 

### `isPrice_zero`

 0 is a price. 

### `unit_two_val`

 The entries of the unit tensor with two legs (a wire before it is placed). 
