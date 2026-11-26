---
{
  "module": "OAI/LinearAlgebra/MatrixExponent/ListBounds.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/MatrixExponent/ListBounds.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/MatrixExponent/ListBounds.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Bounds on independent lists

Here `P w t m` means that the `t`-fold tensor power at width `w` admits
an exact realization of size `m`. The three premises only use this family.


### `listBits`

 A list contains `2^w` records, each with `2*w` bits. 
