---
{
  "module": "OAI/Computability/VPVNP/PairShrinkRoleFieldFrame.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairShrinkRoleFieldFrame.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairShrinkRoleFieldFrame.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Vertex frame, counters and packet cells after both shrinking field stores

The old-child packets lie between the geometry pointer and the histogram. The
hidden-field slots lie beyond the verifier stacks. Hence the physical memory
passed to the first map has the original frame and histogram, and reads each
argument packet exactly as the child batch wrote it.


### `fields_histCell`

 The physical word of an individual histogram counter survives both readers. 

### `fields_histogram`

 Both readers retain the original value of the entire typed histogram. 

### `fields_arguments`

 Throughout the argument arena the hidden scan leaves the logical child batch intact. 

### `fields_packet`

 Every cell of any genuine argument packet, including an older pending sibling,
reads exactly as it would immediately after the logical child writes. 

### `TreeDecode.VertexFrameData.after_shrink_fields`

 Both shrinking readers retain the geometry pointer, all twelve geometry fields,
and the cached validator operands in the scratch used by the resident map loop. 
