---
{
  "module": "OAI/Computability/VPVNP/PairTreeDecodeDomain.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairTreeDecodeDomain.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairTreeDecodeDomain.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 # Reachability of every role visit on arbitrary private streams 

### `valid_append`

 A failing visit can stop the stream in the middle of any one child.
The later siblings need to be prepared only after that entire child succeeds. 

### `AlongBlock`

 The decoder remains in its admitted domain at every node of this block when the block's
argument packets precede the pending suffix. 

### `HeadDomain`

 The prepared frontier entails the native role domain of its first
packet. The domain may retain geometry words, old half-wires and headers. 

### `SubtreeAlong`

 The admitted-domain condition holds along each selected subtree's full word-encoded
preorder starting from its root packet. 

### `PointerLayers`

 The address component of each level's half-wire packet is the numeric
header pointer of that level. 

### `chain_along`

 All native calls visited before the first failed read have their actual
input domain. This includes malformed, short, and extra incoming streams. 
