---
{
  "module": "OAI/Computability/VPVNP/CompressorRecordsPortRankScan.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorRecordsPortRankScan.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorRecordsPortRankScan.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Filling the absolute-port rank table

The classifier's owner and pivot columns, the bundle counts and the rectangular
key table are read-only throughout the scan. The output column is indexed by
the original arc's full outgoing-port ID, including the residual lane.


### `inputs`

 All addresses that can be read by the call at this port in its input memory. 

### `Regions`

 Regions for a full absolute-port scan. Input arrays may be placed in
arbitrary order and used by other phases of the compressor. 

### `interval_run`

 The native segment visits exactly the requested subinterval of the old IDs. 

### `scan_run`

 The complete increasing-cursor rank scan has one call per old port,
`cap+4` probes per call, and a frame covering every other external array. 

### `StoredRow`

 Contents of the cells read for one genuine port. The live keys can
occupy any prefix of the uniform-stride row. 

### `graph_scan`

 From the two materialized key tables, a single fixed template fills the
entire rank column. Its entries are the exact piece numbers and concatenation
numbers of the packed graph, including distinct old wires with shared endpoints. 
