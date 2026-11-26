---
{
  "module": "OAI/Computability/VPVNP/RAMTapeAddressLogLoad.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMTapeAddressLogLoad.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMTapeAddressLogLoad.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Private log lookup on a fixed finite bit-stack machine

The scan compares each full address against the query, starting at the newest
write. The first hit supplies the output. Exhaustion supplies a width-matched
zero. Rewinding the consumed prefixes restores every occupied entry.


### `scanSplit`

 Split after the first matching entry, or after the entire log on a miss. 

### `seekCost`

 Cost up to the rewind of the key stream. An unsuccessful final empty
test includes making the zero result and restoring the query. 

### `entryRun`

 One occupancy pop and push, one width-driven comparison, and one value scan. 

### `loadCost`

 The load includes rewinding the visited keys, values, occupancy marks and output. 

### `load_run`

 A lookup preserves the query and the full log, clears its work stacks,
and prepends the encoded result to the output port. 

### `loadCost_le`

 The time bound is linear in the length of the encoded log. 
