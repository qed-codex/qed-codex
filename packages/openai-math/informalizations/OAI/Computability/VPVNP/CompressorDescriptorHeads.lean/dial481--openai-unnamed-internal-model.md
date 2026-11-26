---
{
  "module": "OAI/Computability/VPVNP/CompressorDescriptorHeads.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorDescriptorHeads.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorDescriptorHeads.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Publishing the pointer words of a compressor level

After the scalar publisher has installed the current base count, degree and
lane count, a fixed burst writes the six incidence column heads and the heads
of all fixed-width record tables. The current row count comes from the current
header. The rectangular table capacity comes from the initial header, whose
base count times lane count gives the initial number of positions.


### `publisher`

 The shape is compiled into the worker. Public words zero and one hold
the current level header address and the level-zero header address. 

### `worker`

 Catalog entry for one guarded call at cursor zero. 

### `CountsAt`

 The three live scalar cells shared with the scalar publisher. 

### `publish`

 Natural addresses calculated by the native code, expressed in the same
level-major coordinates as the cursor, shrink and refresh consumers. 
