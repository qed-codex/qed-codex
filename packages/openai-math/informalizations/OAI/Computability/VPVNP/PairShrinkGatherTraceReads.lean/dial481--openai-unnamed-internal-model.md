---
{
  "module": "OAI/Computability/VPVNP/PairShrinkGatherTraceReads.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairShrinkGatherTraceReads.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairShrinkGatherTraceReads.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# External reads of the selected shrinking-party gather

Each visited frame contributes its compiled pointer loads and the three
possible slice-header reads. The published interval banks identify the
header addresses and prove that they fit in the native word.


### `trace_reads`

 The allowed pointer and header addresses of the rows cover every external
read in their chronological trace. 

### `Job.trace_reads`

 The public trace of the actual resident job reads only the addresses
allowed for its AB and surviving rows. 
