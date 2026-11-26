---
{
  "module": "OAI/Computability/VPVNP/CompressorDetailedResident.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorDetailedResident.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorDetailedResident.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Selected payloads at a compressor boundary

The current incidence graph and placement directories share their memory
with the parser data produced by earlier passes. Appending a selected pass
retains its post-memory as the new snapshot. For older snapshots, only the
completed levels and the current graph's pointer and incidence bank need
to agree with the previous boundary.


### `resident`

 Readable current graph, placement directories and selected parser snapshots. 

### `initial_live`

 The first cursor publisher creates the current graph with an empty
list of completed parser passes. 

### `append`

 Both the newly published graph and its parser data are read from the
same post-memory. The predecessor frame keeps the last pass's output graph
as well as the full data of strictly earlier levels. 

### `currentBoundary`

 Project a detailed boundary to the current graph expected by the
terminal bootstrap, preserving the concrete scheduler words. 

### `initialBoundary`

 The existing cursor interval supplies the detailed initial boundary
for any selected parser predicate. 
