---
{
  "module": "OAI/Computability/VPVNP/PairSimulationLeafFrame.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSimulationLeafFrame.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSimulationLeafFrame.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# The private-memory frame of a cursor leaf visit

All writes made by the bounded stack program lie inside its own stack
intervals. In particular a successful leaf preserves the earlier private
histogram and the stored arguments of other pending vertices, cell by cell,
whenever the deterministic input preparation preserves those cells.


### `footprint_writes_inside`

 Even a partial or rejected prefix only writes inside the designated
intervals. Each source step can increase any one stack by at most one. 

### `footprint_scratch_outside`

 Cell-level scratch frame on every stream, for use by the DFS histogram
and by any remaining pending argument packets. 

### `parser_observations`

 The leaf's trace, its enabling scratch, and the cells it preserves are
all determined by the actual native stack path. 

### `parser_pending`

 Every other pending packet below the virtual stack intervals retains
the bit values established by the deterministic input preparation. 

### `realizes_zero`

 Realize a selected zero-label occurrence after the suffix comparison.
This proof is independent of how the original cursor factors were transported. 

### `Regions.histCell`

 A real histogram cell of the private layout, above the DFS stack and
strictly before the operand cache and all verifier stacks. 

### `Regions.packet_below`

 A still-pending argument packet is below every verifier stack in the
same allocated layout, regardless of its assigned bits. 
