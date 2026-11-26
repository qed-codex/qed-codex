---
{
  "module": "OAI/LinearAlgebra/MatrixExponent/AdjacentDuplicates.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/MatrixExponent/AdjacentDuplicates.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/MatrixExponent/AdjacentDuplicates.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Testing a sorted list for duplicates

Each internal node checks the boundary between its two sublists. Even
copying the input at every level costs only a logarithmic factor.

