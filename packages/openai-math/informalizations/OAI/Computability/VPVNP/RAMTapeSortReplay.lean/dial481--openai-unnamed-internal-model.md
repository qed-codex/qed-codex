---
{
  "module": "OAI/Computability/VPVNP/RAMTapeSortReplay.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMTapeSortReplay.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMTapeSortReplay.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 # Acceptance and output of the chronological physical sorting replay

A failed check is retained through every remaining stage, irrespective of
the later messages. On a successful prefix the physical block is canonical,
so the next stage starts from the exact block of the checked word-work scan.


### `fold_spec`

 Starting from any canonical local block and any saved check flags, both
sort scans have the same acceptance. When they pass, parsing the physical
output gives the replayed record array. 

### `fold_messages`

 For the actual incident messages, passing the physical rows checks both
canonicality and the typed send constraints at this site. 

### `fold_messages_output`

 On passing physical messages the output supplied to the predecessor
test is the sorted record block of the typed distributed validator. 
