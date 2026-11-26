---
{
  "module": "OAI/Computability/VPVNP/PairTreeDecoder.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairTreeDecoder.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairTreeDecoder.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Exact private-bit decoding through the selected term tree

A term visit selects its placed half-wires and a local kernel occurrence.
Its children then run on these precise half-wires, in the stored order.
Every successful subtree consumes the code of a factor occurrence, and
every occurrence runs with any following suffix. Both statements maintain
the argument packets belonging to the other pending visits.


### `ExactBlock`

 A list of prepared packet arguments and native addresses realizes one
prefix code. On success the older pending suffix is still prepared. 

### `forest`

 Decode all children in order, including an empty fiber, passing along
the scratch produced by each preceding child. 

### `Packets`

 The concrete pointer and ordered private half-wire words for a site. 

### `Subtrees`

 Each selected subtree decodes precisely the corresponding site's encoded choice tape while
preserving the pending packet suffix. 

### `children`

 Child packets of a selected term at one output site, enumerated in the parser's order of
the placement preimage. 

### `NodeStep`

 The only term-specific obligations concern the single popped row.
Its successful reads determine the placed half-wires and local factor,
and its native updates prepare the genuine child buffers. 

### `PacketLayers`

 The sequence of packet assignments to output sites along a selected term chain. 

### `finalPackets`

 Propagate the packet assignments down the selected chain and return the packets at the
final output sites. 

### `StepLayers`

 Node-step correctness holds at each selected layer, relating the incoming packets to that
layer's output packets and row pointers. 

### `chain_exact`

 Exact decoding, including failure, for every selected term chain.
Local implementation proofs are needed only for individual role rows. 
