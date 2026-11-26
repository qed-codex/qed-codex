---
{
  "module": "OAI/Computability/VPVNP/CompressorSelectedPayloadHistory.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorSelectedPayloadHistory.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorSelectedPayloadHistory.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Retaining the data of each selected pass for native site reads

The completed pass owns all the tables of its input level. Its selected
output graph lives in the successor incidence bank. Later passes can
replace the successor scalars and scratch tables while preserving that
bank. Each stored occurrence keeps the memory image in which its physical
parser data was produced and an agreement on both regions.


### `GraphCells`

 Pointer words and the packed canonical incidence of an input graph.
Scratch begins at the exclusive end of this range. 

### `Cells`

 All the producing level's fields, plus the pointer and incidence bank
of the state produced by that pass. 

### `cells_interval`

 Earlier payloads occupy addresses below the final state's first scratch
table, including the last producing pass's successor incidence. 

### `cells_before_or_input`

 At the very next pass only its input pointer and incidence bank can
overlap a previous payload. Every older successor already precedes it. 

### `Data`

 A predicate describing the physical parser data of an actual selected
pass, with its chronological index available to compute physical addresses. 

### `Past`

 Store actual producing memory images, preserving the physical words
needed to recover each pass's data in the terminal memory. 

### `Past.atLevel`

 Recover a stable physical predicate from its producing snapshot. 

### `Past.append`

 Capture the completed level and retain the selected parser data for
every older occurrence, including the immediately preceding output graph. 

### `Past.append_reports`

 Footprints of native worker batches may include scheduler addresses,
input scalars, input scratch, and any successor data. 

### `refresh_stored`

 Recover the native refresh builder's segment rows, term records and
dense demands from the historical snapshot of the selected occurrence. 
