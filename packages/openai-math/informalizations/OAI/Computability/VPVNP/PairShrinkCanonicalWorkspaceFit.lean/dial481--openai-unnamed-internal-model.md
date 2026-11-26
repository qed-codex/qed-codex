---
{
  "module": "OAI/Computability/VPVNP/PairShrinkCanonicalWorkspaceFit.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairShrinkCanonicalWorkspaceFit.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairShrinkCanonicalWorkspaceFit.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Workspace capacity at a scheduled shrinking motif

The terminal row end determines the private argument arena and histogram.
The hidden fields begin after the scalar stacks and use the square stride
computed by the handoff. These are the addresses used by the canonical job
for every party of the motif.


### `canonicalFits`

 Workspace capacity for the motif at the old level's published row base. 

### `canonicalFits_of_selected`

 The selected level's capacity applies at the canonical row end. In
particular this specializes the capacity supplied by
`ShrinkCallCapacity.eventually_packed_occurrence` for the physical level. 
