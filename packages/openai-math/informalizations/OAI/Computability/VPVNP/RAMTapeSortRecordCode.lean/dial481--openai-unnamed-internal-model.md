---
{
  "module": "OAI/Computability/VPVNP/RAMTapeSortRecordCode.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMTapeSortRecordCode.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMTapeSortRecordCode.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 # Returning stack routines for sorting, selecting and validating two complete records 

### `Mode`

 Select either a record-equality check or a sorting comparison that retains the designated
minimum or maximum. 

### `Route`

 Post-comparison transfer through the saved operands, temporary staging and next-block
output, including the discard and verification cases. 

### `Route.src`

 The stack to drain at this cleanup or transfer step. 

### `Route.dst`

 Destination for a moved bit, using staging and then the next block for the selected
operand. Verification and discard routes drop the bit. 

### `State`

 Control of a five-field comparator, retaining the observed fields, cleanup route and
Boolean verdict through the final return. 

### `Route.after`

 Choose the next cleanup, staging or verdict state after exhausting the current route's
source stack. 

### `bothCanonical`

 Check that each scanned five-word operand is a canonical encoded record. 

### `cleanup`

 After all fields are scanned, choose the operand-transfer route and verdict for equality
checking or minimum/maximum selection. 

### `fieldExit`

 Save the observation for the completed field, then start the next field or proceed to
cleanup after field five. 

### `recordCode`

 Execute the field comparisons, drain or transfer the saved records, and emit the validity
bit for the selected mode. 

### `entry`

 Start at field zero with empty field observations and an initial word comparison state. 

### `routine`

 Package the five-field record comparator as a returning finite routine for the chosen mode. 

### `select`

 Sort two raw records and stage the requested minimum or maximum with a canonical-format
verdict. 

### `verify`

 Consume both records and emit the verdict that they are canonical and equal in all fields. 

### `selectOK`

 Validity flag for a sorting selection, requiring both operands to be canonically encoded. 

### `verifyOK`

 Validity flag for checking a transmitted copy, requiring canonical encodings and equal
words in all five fields. 

### `chosen`

 The raw operand selected by the record order and the wire's minimum-or-maximum direction. 

### `selectOK_iff`

 The returned validity bit for a comparison checks both five-word encodings. 

### `verifyOK_iff`

 The outgoing field must be exactly the same canonical five words as
the staged local record. 

### `chosen_parsed`

 The selected bit string represents the requested comparator output
even when a malformed slot was presented and its validity bit is false. 

### `record_run`

 The five-word pass consumes exactly two records and preserves their
complete bit strings on the two save stacks. 
