---
{
  "module": "OAI/Computability/VPVNP/RAMProcessorProbeStep.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMProcessorProbeStep.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMProcessorProbeStep.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Executing one charged probe inside the physical call

The four transfers from the instruction callback to the next instruction
charge the budgets, stage the address and value, append the record, and
advance its ordinal. The recorded address is always read from the original
register bank, including when a read overwrites its own address register.


### `ProbeStep`

 One external read or write with its successor instruction. A read also specifies the
guessed word and the choice suffix left after consuming it. 

### `next`

 Private program counter at which execution resumes after the read or write. 

### `callback`

 Interpreter callback for the probe, retaining its register operands and successor
instruction. 

### `accepts`

 Choice-stream condition for staging a probe. A read requires the encoded guessed word
followed by the declared suffix, and every write satisfies the condition. 

### `record`

 Five-word record of the probe, with operation tag, original address, read or write value,
call start and current ordinal. 

### `stage`

 Stage the probe payload and advance the private program counter. A read also installs the
guessed word in its destination and consumes the corresponding choice bits. 

### `finish`

 Complete the probe by charging its cost, staging the payload, emitting the timestamped
record and incrementing the ordinal. 

### `run`

 One external action on the literal graph from the callback to the next
instruction, including the emitted record and both timestamp fields. 
