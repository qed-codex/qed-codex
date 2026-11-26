---
{
  "module": "OAI/Computability/VPVNP/CompressorRecordsShrinkInput.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorRecordsShrinkInput.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorRecordsShrinkInput.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Physical input to term selection at a shrinking level

Starting from the old incidence directory, run the two greedy assignments, a
preliminary layout, arc classification and ranking, width sorting, and both
prefix constructions. The preliminary layout places thin sites at their bundle
source. The thick-wire and CD assignments computed before term selection
depend only on the two thickness flags, the old slot, and the assigned bundle.

The report lists in the execution begin with the memory produced by their
predecessors. All counters needed by the list pass are explicitly cleared.
The original directory, the greedy colors and offsets, and the preliminary
placement records remain readable alongside the sorted AB and CD inputs.


### `placementBase`

 The start of the preliminary old-site placement columns, immediately after the greedy
workspace. 

### `rankBase`

 The start of the bundle classification and ranking arena, immediately after the preliminary
placement columns. 

### `plan`

 The layout of bucket, key, count, identifier, gathered-key, and rank storage for the old
ports. 

### `widthBase`

 The start of the sorted width and prefix tables following the bundle ranking arena. 

### `stop`

 The exclusive end of the deterministic shrinking-input arena, including width rectangles
and bundle totals. 

### `placementBank`

 The preliminary placement worker's operands, using the greedy color and offset columns and
the layout that assigns thin sites to their bundle source. 

### `Run`

 Chronological execution of the deterministic, pre-selection part of a
shrinking level. Each component exposes its actual instruction tables. 

### `Run.greedy`

 The color and offset assignments supplying the preliminary placement pass. 

### `Run.sites`

 Reports of placing all old sites under the preliminary layout. 

### `Run.clear`

 Reports of clearing the thick-wire and CD row counts before appending any old ports. 

### `Run.classify`

 Reports of computing the bucket and sorting key for every old outgoing port. 

### `Run.append`

 Reports of appending each old port identifier to its classified bundle row. 

### `Run.gather`

 Reports of reading each row's identifiers to gather the corresponding old-port sorting
  keys. 

### `Run.rank`

 Reports of calculating each old port's rank in its classified row from the gathered keys. 

### `Run.scatter`

 Reports of scattering old arc widths into their bundle rows at the computed ranks. 

### `Run.thickPrefixes`

 Reports of computing starts and totals of sorted thick-wire payloads in each bundle. 

### `Run.cdPrefixes`

 Reports of computing starts and totals of sorted CD motif payloads in each bundle. 

### `Run.abPieces`

 Reports of splitting each thick payload total into AB piece widths and prefix offsets. 

### `rankPost`

 The memory after preliminary site placement and all bucket, append, key-gathering, and
ranking passes. 

### `post`

 The final shrinking-input memory containing the ranked widths, prefix tables, and split AB
piece data. 

### `inputBounds`

 The extents of the old color, offset, mate and shift columns in the
preliminary and selected-layout scans. 

### `directory_before`

 Both assignments can be read in any later memory preserving the shrinking input. 

### `bankParams`

 Public parameters of the deterministic preliminary placement scan. 

### `stored`

 The actual sorted width and prefix arrays in the final memory. 

### `reports`

 Replay the reports of every native substep in their execution order. 

### `reports_cost`

 The exact deterministic pre-selection cost. All factors multiplying the
site, bundle and port counts depend only on the degree. 
