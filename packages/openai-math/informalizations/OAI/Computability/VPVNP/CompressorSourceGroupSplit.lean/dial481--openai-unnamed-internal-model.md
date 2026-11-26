---
{
  "module": "OAI/Computability/VPVNP/CompressorSourceGroupSplit.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorSourceGroupSplit.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorSourceGroupSplit.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 # Splitting a chronological group at a selected source row

The tail starts in the actual memory returned by the preceding packets,
and the native row ordinal advances by their number. In particular the
packet following a selector sees the selector's own output memory.


### `split`

 Split without choosing new executions or resetting the ordinal. 

### `split_at_selector`

 The selector is the next executed packet after the prefix. Its own
output memory is the source of the suffix, including when either side is empty. 
