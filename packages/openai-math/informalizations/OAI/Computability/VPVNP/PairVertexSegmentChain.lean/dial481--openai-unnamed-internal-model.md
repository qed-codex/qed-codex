---
{
  "module": "OAI/Computability/VPVNP/PairVertexSegmentChain.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairVertexSegmentChain.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairVertexSegmentChain.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Sequencing native vertex segments

The two code ranges are consecutive. The first segment's successful continuation
is the entry of the second. Register placements are explicit so a preparation block
can fill the operands of its successor and disjoint scratch banks can be framed.


### `leftPC`

 Program counters for the first segment in a consecutive two-segment instruction range. 

### `rightPC`

 Program counters for the second segment, shifted past all instructions of the first. 

### `thenWith`

 The two segments may use the same register for an explicit operand handoff. 

### `seq`

 Separate the two private register files while keeping the shared DFS and saved registers. 
