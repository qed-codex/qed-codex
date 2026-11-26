---
{
  "module": "OAI/Computability/VPVNP/CompressorShrinkSlotPlan.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorShrinkSlotPlan.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorShrinkSlotPlan.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# The chronological shrinking slot program

Four fixed writes install the subdivision counts. Two scans prepare the
selected role and cyclic successor tables, and one clears the append counters.
Five sorted-slot scans and four output scans fill the six incidence columns.
Finally the program copies these columns, at their own base or lane-slot
lengths, into the following level's canonical incidence arrays.


### `Template`

 Fixed tag, degree, color and subdivision data used to build the shrinking output slots. 

### `Inputs`

 Runtime expressions for the graph dimensions and table heads needed by the shrinking slot
recipes. 

### `core`

 Build the visit for a slot-core phase using its phase-specific stop bound and public
operand expressions. 

### `output`

 Build the visit for an output incidence phase, supplying the split-width head along with
its derived operands. 

### `subdivision`

 Publish one role's fixed subdivision count in the runtime subdivision table. 

### `roles`

 The eight-row pass that publishes the role lookup for the selected layout side. 

### `cyclic`

 The pass that fills the cyclic successor-site table from the lane and tag counts. 

### `clear`

 The unused owners have append counters too. Clear their cells and the real
owners' cells before the uninterrupted five scans. 

### `sourceHeads`

 Expressions for the six constructed incidence-column heads used as sources of the final
copy passes. 

### `columnCount`

 The number of cells to copy for a column, using the base-arc count for the first three
columns and the actual port count for the last three. 

### `copyColumn`

 Copy a completed incidence column from the shrinking slot arena to the canonical head
published by the next level. 

### `visits`

 The list itself fixes the order of the native workers. Expression evaluation
supplies the current heads, selected layout and split-width input at runtime. 

### `operand_counts`

 Public-bank widths, in chronological order. The rectangular catalog can
reserve eight parameter words for every shrinking slot visit. 

### `words`

 Agreement of a worker's actual register arity, cursor bounds and operands
with its native unpadded frame. The external catalog assigns its tag. 

### `script_words`

 The chronological script compiler uses the worker's position as its tag
and pads the checked operand list to the largest arity in the catalog. 

### `clear_run`

 Even with arbitrary old scratch contents, the clearing worker establishes
the zero-counter input to the five native scans and preserves every earlier input table. 
