---
{
  "module": "OAI/Computability/VPVNP/PrimedCounterChronologySlots.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PrimedCounterChronologySlots.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PrimedCounterChronologySlots.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Chronological branch lists of the pair counter

The input and node calls have independent tapes. Clearing the marks, initializing
a root, and comparing histogram entries consume no branch bits. Reassembling
the two varying arrays and these empty tapes fixes every absolute cursor slot.


### `Tape`

 A choice-bit list at each absolute position of the input, site and comparison schedule. 

### `inputPart`

 Read the private bit list at an input-assembly slot of the complete tape. 

### `nodePart`

 Read the bit list for a given site's node visit after its mark-clearing and
root-initialization calls. 

### `AdminEmpty`

 The three administrative subroutines are deterministic at every call. 

### `acceptedSlotsEquiv`

 Every admitted input assignment specifies its entire array of input calls.
An injective input encoding lets us count the independent choices even when
they yield the same row data. 
