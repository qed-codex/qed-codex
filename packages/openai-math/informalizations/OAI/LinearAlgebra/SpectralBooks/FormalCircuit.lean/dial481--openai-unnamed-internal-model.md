---
{
  "module": "OAI/LinearAlgebra/SpectralBooks/FormalCircuit.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/SpectralBooks/FormalCircuit.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/SpectralBooks/FormalCircuit.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 # Formal polynomial semantics for division-free arithmetic circuits

Registers in the repository's straight-line programs can be interpreted in the
polynomial ring on the inputs. This distinguishes formal identities over a finite
field from equality of polynomial functions on its rational points.


### `gatePolynomial`

 The polynomial produced at one gate from the polynomials in its registers. 

### `registerPolynomial`

 Formal polynomial in each register of a straight-line program. 

### `FormalCorrect`

 Formal correctness in the paper, including over a finite ground field. 

### `formalCorrect_naiveAlgorithm`

 The usual entrywise algorithm computes the formal matrix product over every field. 
