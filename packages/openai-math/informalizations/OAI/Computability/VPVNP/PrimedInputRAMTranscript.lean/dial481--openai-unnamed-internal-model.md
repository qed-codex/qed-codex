---
{
  "module": "OAI/Computability/VPVNP/PrimedInputRAMTranscript.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PrimedInputRAMTranscript.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PrimedInputRAMTranscript.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Addressing internal transcript bits for the paired-group counter

Section 11 of *VP and VNP differ over every field* chooses each internal
directed-message bit at its sending endpoint. The second pass reads this
bit at either endpoint, while the two absent successor ports return zero.
The scratch location is the sender site and the sender's local input offset.
This address calculation uses only public indices.


### `sourcePort`

 Compute the designated sending endpoint, using only the slot indices. 

### `designated`

 The first pass chooses one bit at each actual successor or sorting send. 

### `designatedEquiv`

 The bit-choice domain of the first pass is exactly the primed transcript's
shared-bit domain. 

### `sourcePort_idempotent`

 Every lookup that finds a sender terminates there. 

### `Address`

 Rectangular scratch coordinates within one of the two groups. 

### `portAddress`

 Identify a transcript endpoint with its site index and its local bit offset in the
rectangular scratch array. 

### `scratchBits`

 In the first pass only designated cells are assigned a choice bit. 

### `readPort`

 In the second pass every connected port makes one scratch read.
A missing connection returns zero without reading the scratch array. 

### `readPort_eq_assignment`

 Reading a primed endpoint supplies exactly the bit obtained by identifying
its transcript ports, for every assignment of sends. 

### `readPort_eq_incident`

 Correctness at a linear incident-input offset. No message parser
participates in this read. 
