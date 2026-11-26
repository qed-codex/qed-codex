---
{
  "module": "OAI/Computability/VPVNP/RankQueryGramScalarSpace.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RankQueryGramScalarSpace.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RankQueryGramScalarSpace.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Storage of a signed weighted Gram coefficient call

The two input-matrix reads may take singly exponential time. Their stack
space bound is reused for each read. The fixed binary index program and
finite-field operations add polynomial storage independently of the time
spent inside either input query.


### `space`

 Peak stack height for a signed Gram coefficient, reusing the same read cap `S` for both
entries and allowing for index dispatch from height `A` and local field arithmetic. 
