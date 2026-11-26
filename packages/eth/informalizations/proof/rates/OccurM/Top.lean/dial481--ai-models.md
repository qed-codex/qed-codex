---
{
  "module": "proof/rates/OccurM/Top.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/OccurM/Top.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/OccurM/Top.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # The top level in m after the preparation

`GeneralPieces.Tied.TopM S pick (SatM.rPow α)` is the bound in m for the named top level (`AM`,
`eM`) on formulas in which every variable occurs. `after_front` puts a front end before both
functions: a polynomial-time function that maps
the code of (k, φ), in any coding, to `SatM.enc k (ren φ)`, the code of the formula with the
variables that occur numbered. It gives what becomes the five fields of `TopOccur`:

* both functions stay polynomial-time (composition);
* correctness and the rate are those of `TopM` at `ren φ`, which has as many clauses as φ, with log
  m in place of log₂(m+2) (`shift_le`);
* the machine is the padding machine (`CountKSatRate.stPaddedW`) on the two composed functions, so
  it computes the named function on every input; its steps are bounded by `steps_le`.

`topOccurOfTop` is this for the compact code with `rencC` and for the code with N in unary with
`renc`. 

### `one_le_length_encC`

 The compact code is not empty. 

### `one_le_length_enc`

 The code with N in unary is not empty. 

### `rate_ren`

 The exponent of the top level at the renamed formula is at most G·km/(log m)^α, with the G of
`TopM.rate`. 

### `after_front`

 For any coding `code` by nonempty words and any polynomial-time `front` that maps the code of
(k, φ) to `SatM.enc k (ren φ)`: five statements, which for the compact code with `rencC` are the
five fields of `TopOccur`, and for the code with N in unary with `renc` those of
`TopOccurUnary`. 

### `topOccurOfTop`

 From the bound in m for the named top level on formulas in which every variable occurs to the
bound for the same top level after the named preparation, for both codes. 
