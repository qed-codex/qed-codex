---
{
  "module": "OAI/Computability/VPVNP/PairTraversalControllerMemory.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairTraversalControllerMemory.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairTraversalControllerMemory.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Memory and call accounting for the two traversal-directory passes

The controller processes all role layers, then all descriptor layers. Its
administrative reads and its writes to terminal header cells at or above
`H` preserve the worker writes below `H`. This region contains the raw
placement directories, the descriptor rows, the final bits, and the tags.


### `AgreeBelow`

 Equality on the protected prefix of external memory. 

### `write_header`

 A terminal header word, including the outer dispatcher's ordinal cell
at displacement 31, preserves the entire lower memory interval. 

### `writesBelow`

 The ordered external writes visible below the control header. 

### `replay_below`

 Two executions with the same visible writes agree below the controller's
header even when they insert different read, control, or high-address events. 

### `tag_at`

 The model of a single role write only consults the previous value of
the same cell. This holds for padding and for arbitrary prior memory. 

### `row_at`

 Descriptor writes have the same pointwise property. Child addresses
come from the selected placement, and padding comes from this cell of memory. 

### `header_commute`

 A high header write commutes, as a full memory equality, with the two
passes below it. The row and tag regions may have unused cells. 

### `passReports`

 Reports of one pass in layer order. Each layer has one additional call
that returns the first site of the next layer. 

### `pass_cost`

 Exact native cost, including every reset and all reported operand reads. 

### `pass_cost_le`

 Bound a pass by the measured probe allowance for active calls and its
separate reset allowance. The terminal acceptance is accounted for separately. 

### `controller_calls`

 All tags, all rows, and the accepting controller call. The exact count
charges two resets for every layer and a final acceptance even at zero blocks. 

### `controller_cost_le`

 With a fixed operand setup cost on every burst, a role costs one
additional probe. A leaf costs two and a fiber costs two per child plus
three header probes. The resets and the accepting call use setup alone. 

### `pass_writes`

 Insert a reset after each stage. No protected write is added if the
active wrapper agrees with its worker on those writes and the reset only
reads or writes above the header. 

### `controller_setup_loads`

 Evaluating the actual register setup counts repeated header loads in each
of its eighteen output expressions. 

### `selected_controller_cost`

 With those setup reads included on every burst, the cost of the complete
two-pass controller is linear in the initial site count times the stage count.
The constant includes the resets and final acceptance. 

### `selected_readback`

 All protected data needed by the DFS survives the control-cell updates:
the selected role words and ordered placement rows, the final-bit gap, and
every raw input below the descriptor base. 

### `selected_native_replay`

 Select native workers on the actual branch. Any controller log with the
same visible writes reproduces their complete memory below the header. 
