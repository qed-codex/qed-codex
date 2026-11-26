---
{
  "module": "OAI/Computability/VPVNP/PairSimulationBranchDecoder.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSimulationBranchDecoder.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSimulationBranchDecoder.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 # Decoding the physical term bursts along a compression branch

A packet at one level consists of one full native burst per motif, in
worker order. The worker executes those bursts in its advised memory.
Its accepted choice determines the next state and the decoder of the
remaining levels. The final state consumes exactly the empty suffix.


### `WorkerInput.decodePacket`

 Check the number of bursts and the actual ordinal worker execution
before using the worker's proved inverse to recover the term. 

### `decodeOrdinalTapes`

 Decode an arbitrary list of chronological level packets. The order
of subsequent workers depends on the term recovered at each level. 

### `decodeOrdinalTapes_iff`

 Exact inverse on all inputs, including empty executions, malformed
bursts, missing motifs and surplus level packets. 
