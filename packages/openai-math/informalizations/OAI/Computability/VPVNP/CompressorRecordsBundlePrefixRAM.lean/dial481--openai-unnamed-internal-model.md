---
{
  "module": "OAI/Computability/VPVNP/CompressorRecordsBundlePrefixRAM.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorRecordsBundlePrefixRAM.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorRecordsBundlePrefixRAM.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Native prefix sums of sorted thick-wire widths

A persistent cursor visits each live width in row order. On the first visit
to a bundle the running total is reset, regardless of the previous memory
contents. The start of each wire and the final total of each bundle are
written to separate descriptor tables.


### `visit`

 Public words give the live row size, physical row stride, sorted-width
base, wire-start base, and row-total base. 

### `row`

 The bundle row visited by a linear prefix-scan cursor. 

### `pos`

 The cursor's position among the live items of its current bundle row. 

### `index`

 The item's offset in a strided rectangle, computed from its row number and live position. 

### `gate`

 The word multiplier that discards the previous total at position zero and retains it at
later positions of a live row. 

### `start`

 The prefix offset for the current item, starting a fresh sum at the first item in each
bundle. 

### `width`

 Read the current item's width from the strided input rectangle. 

### `stepMemory`

 Store the current item's prefix offset and advance its bundle's total by the item's width. 

### `events`

 One prefix-scan visit's ticks and probes, reading the width and old row total before
writing the item start and updated total. 

### `prefixSum`

 Natural prefix sum in row `b` of the sorted-width table. 

### `Layout`

 The three physical regions fit, and each pair is disjoint in either order. 

### `Saved`

 The starts of all visited wires, and the latest nonempty prefix total
of each visited bundle, are stored. Every cell outside the writable rows
and the total column retains its initial value. 

### `ScanRun`

 Execution and work of a prefix of the native calls. 

### `FullRun`

 Full row-major execution, including exact natural wire offsets and row
totals. The frame includes the padding cells between live row prefixes. 

### `full_run`

 A single fixed program scans all `B*k` entries. Only input width sums
must fit in a word. Every row total is initialized by the worker itself. 
