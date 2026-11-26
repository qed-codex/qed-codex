---
{
  "module": "OAI/Computability/VPVNP/PairShrinkRoleChildReads.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairShrinkRoleChildReads.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairShrinkRoleChildReads.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# External reads of the native child decoder

Each child consumes one pointer in the selected DFS row. Each slot probes its
width, and each incoming slot first probes its inverse-incidence entry. The
typed inverse column identifies the second probe even when the memory outside
the old level contains arbitrary words. Guessing and storing the payload bits
uses only private memory.


### `ColumnsBelow`

 Bounds for the two physical columns visited by the old-slot scan. 

### `scan_reads_below`

 External reads inside the loop over the child list. 

### `header_reads_below`

 The two descriptor words and the seven old-level fields are the external
reads of the native child header. 

### `trace_reads_below`

 The physical child-stage trace reads only the selected row, its directory
and its incoming and width columns. This also applies to a singleton refresh. 

### `reader_reads_below`

 Complete child reads are strictly below the terminal header whenever the
parent row, old directory words and the two live columns lie below it. 

### `ColumnsBelow.packed`

 In the descriptor allocation both columns end before the DFS row table. 

### `selected_row_end`

 The whole reserved child row fits inside the selected tag sequence's row
table, including the payload of its last site. 

### `old_fields_below`

 Starting the child header at scalar 14 leaves all seven fields inside the
old level, before the first DFS row. 

### `selected_reads_below`

 Specialize the read bound to a popped descriptor at its selected row
address, with the old field bank starting at scalar 14 of the preceding
physical level. 

### `bank_reads_of_reader`

 The register-bank initializer precedes the decoder with local ticks. Thus
every external read of the hosted segment belongs to the child decoder. 

### `worker_reads_of_below`

 A strict read bound excludes both physical terminal control addresses. 
