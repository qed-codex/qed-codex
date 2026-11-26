---
{
  "module": "OAI/Computability/VPVNP/LiveProgramCompressedPair.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LiveProgramCompressedPair.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LiveProgramCompressedPair.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# The eleven-operand compressed pair instruction table

The group enters at cursor zero with the histogram and auxiliary shadow already
prepared. The pair computes the online calendar size from `n`, publishes the
cursor geometry, derives and saves its actual level stride, and arms the online
calendar. The online program then invokes its planners and workers. On its
accepting exit the final field and vertex evaluator starts at cursor zero.
An accepting exit there returns to the live exponent checker.

The catalog, calendar recipes and final evaluator are finite instruction
tables selected before the input length. All mutable tags, pointers, widths
and entries are recovered or computed at runtime from the actual pair ABI.


### `Stage`

 Index of one of the ten components in the compressed pair, ordered from calendar
initialization through online compression to terminal evaluation. 

### `calendarRows`

 First stage, which computes the online calendar’s row count from the live input length and
fixed block-count ratio. 

### `cursorFrame`

 Bootstrap stage that prepares the cursor-parameter inputs in the workspace frame. 

### `cursorGeometry`

 Load the prepared frame and publish the computed cursor parameters in level zero. 

### `copyGeometry`

 Copy the saved cursor parameters back to the active workspace frame for the stride
calculation. 

### `stride`

 Compute and save the runtime address stride between successive descriptor levels. 

### `arenaBase`

 Install the history arena base at the end of the descriptor allocation, together with the
level count and input length. 

### `pointers`

 Install the scheduler’s six workspace pointers and reset its tag and ordinal. 

### `calendarStart`

 Set the inner scheduler tag to the calendar entry before online compression begins. 

### `online`

 Run the online calendar, planners, and workers that construct the compressed descriptor
history. 

### `terminal`

 Run the final field and vertex evaluator on the compressed history. 

### `Bootstrap`

 Fixed geometric parameters used by the native descriptor bootstrap.
The ratio is the numerator and denominator of the block-count exponent. 

### `Bootstrap.shape`

 Fixed dimensions of the descriptor directory, level headers, incidence columns, and slot
  tables. 

### `Bootstrap.degreeBits`

 Initial degree exponent used to set up the descriptor cursor parameters. 

### `Bootstrap.lanesPerBlock`

 Number of lane bits per compression block supplied to the initial cursor calculation. 

### `Bootstrap.steps`

 Fixed step count of the block schedule used to compute the descriptor allocation and
  traversal limits. 

### `Bootstrap.numerator`

 Numerator of the block-count exponent used by the calendar’s row-count calculation. 

### `Bootstrap.denominator`

 Denominator of the block-count exponent used by the calendar’s row-count calculation. 

### `stages`

 Ten native pair tables in execution order, comprising eight bootstrap stages, the online
scheduler, and the supplied terminal evaluator. 

### `next`

 Successor of a completed pair stage in execution order, with no successor after terminal
evaluation. 

### `regs`

 Maximum register count among the ten native pair tables, used as their common register-bank
size. 

### `embedding`

 Include a component’s registers into the common pair register bank at the same register
indices. 

### `components`

 Widen the selected native pair template to the common register bank while retaining its
eleven public operand indices. 

### `pairTable`

 Single fixed native body, with the same eleven public words as the pair
row in the outer live program. 

### `program`

 Burst RAM program obtained by instantiating the linked compressed-pair table with the
supplied word width and eleven public words. 

### `original`

 Burst RAM program of the selected native component before register widening and stage
linking. 

### `report`

 Wrap a native component report with five ticks to calculate the pair tag address, the tag
dispatch, and any transfer to the next component. 

### `tag_address`

 The outer pair linker uses the otherwise unused tail-state word. The
physical auxiliary shadow, and even its final site, are independent of this tag. 

### `execute_stage`

 Five ticks to compute the tag address, followed by the native stage
scan, source execution and, when applicable, a single tag transfer write. 

### `report_effect`

 Accounting of every deterministic pair-level link action. 
