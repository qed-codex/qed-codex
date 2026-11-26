---
{
  "module": "OAI/Computability/VPVNP/PrimedCounterLength.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PrimedCounterLength.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PrimedCounterLength.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Number of calls in a native pair-counter history

Every successful call returns the next absolute cursor, or accepts at the final
item. This follows from the code for all five branches, even on arbitrary external
memory. Consequently a successful history halts exactly at the public call count.


### `native_result`

 All five branches preserve the prepared successor and total through the final jump. 

### `history_halts_iff`

 A successful partial run halts precisely when its number of supplied call tapes
equals the public call count. 

### `history_end`

 Every successful fixed-size tape reaches the accepting state. 

### `historyEquiv`

 Read an accepting native history as the unique array of choices at its absolute
cursors. Reading the array back in order recovers the original history. 
