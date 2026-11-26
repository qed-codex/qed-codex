---
{
  "module": "Nc/Tow/Defs.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/vp-vnp/Nc/Tow/Defs.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/vp-vnp/Nc/Tow/Defs.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# Towers, routes: interface

A tower: levels of chambers `X j`, typed edges `Ed j`, vertices `V j i` of type `i` (all with the local
structure `Fl`, `Nr`), coverings `X j → X (j + 1)` of degree `D`, and hosts.


### `Tower`

 A tower of coverings, `J` steps, with `h` types. 

### `Tower.X`

 chambers 

### `Tower.Ed`

 typed edges 

### `Tower.V`

 vertices of type `i` 

### `Tower.Fl`

 the chambers at a vertex 

### `Tower.Nr`

 the near pairs at a vertex 

### `Tower.e0`

 the ends of an edge 

### `Tower.e1`

 the ends of an edge 

### `Tower.ty`

 the type of an edge 

### `Tower.vx`

 the vertex of a chamber 

### `Tower.co`

 the place of a chamber at its vertex 

### `Tower.cN`

 the ends of a near pair 

### `Tower.dN`

 the ends of a near pair 

### `Tower.nr`

 the edges of types other than `i` are the near pairs at the vertices of type `i` 

### `Tower.π`

 the covering 

### `Tower.πE`

 the covering on edges 

### `Tower.πV`

 the covering on vertices 

### `Tower.host`

 hosts 

### `step`

 The other end of an edge. 

### `Walk`

 The list of edges is a walk from `c` to `c'`. 

### `Routes`

 Routes: a walk from every chamber of `X 0` to every other one, at most `m` steps, in which every edge is used at
most `Uu` times in all. 

### `Routes.rt`

 the route 
