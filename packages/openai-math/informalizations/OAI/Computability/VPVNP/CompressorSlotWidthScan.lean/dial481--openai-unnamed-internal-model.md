---
{
  "module": "OAI/Computability/VPVNP/CompressorSlotWidthScan.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorSlotWidthScan.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorSlotWidthScan.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Materializing widths in canonical outgoing-port order

Look up an outgoing slot's absolute field in the sorted incidence row. Its
numeric arc identifier identifies the old arc, role edge and subdivision.
Read the corresponding split-width cell. A dummy uses a masked zero offset
and writes zero independently of the value read there.


### `visit`

 Public words give the degree, lane count, total subdivisions, old-base arc
count, genuine address-space size and the row, split-width and output heads. 

### `row`

 Address of the source endpoint field for an actual outgoing port in the rectangular row
table. 

### `arc`

 Absolute arc ID recovered from the source field in the row table by dropping its endpoint
bit. 

### `offset`

 Reindex a genuine candidate arc as a split-width table offset ordered by absolute old arc,
edge type, and subdivision. 

### `splitAddr`

 Address of the selected split-width entry for a genuine arc, or the split table base for a
dummy arc. 

### `width`

 Width written for the actual outgoing port, taking the selected split width for a genuine
arc and zero for a dummy. 

### `events`

 Trace of one width visit, reading the source field and split-width table before writing the
outgoing port's width. 

### `rowNumber`

 Natural offset of the outgoing field in the rectangular rows, accounting for both endpoint
sides at every site. 

### `splitNumber`

 Natural split-table offset obtained by rearranging the genuine arc's digits into old arc,
edge type, and subdivision order. 

### `width_eq`

 A genuine field reads its old arc's split-width word. A dummy reads a
safe fixed address and supplies zero irrespective of that word. 

### `run`

 Full canonical outgoing-width pass, with read-only input regions below
the output head. Each record costs one call, two reads and one write. 
