---
{
  "module": "OAI/LinearAlgebra/MatrixExponent/Assembly/History/Entry.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/MatrixExponent/Assembly/History/Entry.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/MatrixExponent/Assembly/History/Entry.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Encoding the active atoms and local wire spans

Unused atom slots are turned off. Unused hidden slots have zero
width. Counting them as unused but positive-width wires would
multiply a contraction by an unwanted power of two.



# A common menu for heterogeneous atomic factors

Spans of different types share one address space. The description
contains no array of scalar coefficients. A label fixes both the
span widths and the function of their bits.

