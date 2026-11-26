---
{
  "module": "OAI/Computability/VPVNP/IncidenceProjection.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/IncidenceProjection.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/IncidenceProjection.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 # Exact-one weighted projections at prescribed lengths

Serialize each column once, interleaving its free selection bit with fixed
incidence data. The read-only control checks every row on this same input.
The unary program table depends only on the number of rows, while the data
occupy exactly `k * (m + 2) + 1` bits.


### `weighted_projection`

 For fixed row count, the required source length is linear in the number of columns. 
