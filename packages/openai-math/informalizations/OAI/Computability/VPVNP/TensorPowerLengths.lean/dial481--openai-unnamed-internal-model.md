---
{
  "module": "OAI/Computability/VPVNP/TensorPowerLengths.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/TensorPowerLengths.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/TensorPowerLengths.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 # Selecting powers at lengths with a small circuit

A polynomial-size literal encoding of each tensor power suffices for cube
exclusion if its polynomial exponent is absolute. Use the largest power whose
encoding fits at the given length. The cutoff is selected after the circuit
length, which can belong to an arbitrary unbounded set.

