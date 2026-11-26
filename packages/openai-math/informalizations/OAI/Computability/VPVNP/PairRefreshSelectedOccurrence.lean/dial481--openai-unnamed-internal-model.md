---
{
  "module": "OAI/Computability/VPVNP/PairRefreshSelectedOccurrence.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairRefreshSelectedOccurrence.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairRefreshSelectedOccurrence.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 # Refresh rows of a selected execution

The native site order identifies a refresh output with a base, residual lane
and promoted port. Unpacking the origin of the chosen pass recovers the input
state and term that produced this row. The numerical directory uses the same
ordinal and distinguishes repeated occurrences of a term.


### `Row`

 Output sites whose selected pass is a refresh, indexed by their chronological level. 

### `level`

 The literal selected-level record determined by a refresh origin. 

### `Occurrence`

 Typed input state, branch choice, and physical port of an output row. 

### `Occurrence.lanes`

 Number of lanes remaining after port promotion. 

### `Occurrence.state`

 Input state recorded at this occurrence. 

### `Occurrence.choice`

 Refresh term selected by the branch. 

### `Occurrence.port`

 Base, residual lane and promoted port of the output site. 

### `occurrence`

 Decompose the recorded origin and undo the port promotion on the actual
output site. The shrink branch is ruled out by the stored role. 

### `Row.occurrence`

 The typed refresh data at this chronological output row. 

### `decode`

 The typed row returned by matching a popped word to a physical output
header and checking the chosen pass's role. 

### `unique_row`

 A parent address selects a unique chronological refresh occurrence. 
