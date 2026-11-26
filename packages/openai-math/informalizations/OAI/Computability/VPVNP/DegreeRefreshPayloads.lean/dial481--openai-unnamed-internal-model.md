---
{
  "module": "OAI/Computability/VPVNP/DegreeRefreshPayloads.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/DegreeRefreshPayloads.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/DegreeRefreshPayloads.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Shared payloads of the refreshed graph

The summation over the actual arcs in (7.1) is equivalent to choosing the
external strings and a separate internal expander assignment in each block.
Every padding arc carries the unique string of length zero.


### `ActualArc`

 A refreshed outgoing arc consists of a base port, a remaining lane, and
one of the new degree-`d₀` slots. 

### `arcCoordinates`

 Read the block, its port, and the class of the numbered slot. 

### `actualWidth`

 Width on the actual outgoing arc index of `degreeRefresh`. 

### `payloadsEquiv`

 Shared actual-arc payloads are exactly one external assignment and one
internal assignment per block. Empty padding payloads add no summation index. 

### `actualWidth_eq_newWidths`

 This actual-arc width specializes to the width charged in (7.3). 

### `payloadsEquiv_external`

 Read the external component at its numbered actual slot. 

### `payloadsEquiv_internal`

 Read a block's internal component at its numbered expander slot. 

### `sum_payloads`

 The equality of finite sums used to replace the separate external and
internal choices by the single shared arc assignment of (7.1). 
