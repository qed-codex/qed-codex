---
{
  "module": "OAI/Computability/VPVNP/PairTreePacketLayers.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairTreePacketLayers.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairTreePacketLayers.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 # Canonical ordered packets of all layers of the selected compression 

### `fromRows`

 A nonterminal layer uses the half-wire layout of the next real term.
The final layer uses the endpoint collector's root half-wire layout. 

### `fromRows_final`

 At the singleton final root this gives the exact packet prepared by
the external endpoint gather, independent of the branch's depth. 

### `fromRows_children`

 The list of half-wire buffers used by the local row is exactly
the list prepared by its physical child-field pass. 

### `fromRows_packed`

 On a real state the incoming layer of the pass is in the arena's exact
outgoing-then-incoming slot layout. 
