---
{
  "module": "OAI/Computability/VPVNP/CompressorPublishedHeadPackets.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorPublishedHeadPackets.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorPublishedHeadPackets.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 # Source packets for the term and DFS address publications

The actual block uses four term pointers, then either fourteen shrinking
addresses or one refresh pointer. Each publication retains its input
outside its own field block.


### `termValues`

 The four expressions published for a term's record head, stride, layout, and absolute
address. 
