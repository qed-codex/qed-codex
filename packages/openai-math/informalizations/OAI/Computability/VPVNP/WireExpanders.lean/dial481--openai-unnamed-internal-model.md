---
{
  "module": "OAI/Computability/VPVNP/WireExpanders.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/WireExpanders.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/WireExpanders.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Common expanders for spectral wire pseudometrics

In Corollary 5.2 the class of complete CAT(0) targets consists of spaces whose
finite distance configurations are realizable by wires over the given field.
Closedness upgrades exact cube exclusion to uniform exclusion throughout the
class. Theorem 5.1 then provides a single graph at each selected order. Its
Poincaré bound pulls back to every labeling by parties of every spectral point.


### `HasWireExpanders`

 Connected loopless regular graphs of arbitrarily large power-of-two orders
have the same power-of-two degree and Poincaré bound for all spectral wire
pseudometrics over the field. Arc multiplicities come from port reversal. 

### `wire_expanders_of_cube_exclusion`

 Exact exclusion of one cube over the field implies the common graph
family of Corollary 5.2, with all its bounds uniform over the spectral points. 

### `wire_expanders_of_small_circuits`

 Corollary 5.2. Infinitely many small exact circuits for the integer
family over a fixed field provide one common expander family for its wire
pseudometrics. The excluded dimension can be chosen after the circuit exponent. 
