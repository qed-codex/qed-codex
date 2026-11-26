---
{
  "module": "OAI/Algorithms/SubexponentialSAT/Subexp/ElementaryMatrix.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/Subexp/ElementaryMatrix.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/Subexp/ElementaryMatrix.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Executable elementary recurrence for the multicolor layout operator

This module connects the list algorithm to the exact operator used by the
support and spectral proofs. The algorithm enumerates positions in Fin Q
directly and never computes a powerset or selects a list from a quotient.


### `activeList`

 A fixed, computable enumeration of all active positions. 

### `operatorCoefficients`

 The coefficient array computed by the finite recurrence. 

### `operatorCoefficients_getD`

 Every retained coefficient is exactly the subset-defined elementary
projector from the mathematical construction. 

### `matrixLinearDP`

 The actual layout operator computed from one shared coefficient array,
without enumerating subsets. 

### `matrixLinearDP_eq`

 The executable recurrence realizes exactly the operator in equation (3.5). 

### `jointMatrixDP`

 An executable matrix on the joint fiber, obtained by applying the
computed operator to its actual ambient coordinate vectors. 

### `jointMatrixDP_eq`

 The executable joint matrix is exactly the one used by the rank and
support theorems. 

### `operatorCoefficients_operations_le`

 The matching instrumented coefficient computation uses at most 2 R Q
additions and multiplications of endomorphisms. No bit-cost claim is hidden
in this arithmetic-operation count. 
