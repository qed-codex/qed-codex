---
{
  "module": "OAI/Computability/VPVNP/RAMTapeSiteTerminal.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMTapeSiteTerminal.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMTapeSiteTerminal.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Terminal predecessor check on the actual sorted site tapes

The address selects the missing-edge cases. The record scan adds its verdict
to the list of flags produced by the sort. A final linear pass halts with the
conjunction of all of these flags, including after a failed comparison.


### `inputs`

 Prepare the final sorted block, the predecessor and sent boundary records, a unary
word-width counter and one marker per slot for the boundary scan. 

### `routine`

 Use the site address to choose the endpoint checks, scan the sorted records, then halt with
the conjunction of the scan verdict and the accumulated sort flags. 

### `steps`

 Tick allowance for selecting the endpoint case, checking the sorted records and consuming
every accumulated verdict flag. 
