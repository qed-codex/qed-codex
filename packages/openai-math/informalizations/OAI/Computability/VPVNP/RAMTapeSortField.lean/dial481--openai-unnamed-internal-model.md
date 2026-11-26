---
{
  "module": "OAI/Computability/VPVNP/RAMTapeSortField.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMTapeSortField.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMTapeSortField.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 # Scanning and saving both words of one comparator field 

### `Port`

 Comparator ports for the two operands, the reversible width counter, saved operand bits,
staging, output block and validity flags. 

### `Bank`

 Bit-stack contents while a pair of records is scanned, preserved and optionally copied into
the next sorting layer. 

### `Bank.left`

 Unread bits of the left record stream. 

### `Bank.right`

 Unread bits of the right record stream. 

### `Bank.width`

 Unary markers limiting the scan of one field to one machine word. 

### `Bank.widthBack`

 Consumed width markers kept for restoring the counter after a field scan. 

### `Bank.savedLeft`

 Left operand bits accumulated in reverse order during comparison. 

### `Bank.savedRight`

 Right operand bits accumulated in reverse order during comparison. 

### `Bank.tmp`

 Temporary stack used to stage a selected record during the move to the next block. 

### `Bank.next`

 Stack accumulating the selected output records for the next sorting layer. 

### `Bank.valid`

 Stack of Boolean comparison and format verdicts retained for the final acceptance check. 

### `Bank.stacks`

 Interpret the named comparator bank as a stack indexed by each physical comparator port. 

### `Bank.update`

 Replace the bit stack on a single comparator port while retaining the others. 

### `FieldState`

 Control for scanning one fixed-width field, comparing and saving its bits, and restoring
the unary width counter. 

### `fieldCode`

 Pop paired operand bits under the unary width counter, update their comparison summary,
save both words and restore the counter. 

### `field_runs`

 Both consumed operands remain available on the two saved stacks in
reverse order. The width counter is returned intact. 
