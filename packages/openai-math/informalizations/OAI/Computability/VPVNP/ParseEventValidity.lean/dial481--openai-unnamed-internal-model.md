---
{
  "module": "OAI/Computability/VPVNP/ParseEventValidity.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/ParseEventValidity.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/ParseEventValidity.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 # Local incidence validity of an ordered parse tree

Each non-root occurrence is requested by its parent, and each binary occurrence
requests exactly the roots of its two ordered subtrees. Their disjoint leaf
intervals give uniqueness at every occupied interval.


### `events_isParseTable`

 The interval occurrences of an ordered parse satisfy all local table conditions. 
