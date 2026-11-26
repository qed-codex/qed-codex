---
{
  "module": "OAI/Computability/VPVNP/PrimedInputRAMFlowEval.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PrimedInputRAMFlowEval.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PrimedInputRAMFlowEval.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Finite executions of structured burst-RAM code

A derivation records the successful elementary instructions of a block and its final
registers and memory. Every test contributes a tick, every binary choice retains its
bit, and every visit to a loop test is counted, including the final false test.


### `Exec`

 Fuel-free successful execution of structured code. A derivation is finite even when
the program contains a loop. The event-list length is its exact number of instructions. 

### `line_choices`

 A successful straight-line opcode never consumes a binary branch bit. 

### `prependEvents`

 Attach the actual executed instruction events to the report of the continuation. 

### `Exec.execute`

 A finite structured execution runs on the actual machine using exactly one fuel
unit per event. Its branch bits are the choices in the derivation. It transfers control
to the linked exit with the remaining fuel and bits and the updated registers and memory. 
