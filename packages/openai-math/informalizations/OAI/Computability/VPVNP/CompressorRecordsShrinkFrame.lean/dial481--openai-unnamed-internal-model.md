---
{
  "module": "OAI/Computability/VPVNP/CompressorRecordsShrinkFrame.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorRecordsShrinkFrame.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorRecordsShrinkFrame.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Retaining the old incidence and placement directories across shrink passes

Both directories precede the temporary width and ordering arrays. A frame
theorem below the new arena therefore retains their typed readbacks even
when the following pass starts with arbitrary contents in its own region.


### `slotCount`

 The number of actual port slots, counting every base vertex, lane, and slot in the state. 
