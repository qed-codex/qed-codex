---
{
  "module": "OAI/Computability/VPVNP/ParseEventBounds.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/ParseEventBounds.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/ParseEventBounds.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 # Finite Boolean coordinates for ordered parse occurrences

The coordinates bound the start, layer and binary split independently. This rectangular
index set includes candidate productions which may be ruled out by the local grammar
conditions. Its cardinality is polynomial in the degree cutoff and the alphabet sizes.
A Boolean word specifies a finite table by its characteristic function on these coordinates.


### `ParseEvent.Bounded`

 An occurrence fits the coordinate table if all its numerical fields are below `D`. 

### `EventCode`

 A candidate event has an interval, parent state and either a terminal or a split
together with the two ordered child states. 

### `event`

 Decode a candidate event by taking the natural values of its start, layer and binary split
indices. 

### `ofEvent`

 The coordinate tuple is recovered from the natural-valued event and its bounds. 

### `boundedEquiv`

 The bijection between event codes with indices in `Fin D` and parse events whose start,
layer and binary split are below `D`. 

### `enumerate`

 Enumerate the rectangular coordinate set with a single finite address. 

### `selected`

 Table of all occurrences whose enumerated Boolean flags are set. 

### `selectedEquiv`

 Boolean words and bounded occurrence tables are in bijection, without additional
bits for unused events or auxiliary witnesses. 
