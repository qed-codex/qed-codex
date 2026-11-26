---
{
  "module": "OAI/Computability/VPVNP/CompressorShrinkScheduledTail.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorShrinkScheduledTail.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorShrinkScheduledTail.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 # The three terminal DFS publication windows of a shrink

Starting at the actual memory after the slot construction, the metadata
writer emits its twelve old-header operands and two successor words. The
term and data writers then fill eighteen old-header words. Each report is
from the installed phase at its chronological ordinal.


### `termImage`

 Memory after writing the term base, term stride, selected layout bit, and absolute motif
table base to offsets 36 through 39 of the old level header. 

### `dataImage`

 Memory after writing the fourteen data pointers used by the shrinking node reader to
offsets 40 through 53 of the old level header. 

### `Result`

 Exact post-images of the three groups, together with their fixed online
control positions. 

### `Result.old_data`

 Both this level's packed tables and the successor's canonical packed
incidence region lie outside the two scalar publication blocks. 

### `run`

 Run Parts 9, 10 and 11 at their fixed program ordinals from the
post-slot memory. All capacity bounds use the real table-zero allocation. 
