---
{
  "module": "OAI/Computability/VPVNP/CircuitDescent.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CircuitDescent.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CircuitDescent.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Descent without changing the circuit topology

A circuit for a polynomial defined over a base field `k` can replace every scalar
label with a new value in an algebraically closed extension of `k`. This applies
when the original labels belong to an arbitrary extension of `k`. Binary gate
types, wiring, reuse, the designated output and the gate count all persist.


### `Circuit.scalarLabels`

 All scalar occurrences in a circuit, including an output that is a scalar. 

### `Circuit.exists_scalar_relabeling`

 Descent of an exact circuit by changing only its scalar labels. The formal target
polynomial is interpreted in the two fields by their respective algebra maps. 
