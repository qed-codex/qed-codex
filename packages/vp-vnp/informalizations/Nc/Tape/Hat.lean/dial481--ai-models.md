---
{
  "module": "Nc/Tape/Hat.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/vp-vnp/Nc/Tape/Hat.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/vp-vnp/Nc/Tape/Hat.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# Series on several channels

Letters are pairs (channel, letter). `hat f v` is the sum of the series `f` over all words whose projections
to the channels are the words `v z`. Products of series become convolutions.


### `proj`

 The words on the channels. 

### `fib`

 The words with given projections. 

### `hat`

 The sum of a series over the words with given projections. 

### `anti`

 All ways to cut the words on the channels into two parts. 

### `Series.ne`

 The part of a series at non-empty words. 

### `hat_kstar`

 The recursion for the star. 
