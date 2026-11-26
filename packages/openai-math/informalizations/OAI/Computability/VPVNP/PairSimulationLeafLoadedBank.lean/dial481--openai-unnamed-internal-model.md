---
{
  "module": "OAI/Computability/VPVNP/PairSimulationLeafLoadedBank.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSimulationLeafLoadedBank.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSimulationLeafLoadedBank.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Exact private workspace after initializing a virtual validator

The stack bank determines every word inside its occupied intervals.
Outside them initialization preserves the old word, including stale cells
from earlier leaves in the same private call. This determines the scratch
state passed to the native stack interpreter.


### `occupies`

 Addresses actually written for one occupied stack. 

### `readCell`

 Look up the encoded bit occupying a private stack address, counting from the bottom of the
stack. Return none for an unoccupied address. 

### `memory`

 Initialize occupied private stack cells with their encoded bits and retain the old memory
at every other address. 

### `memory_eq`

 The exact updated memory follows from physical occupancy and the frame.
The right side is a function of the old memory and the logical stack bank. 

### `scratch`

 Apply stack initialization to the saved DFS scratch by replacing its occupied cells with
encoded stack bits. 

### `incidentPort`

 The leaf startup port that supplies the serialized incident data to the virtual site
processor. 

### `field_incident_iff`

 The finite source decoder designates precisely one incident port. 
