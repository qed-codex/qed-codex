---
{
  "module": "OAI/Computability/VPVNP/PairSimulationSharedBitPhase.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSimulationSharedBitPhase.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSimulationSharedBitPhase.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# The completed shared-bit phase of the terminal machine

The phase reads the base and size of the wire bank from its terminal header.
Every binary assignment determines one complete physical record, including
the closing call and the handoff to the vertex worker. The reverse direction
classifies the reads of an arbitrary successful worker call before
transporting its reports back to the ordinary shared-bit scan.


### `call_reads`

 Every successful call, even on an arbitrary candidate tape and memory,
reads only header words 12 and 13. 

### `block`

 The physical phase record for an assignment to the entire wire bank. 

### `phase_iff`

 All three components of the physical record are forced by its bit assignment. 

### `equiv`

 Binary wire assignments enumerate all completed records with their
individual private strings, raw tagged reports, and final physical memories. 

### `native`

 Native execution realizes the completed block and initializes the vertex
worker's stage and ordinal in the two control cells. 

### `memory_image`

 Outside the two terminal control cells the entire physical memory agrees
with the contraction's shared-wire memory, including every untouched descriptor. 

### `readback`

 The phase corresponding to a wire assignment returns the chosen bit at every wire address. 

### `probe_cost`

 The linked cost includes the closing call and every transfer of control. 

### `local_caps`

 The data calls have at most seven linked probes and at most 53 physical
events. The same bounds include the closing call. 
