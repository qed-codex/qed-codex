---
{
  "module": "OAI/Computability/VPVNP/CircuitGrammarSpan.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CircuitGrammarSpan.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CircuitGrammarSpan.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Eliminating same-degree dependencies in a circuit

For degrees at least two, every homogeneous piece of a gate lies in the linear span
of products of two positive-degree pieces of circuit nodes. Constants, additions,
subtractions and degree-zero factors can thus be absorbed into the scalar labels
of the graded grammar in Section 8.1 of *VP and VNP differ over every field*.


### `Circuit.GrammarSlots`

 The start state, all variable inputs and one state per binary gate. 

### `Circuit.slotPolynomial`

 Read the polynomial at a grammar slot, returning the circuit output at the start slot, `X
v` at a variable slot, or the computed gate polynomial at a gate slot. 

### `Circuit.slot_component_mem`

 Every graded state of degree above one is in the span of lower-degree productions,
using the specified slots for this very circuit, including its output slot. 
