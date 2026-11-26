---
{
  "module": "OAI/Algorithms/SubexponentialSAT/Subexp/MatrixScalarProgram.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/Subexp/MatrixScalarProgram.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/Subexp/MatrixScalarProgram.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Scalar subroutines with the matrix checker's surrounding data preserved

These are calls to the actual finite modular-arithmetic instruction tables.
The eight additional ports carry vector streams, output, and runtime metadata.


### `accumulate_eval`

 One genuine modular multiply-add, preserving both vector streams and all
saved caller data. The accumulator is returned on port 8. 
