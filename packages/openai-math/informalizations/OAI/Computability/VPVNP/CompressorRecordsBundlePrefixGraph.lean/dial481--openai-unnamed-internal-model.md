---
{
  "module": "OAI/Computability/VPVNP/CompressorRecordsBundlePrefixGraph.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorRecordsBundlePrefixGraph.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorRecordsBundlePrefixGraph.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Field starts and totals in the two sorted rows of a packed bundle

Each prefix scan reads a fixed-size live row within a rectangle. The thick row
uses the old concatenation order, and the motif row uses the CD piece numbers.
Their two full scans run consecutively on the external width arrays produced by
scattering the original ports.


### `Widths`

 Width, offset and total readbacks for a physical set of rows indexed by
a finite site type, each row indexed by a possibly different fiber type. 

### `Starts`

 Every live item in each bundle row stores the sum of widths of the items preceding it in
the given ordering. 

### `numbered_run`

 Execute the full row scan with a bound on the mathematical sum, recovering
every source-field start and total at its physical address. 

### `Outside`

 Static separation of a region from the two tables a prefix scan writes. 

### `ThickTotals`

 The AB width producer reads one old thick-wire total per absolute bundle. 

### `motifTotal`

 Sum of the original CD widths assigned to a bundle. 

### `thickWidth`

 The original arc width carried by a thick wire in the selected bundle. 

### `motifWidth`

 The original arc width carried by a CD motif assigned to the selected bundle. 

### `RowLayout`

 Prefix parameters use the two halves of the sorted-width rectangle in
the same port order. Each scan may place its output tables independently. 

### `prefixPublic`

 Public words for a contiguous pair of start rectangles followed by the
two total columns. The input sorted-width rectangle stays at its original
base. The two modes use the same fixed worker. 

### `RowLayout.packed`

 A single capacity bound certifies the layout of both prefix scans. 

### `Completed`

 The two prefix workers, and the typed contents of all six tables after the
second worker finishes. Each worker's full frame is available in its report. 

### `prefix_runs`

 Given the actual output rows of the width scatter, execute the thick and
CD prefix scans in sequence. The final tables retain every live sorted width,
its offset in the corresponding concatenation, and the row's total. 

### `scatter_prefix_runs`

 Scatter each old port once, then visit each occupied width cell exactly
once across the two prefix scans. Their combined call-plus-probe count is ten
times the number of old ports. A uniform bound on the old widths suffices. 
