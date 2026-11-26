---
{
  "module": "OAI/Computability/VPVNP/SlotIdentifierOrder.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/SlotIdentifierOrder.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/SlotIdentifierOrder.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Integer keys for the unweighted shrinking slots

Appendix C numbers surviving slots using their motif ID, surviving type
and subdivision. A lane-zero motif is recovered from the base and tag of
the original CD wire, its old outgoing slot, its color bits and its slot
coordinate. Packing these fields into integers gives an explicit order
with no dependence on widths, maps, or the unconsumed lane length.


### `baseMotifIndex`

 Mixed-radix index of the source coordinates of the original CD wire,
suppressing its remaining lane, which is zero in a base representative. 

### `slotIdentifier`

 Mixed-radix integer key for a role edge. Subdivision indices use the
sum of all four subdivision counts as their common radix. 

### `slotIdentifierOrder`

 Sorting the lane-zero IDs is ordinary integer sorting of their keys. 
