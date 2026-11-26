---
{
  "module": "OAI/Computability/VPVNP/RAMSortCost.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMSortCost.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMSortCost.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Word work of the local bitonic validator

A site materializes its next block in a second array, scanning every local
offset once per layer. At a cross-site stride it reads both five-word fields
from the site's incident bit array. It validates both encodings, checks the
send against the current record, and uses the receive in the comparator.
Malformed fields set a failure flag. All loop lengths are public, including
on paths that have already set this flag.


### `readSlot`

 Parse one record at its exact linear address in the incident bit array.
In addition to the word scan, each of its `5*w` reads adds the record's base
to the within-record bit index. 

### `SiteRow`

 Result of processing one wire offset in a local sorting layer, with its selected record,
validation flag, and work charge. 

### `SiteRow.slot`

 Padded record selected by the comparator for this wire in the next layer. 

### `SiteRow.ok`

 Per-offset validation flag. At a cross-site layer it checks both encodings and agreement
  of the outgoing record with the current wire. 

### `SiteRow.steps`

 Word operations charged to addressing, reading, checking, and comparing the records at
  this offset. 

### `scanRow`

 One bounded per-offset operation. Local strides have no incident fields.
The additional constant steps cover tag-presence checks, Boolean operations,
five output writes and offset-loop control. 

### `Loads`

 What the local send and receive field parsers return for this layer.
The receive field comes from the unique designated partner. 

### `Scan`

 Output array, status flag and work accumulated during a materialized
scan of one site block or of several consecutive layers. 

### `Scan.block`

 The site’s array of padded records after the scanned sorting layers. 

### `Scan.ok`

 Conjunction of the per-offset validation flags over the layers processed by the scan. 

### `Scan.steps`

 Accumulated word work of the site’s scan, including the row charges and public loop
  overhead. 

### `scanLayer`

 Tabulate all offsets into the next buffer, retaining the conjunction of
their flags. Each row is computed once. The two buffers can swap roles. 

### `scanStages`

 Public phase and stride loops. Rejection is latched, so the upper bound
also covers arbitrary messages after the first failing check. 

### `LoadsStages`

 Successful raw parsing of all chronological send/receive fields into
the corresponding records of a replay assignment. 

### `scanStages_spec`

 Whenever the physical fields parse, this costed scan runs exactly the
local validator: it gives the same resulting records and the same decision. 

### `scanStages_canonical`

 Passing the costed scan forces every raw send and receive field used by
this site to be a canonical encoding. A malformed tag or noncanonical
padding at any layer prevents acceptance. 

### `scanRow_cost`

 Work bound for one offset, including two arbitrary five-word fields on
a cross-site layer. 

### `sortScan_cost`

 Exact public loop bound. The slot bound applies even when a field
encodes a bad tag or nonzero padding. 

### `emitStrides`

 Emit the `k` stride entries of a phase directly onto a supplied suffix.
Each iteration tests and decrements the counter, writes the two stage words,
and links the new entry. 

### `emitPhases`

 Generate the public chronological layer schedule in a single pass,
using a suffix accumulator. The construction copies each stage only once. 

### `emitPhases_spec`

 Exact word charge for emitting the public phase and stride schedule. 

### `scanSort`

 Complete costed sorting subroutine, including the linear-time generation
of all comparator layers. 

### `scanSort_cost`

 All parsing, address computations, comparator applications and public
schedule generation in the sorting subroutine have a uniform word bound. 
