---
{
  "module": "OAI/Algorithms/SubexponentialSAT/Subexp/MatrixProgramSemantics.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/Subexp/MatrixProgramSemantics.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/Subexp/MatrixProgramSemantics.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 Mathematical interpretation of the actual encoded matrix-program outputs. 

### `matrix_result_values`

 The program's elementwise result relation is the ordinary matrix-vector
product for any faithful scalar encoding. Canonicality is additionally kept
in the relation for the later executable zero test. 

### `matrix_result_words`

 With the canonical prime-field code, the output frames contain exactly
the standard words for the mathematical product. This also justifies using
the first product's actual bytes as the second product's input. 
