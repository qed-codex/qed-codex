---
{
  "module": "OAI/Computability/VPVNP/CompressorShrinkSliceArrays.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorShrinkSliceArrays.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorShrinkSliceArrays.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Width arrays for shrinking-step kernel slices

The AB bundle and each surviving supply wire are repartitioned by the same
quotient and remainder rule. Each visit reads the total from external memory
and writes one subdivision width. A surviving supply total includes the
selected payload and one selector field per repetition.


### `splitOps`

 Public data give the total address, number of pieces, and output base. 

### `splitValue`

 Word width assigned to piece `i` when splitting a total `b` among `q` pieces. For `i < q`,
the first `b % q` pieces get one more than `b / q`. 

### `splitReport`

 Trace of one split visit, reading the total, writing the width at the output base plus
piece index `i`, and returning `i + 1`. 

### `splitValue_eq`

 Division of the remainder by the next cursor, followed by its nonzero
indicator, supplies the extra bit exactly to the initial remainder-many fields. 

### `SplitAt`

 Initial contents outside the target width row are preserved. 

### `split_prefix`

 The piece-count word is also the stopping cursor. Every call has two probes
and sixteen instructions, including the return. 

### `split_run`

 Materialize the complete target array from the total cell. 

### `Built`

 The native descriptor pass with its exact local cost. 

### `splitData`

 Put the source total and piece count in the fixed split-worker slots. 

### `SplitPass`

 A complete native split scan from cursor zero to `q`, with one two-probe report per piece
and the resulting widths in the output row at `t`. 

### `split_build`

 Repartition a physical old row. The native split and descriptor schedules
share external memory, including the computed total and the old widths. 

### `supplyOps`

 Read the selected supply field and repetition word, multiply by the fixed
selector width, and store the complete width for the subsequent split pass. 

### `supplyData`

 The supply worker’s three public operands in order are the term-field coordinate, selector
width per repetition, and address for the resulting total. 

### `supplyValue`

 Total width of the selected supply field, equal to its payload word plus the repetition
count times the selector width. 

### `supplyReport`

 Report of the supply worker, reading the repetition count and selected payload from the
term record, writing their combined width to the total cell, and returning zero. 

### `supply_build`

 Given the two addressed cells of the actual term-record image, the native
source reader, subdivision pass and interval construction produce both endpoint
directories for this supply edge. The rest of memory can hold other motifs. 
