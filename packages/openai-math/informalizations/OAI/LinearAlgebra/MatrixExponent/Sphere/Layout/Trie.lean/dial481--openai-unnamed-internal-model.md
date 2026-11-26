---
{
  "module": "OAI/LinearAlgebra/MatrixExponent/Sphere/Layout/Trie.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/MatrixExponent/Sphere/Layout/Trie.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/MatrixExponent/Sphere/Layout/Trie.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# A common binary tree for each host position

At a core position edges for different neighbors share a prefix tree.
At a frozen position each neighbor has a separate path from the root.
Thus a frozen station of large arity need not send all its bits through
one core relay. All potential relay positions are fixed by the host.


### `Trie`

 Each potential neighbor gets its own address. 
