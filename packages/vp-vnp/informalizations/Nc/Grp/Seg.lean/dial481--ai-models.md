---
{
  "module": "Nc/Grp/Seg.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/vp-vnp/Nc/Grp/Seg.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/vp-vnp/Nc/Grp/Seg.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# Cutting the letters of a tape into segments

The letters come in reverse order; the segments are made from the last partner to the first one. Every segment is
closed by a separator and stands in front of the string that the partner has from the later tapes.


### `okFlag`

 Flags: 0 = nothing is taken, 1 = something, 2 = anything. 

### `segL`

 All ways to cut the letters `rest`: `f`, `tk`, `cur` flag, `something has been taken`, string of the partner at hand;
`fs`, `as` flags and strings of the partners before; `out` strings of the partners behind. 

### `segS`

 The state of the program. 

### `sgF`

 Parts of the state, in the argument (this program, state). 

### `sgTk`

 tk 

### `sgCur`

 cur 

### `sgFs`

 fs 

### `sgAs`

 as 

### `sgRest`

 rest 

### `sgOut`

 out 

### `appB_gives`

 Concatenation of lists of bits. 

### `segNext`

 The next partner. 

### `segTake`

 Take a letter. 

### `segClose`

 Close a segment. 

### `segB`

 The program. 

### `encL`

 The results of a program without weights. 

### `closeL`

 What remains to do when a segment is closed. 

### `takeL`

 What remains to do when a letter is taken. 

### `segB_does`

 **The program cuts.** 

### `segRow`

 All ways to cut the letters of a tape. 
