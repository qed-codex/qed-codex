---
{
  "module": "OAI/Computability/VPVNP/CompressionBlockHistory.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressionBlockHistory.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressionBlockHistory.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Local records for one compression block

The record list at each site comes from the actual shrinking or refresh
kernel. Composition follows the same indexed schedule as the energy and
position estimates. A maximum over the finitely many substep constants
bounds every local record, and each branch takes at most one step per
shrinking degree followed by one refresh.


### `Procedure.RecordBounds.reindex`

 Transport the chosen records along equal presentations of a procedure's
degrees, lane length, divisor and energy coefficient. 

### `assembleBlockRecords`

 The bound records the actual kernels passed into `assembleBlock` and
is independent of the network order, widths, and chosen execution path. 
