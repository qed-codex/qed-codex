---
{
  "module": "OAI/Computability/VPVNP/RankQueryStackWords.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RankQueryStackWords.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RankQueryStackWords.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Numeric query registers for the Schur coefficient machine

The first register selects a query tag. The other five hold indices and degrees.
Power and factor convolution queries share the same row, column, exponent and
degree positions.


### `words`

 Six numeric fields of the current scalar query, including its tag. 
