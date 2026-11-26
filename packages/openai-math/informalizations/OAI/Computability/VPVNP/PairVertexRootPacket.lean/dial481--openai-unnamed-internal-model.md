---
{
  "module": "OAI/Computability/VPVNP/PairVertexRootPacket.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairVertexRootPacket.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairVertexRootPacket.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# The typed root argument after the native terminal gather

The root packet records the selected vertex's outgoing and incoming half-wire
bits in DFS order. Its private interval starts at the destination computed by
the terminal gather and ends before the common histogram.


### `packet`

 The root argument packet pairing the final site's DFS address with its packed half-wire
assignment from the shared bit array. 

### `length_le_stride`

 The physical frame stride covers both half-wire lists of the terminal
vertex, including repeated endpoints of a loop. 

### `of_gather`

 Translate the private-memory equality produced by the installed gather
into the packet invariant at the first DFS instruction. 
