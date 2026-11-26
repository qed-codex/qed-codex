---
{
  "module": "OAI/LinearAlgebra/MatrixExponent/Coloring/Add.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/MatrixExponent/Coloring/Add.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/MatrixExponent/Coloring/Add.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 # Ripple-carry addition of addresses modulo `2^n` 


# A circuit for alternating colours

Keep the orbit minimum and the next pointer at every position.
Two gathers and a pointwise minimum double the range in one step.



# Computing balanced edge splits

Sort edges by endpoint and activity. At every active edge, use the
inverse order to find its rank, pair neighboring ranks, and retrieve
the partner. The two resulting arrays determine the colouring.

