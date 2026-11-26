---
{
  "module": "OAI/Computability/VPVNP/PairSimulationTerminalBlocks.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSimulationTerminalBlocks.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSimulationTerminalBlocks.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Native phase blocks at the terminal workspace

Three deterministic phases set up the row and role metadata. The following
shared-bit phase changes the memory on which the vertex traversal runs.
The complete block includes the physical reports, supplied choices and
final memory so all three can be used at the next phase.


### `CompletedPhase`

 All completed native blocks for one selected phase at one physical memory. 

### `completedBlock`

 A proved source execution realizes a concrete completed block in the
physical memory, including its dispatch and final transfer. 

### `QuietPrefix`

 The first three completed terminal phases in sequence, with each call taking an empty
choice tape and each phase starting in the preceding phase's output memory. 

### `QuietPrefix.boot`

 Completed bootstrap phase starting at the terminal controller's initial entry and
  supplied memory. 

### `QuietPrefix.prefixRows`

 Completed prefix-row phase resumed at state zero in the memory left by bootstrap. 

### `QuietPrefix.traversalRows`

 Completed traversal-row phase resumed at state zero in the memory left by the prefix-row
  phase. 

### `QuietPrefix.BitPaths`

 Completed shared-bit phase beginning at state zero after the three deterministic terminal
phases. 

### `QuietPrefix.VertexPaths`

 Completed vertex phase beginning at state zero in the memory produced by the given
shared-bit phase. 

### `QuietPrefix.trace`

 Assemble the bootstrap, prefix-row, traversal-row, shared-bit, and vertex completions into
one certified five-phase execution trace. 
