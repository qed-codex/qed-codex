---
{
  "module": "OAI/Computability/VPVNP/RAMProcessorGraphProbeEmit.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMProcessorGraphProbeEmit.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMProcessorGraphProbeEmit.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Emitting and closing the physical site record buffer

The linked emission routine pops one vacant slot and copies the five staged words
into the reversed buffer. Closing fills each vacant slot with zero words and reverses
the bits onto the output stack for the site's sorting circuit.


### `Snapshot.afterEmit`

 A single slot holds the reversed serialization of the actual staged record. 

### `record_emit_run`

 Emit a staged initialization or probe record at its linked occurrence. 

### `emit_run`

 A probe reaches its ordinal increment after exactly the five word copies. 

### `record_emit_reject`

 The actual pop reaches a rejecting row in one step when the slot stack is empty
or when its top is a false mark. 

### `Snapshot.afterClose`

 After the close routine, the padded record array is serialized on the output stack. 

### `close_run`

 The site reaches its accepting row with the canonical serialized, padded record block. 
