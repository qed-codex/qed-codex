---
{
  "module": "OAI/Computability/VPVNP/PairTerminalQuietFrame.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairTerminalQuietFrame.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairTerminalQuietFrame.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# The low-memory frame of the linked bootstrap and width scan

Each canonical terminal burst is replayed on its own physical input memory.
The terminal controller writes the phase and the saved state above the packed
workspace. The width scan's own stores are confined to its live directory and
header words.


### `replayFrame_stage`

 A source frame at one address survives the two linker stores, even when
the linked worker starts with different values at its control cells. 

### `QuietPrefix.force_start`

 Recover the physical first two stages from any forced three-stage
prelude, including a prelude for which all later paths reject. 

### `QuietPrefix.replayFrame_of_start`

 Join the two canonical initialization phases to the frame for the actual
third-stage reports. All memories in the conclusion are the successive
physical memories of the selected three-stage trace. 
