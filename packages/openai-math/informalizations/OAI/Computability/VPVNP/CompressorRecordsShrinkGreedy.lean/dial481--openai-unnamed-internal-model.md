---
{
  "module": "OAI/Computability/VPVNP/CompressorRecordsShrinkGreedy.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorRecordsShrinkGreedy.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorRecordsShrinkGreedy.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Computing the shrinking placement directory from the old incidence table

The tag extraction visits the old outgoing slots and initializes the zero
operand. A color scan and an offset scan then fill their disjoint fresh
directories. The full old displacement word remains available to the
placement worker, while the offset worker sees only the projected tag.


### `ShrinkingState`

 A compressor state whose lane width supplies the packing fields required by shrinking at
the given degree and residual width. 

### `projectedTag`

 Extract the packing-tag component of an outgoing base port's lane displacement for the
offset assignment. 

### `projectionWords`

 The tag-projection worker's public operands, including the old incidence data and
destinations for projected tags and zero. 

### `projectedMemory`

 The memory after scanning all old base ports to write projected displacement tags and
initialize the shared zero operand. 

### `colorTables`

 The greedy color pass's port tables, using the fresh color column, shared zero, and
original displacements. 

### `tagTables`

 The offset pass's port tables, using the fresh offset column and projected tag
displacements. 

### `Run`

 The report traces of all six native visits, in their memory execution order. 

### `Run.color`

 The executed greedy color assignment in the color walk's workspace. 

### `Run.offsets`

 The executed tag-offset assignment using the projected displacement table after coloring. 

### `post`

 The final memory of the greedy shrinking run, after the offset assignment completes. 

### `column`

 Read a natural-number label from an indexed word of a greedy assignment column. 

### `build`

 Build the native color and offset setup in arbitrary scratch memory. The
input comprises exactly the old represented incidence table and the fresh range. 

### `reports`

 Chronological reports of the two tag-extraction visits, the color setup and
reader, and the tag setup and reader. 

### `reports_cost`

 Total native calls plus probes depend linearly on the number of base
vertices for each of the fixed degrees used by the compressor. 
