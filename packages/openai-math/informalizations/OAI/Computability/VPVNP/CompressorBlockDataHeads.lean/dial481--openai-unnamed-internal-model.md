---
{
  "module": "OAI/Computability/VPVNP/CompressorBlockDataHeads.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorBlockDataHeads.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorBlockDataHeads.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Cached physical addresses for a shrinking node reader

After the slot and subdivision visitors finish, the local evaluator needs
direct access to the packed AB and surviving arrays, the chosen arc roles,
and both incidence directories. Fourteen fixed header cells hold these
addresses. The next-level pointer also locates its DFS layer base.


### `values`

 Offsets 40 through 53 in the old level header. 

### `visits`

 Fourteen visits that publish the shrinking reader's physical addresses at header offsets 40
through 53. 
