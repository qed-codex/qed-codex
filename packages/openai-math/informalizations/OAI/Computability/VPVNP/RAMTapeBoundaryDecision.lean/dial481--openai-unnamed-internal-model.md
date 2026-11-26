---
{
  "module": "OAI/Computability/VPVNP/RAMTapeBoundaryDecision.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMTapeBoundaryDecision.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMTapeBoundaryDecision.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Decision of the RAM boundary tape pass

The pass retains the last physical record, including padding, and latches
every read check. Missing predecessor and successor fields are checked bit
by bit against zero.


### `recordBytes`

 Flatten the five word encodings of one physical slot into its bit stream. 

### `blockBytes`

 Concatenate the physical slot encodings in block order. 

### `rows`

 Each visited record replaces the predecessor, even after a failed check. 

### `decision`

 An interior send is compared with the last physical record. At either
missing edge the transmitted bits must all be zero. 

### `decision_scan`

 The tape decision is the parsed-slot scan conjoined with a zero-bit
test on each missing endpoint. The raw records may use any tag or payload. 
