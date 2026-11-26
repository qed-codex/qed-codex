---
{
  "module": "OAI/Computability/VPVNP/MacaulayPairPorts.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/MacaulayPairPorts.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/MacaulayPairPorts.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 # Physical ports shared by the two ordinal scans and their entry routine 

### `Field`

 `false` designates the source monomial and `true` the column. 

### `OrdBank`

 Private stack ports for the thirteen-register dense ordinal lookup with no public RAM
operands. 

### `PowerBank`

 Private stack ports for the fifteen-register powered-monomial comparison with no public RAM
operands. 

### `Private`

 The disjoint private stacks used by ordinal lookup, residual-exponent packing and
powered-exponent comparison. 

### `Port`

 Complete call frame containing the shared monomial fields, private routine stacks and copy
scratch. 

### `Inputs`

 Query parameters for the two monomial scans and the optional shift and scale applied to the
source. 

### `Inputs.arity`

 Number of variables in both monomials and number of iterations in the exponent packer. 

### `Inputs.degree`

 Total-degree bound for the source when false and for the column when true. 

### `Inputs.ordinal`

 Zero-based position to look up in each of the two bounded-degree monomial enumerations. 

### `Inputs.scale`

 Power applied to the source monomial after its possible multiplication by a variable. 

### `Inputs.mark`

 One-based coordinate incremented before powering the source. Zero selects an unshifted
  source. 

### `values`

 Populate the public field stacks with scan parameters, unary markers, supplied raw keys,
output buffers and the zero and one words. 

### `publicBank`

 Install the public monomial query fields with all private stacks and copy scratch empty. 

### `embed`

 Embed a routine's internal ports into the joint private bank while preserving its external
fields and shared scratch port. 

### `lift_call`

 Lift a cleaned private call into the shared bank. Ports outside the
installed private block and caller slots are empty throughout the lift. 
