---
{
  "module": "Nc/RunGood.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/vp-vnp/Nc/RunGood.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/vp-vnp/Nc/RunGood.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# Certificates of matched runs

A run of an automaton on tapes and inputs is certified by the states, the places of the heads and the contents
of the tapes. The certificate of a run is unique, and it exists if and only if the run is matched.


### `prod_ofFn_apply`

 An entry of a product of matrices is a sum over paths. 

### `Ch.start`

 The channels whose places start at 0. 

### `Good`

 The conditions on a certificate: `o` letters, `q` states, `P` places, `c` contents; `x` is the code. 

### `place0`

 The first place of a channel in a run. 
