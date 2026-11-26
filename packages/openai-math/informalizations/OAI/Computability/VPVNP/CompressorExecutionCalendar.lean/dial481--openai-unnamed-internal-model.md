---
{
  "module": "OAI/Computability/VPVNP/CompressorExecutionCalendar.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorExecutionCalendar.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorExecutionCalendar.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 # The block calendar of the actual mathematical compression execution

The initial cursor network undergoes shrinking at indices zero through
the last shrinking index, followed by one refresh, on every completed block.
Dependent bind and the intermediate degree casts preserve the chronological
order. The schedule also identifies the active pass before choosing a term,
which matters when that selector has no admitted term.


### `Phase`

 Calendar label for an indexed shrinking pass or the subsequent degree refresh. 

### `kind`

 Read the calendar label from the origin of a concrete state pass. 

### `Follows`

 Follow the prescribed schedule on every choice, including the next
row's phase on branches for which no later full path exists. 

### `oneBlock`

 Chronological pass labels of one compressor block, with each shrink in order followed by
refresh. 

### `blocks`

 Calendar obtained by concatenating the pass lists of the requested number of complete
blocks. 

### `execute_follows`

 The selected compressor's mathematical tree follows precisely the
finite block program's repeating shrinking and refresh schedule. 
