---
{
  "module": "OAI/Computability/VPVNP/RAMProcessorProbePayload.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMProcessorProbePayload.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMProcessorProbePayload.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Probe record payloads and call returns

External writes copy both source registers to the record fields. External
reads stage the address before assigning the guessed word to its destination,
so a read may use the same register for its address and destination. A call
return copies the next persistent state and signals that the RAM is running.
An accepting call signals that execution has finished.


### `writePayload`

 Tag three marks an external write record. 

### `writePayload_run`

 The write fields contain the register values at the start of the probe. 

### `readPayload`

 Tag two marks an external read. Copy the old address before assigning
the guessed word from the value field. 

### `readPayload_run`

 The read record retains the address, even when the guessed value replaces
that address in the architectural bank. 

### `returnState`

 Return a register as the persistent input for the next call. 

### `accept`

 A final accepting call writes the stopped status. 
