---
{
  "module": "OAI/Computability/VPVNP/PairPendingArguments.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairPendingArguments.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairPendingArguments.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Pending arguments of the depth-first native hook

The node address indexes a private argument interval. Writing a batch of
child half-wires establishes their exact bit values, preserves distinct
pending siblings, and leaves the DFS stack below the scratch boundary.
The row traversal then propagates the local hook's input invariant through
all visited addresses, including prefixes that reject.


### `Packet`

 A genuinely supplied local half-wire argument, named by its node address. 

### `Packet.node`

 Absolute DFS node address used as the index of this packet’s interval in the private
  argument arena. 

### `Packet.bits`

 Ordered half-wire bits supplied to the node’s handler, stored one bit per word in its
  argument interval. 

### `Packet.Fits`

 Bounds ensuring the packet starts at or above the DFS stack boundary, occupies at most one
arena stride and ends within the machine-word address space. 

### `rawScratch`

 Extend the typed scratch to the full private word space solely for
expressing native stores above the stack boundary. 

### `Packet.Stored`

 States that each addressed scratch word of the packet equals the machine-word encoding of
the corresponding bit, beginning at the node’s arena base. 

### `Packet.write`

 Updates scratch by storing the packet bits consecutively from its node’s arena base and
restricting the resulting private memory to addresses at or above the stack boundary. 

### `writePackets`

 The physical child writes occur in their listed order. 

### `writePackets_children`

 Distinct child records retain every bit value assigned to them. 

### `Packet.Stored.congr`

 Other private work may change the histogram or scratch tables. Matching
the packet's own addressed words is sufficient to retain its arguments. 

### `PreparedPackets`

 Ghost values of all current argument frames. The predicate on packets
specifies the node's actual half-wire format while retaining all its bit values. 

### `preparedPackets_push`

 Replace the popped argument by its ordered children. The physical
argument cells of every child and every older pending sibling agree with
the corresponding logical half-wire packet after the native update. 

### `HookParser.PreparesChildren`

 A node's completed local hook establishes the invariant on the recorded
children and preserves it on the existing stack suffix. No reachability
requirement is imposed on unrelated scratch cells. 

### `HookParser.PreparesFrontier`

 A prepared frontier may contain node-specific argument values, stack
separation and histogram information shared by its pending vertices. 

### `HookParser.validAlong_of_frontier`

 The admissibility of actual hook calls can use the whole current
frontier, including the distinctness of unprocessed sibling buffers. 

### `HookParser.validAlong_of_visits`

 Follow the concrete chronological DFS. Every hook is entered on its
prepared argument cells, for every possible remaining binary stream. 
