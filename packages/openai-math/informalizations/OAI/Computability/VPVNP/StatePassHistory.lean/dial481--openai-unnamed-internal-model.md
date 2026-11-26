---
{
  "module": "OAI/Computability/VPVNP/StatePassHistory.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/StatePassHistory.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/StatePassHistory.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Field records for the actual slots of a compression pass

At each output site, keep the local motif records, both half-fields of every
placed old vertex in every slot, and the new site's incoming and outgoing fields.
Outgoing fields in these records cover the entire output width profile.


### `State.halfWidth`

 An outgoing slot reads its own arc and an incoming slot recovers its
source by the inverse of the actual slot permutation. 

### `outputSite`

 Identify the term's output site with its site in the new lifted state. 

### `slotRecords`

 Include all old and new slot fields alongside the motif's local entries. 

### `slotRecords_bounded`

 One constant bounds the substep even when the old graph, widths, placements,
and selected terms vary. The extra records describe the local motif computations. 
