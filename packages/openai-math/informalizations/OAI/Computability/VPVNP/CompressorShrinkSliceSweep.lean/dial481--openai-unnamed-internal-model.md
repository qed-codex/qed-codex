---
{
  "module": "OAI/Computability/VPVNP/CompressorShrinkSliceSweep.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorShrinkSliceSweep.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorShrinkSliceSweep.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Scanning the shrinking supply rows

Each dense term contributes four surviving rows. The width cells use the
absolute old CD arc number. The interval frames use the dense term number.
The total cell immediately precedes each row's private interval workspace.


### `Row`

 Per-row physical ports of the surviving slice schedule. 

### `Row.term`

 Address of the selected term record supplying the surviving width for this motif and
  role. 

### `Row.supply`

 The supply worker receives the selected layout and role coordinate, the selector width,
  and the address of the total. 

### `Row.count`

 Number of subdivisions into which this surviving supply width is split. 

### `Row.dst`

 First output address for the subdivision widths of this old arc and role. 

### `Row.bank`

 First address of the interval descriptor workspace for this dense motif and role. 

### `Row.total`

 The cell where the supply worker writes the selected role's total width before subdivision. 

### `Row.Outside`

 The address is outside the row's total cell, subdivision widths and interval descriptor
bank. 

### `Run`

 Native reports in chronological order, with every return/choice checked
by the existing segment semantics. 

### `Image`

 Readout and frame information for one completed row. The terminal memory
of its interval pass supplies the values inside that row's descriptor bank. 

### `Run.replay`

 Replaying the reports reaches the final memory used by the next row. 

### `Run.frame`

 All supply-row writes preserve every cell outside that row. 

### `Run.image`

 Once the split and descriptor workspaces fit, the complete row stores
the chosen width, the subdivisions and the interval records. 

### `Run.cost`

 A supply row with q subdivisions uses one source-reader call, q split
calls and the descriptor builder. Its total calls plus probes are linear in q. 

### `Runs`

 In the supplied order, thread each interval builder's output memory into
the first width read of the next row. 

### `Runs.frame`

 Exact memory frame of a sequence of native rows. 

### `scan`

 Scan actual workers with disjoint output rows. The returned images coexist
in a single final memory and the read-only term table remains usable throughout. 

### `Allocation`

 The dense term rectangle precedes the absolute-ID width rectangle.
Interval records follow in dense order, leaving the term rows read-only. 

### `Allocation.termBase`

 First address of the selected term records, stored in dense motif order. 

### `Allocation.termStride`

 Reserved word count between consecutive dense term records. 

### `Allocation.widthBase`

 First address of the surviving-width table indexed by absolute old arc and supply role. 

### `Allocation.absolute`

 Injectively map a dense motif ordinal to its absolute old CD arc number for locating its
  widths. 

### `Allocation.subdiv`

 The subdivision count assigned to each of the four supply roles. 

### `Allocation.selectors`

 Selector-bit count supplied to the worker when it reads a selected term's supply
  coordinate. 

### `Allocation.layout`

 The selected layout side used to choose the four supply coordinates from each term. 

### `Id`

 A surviving row identified by its dense motif ordinal and one of four supply roles. 

### `stride`

 Words reserved for a surviving-width row, using the sum of the four role subdivision
counts. 

### `recordStride`

 Words reserved for each dense role's total and interval workspace, five plus seven times
the width-row stride. 

### `widthEnd`

 Exclusive end of all absolute arc/role width rows and starting address for the dense
interval records. 

### `last`

 Exclusive end of the full allocation, after the width table and all dense motif/role
interval records. 

### `absoluteKey`

 Flatten the absolute old arc number and role into a single index of the width table. 

### `denseKey`

 Flatten the dense motif ordinal and role into a single index of the interval-record table. 

### `termStart`

 Starting address of the selected term at a given dense motif ordinal. 

### `widthStart`

 Starting address of the surviving widths for the given motif's absolute old arc and role. 

### `recordStart`

 Starting address of the total and interval workspace for a given dense motif and role. 

### `Fits`

 Term records have room for ten fields and precede the widths, all roles have positive
subdivisions, and the allocation and eight supply coordinates fit in words. 

### `row`

 Build the physical operands for a motif/role sweep, placing its total first in the dense
record and its interval workspace immediately afterward. 

### `rowOutside`

 The two rectangles cover every address touched by any surviving row. 
