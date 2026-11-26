---
{
  "module": "OAI/Computability/VPVNP/CompressorRecordsSelectedScore.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorRecordsSelectedScore.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorRecordsSelectedScore.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Layout scores from the selected term records

For each motif the row stores its common repetition count and the payload
width of each of its eight supply coordinates. Adding selector bits recovers
the widths entering the two competing layout energies. Reindexing the sum by
the physical motif scan order proves that a strict comparison of the two
integer totals selects exactly the compressor's common layout.


### `motifOrder`

 The physical scan order of motifs used to index the selected term records. 

### `supplyOrder`

 Enumerate the eight supply coordinates as a choice of layout side and one of its four
coordinates. 

### `Selection`

 An admissible shrinking choice for every motif of the current packing. 

### `coordinate`

 The contiguous supply coordinate of one layout and role edge. 

### `Stored`

 The established term readback predicate, over the actual filtered old arc list. 

### `widthAt`

 Read a selected coordinate's payload width and add the selector bits contributed by each
repetition in its motif row. 

### `score`

 The weighted sum of squared selected widths over all motifs and four supply coordinates on
one layout side. 

### `chosenLayout_eq`

 The bit written on a strict improvement is the actual term-dependent shrinking layout. 
