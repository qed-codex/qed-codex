---
{
  "module": "OAI/Computability/VPVNP/RAMProcessorProbeFields.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMProcessorProbeFields.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMProcessorProbeFields.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Staging ports for external reads, writes, and call returns

The architectural bank shares the read destination and the address and value
registers with the instruction interpreter. Three separate field stacks feed
the pre-sort record writer. Both copy stacks are empty at every boundary.


### `Extra`

 Non-architectural ports for the choice stream, staged record fields, running flag and two
copy stacks. 

### `Port`

 Combined port space for the instruction interpreter and the extra stacks used to stage
external probes. 

### `Bank`

 Stack contents at a probe-stage boundary, comprising the architectural bank, unused
choices, staged record fields and running flag. 

### `Bank.isa`

 Architectural register, public-word, persistent-state and interpreter workspace stacks
  available to the probe stages. 

### `Bank.choices`

 Remaining private bits from which an external read draws its guessed word. 

### `Bank.tag`

 Encoded operation tag staged for the next memory record. 

### `Bank.address`

 Bits of the probed address, saved before a read may overwrite its address register. 

### `Bank.value`

 Payload bits for the next record, drawn from the choice stream on a read and from a
  register on a write. 

### `Bank.running`

 Stack encoding the site's running flag, which the accept callback sets to false. 

### `Bank.stacks`

 Realize the probe-stage bank on the combined port space, supplying empty stacks at both
copy ports. 

### `Transfer`

 Word transfers for staging register operands, assigning a read result, returning a
persistent state or forming a record tag. 

### `Transfer.src`

 Source port for a staged word transfer. Tag generation uses the persistent word as its
width template. 

### `Transfer.dst`

 Port receiving the transfer's word, selected among the record fields, a read destination
register and persistent state. 

### `Transfer.set`

 Install a bit string at the transfer's destination in the structured probe bank. 

### `copy`

 Copy a transfer's source word to its destination using the two staging scratch stacks and
restore the source. 

### `setTag`

 Write the literal record tag at the width of the persistent word, reducing the literal
modulo the word capacity. 
