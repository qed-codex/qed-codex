---
{
  "module": "OAI/Computability/VPVNP/Circuits.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/Circuits.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/Circuits.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 # Exact arithmetic circuits and projections

Gates are listed in topological order. Each operand may use any earlier gate, a variable,
or any scalar in the coefficient ring. Only binary operations count toward the size.
The designated output is evaluated in the ring of formal multivariate polynomials.


### `BinOp`

 A binary addition, subtraction, or multiplication gate in an exact arithmetic circuit. 

### `BinOp.apply`

 Interpret a gate's operation on its two ordered inputs in the target ring. 

### `Ref`

 A reference available after exactly `n` gates have been computed. 

### `Program`

 A topologically ordered list of arithmetic gates. The index counts the gates already
available to subsequent operands. 

### `Circuit`

 An arithmetic program with one designated output. Its size index counts binary operations. 

### `Circuit.program`

 The sequence of binary gates available to the output reference. 

### `Circuit.output`

 The input variable, ring constant, or previously computed gate selected as the output. 

### `Ref.read`

 Resolve an operand using the supplied interpretation of constants, inputs, and earlier gate
values. 

### `Program.run`

 Evaluate the gates in topological order and return the value at every gate index. 

### `Circuit.eval`

 Read the designated output after evaluating the circuit with the supplied scalar and
variable assignments. 

### `Circuit.polynomial`

 The formal polynomial computed when each input is its corresponding indeterminate and each
scalar is a constant polynomial. 

### `Projection`

 Substitutions allowed in a projection. A variable may become a variable or a scalar. 

### `Ref.subst`

 Apply a projection to a variable operand and the supplied scalar map to a constant operand.
A gate reference keeps its index. 

### `Program.subst`

 Project the variable operands and map the constants of every gate in the program. 

### `Circuit.subst`

 Apply the same variable projection and scalar map to the program and its designated output
reference. 

### `Circuit.mapConstants`

 Specialize each scalar operand along the given map while retaining the circuit's input
variables. 

### `Circuit.map_polynomial`

 Scalar specialization preserves every binary gate of the circuit. 

### `Projection.hom`

 The coefficient-preserving polynomial semiring homomorphism substituting each source
variable by its prescribed target variable or scalar. 

### `Circuit.project_polynomial`

 Projecting a formal polynomial computed with `n` gates gives an `n`-gate circuit. 
