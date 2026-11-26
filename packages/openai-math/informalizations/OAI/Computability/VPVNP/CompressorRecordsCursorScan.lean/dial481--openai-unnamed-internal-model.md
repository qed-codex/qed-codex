---
{
  "module": "OAI/Computability/VPVNP/CompressorRecordsCursorScan.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorRecordsCursorScan.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorRecordsCursorScan.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Native scan of the initial cursor graph

One burst call writes the six forward, inverse, displacement and width cells
for one numbered outgoing slot. This scan allows repeated visits to the same
base cell from different lanes. Agreement with a common specification suffices
for every visited cell to contain its specified value at the end of the scan.


### `rowWrites`

 Six address/value pairs written by the call with natural index `j`. 

### `Touches`

 Addresses visited in the half-open interval of row indices `[k,k+n)`. 

### `scanReports`

 The complete trace with one report per row, including the persistent
index for the next call. 

### `scan_native`

 Execution of precisely the calls whose initial indices are in the interval. 

### `scanReports_endState`

 The returned state can be used as the starting cursor of a following segment. 

### `scan_cost`

 One call plus six probes per slot, with six matching writes even when
multiple lanes visit the same base incidence. 

### `scan_run`

 All native calls, their exact work, the contents of each constructed
record, and preservation of every address outside the six scanned columns. 
