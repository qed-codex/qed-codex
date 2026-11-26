---
{
  "module": "OAI/Computability/VPVNP/RAMTapeStackControl.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMTapeStackControl.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMTapeStackControl.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Two physical tapes for a fixed finite bank of bit stacks

The first tape lists the stacks in order, each terminated by a blank.
To reach stack `i`, move the preceding symbols onto the second tape. Each
saved symbol gets a nonblank tag, so a stored delimiter is distinguishable
from the empty scratch tape. A push or pop takes place at the exposed top.
Then restore the saved prefix, clearing every scratch cell as it is consumed.


### `Phase`

 Control states used to scan to one stack and restore the packed tape. 

### `bit`

 Encode a Boolean by one of the two nonblank tape symbols. 

### `remaining`

 Number of further stack separators to cross after reading this symbol. 

### `rows`

 The physical two-tape instructions implementing the given stack table. 

### `scratch`

 Store the nearest saved symbol first. 

### `fields`

 The byte stream of a block of consecutive stacks. 
