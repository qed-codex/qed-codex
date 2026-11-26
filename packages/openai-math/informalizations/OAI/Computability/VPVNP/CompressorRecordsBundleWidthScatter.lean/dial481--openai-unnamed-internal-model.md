---
{
  "module": "OAI/Computability/VPVNP/CompressorRecordsBundleWidthScatter.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorRecordsBundleWidthScatter.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorRecordsBundleWidthScatter.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Sorting the old widths by absolute bundle and rank

One burst call per old outgoing port reads its bucket, its rank, and its width.
It copies the width directly into that rank of the corresponding bundle row.
Each row is visited in old-port scan order but is stored in sorted key order.


### `visit`

 The scatter worker reads one old port's bucket, rank, and width, stores the width in the
ranked bundle row, and advances the cursor. 

### `source`

 Address of the current old port in one of the three input columns for bucket, rank, and
width. 

### `outAddress`

 Address of the width's destination, determined by the port's bucket, the public row stride,
and its rank. 

### `width`

 Read the width of the current old port from the third input column. 

### `events`

 The ticks, three input reads, and single width write made by one scatter visit. 

### `word`

 Represent a natural scan index as a machine word of the scatter worker's width. 

### `Filled`

 Exactly the occupied width cells of the scanned prefix have been written. 

### `Regions`

 The input cells are disjoint from all scatter destinations, and distinct live ports have
distinct destinations. 

### `scatter_values`

 Scatter a word computed from the port index and the third input column.
All workers using this layout share the same address, frame and cost proof. 

### `run`

 Complete native scatter, with a frame also covering holes inside the rectangle. 

### `fiberNumber`

 Each old arc belongs to exactly one of the two finite fibers, numbered by
the piece order for CD and the concatenation order for DD. 

### `rankOf`

 The arc's position in its assigned bucket under the supplied ordering of CD motifs or thick
wires. 

### `arcWord`

 Absolute old-port identifier, shared by the width, rank, and owner columns. 

### `RankedInput`

 Contents of the three columns consumed by the width scatter. 

### `Layout`

 Both sets of rows share a stride. The three input arrays can occupy any
intervals disjoint from the output rectangle. 

### `rowBase`

 First width word of a chosen absolute bundle. 

### `graph_run`

 Scattering directly from the absolute-port rank and width columns yields
the sorted concatenation at both bundle ends and the CD piece widths in their
own order. The scan consumes exactly five calls-plus-probes units per old port. 
