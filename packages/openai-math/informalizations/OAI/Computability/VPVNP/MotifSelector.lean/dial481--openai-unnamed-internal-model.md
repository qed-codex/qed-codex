---
{
  "module": "OAI/Computability/VPVNP/MotifSelector.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/MotifSelector.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/MotifSelector.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Synchronizing selectors on a wire motif

In Theorem 6.1 of *VP and VNP differ over every field* the same finite
selector list is carried on every supply edge. Each party checks only
its incident edges. Connectivity makes the surviving selector lists
global, with each list contributing once.


### `Supply`

 Endpoint data and connectedness of the supply wires, with an incident
edge chosen at each party for reading its selector. 

### `Supply.src`

 Party at the source of each directed supply edge. 

### `Supply.dst`

 Party at the destination of each directed supply edge. 

### `Supply.anchor`

 Incident edge at each party whose selector is compared with the selectors on all other
  incident edges. 

### `Agrees`

 Each selector incident to the party agrees with the selector at its anchor edge. 

### `agrees_iff_constant`

 All local consistency checks succeed exactly on constant assignments. 

### `sum_local_checks`

 Summing over all edge selectors with the local checks gives a single
sum over global selectors. The factors may vanish or cancel in the ring. 
