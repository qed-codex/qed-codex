---
{
  "module": "OAI/Computability/VPVNP/PairTerminalPrefix.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairTerminalPrefix.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairTerminalPrefix.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Publishing final arc offsets and total bit width

The terminal prefix worker reads the final state's outgoing widths in physical
base, lane and slot order. The running total before each arc is precisely the
offset expected by the endpoint reader. The accumulator after the last arc
holds the exclusive end of the shared bit array, relative to its base.


### `arcCount`

 The edge order used by both the terminal bit scan and the physical incidence directory. 

### `width`

 Width of the final arc at this ordinal in the terminal prefix scan's physical order. 

### `operands`

 Three physical operands of the standard one-arc prefix worker. 

### `table`

 Prefix-sum instruction template for the terminal width array, entered with an initial zero
running total. 

### `Stored`

 Every live start cell, the running total and the unchanged memory around the
two output regions. These facts also apply to an empty final graph. 

### `run`

 Execute one call per outgoing arc. The word-indexed incidence column is the
source. The start and total cells are the only cells the execution can change. 
