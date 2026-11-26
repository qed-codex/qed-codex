---
{
  "module": "OAI/Computability/VPVNP/PairShrinkLiveOperands.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairShrinkLiveOperands.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairShrinkLiveOperands.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Live resident operands for one physical shrinking map

The resident loop carries the old header, term pointer, constant stride,
one word and the writer's five public inputs in the same eight shared
registers throughout. Packet and shared-field readbacks are those of the
loop-entry private memory. The fixed map row runs against its own selected
motif, while its exterior frame maintains these inputs for the next row.


### `residentSlot`

 Live registers at a map-row entrance. Header registers 0, 4, 5 and
10 and the five public operands share the old-level register 11. 

### `residentLive`

 A host register is live at a resident map entrance when it is the image of one of the eight
operand slots. 

### `residentLive_cursor`

 The resident loop's cursor can advance without changing any live map
operand register. 

### `Job.liveOperands`

 Supply the non-static inputs of the exact row interpreter from the
loop-entry configuration and the chronological source readbacks. 
