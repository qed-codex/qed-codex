---
{
  "module": "OAI/Computability/VPVNP/RAMTapeSuccessorValues.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMTapeSuccessorValues.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMTapeSuccessorValues.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Typed values of the two physical successor checks

An interior field carries a canonical typed message. A missing field carries
the zero clamp. Once both fields pass, the physical cost, state and record
stacks give the cuts and last records used by the call loop and boundary pass.
The first processor starts from the public initial word at cost zero.


### `EdgeExpectation`

 Match a physical field to a typed edge, with a zero clamp for a missing edge. 

### `atSide`

 Select the optional outgoing or incoming typed successor message for the requested side. 

### `costWord`

 The endpoint cost fits in one physical word even when it equals the cap. 

### `savedState`

 A missing incoming edge installs the initial word. A missing outgoing
edge has no running target. A present edge takes its state from the message. 

### `Outputs`

 The stacks consumed by the call and sorting passes, stated relative to
their caller so a saved flag or record may have a nonempty stack tail. 

### `finish_values`

 All physical output values after both decoded fields, including the
initial cut and the missing target at the ends of the chain. 

### `finish_verdicts`

 Both physical verdict bits are set when the fields match their typed edges. 

### `guardResult_values`

 The guard consumes the verdicts, preserving every register needed by the
processor's continuation. 
