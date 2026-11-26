---
{
  "module": "OAI/Computability/VPVNP/CompressorRefreshBeforeSelector.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorRefreshBeforeSelector.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorRefreshBeforeSelector.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Choice-independent native refresh preparation

Before the motif selector runs, the gather, bundle and offset workers and all
ordered demand workers already determine their report sequences. Their only
numerical width requirement is that the sum of the old port widths fits a word.
The post-memory contains the exact demand at every block of the current graph.


### `PreSource`

 The fixed deterministic worker, initialized from the current public bank, before any choice tape. 

### `prepare_verified`

 Prepare the actual numerical selector input without a selected term. Each raw
worker comes with its physical bank, ordinal guard, reads above `low`, and writes
only within this level. The report list and demand post-memory are the same ones
used by `Build.Run` and its reverse enumeration. 
