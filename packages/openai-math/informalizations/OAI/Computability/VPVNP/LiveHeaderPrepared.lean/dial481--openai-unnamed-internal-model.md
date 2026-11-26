---
{
  "module": "OAI/Computability/VPVNP/LiveHeaderPrepared.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LiveHeaderPrepared.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LiveHeaderPrepared.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# The native header prefix before incident-field extraction

Index and advice scans, all scalar dispatches, and both primed-index stages
run on a single physical memory. The prefix leaves the field buffers zero
and the processor headers intact.


### `Metadata.ordinal`

 The scalar field's position in the eleven-stage metadata sequence. 

### `Prepared`

 Values at the interface from the primed-index phase to the field scans. 

### `prepared_prefix`

 The first fifteen actual stages, with the exact state seen by the
incoming and outgoing field descriptor scans. 
