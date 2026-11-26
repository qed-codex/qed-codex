---
{
  "module": "OAI/Computability/VPVNP/PrimedStackRAMState.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PrimedStackRAMState.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PrimedStackRAMState.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Word-memory updates on a represented grammar visit

A location mark changes one bit. A production increment changes one dense
counter by one. Neither operation changes pending frames or input rows.
Popping a frame has the complementary effect on these regions.


### `Holds.mark`

 Set a location mark while preserving every other represented component. 

### `Holds.increment`

 Increment exactly the logical Finsupp component selected by the dense label. 

### `pop_holds`

 Pop the next logical frame. The row register survives, and the branch test
register is zero even when arbitrary temporaries were supplied on entry. 

### `pop_holds_empty`

 Zero pending frames reject immediately at the underflow guard. 

### `leafBit_cell`

 Read the assembled terminal bit from the physical row selected by the outer schedule. 
