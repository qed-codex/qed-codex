---
{
  "module": "OAI/Computability/VPVNP/CompressorSourceSequence.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorSourceSequence.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorSourceSequence.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Executing a complete chronological sequence of native descriptor visits

The input is the sequence of original source packets and its memory
invariants. Each row recipe is evaluated at its own calendar ordinal in
any live memory that agrees with that packet's input data. The construction
threads the *actual* post-memory of the dispatcher through all packets,
preserving source reports and branch choices, and terminates at exhaustion.


### `Checked`

 Facts obtained by inspecting the actual source program for this packet. 

### `Prepared`

 Physical recipe evaluation at the packet's true offset. 

### `interval_stable`

 A semantic source-packet sequence determines valid steps of the concrete
online program, with precisely the same worker reports and worker tapes. 

### `interval`

 A semantic source-packet sequence determines valid steps of the concrete
online program, with precisely the same worker reports and worker tapes. 

### `sequence`

 A semantic source-packet sequence determines valid steps of the concrete
online program, with precisely the same worker reports and worker tapes. 
