---
{
  "module": "OAI/Computability/VPVNP/PairSimulationLeafIncidentGeometry.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSimulationLeafIncidentGeometry.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSimulationLeafIncidentGeometry.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Initial private registers for copying the virtual validator's incident vector

The 24 straight-line instructions compute the rectangular arc stride, the
triangular sorting-layer count, the four source bases, and the exclusive
end of the incident stack. Each arithmetic row is width independent.


### `Operand`

 An incident-geometry assignment's right-hand side, drawn from a five-bit literal, a
register copy, or a binary operation on two registers. 

### `Line`

 One incident-geometry assignment pairing a destination in the thirty-register bank with its
right-hand side. 

### `rows`

 The straight-line assignments that derive payload widths, the four argument-buffer bases,
and the incident stack endpoint from the raw geometry. 

### `Stage`

 Index of an instruction in the 24-row incident-geometry calculation. 

### `target`

 The program counter for the next geometry row, or the caller's continuation after the last
assignment. 

### `emit`

 Compile a geometry assignment into a native constant, copy, or binary instruction with the
specified continuation. 

### `instruction`

 The native instruction for a given geometry row, using the linked registers and the next
row's program counter. 

### `Linked`

 The machine contains the compiled geometry instruction at every assigned row and uses the
specified continuation for the last one. 

### `Operand.eval`

 Evaluate a geometry assignment's right-hand side on the current thirty-register word bank. 

### `Ready`

 The six input registers hold the dimension, site, bucket size, word width, argument base,
and stack base for the incident copy. 

### `Prepared`

 The geometry registers hold the derived counts, payload widths, four buffer bases, and
destination stack endpoint needed for the incident copy. 

### `run`

 Exact deterministic prefix from the six caller-supplied geometry registers. 
