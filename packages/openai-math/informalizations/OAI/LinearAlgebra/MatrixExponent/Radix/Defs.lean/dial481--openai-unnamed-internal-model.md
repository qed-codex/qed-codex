---
{
  "module": "OAI/LinearAlgebra/MatrixExponent/Radix/Defs.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/MatrixExponent/Radix/Defs.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/MatrixExponent/Radix/Defs.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Stable radix passes with spare slots

A set presence flag denotes an empty slot. Each block receives a
pack's worth of separators for every digit. Stability places these
after the real rows of that digit.

