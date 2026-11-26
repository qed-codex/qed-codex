---
{
  "module": "OAI/Computability/VPVNP/QueryPrefix.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/QueryPrefix.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/QueryPrefix.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Query predicates as coefficients of the explicit family

The literal encoding of a bounded query program supplies a fixed prefix.
Appending any payload computes its Boolean query result with the universal
coefficient machine's prescribed clock.


### `exists_prefix`

 A single program prefix compiles the entire finite query program at a
given query budget. Every payload is interpreted with the fixed clock of §1.1. 
