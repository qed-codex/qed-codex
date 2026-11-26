---
{
  "module": "OAI/Computability/VPVNP/CompressorRecordRefreshSupplyScan.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorRecordRefreshSupplyScan.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorRecordRefreshSupplyScan.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Reading the chosen supply widths of every refresh block

A term record stores its grid row, repetition count, and integer payload widths in
port/expander-slot order. The internal arcs in the degree refresh have additional selector
fields, one per repetition. This pass reads the chosen term at the source's block and
writes the total width to the supply column in the site order used by the slot emitter.


### `params`

 The seven supply-scan operands give port and lane counts, expander degree, term base and
stride, selector width, and supply base. 

### `visit`

 The cursor ranges over all site/expander-slot pairs in supply-table order. 

### `site`

 Recover the promoted site from a supply cursor by dividing out the expander slot. 

### `vertexPort`

 Recover the packed old vertex and promoted port by dividing out the residual lane. 

### `block`

 Compute the selected term's block ordinal from the old vertex and residual lane, discarding
the promoted port. 

### `coordinate`

 Index the selected payload coordinate by promoted port and local expander slot. 

### `header`

 First word of the fixed-stride term record for the cursor's block. 

### `payload`

 Address of the selected port-and-slot payload width after the term record's two header
words. 

### `value`

 Compute the internal width as the stored payload width plus the repetition count times the
selector width. 

### `events`

 The 33-event visit reads the repetition count and payload width and publishes the resulting
internal width. 

### `Apart`

 The term fields used by the pass lie outside the output column. 

### `Outside`

 The address is outside every supply destination whose cursor is less than the specified
count. 

### `Prefix`

 Materialized width rows and the memory frame through the given cursor. 

### `scan_run`

 Native visits extend any prefix in order, preserving all term records. 

### `recordBase`

 Term records are indexed by base vertex and residual lane. 

### `TermFields`

 The two physical fields consumed from each selected term. The outer vector uses
the port/expander-slot order of the term writer. 

### `TermFields.ofValues`

 The natural-number fields of the batch term reader, in its supply-coordinate order,
suffice to construct the word-valued inputs of this scan. 

### `TermFields.ofRecordMemory`

 Read the two fields from a physical table of the actual native term memory images.
Each block can have a different input memory, row, and selected repetition count. 

### `Fits`

 Dimension and output-index bounds for the sweep. 

### `addresses`

 The runtime quotient/remainder operations recover the block number and payload
coordinate from the site/slot cursor. 

### `apart_of_intervals`

 A strided term region and a disjoint contiguous supply region satisfy the separation
needed by the physical sweep. Either order of the two regions is allowed. 

### `read_supply`

 Each computed value is the actual selected supply width including selector bits. 

### `supply_pass`

 Full table for the expander slots of the selected branch, with one native call and
three probes per row, and the exact frame for the shared memory. 
