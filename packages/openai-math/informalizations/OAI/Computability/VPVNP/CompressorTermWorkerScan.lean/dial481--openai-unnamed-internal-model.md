---
{
  "module": "OAI/Computability/VPVNP/CompressorTermWorkerScan.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorTermWorkerScan.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorTermWorkerScan.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# A complete motif pass of the fixed native program

The native RAM starts at ordinal zero and returns the successor on every
admitted row. Its execution on a list of row tapes has the same final memory
as the five-call descriptor scan. Disjoint term rows preserve all demand
inputs as well as the descriptors already written.


### `Addresses`

 Public address operands describe every ordinal in the supplied layout. 

### `program`

 Native strided motif program instantiated with the grid, column orders, and four address
operands. 

### `call_frame`

 Any successful call at a valid row ordinal returns its successor and
preserves every demand input and every cell outside that row's descriptor.
This includes the dispatch frame when it is allocated outside the term rows. 

### `scan_native`

 One fixed native table traverses the complete layout. Each vector family
determines one successful tape tuple, and all stored row headers and supply
fields survive in the final memory. 

### `scan_site_bound`

 The local resource bound applies to each reset call even when the full
segment runs with a larger instruction cap. 
