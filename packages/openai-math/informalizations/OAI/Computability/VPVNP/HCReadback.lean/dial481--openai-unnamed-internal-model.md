---
{
  "module": "OAI/Computability/VPVNP/HCReadback.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/HCReadback.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/HCReadback.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Reading an assignment from a spanning cycle of the exact-one graph

At a buffer, the predecessor and successor must lie on opposite sides. Two
consecutive buffers must point in the same direction: otherwise both intervening
ports would have to send edges to the same clause vertex, or both would need
incoming edges from it. Thus a single bit determines the direction of each track.


### `trackDirection`

 The two edges of a cycle incident to a buffer have the direction indicated
by the variable bit. 

### `exists_exact_assignment`

 Every allowed spanning cycle is precisely the traversal constructed from
an assignment satisfying every exact-one constraint. 

### `cycleOfAssignment_injective`

 The outgoing arc at each separator recovers its track bit, so distinct
satisfying assignments give distinct tours. 
