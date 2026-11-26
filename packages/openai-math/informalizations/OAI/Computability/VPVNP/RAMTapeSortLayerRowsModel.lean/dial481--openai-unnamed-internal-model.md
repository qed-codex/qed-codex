---
{
  "module": "OAI/Computability/VPVNP/RAMTapeSortLayerRowsModel.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMTapeSortLayerRowsModel.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMTapeSortLayerRowsModel.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Streams after a prefix of sorting rows

The local record array is immutable during one layer. The selected records
accumulate in reverse bit order and the row checks accumulate in reverse
row order. At a cross-site stride the unread messages are suffixes of the
supplied outgoing and incoming fields.


### `other`

 Right comparator operand at a row, obtained from the partner in the local block for a local
stride and from the received row for a cross-site stride. 

### `selected`

 Output record at this row after comparing it with its partner and applying the stage's
minimum-or-maximum orientation. 

### `checks`

 Per-row validity bits checking both operands' formats and, on a cross-site stride, equality
of the sent record with the current row. 

### `pending`

 The pending suffix for a given direction. On a local stride the following
fields have not been consumed. 

### `pushed`

 Bits of the first k chosen records in reverse order prepended to the existing next-block
stack. 

### `latched`

 Flags for the first k completed rows, stacked in reverse row order ahead of earlier flags. 

### `prefixBank`

 Ambient state between callbacks, with all address and record scratch free. 

### `fieldsBefore`

 The incident stream at layer entry, beginning with the stage's record block exactly when
the stride crosses sites. 

### `budget`

 The counter pass and the two physical record lookups per row have a quadratic
bound in the local row count, with linear dependence on the two widths. 
