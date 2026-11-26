---
{
  "module": "OAI/Computability/VPVNP/CompressorRecordsRankedDirectory.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorRecordsRankedDirectory.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorRecordsRankedDirectory.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# The first four native passes for a shrinking state

Starting with the incidence and placement directories, the four passes classify
the arcs, append their IDs, gather their sorting keys, and write their ranks.
The output rank and original width of every port are now both directly
addressed by its actual outgoing ID. Each pass starts in the post-memory of
the preceding one.


### `RankedDirectoryRun`

 Post-memory at each pass boundary is computed from the preceding reports. 

### `ranked_directory`

 All four native report sequences, their combined cost, and the final
`shrinkNumber`, `shrinkOrder` and width entries. 
