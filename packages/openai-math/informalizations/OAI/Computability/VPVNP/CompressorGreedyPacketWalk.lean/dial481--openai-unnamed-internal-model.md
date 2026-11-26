---
{
  "module": "OAI/Computability/VPVNP/CompressorGreedyPacketWalk.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorGreedyPacketWalk.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorGreedyPacketWalk.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 # Evaluating each greedy packet in its own source memory

The old level scalars, incidence heads and table pointer are below the
greedy workspace. The six native workers preserve that prefix. Their
dynamic launch expressions consequently read the same inputs at each
stage, even after earlier workers have written the two directories.


### `maxFuel`

 Uniform fuel bound obtained by summing the fuel budgets of all greedy stages. 

### `packet_walk`

 Turn the six actual native kernels into header-relative source packets.
The only memory facts used about their traces are the two access bounds. 
