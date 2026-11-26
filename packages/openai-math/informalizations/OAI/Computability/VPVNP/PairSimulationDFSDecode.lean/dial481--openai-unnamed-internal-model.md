---
{
  "module": "OAI/Computability/VPVNP/PairSimulationDFSDecode.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSimulationDFSDecode.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSimulationDFSDecode.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Exact-use decoding of linked depth-first calls

For a fixed descriptor tree the node order is deterministic. A local reader
may reject its remaining stream, or consume a prefix and return the updated
scratch state. If the linked local instructions realize each successful
prefix and reject failed reads, the complete native traversal accepts
exactly the strings that decode through all sites with empty suffix.


### `Returns`

 Some fuel suffices to reach an accepting or returning native instruction. 

### `HookParser`

 Branch parser for the descriptor indicated by the top stack word. The
argument data are the caller's scratch above the reserved stack interval. 

### `HookParser.read`

 Read one descriptor visit from its node address, the current private scratch and the
  remaining choice bits. A successful read returns the selected visit path and unused
  suffix. 

### `HookParser.decode`

 Decode the nodes in traversal order. After each successful read, apply that visit's scratch
update and pass its unused bits to the next node. A failed read rejects the entire list. 

### `HookParser.Exact`

 The failed-read obligation applies on any incident bits or scratch
state, including field combinations incompatible across an older wire. 

### `HookParser.ExactOn`

 Local equivalence on the supplied argument states at a genuine descriptor
address. The domain can record the private pointer layout and the canonical
bit words written by the parent without constraining the bit values. 

### `HookParser.ValidAlong`

 The invariant is needed at the current visit and, on success, at every
visit reached from its updated scratch state and unconsumed branch suffix. 

### `returns_iff_decode_on`

 Both directions of the native whole-call characterization, for
a terminal continuation that requires exact consumption of the bit stream.
The proof also handles zero-child rows and zero-bit local checks. 

### `returns_iff_decode`

 Both directions of the native whole-call characterization, for
a terminal continuation that requires exact consumption of the bit stream.
The proof also handles zero-child rows and zero-bit local checks. 
