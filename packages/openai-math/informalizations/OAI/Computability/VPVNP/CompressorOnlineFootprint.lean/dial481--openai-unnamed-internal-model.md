---
{
  "module": "OAI/Computability/VPVNP/CompressorOnlineFootprint.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorOnlineFootprint.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorOnlineFootprint.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Memory agreement across online descriptor calls

The calendar, row recipe, launcher and closing worker call access the same
memory as the native source scans. Their writes end before the first level
header. In particular, a script can replay a source scan on the prepared
memory and carry its output into the next phase.


### `row_bound`

 The current row's exclusive end is at most the first level address,
including the final allocated row. 

### `prepared`

 The source worker enters with the same contents at every level address
as at entry to the calendar. 

### `preparation_effect`

 The three actual linked reports have the prepared memory as their
effect, including the parameter snapshot and the ordinal increment. 

### `post`

 The worker's closing transfer passes its data output to the next calendar. 

### `replay`

 A source packet computed on its own input replays on the launched
worker's memory. Its output agrees with the memory of the next calendar. 
