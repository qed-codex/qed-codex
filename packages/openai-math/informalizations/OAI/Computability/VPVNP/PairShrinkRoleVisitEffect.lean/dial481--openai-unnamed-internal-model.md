---
{
  "module": "OAI/Computability/VPVNP/PairShrinkRoleVisitEffect.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairShrinkRoleVisitEffect.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairShrinkRoleVisitEffect.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Private memory of a scheduled shrinking visit

On the encoding of a kernel witness, the field readers write the preceding
sites' argument packets and then the owned hidden words. The resident maps run
on the projection of these two native store sequences, with an arbitrary tape
suffix and arbitrary initial private memory.


### `hiddenReader_stores`

 The hidden reader's scratch is the projection of the ordered native row stores
for any full private memory representing its entry scratch. 

### `scheduledVisitEffect`

 The scratch returned by the physical hook on a witness prefix is exactly the
resident scan's output on that witness's child packets and absorbed field rows.
This equality covers rejection by any map in the scan. 
