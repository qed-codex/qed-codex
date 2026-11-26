---
{
  "module": "OAI/Computability/VPVNP/CompressorRecordRefreshPrepare.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorRecordRefreshPrepare.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorRecordRefreshPrepare.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Preparing the external fields and internal demands of a refresh

The initial state is the shared six-column incidence directory. The three external passes
produce both ends of every segment. The fixed ordered ties then copy the appropriate
outgoing or incoming width into a contiguous demand record at each port block. No term
selection or payload assignment precedes this construction.


### `SegmentFields`

 The directory fields needed after the demand scan, including both physical endpoints
of every segment and the individual old width at each end. 

### `SegmentFields.transfer`

 Preserve the segment data across writes in other level arrays. 

### `demandApart`

 A demand row lies outside the seven segment arrays so all segment descriptors remain
available for the local kernel, even after copying the dense internal demand vector. 

### `PrepareRun`

 Four native passes in their shared-memory execution order. 

### `prepare_demands`

 From an existing incidence directory to all numerical inputs of the block term tests.
The same output memory also retains all external widths, endpoint offsets and bundle targets. 
