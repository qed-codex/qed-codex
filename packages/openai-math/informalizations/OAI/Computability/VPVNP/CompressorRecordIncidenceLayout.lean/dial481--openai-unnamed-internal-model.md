---
{
  "module": "OAI/Computability/VPVNP/CompressorRecordIncidenceLayout.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorRecordIncidenceLayout.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorRecordIncidenceLayout.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Shared incidence columns between compressor levels

The same slot numbering serves cursor, shrink and refresh states. This module records the
three actual columns independently of the three base columns. A packed six-column layout
assigns each cell a distinct address for the entire state, including at every parallel slot.


### `ActualColumns`

 The three actual columns use the common state-relative slot numbering. 

### `column`

 Base forward, base inverse, displacement, actual forward, actual inverse and width. 

### `baseOrder`

 Canonical base and actual slot orders as finite equivalences. 

### `actualOrder`

 Number actual slots in base-vertex, lane, then local-port order, with the local port
varying fastest. 

### `Layout`

 Column addresses are disjoint through the last actual slot, and all slot IDs fit. 
