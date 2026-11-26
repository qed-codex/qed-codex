---
{
  "module": "OAI/LinearAlgebra/MatrixExponent/Coloring/Matching.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/MatrixExponent/Coloring/Matching.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/MatrixExponent/Coloring/Matching.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# A perfect matching at arbitrary positive degree

Enlarge the edge array by one bit. Its second half contains a fixed
dummy matching of the supported vertices. Give each real and dummy
edge the quotient and remainder, respectively, when a power of two
is divided by the degree. Repeated halving deletes every dummy edge.

