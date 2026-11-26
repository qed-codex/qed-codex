---
{
  "module": "OAI/Computability/VPVNP/JointScalarCore.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/JointScalarCore.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/JointScalarCore.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Gates and bit addresses of the joint scalar query

The input contains the sign selector, the unsigned equation address, and one
fixed-width exponent per formal coordinate. Witnesses for the parse, the
clocked computation, and the fixed motif comparison occupy separate banks.


### `parallel`

 Evaluate two verifier frames on a shared input and expose both sets of outputs, indexed by
their disjoint union. 

### `allZero`

 A linear-size conjunction checking that every specified bit is zero. 

### `queryWidth`

 Number of bits for the sign selector, equation address and fixed-width array of formal
exponents. 

### `witnessWidth`

 Combined width of the parse flags, clocked computation choices and motif coefficient
witness. 

### `Input`

 Input addresses of the signed coefficient checker, divided between the coefficient query
and its witness. 

### `polarity`

 First query wire, which selects the positive or negative part of the requested coefficient. 

### `rowWire`

 Query wire carrying a specified little-endian bit of the joint equation address. 

### `exponentWire`

 Query wire carrying bit `b` of the fixed-width exponent of formal label `j`. 

### `flagWire`

 Witness wire carrying one parse-event flag at the start of the witness array. 

### `choiceWire`

 Witness wire carrying one clocked machine choice after the parse-event flags. 

### `motifWire`

 Witness wire carrying one bit of the motif coefficient witness after the parse and
clocked-choice fields. 

### `query`

 Physical little-endian row and exponent words. The sign bit is the head. 

### `witnesses`

 The physical witness bit string has the three banks in this order. 

### `assignment`

 Supply the signed row and exponent query together with the parse, clock and motif witness
bits to the checker. 

### `sum_witnesses`

 Split a sum over joint witnesses into three independent sums in physical
bit order. This permits zero padding on every inactive bank without changing
the number of accepted witnesses. 
