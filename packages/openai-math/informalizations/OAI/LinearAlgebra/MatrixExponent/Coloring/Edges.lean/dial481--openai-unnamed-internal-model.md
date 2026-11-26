---
{
  "module": "OAI/LinearAlgebra/MatrixExponent/Coloring/Edges.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/MatrixExponent/Coloring/Edges.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/MatrixExponent/Coloring/Edges.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Parallel bisection of a regular bipartite graph

At odd degree a perfect matching takes the last colour. In the even
remainder, append the split bit to both endpoints. This encodes *both*
subproblems on the original edge array. One recursive call suffices.

