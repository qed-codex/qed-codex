---
{
  "module": "OAI/Computability/VPVNP/IncidenceControl.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/IncidenceControl.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/IncidenceControl.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Read-only control for an exact-one incidence matrix

Each column on the input tape carries a tag, its selection bit, and one incidence bit per
row. The control checks one row on each pass from the right end of the tape. A three-valued
counter distinguishes zero, one, and at least two selected columns incident with the row.


### `Column`

 One incidence column, consisting of a selection bit and an incidence bit for each of the
`m` rows. 

### `columnBits`

 Bits of one column in the order read by the leftward scan. 

### `State`

 Control states for searching for a row and reading each column's tag, selection bit, and
incidence bits, with a count saturated at two. 

### `start`

 Begin the incidence check by searching for row zero. 

### `tally`

 Saturating count of selected incidences. 

### `command`

 Literal instructions, with directions 0 (stay), 1 (left), and 2 (right). 

### `machine`

 Compile the read-only exact-one incidence checker for `m` rows into a universal-machine
program. 

### `countAt`

 Number of accepting paths within the fuel bound when the input head is at `pos` and the
checker is in state `q`. 

### `ReadsLeft`

 The head sees these bits in order as it moves left, finishing at position `base`. 
