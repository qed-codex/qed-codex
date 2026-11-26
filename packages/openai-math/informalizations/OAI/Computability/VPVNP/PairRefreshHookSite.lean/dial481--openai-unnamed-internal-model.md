---
{
  "module": "OAI/Computability/VPVNP/PairRefreshHookSite.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairRefreshHookSite.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairRefreshHookSite.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Frozen row data and the refresh role parser

A selected row supplies its two graph states, site, stored term choice and
physical workspace. The reader reconstructs the newer half from the popped
packet in scratch. Its one nondeterministic input is the independently chosen
older half.


### `Site`

 Input state, selected refresh term, and physical row and workspace addresses used by the
refresh hook. 

### `Site.lanes`

 Number of lane bits left after moving the port bits into the base. 

### `Site.state`

 Network state entering the selected refresh, with the port bits still in the lane. 

### `Site.choice`

 Dyadic refresh choice recorded for this input state. 

### `Site.port`

 Input base, residual lane, and promoted port identifying the output row. 

### `Site.degree`

 Slot degree used to size the private argument arena. 

### `Site.rowEnd`

 Address immediately following the traversal rows. 

### `Site.older`

 Starting address of the input layer, used to locate the child row. 

### `Site.parent`

 Address of the promoted output row whose packet supplies the newer half. 

### `Site.listHead`

 Address of the first entry in the parent row’s child list. 

### `Site.level`

 Chronological index of the input layer of this refresh. 

### `Site.later`

 Number of traversal layers following this refresh’s output layer. 

### `Site.start`

 Starting address of the stored refresh terms for this level. 

### `Site.prev`

 Incidence directory for the input state. 

### `Site.next`

 Incidence directory for the state produced by the refresh. 

### `Site.geometry`

 Private address of the geometry words used by the traversal. 

### `Site.roleOffset`

 Offset stored in the traversal geometry for locating the role data. 

### `nextState`

 State produced by applying the selected dyadic refresh to the input state. 

### `olderSite`

 Input site obtained by putting the promoted port back into the lane. 

### `newerSite`

 Output site with the promoted port in its base and the residual lane unchanged. 

### `oldNode`

 Child row address computed from the input layer start and the input site ordinal. 

### `regions`

 Private memory layout for the row arguments, histogram, and cache. 

### `arena`

 Private argument arena holding the packed child and parent half-wire assignments. 

### `front`

 Event prefix for locating the parent layer and reading the child’s half-wire assignment. 

### `action`

 Local refresh action on the two half-wire assignments, returning the event trace and
updated scratch on success. 

### `read`

 Refresh reader that decodes the parent packet, consumes the old half from the tape, and
runs the local action. 

### `hook`

 DFS visit parser built from the refresh reader at this row. 

### `Prepared`

 The popped packet contains a typed parent argument and the three geometry
words used by the native role. The node number ties it to this selected row. 

### `Published`

 Published memory, scalar fits, and the selected row in the completed
traversal layers. The register and memory semantics of the role are proved
separately from these source data. 
