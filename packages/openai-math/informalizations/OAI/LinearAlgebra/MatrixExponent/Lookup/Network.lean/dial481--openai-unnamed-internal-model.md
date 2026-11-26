---
{
  "module": "OAI/LinearAlgebra/MatrixExponent/Lookup/Network.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/MatrixExponent/Lookup/Network.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/MatrixExponent/Lookup/Network.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Substituting batched lookups into a wide network

A vertex of arity `t` uses batches of `2^t` copies. Repeating these to reach
a common batch size `2^u` costs at most a constant times `(1 + u)^(p - 1)`
per incident bit per copy, with one extra unit per vertex.


### `lookup_network`

 A uniform sorting bound suffices for arbitrary labels and all extensions. 
