---
{
  "module": "OAI/Computability/VPVNP/RAMTapeSuccessorEdge.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMTapeSuccessorEdge.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMTapeSuccessorEdge.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Executing one successor field check on the incident stack

Read the next eight words, check the successor or its boundary clamp, and
retain the five-word raw record for the final predecessor check. Every
fixed-length bit pattern returns both flags in the same number of steps.


### `Port`

 Registers for reading an incident successor field, checking its cost and tags, and
retaining its record and flags. 

### `recordBits`

 Raw little-endian bits of words 3 through 7. They are copied even for a
malformed record, so the boundary check sees the actual incident payload. 

### `edge`

 A caller chooses the physical stacks for all inputs, scratch, and outputs. 

### `edgeResult`

 Exact state at the return from one edge check. The input head now points
to the next field. The cap word and unary width are available for that field. 

### `edge_runs`

 On all wire values, the same exact stack cost covers extraction, testing,
and the copy needed for the predecessor condition. 
