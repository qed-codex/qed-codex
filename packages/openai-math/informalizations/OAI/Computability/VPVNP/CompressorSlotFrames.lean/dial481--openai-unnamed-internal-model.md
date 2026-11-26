---
{
  "module": "OAI/Computability/VPVNP/CompressorSlotFrames.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorSlotFrames.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorSlotFrames.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# The persistent cursor and memory frame of the preimage pass

Every successful call checks the owner and the current row length before its two
writes. Thus a scan in one descriptor level preserves other levels' tables, even
when the initial contents of the latter are arbitrary. The persistent cursor
advances once per call, including in a partial scan.


### `OutsidePreimageWrites`

 The two writable intervals of the preimage pass are the count column and the
rectangular row data. Space between these intervals is also preserved. 

### `collectPreimages_cursor_frame`

 Any successful native scan retains its exact end cursor and preserves each
address outside the two writable intervals. This applies directly to the reports
produced by `collectPreimages_run`. 

### `collectPreimages_frame`

 In particular every cell in a previous or subsequent level's disjoint interval
keeps its value through this pass. 
