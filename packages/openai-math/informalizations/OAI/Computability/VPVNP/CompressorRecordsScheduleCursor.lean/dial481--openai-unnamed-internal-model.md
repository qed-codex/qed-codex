---
{
  "module": "OAI/Computability/VPVNP/CompressorRecordsScheduleCursor.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorRecordsScheduleCursor.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorRecordsScheduleCursor.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Executing the cursor incidence scan in the descriptor dispatcher

Each row writes six entries. The external tag and twelve frame cells therefore
retain their values throughout the scan when they are disjoint from the six
output columns. At the exclusive bound the linked worker writes the controller
tag and returns the initial cursor for the controller.


### `CursorDisjoint`

 All row writes in the scanned interval avoid the dispatch tag and the
twelve input cells (bound and eleven public words). 

### `cursor_row_preserves`

 A single visit leaves each protected address available to the next call,
regardless of earlier contents of the output columns. 

### `cursor_valid_trace`

 Every cursor returned by the body is the next row number. Together with
frame preservation this gives the dispatch guard at every call boundary. 

### `cursorPassReports`

 Chronological reports of all data calls and the final transfer. The
closing call reads the same frame and sends the next call to the controller. 

### `cursor_segment`

 Execute all rows from the current cursor through the exclusive bound
and resume the controller with the exact new incidence columns. 

### `cursor_pass_effect`

 Nineteen probes per data call (six writes, twelve frame reads, one tag
read) and fourteen probes for the closing call. Only the latter writes the
tag, and it returns cursor zero. Costs include one unit per call. 

### `cursor_write_address`

 The two base indices and the two actual indices used by a row are port
numbers of the typed graph. Hence even indirect inverse-column writes stay
inside the reserved output region. 

### `cursor_disjoint_layout`

 Natural-address layout conditions suffice for the complete cursor scan.
The frame may be placed on either side of the incidence columns. 

### `cursor_directory_write_tag`

 The closing transfer can write its tag after the scan without changing
any of the six typed incidence tables. 

### `initialize_linked_cursor`

 The native linked worker builds the level-zero cursor directory and
returns the dispatcher to its controller. The protected frame may be before
or after the columns. The tag and frame are read from the supplied memory. 
