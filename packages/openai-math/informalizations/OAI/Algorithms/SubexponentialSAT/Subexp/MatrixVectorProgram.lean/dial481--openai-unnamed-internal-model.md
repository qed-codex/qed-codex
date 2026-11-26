---
{
  "module": "OAI/Algorithms/SubexponentialSAT/Subexp/MatrixVectorProgram.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/Subexp/MatrixVectorProgram.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/Subexp/MatrixVectorProgram.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 A fixed row controller for encoded matrix-vector multiplication. 

### `row_eval`

 One row is read from the right stream. The saved vector, zero word,
modulus, and outer-loop counter are preserved. Its framed result is emitted
in reverse on port 13 for a final linear-time reversal. 

### `matrix_trace`

 A whole matrix-vector product with actual framing, scalar arithmetic,
row iteration, and output reversal. The unary row count is runtime input;
empty rows and zero-column matrices are handled without an EOF assumption. 
