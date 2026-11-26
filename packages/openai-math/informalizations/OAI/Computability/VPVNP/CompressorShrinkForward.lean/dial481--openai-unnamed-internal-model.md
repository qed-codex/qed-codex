---
{
  "module": "OAI/Computability/VPVNP/CompressorShrinkForward.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorShrinkForward.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorShrinkForward.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Joining the scheduled shrinking visit windows

The concrete script breaks a shrinking substep into twelve chronological groups.
The live ordinal of each group's first visit includes the initial startup rows, all
completed compression blocks, all preceding shrinking substeps, and all earlier
groups of this substep. Source runs, clock and memory checks, and operand readback
are transported across these offsets by concatenating the true packet lists.


### `flatten`

 Concatenate finitely many checked groups, each evaluated from the post-memory of
all groups before it. The earlier packet lengths determine the current ordinal. 

### `first`

 Ordinal of the first call in the substep, including all earlier iterations. 

### `visitsBefore`

 The static visit count in a prefix of the twelve constituent windows. 

### `Groups`

 A physical group retains all data and guard checks, and is attached to the actual
catalog occurrences of this particular shrinking substep. 

### `joined`

 Source execution and operand/clock/footprint facts for the whole chronological
window of the actual online script. 
