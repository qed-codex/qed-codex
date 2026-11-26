---
{
  "module": "OAI/Computability/VPVNP/CompressorRecordsShrinkRAM.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorRecordsShrinkRAM.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorRecordsShrinkRAM.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Native computation of shrinking placement rows

Scan old positions in their original order. Four reads recover the greedy color and
offset and the selected outgoing base slot's mate and shift. The resulting four
columns give the layout owner, the thickness bit, the assigned bundle's outgoing
index, and its target site. The bundle's source site is the quotient of its index by
the degree.


### `visit`

 Public words are the residual and tag radices, degree, color-mask radix, last
color, layout bit, four input columns and four output columns. 

### `div`

 Unsigned word quotient used to remove low fields when decoding a shrinking position. 

### `mod`

 Unsigned word remainder used to isolate a low field or a single color bit. 

### `xor`

 Bitwise exclusive OR of two words, used to apply tag offsets and lane displacements. 

### `select`

 Arithmetic selection in the word ring, used with zero-or-one selectors. 

### `Fields`

 The four machine words obtained by unpacking an old-position cursor in the shrinking scan. 

### `Fields.base`

 Base vertex index used to look up the greedy color and tag offset. 

### `Fields.mask`

 Color mask of the old position. Its bit for the base vertex's color determines thickness. 

### `Fields.slot`

 Slot label selecting the outgoing base port whose mate and displacement are read. 

### `Fields.low`

 The tag and residual lane packed together, with the residual lane in the least
  significant bits. 

### `decode`

 Split the old-position cursor into base vertex, color mask, slot label, and combined tag
and residual lane using the public radices. 

### `baseArc`

 Linear index of the outgoing base port, computed as the base vertex index times the degree
plus the slot label. 

### `readColumns`

 Read the color and tag offset at the base vertex, then the mate and displacement at its
selected outgoing port. 

### `Outputs`

 The four entries of a shrinking placement row, parameterized by the type used to represent
their values. 

### `Outputs.owner`

 Packed site to which the chosen layout assigns the old position. 

### `Outputs.thick`

 Thickness flag obtained from the old position's color mask at the base vertex's greedy
  color. 

### `Outputs.assigned`

 Outgoing port index of the assigned bundle, encoding its source site and slot. 

### `Outputs.target`

 Packed target site of the assigned bundle. 

### `outputs`

 Compute the placement row from the four input columns. A thick position keeps its packed
site, while the layout bit selects the source or target for a thin position. 

### `events`

 The 64-event trace of one shrinking visit, including four directory reads and four output
writes at the old-position cursor. 

### `store`

 Write the owner, thickness, assigned port, and target to their respective output columns at
the old-position cursor. 

### `visit_native`

 One deterministic burst builds all four output columns and advances the old-site cursor. 
