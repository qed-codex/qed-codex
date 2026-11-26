---
{
  "module": "Nc/RunMn.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/vp-vnp/Nc/RunMn.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/vp-vnp/Nc/RunMn.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# Automata with one input: the polynomial of degree at most `N`

Clauses on the input bits allow at most one letter at each place and ask for a letter at each place unless the end
mark came before. The monomial extension then has degree at most `N`, and below the code of a word only this
code is allowed.


### `VOk`

 At most one letter at each place; at each place a letter, or the end mark before. 

### `code1_le`

 The letter at a place of a word with its end mark. 

### `eq_code1`

 Below the code of a word only this code is allowed. 

### `RC`

 The rules on the input bits. 

### `cLits`

 Their literals. 

### `cRWt`

 Their weights. 

### `fdSum_valid`

 The sum over finite domains with the clauses on the input bits. 

### `line_mnExt`

 The monomial extension along the line through a 0/1 point. 

### `totalDegree_mnExt`

 The degree of the monomial extension. 
