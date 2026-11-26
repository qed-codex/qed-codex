---
{
  "module": "OAI/Computability/VPVNP/JointScalarLeafPorts.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/JointScalarLeafPorts.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/JointScalarLeafPorts.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Returning ports for an original Macaulay coefficient

The packed residual exponents and row register are immutable. The two
invocations of the counted checker share their input and advice, and write
their totals into the positive and negative operands of the field converter.


### `Port`

 Stack names for the row and exponent inputs, counter templates, row-prefix scratch, Boolean
checker and signed field conversion. 

### `queryPort`

 Checker input stack holding the polarity bit, equation address and packed exponent
coordinates. 

### `choicePort`

 Counter stack holding the current Boolean witness for the advised circuit. 

### `totalPort`

 Arithmetic input stack that receives the witness count for the selected polarity. A true
argument selects the negative count. 

### `resultPort`

 Stack onto which the converter prepends the signed coefficient in the extension field’s
polynomial basis. 

### `advicePort`

 Persistent checker stack containing the encoded gate instructions used for both witness
counts. 

### `Layout`

 Static bank data, supplied once for the family of queries. The row width
is the expected width of the equation address in the circuit query. 

### `Layout.prime`

 Prime modulus used to reduce the two integer witness counts. 

### `Layout.degree`

 Number of base-field coordinates in the polynomial-basis encoding of a field element. 

### `Layout.limbWidth`

 Bit width of each base-field coordinate in the packed field result. 

### `Layout.rowBits`

 Number of row-address bits to place between the polarity bit and the exponent payload. 

### `Layout.witnessBits`

 Width of the enumerated witness word. Each count receives one extra bit to hold the total
  when every witness accepts. 

### `Layout.circuitAdvice`

 Encoded Boolean gate instructions shared by the positive and negative coefficient
  queries. 

### `bank`

 Initialize the leaf’s named stacks with the row, exponents, checker inputs, two count
operands and output suffix, using the layout for the advice and width templates. 

### `clean`

 Leaf bank at a call boundary, with the row, packed exponents and output suffix in place and
the query, witness and count registers empty. 

### `countPorts`

 Route the checker’s total to the arithmetic operand for the selected polarity and its other
ports to the checker bank. 

### `counter`

 Run the fixed circuit-witness enumerator with its total directed to the selected
signed-count operand. 

### `reduce`

 Reduce the two counts modulo the advised prime and prepend their difference as a constant
element of the extension field. 

### `counter_bounded`

 Lift a counted checker call without charging its exponential elapsed time
to the space bound. The unselected count operand remains available. 

### `reduce_bounded`

 The converter reads both totals in place and writes only the field-result
port. The larger stack bank keeps the row, packed input and checker advice. 
