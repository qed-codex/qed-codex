---
{
  "module": "OAI/Computability/VPVNP/RAMTapeBoundaryControl.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMTapeBoundaryControl.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMTapeBoundaryControl.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# The finite control for scanning sorted records and both endpoint fields

At each record the previous and current bit streams pass through the same
five field loops. The saved current bits are restored to the predecessor
stack before the next record. At an outgoing interior edge the right-hand
stream comes from the sent field. A missing edge requires all of its bits
to be zero.


### `Port`

 Stack ports for the sorted block, predecessor, sent record, field width, saved bits, and
slot count. 

### `Mode`

 Select an adjacent-row read check or an outgoing-edge equality check. 

### `Phase`

 Control of the boundary pass, carrying accumulated validity through record scans,
restoration, and endpoint checks. 

### `store`

 Assemble the seven boundary stacks from their bit lists. 

### `fieldPorts`

 Route a field scanner to the predecessor on the left and to the block or sent field on the
right according to the mode. 

### `afterField`

 Advance to the next of five fields, or latch the row or edge check and start restoring the
slot. 

### `code`

 Choose one of four fixed controls using the site's endpoint flags.
Neither the width nor the slot count occurs in the control type. 
