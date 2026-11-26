---
{
  "module": "OAI/Computability/VPVNP/PairRefreshSelectedPackets.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairRefreshSelectedPackets.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairRefreshSelectedPackets.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 # Typed half-wire packets at selected refresh rows

At a refresh origin the output network of the chosen term is the promoted
state. Reindexing the output half along this equality preserves all packed
bits in their physical order, including independently chosen endpoint values.


### `halfEquiv`

 The selected output half and the native reader's promoted half carry the
same ordered payload. The equivalence also recovers the original term half. 

### `prepared_at`

 A stored term-output packet prepares the actual row parser, with its
physical parent and the three private geometry words loaded by the vertex. 
