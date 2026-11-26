---
{
  "module": "OAI/Computability/VPVNP/CompressorSurvivingPass.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorSurvivingPass.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorSurvivingPass.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Native scans of surviving wire subdivisions

Each role has a rectangular pass indexed by the dense motif and the subdivision.
A call writes the cells of one subdivision, including shared fields of its row.
Shared cells receive the same value on every write. The terminal memory therefore
contains every slice of every motif, even for widths smaller than the number of
subdivisions.


### `Segment`

 A scan starts at ordinal zero, returns the ordinal after the last call,
and satisfies the stated per-call bounds and memory access conditions. 

### `Segment.footprint`

 A segment's read and write regions are the union of the regions used by
its individual calls. 

### `Segment.validTrace`

 The four role passes can use the ordinary guarded dispatcher. Its bound
is exclusive, and the final cursor equals that bound. 

### `RoleRun`

 All native calls of one fixed role, and all output rows in their shared
terminal memory. 

### `Roles`

 Successive role programs start at zero, with the memory actually produced
by all earlier programs. Each list in `batches` is one role's native segment. 

### `Roles.get`

 Recover an individual native role segment at its actual starting memory.
The preceding batches are replayed in chronological order. 

### `four`

 The four role stages leave the complete endpoint tables of every motif
simultaneously readable. Their per-role traces have exactly `n * subdiv t` calls. 

### `One`

 Local specification of the native program at a dense motif and subdivision.
The single ordinal is computed from these two indices without external advice. 

### `role`

 Run all subdivisions of a single role. Equal-address writes agree, whether
shared by two subdivisions or made at the last unfilled position. 

### `full`

 Execute all four rectangular passes in role order. The frames of earlier
roles and the read-only directory survive, and every resulting interval image
has the chosen width. 
