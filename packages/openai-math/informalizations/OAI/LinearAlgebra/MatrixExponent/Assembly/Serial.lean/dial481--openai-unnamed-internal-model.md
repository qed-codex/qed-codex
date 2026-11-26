---
{
  "module": "OAI/LinearAlgebra/MatrixExponent/Assembly/Serial.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/MatrixExponent/Assembly/Serial.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/MatrixExponent/Assembly/Serial.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Freezing hosts

A retained station keeps all its arguments in order. A span
previously paired to a removed host becomes exterior. The only
additional data per block are one status bit per neighbor and
one for the host itself.



# Retaining all bit ordinals in the core of a frozen diagram



# Starting wire-saving subrounds with ordered core packets


 # Looking up short movement records at the other end of each stub 

 # Selecting six party addresses from the two paired endpoint records 

 # Lexicographic rank of a span at a host 


# A stage boundary with exposed bits

The data are a short record per occurrence, any auxiliary state
needed by the next step, and a dyadic bank for the actual payload.
At initialization the records are constants and each position of the
bank reads at most one exterior bit.



# Grouped announcements

Groups sharing a neighbor list exchange their messages in one record.
Processing within each group uses its own map, so assembling the record
does not require a lookup table spanning the whole processor.


### `announced_eq`

 Agreement on the layout bit within a group suffices. The output
contains the forward and untouched masks, both old ends and all parties. 

### `computes_reports`

 Two whole-record transfers suffice for all groups at once. The
processing between transfers is trivalent. 
