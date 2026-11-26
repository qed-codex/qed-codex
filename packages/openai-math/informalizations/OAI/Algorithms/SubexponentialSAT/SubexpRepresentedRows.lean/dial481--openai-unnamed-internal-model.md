---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SubexpRepresentedRows.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SubexpRepresentedRows.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SubexpRepresentedRows.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Polynomial rows generated from represented field operations

The producer uses code words, finite expression constructors, and the supplied
arithmetic callbacks. It never extracts coefficients from an abstract field
value. Inverse constants are computed by finite-field powering. The canonical
coefficient lift is applied only after compiling the source polynomial.


### `nodeCache`

 The same finite inverse algorithm used by the CRT reconstruction. 

### `matrixValues`

 Zero extension is performed in the finite prime-field matrix before its
entry is embedded as a coefficient word. 

### `powerX`

 A monomial expression with a represented multiplicative identity. 

### `liftCode`

 Compile the source expression first, then lift exactly the requested
coefficient range. A residue section need not preserve sums or products. 

### `originValue`

 The origin vector is evaluated in the source field, using the same
compiled coefficients as the lifted polynomial producer. 
