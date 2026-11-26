---
{
  "module": "OAI/Computability/VPVNP/PairSimulationTerminalProgram.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSimulationTerminalProgram.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSimulationTerminalProgram.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Terminal program of the compressed pair

The first four stages are the actual metadata, prefix, traversal-row and
shared-bit tables. The final stage is the numerical image of the finite
vertex segments, with its ordinal guard and return table. The program has
the eleven public words of the enclosing compressed pair.


### `workers`

 Static opcode tables in the physical order of execution. 

### `table`

 The fixed terminal program linking metadata, scans, traversal rows and vertex code. 

### `siteProgram`

 The physical instruction image with the actual two endpoint guards and
bootstrap/return segments, parametrized only by the five remaining vertex
code segments installed in the role dispatcher. 

### `accepts_iff`

 Full forward and reverse semantics, preserving the user's arbitrary cap
on the native reports and the exact branch strings of the five-stage table. 

### `accepts_five`

 An accepting terminal path contains one completed phase for each of
the five actual workers, in the table's physical order. 
