---
{
  "module": "OAI/Computability/VPVNP/ParseIncidenceDefs.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/ParseIncidenceDefs.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/ParseIncidenceDefs.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 # Local incidence conditions for ordered grammar parses

An event names a half-open interval of leaves by its starting offset and its length
minus one. A binary event requests precisely its two ordered child intervals.


### `ParseEvent`

 A candidate production occurrence in an ordered parse, recording a leaf interval, the state
at its root and the production used there. 

### `ParseEvent.start`

 The zero-based offset of the first leaf in the occurrence. 

### `ParseEvent.layer`

 The length of the occurrence's leaf interval minus one. 

### `ParseEvent.state`

 The grammar state at the root of the occurrence. 

### `ParseEvent.production`

 The terminal variable emitted by a leaf, or the left child's layer and the ordered pair
  of child states at a binary node. 

### `ParseEvent.WellFormed`

 A terminal has one leaf. A binary split has two positive child lengths. 

### `ParseEvent.Matches`

 An occurrence matches a requested interval and state when its start, layer and root state
agree with all three arguments. 

### `ParseEvent.Requests`

 A binary occurrence requests its two ordered child intervals and their states. A terminal
occurrence has no child requests. 

### `IsParseTable`

 Exactly one production at every occupied interval, with the designated root and
both children of each binary production. Every other event has an incoming request. 
