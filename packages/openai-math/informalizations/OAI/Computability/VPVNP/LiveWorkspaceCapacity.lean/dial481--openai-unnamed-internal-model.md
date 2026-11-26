---
{
  "module": "OAI/Computability/VPVNP/LiveWorkspaceCapacity.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LiveWorkspaceCapacity.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LiveWorkspaceCapacity.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Word space for the live buffers and the auxiliary workspace

All live and auxiliary scratch addresses, including a final workspace of
R² words after the virtual header, fit in one word for every sufficiently
large length once B is fixed. The threshold works simultaneously for all
groups, nominations and compressor term choices.


### `eventually_offset_fits`

 The same heap bound applies to every descriptor offset below R². 
