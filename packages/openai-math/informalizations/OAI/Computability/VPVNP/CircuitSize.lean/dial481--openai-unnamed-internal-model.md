---
{
  "module": "OAI/Computability/VPVNP/CircuitSize.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CircuitSize.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CircuitSize.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Minimum exact circuit size

Every formal polynomial has a division-free arithmetic circuit. Taking the
minimum over topologically ordered circuits therefore defines the gate count
`L_F` of §1, including zero-gate circuits for variables and field constants.


### `Circuit.constant`

 A single scalar input is an output of a circuit with no binary gates. 

### `Circuit.variable`

 A single variable is an output of a circuit with no binary gates. 

### `exists_circuit_polynomial`

 Every multivariate polynomial is the formal output of a finite exact circuit. 

### `circuitSize`

 The least number of binary addition, subtraction and multiplication gates
in a circuit computing `p` as a formal polynomial, with arbitrary scalar inputs. 

### `circuitSize_projection_le`

 Replacing variables by variables or constants preserves an upper bound
on the number of binary gates, regardless of the field constants used. 

### `circuitSize_map_le`

 Applying a scalar homomorphism to the output cannot increase its minimum gate count. 

### `circuitSize_descent_le`

 Section 1's reduction to one algebraically closed field. For a polynomial over
the prime field `k`, a lower bound over its algebraic closure `K` holds with the
same numerical value over every field extension `F` of `k`. 
