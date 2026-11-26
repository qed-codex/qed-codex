---
{
  "module": "OAI/Computability/VPVNP/PairTraversalControllerSetupReads.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairTraversalControllerSetupReads.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairTraversalControllerSetupReads.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# External addresses read by the native traversal setup

The register bank loads six terminal scalars and seven kinds of level scalar.
Even when the persistent state is the final sentinel, taking its phase-level
modulo the resident level count selects an allocated level. Its predecessor
saturates at zero. The entry and dispatch ticks introduce no further reads.


### `levelScalars`

 Scalar fields loaded from the initial, current or preceding level. 

### `formulas_reads`

 The resident positive level count confines all formula loads, including
those issued while computing another load's address, to the designated scalars. 

### `formulas_worker_reads`

 The two terminal control cells are excluded when each physical level
header precedes the terminal header. The conclusion holds for every state word. 

### `Native.prefixTrace_reads`

 All reads in the actual native setup and guard trace avoid both terminal
control cells. The worker that follows the setup uses the resulting bank. 

### `selected_prefix_setup_reads`

 Every native setup issued on the selected reference run reads worker
cells, also after any prefix of tag and row writes. 
