---
{
  "module": "OAI/Computability/VPVNP/MotifLocalSelectors.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/MotifLocalSelectors.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/MotifLocalSelectors.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Local selector checks inside wire tensors

The selector carried by each edge is read at its two incident parties. This
realizes the global selector sum as a contraction of one wire network, and
retains the payload on each individual edge.


### `Half`

 Half-wire coordinates local to one party. 

### `mapHalf`

 Apply a separate coordinate transformation at each incident wire. 

### `readAnchor`

 Read the chosen incident edge through its appropriate half-wire. 

### `HalfAgrees`

 A party checks that all of its incident edges carry its anchor selector. 

### `selectedMap`

 Carry selector and payload on every supply edge and use only the payload
in the original map after the selectors have been checked. 

### `applyLocal_selectedMap`

 Exact local-map implementation of the selector sum in Theorem 6.1. 
