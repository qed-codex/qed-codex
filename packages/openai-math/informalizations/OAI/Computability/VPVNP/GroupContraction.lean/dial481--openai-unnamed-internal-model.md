---
{
  "module": "OAI/Computability/VPVNP/GroupContraction.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/GroupContraction.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/GroupContraction.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 # Replacing live groups by native RAM computations

Each cut choice fixes a group's header memory. The sum over its communication
bits is then exactly the number of accepting RAM paths. The site-prefix
compiler supplies the local path-count identity; the regrouping works even
when a particular choice of incident messages is malformed.


### `liveHeader`

 External memory at a live group is initialized with its actual four-bit
headers. Addresses beyond the group receive the RAM's zero default. 

### `original_eq_group_counts`

 The full contraction with the site computations for each group replaced
by one computation of its RAM program, with the same address and cut data. 
