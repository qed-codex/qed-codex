---
{
  "module": "OAI/Computability/VPVNP/HCForward.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/HCForward.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/HCForward.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Directed traversal determined by an exact-one assignment

The bit of each variable orients its entire track. At a satisfied occurrence
the traversal visits the clause vertex, then continues at the other port of
the same slot. The unique satisfied occurrence determines the outgoing arc
from each clause.


### `Exact`

 Occurrences are distinct slots, including repeated literals within a clause. 

### `chosen`

 The unique satisfied occurrence at the clause. 

### `nextVertex`

 The next vertex along the cycle specified by the assignment. 

### `cycleOfAssignment`

 The traversal uses every vertex once as a successor. 
