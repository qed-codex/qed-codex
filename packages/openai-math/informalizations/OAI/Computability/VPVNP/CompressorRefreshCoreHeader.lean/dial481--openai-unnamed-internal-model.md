---
{
  "module": "OAI/Computability/VPVNP/CompressorRefreshCoreHeader.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorRefreshCoreHeader.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorRefreshCoreHeader.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Current header readback for the native refresh

The scalar publisher supplies the old vertex and residual lane counts. The
pointer publisher supplies the old incidence columns and the scratch origin.
These cells precede the first refresh array, so all stages of the native
refresh continue to read them at their original values.


### `Header`

 Specifies the vertex count, residual-lane count, six incidence column heads and scratch
start in a level header that fits in memory. 

### `Header.ofPublished`

 The live scalar and pointer publications produce the exact header used
by the refresh, including the packed old - slot incidence table. 

### `Header.reads`

 Operand support of the six physical level-header loads. 
