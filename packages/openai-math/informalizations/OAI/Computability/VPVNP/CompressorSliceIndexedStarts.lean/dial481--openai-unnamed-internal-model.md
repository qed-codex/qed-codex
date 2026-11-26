---
{
  "module": "OAI/Computability/VPVNP/CompressorSliceIndexedStarts.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorSliceIndexedStarts.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorSliceIndexedStarts.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Interval frames from precomputed field starts

The sorted shrinking-bundle tables already contain field starts. Read them
directly during the pair scan, then index each positive frame at both ends.
A row occupies consecutive count cells, frames and endpoint-reference cells.


### `capacity`

 Workspace size for the endpoint counts, three-word pair frames, and references at both
endpoints. 

### `pair`

 Public operands for the pair scan, including the four input columns and the base of the
output frames. 

### `adj`

 Public operands for indexing the pair frames in the source and target adjacency
directories. 

### `Space`

 The input columns end before the workspace and its exclusive end fits in a machine word. 

### `Reports`

 Logs of the count clearing, pair-frame construction, and endpoint indexing sweeps. 

### `Reports.clear`

 Reports emitted while clearing the source and target count cells. 

### `Reports.pairs`

 Reports emitted while computing the copy frame for every field pair. 

### `Reports.refs`

 Reports emitted while appending positive-length frame references at both endpoints. 

### `Reports.cleared`

 Memory after replaying the count-clearing sweep. 

### `Reports.framed`

 Memory after the cleared workspace has been filled with the pair frames. 

### `Reports.all`

 Concatenate the clearing, frame, and reference reports in execution order. 

### `Native`

 The three native scans produce the supplied reports on empty choice tapes, each starting in
its predecessor's memory. 

### `Stored`

 All offsets and incidence lists of one completed row. Its frame fields
occupy three words at each source-major pair index. 

### `Stored.transfer`

 All reads used by the interval record and both endpoint lists lie in the
row's allocated bank. Thus a subsequent disjoint row preserves the entire
stored interpretation. 

### `build`

 The clearing, intersection and directory passes are deterministic and
work from arbitrary stale output rows. The two input prefixes are reused. 
