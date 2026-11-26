---
{
  "module": "OAI/Computability/VPVNP/CompressorShrinkResidentRun.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorShrinkResidentRun.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorShrinkResidentRun.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 # Native construction of both local resident tables in chronological memory 

### `ownerBank`

 The owner scan takes four words in order, the dense-to-absolute motif table base, the role
table base, the selected side bit, and the output base for hidden or map owners. 

### `outputBank`

 The preimage collector takes six words for the chosen resident kind, giving its size and
owner base, the packed-site count and counter base, the row capacity, and the ID row base. 

### `Areas`

 The resident arena and both input tables fit the address space, each input table lies
outside the arena, and six is representable as a word. 

### `Passes`

 Reports from the three successive scans that build a directory of hidden residents or map
residents at the packed sites. 

### `Passes.owners`

 Reports from writing the packed owner of each resident in motif-major order. 

### `Passes.clear`

 Reports from setting each packed site’s resident counter to zero before collecting its
  IDs. 

### `Passes.collect`

 Reports from appending each resident’s dense ID to its owner’s row and incrementing that
  site’s counter. 

### `Passes.mid`

 Memory after replaying the owner-column writes on the entry memory, ready for the
counter-clear scan. 

### `Passes.cleared`

 Memory after the owner scan and the counter-clear scan, where the ID collection starts. 

### `Passes.final`

 Memory after collecting the resident IDs on top of the owner and counter scans. 

### `Passes.all`

 The complete directory trace in execution order, from the owner writes through counter
clearing to ID collection. 

### `Built`

 Certifies the three native scans, their ordered per-site resident directory, and
preservation outside the resident tables. The total charge is nine per resident and two per
packed site. 

### `run`

 Starting from actual CD and role data, this deterministic three-stage
scan gives precisely the ordered local hidden IDs or map IDs. 

### `Built.inputs`

 The entire resident workspace is disjoint from the two persistent
input arrays. A finished stage therefore leaves their typed readbacks live
for the next stage. 

### `retained_hidden`

 The later map-directory calls retain both the earlier hidden counts
and every earlier hidden ID. 

### `both`

 Six deterministic native visits execute on the same memory image
as the two resident headers describe. No guessed bits are used to recover
the resident lists. 
