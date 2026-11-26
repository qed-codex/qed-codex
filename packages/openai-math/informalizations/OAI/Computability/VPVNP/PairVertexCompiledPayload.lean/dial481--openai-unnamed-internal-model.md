---
{
  "module": "OAI/Computability/VPVNP/PairVertexCompiledPayload.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairVertexCompiledPayload.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairVertexCompiledPayload.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Reading a compiled pass payload in the current physical vertex memory

Each producing pass retains its input level and the successor pointer and
incidence bank. Even for the last pass, this bank ends at the final array base,
before the terminal program's offset table. Earlier physical vertices can
update counters and terminal control words without changing any retained cell.


### `PairSimulation.TerminalProgram.VertexEntry.packedPayloadWindow`

 The complete footprint of a selected pass has its calendar value at this
physical site, including every column of the successor incidence bank. 

### `CompressorRecords.CompiledResident.read_vertex`

 Read a pass of either kind at its chronological index in physical memory. 

### `CompressorRecords.CompiledResident.shrink_vertex`

 All native shrinking sources, header words, selected term and child
directory of the specified occurrence are present in the current site memory. 
