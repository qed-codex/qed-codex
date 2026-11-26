---
{
  "module": "OAI/Computability/VPVNP/CompressorRecordRefreshOldWidths.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorRecordRefreshOldWidths.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorRecordRefreshOldWidths.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Gathering the old actual widths in source-port order

The old directory stores widths by site and outgoing slot. The degree refresh consumes
a port prefix of the old lane. A scan decodes the bundle, residual lane and port fields,
reads each old slot’s width directly and writes it in source-port order.


### `splitBitWord_number`

 The port is the high field of the old lane number and the residual lane its low field. 

### `oldIndex`

 Source order is `(base arc, residual lane, port)`. The old width column uses
`(base vertex, port, residual lane, slot)`. 

### `gather`

 Public fields are port count, residual-lane count, old actual-width base and new
width-array base. Persistent state is the source-ordered segment index. 

### `widthAddress`

 Locate an old actual width by converting a source-ordered segment ordinal to its old
outgoing-slot index. 

### `readWidth`

 Read the old actual width selected by a segment ordinal. 

### `events`

 The 23-event gather visit reads the old slot width and writes it at the source-ordered
segment index. 

### `gather_native`

 A complete native call fetches the named old width, writes the source-ordered width
and returns the next segment number. 

### `SourcesDisjoint`

 The old and new width columns occupy distinct cells. 

### `Gathered`

 Completed rows and the exact frame after `k` gather calls. 

### `gather_run`

 The full native gather pass copies every width and changes only completed output rows. 

### `original_lane_index`

 A segment read reaches the exact old outgoing slot in the unsplit lane numbering. 

### `HasOldWidths`

 Widths at the directly addressed old sites and outgoing slots. 

### `read_state_width`

 The physical width read by the gather call is precisely the source-port field of the
actual dyadic compression state in the common incidence-directory format. 
