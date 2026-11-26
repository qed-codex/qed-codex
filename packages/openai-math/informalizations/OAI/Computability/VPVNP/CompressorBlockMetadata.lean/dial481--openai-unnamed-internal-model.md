---
{
  "module": "OAI/Computability/VPVNP/CompressorBlockMetadata.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorBlockMetadata.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorBlockMetadata.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Publishing the DFS descriptor and prefix of a compressor substep

The planner emits three one-call rows. The first worker copies twelve
computed operands into the input graph header. The other two workers set
the next graph's DFS layer base and producing role. The native writer
reads its public operand bank before its first external store.


### `Fields`

 Substep-specific child placement columns and the exclusive child capacity. 

### `Fields.newSites`

 Expression for the number of sites produced by the selected pass. 

### `Fields.owner`

 Expression for the base of the column mapping old site identifiers to their owners. 

### `Fields.count`

 Expression for the base of the child-count column, indexed by new site identifier. 

### `Fields.row`

 Expression for the base of the rows listing each new site's old children. 

### `Fields.cap`

 Expression for the number of child identifiers reserved per placement row. 

### `Fields.shrink`

 The selected shrink's collector and the DFS reader use the same count
and row intervals and the same maximum preimage cardinality. 

### `Fields.refresh`

 Refresh placement is a bijection. Its owner, count, and unique-child
columns are three consecutive site-sized intervals. 

### `Role`

 The kind of compressor pass that produced a traversal layer. 

### `Role.code`

 Numerical role tag stored in the successor header, one for shrinking and two for refresh. 

### `lengthWord`

 Expression reading the input length from word 29 of the first level header. 

### `fieldExprs`

 Header offsets 15 through 26 in the order consumed by the DFS handler. 

### `nextBase`

 Advance the DFS row base by the current site count times the reserved row stride. 

### `writer`

 Destination followed by the twelve evaluated operands. 

### `current`

 The visit that writes the twelve traversal metadata operands starting at offset 15 of the
input header. 

### `outputBase`

 The visit that stores the computed DFS row base at offset 14 of the successor header. 

### `outputRole`

 The visit that stores the producing pass's role tag at offset 27 of the successor header. 

### `visits`

 Publish the input level's traversal metadata, then the successor's row base and role tag. 

### `write_native`

 The worker uses 12 external probes, all writes. The returned cursor
advances once even when the first input field has numerical value zero. 

### `writer_footprint`

 Native worker footprints. Planner evaluation of the operand expressions
takes place in a separate burst. 

### `bank`

 Evaluate a phase's public parameters before executing its worker. 

### `current_bank`

 The address and all data supplied by the actual online planner. 

### `Placement`

 Data values supplied by the physical child-directory implementation at this substep. 

### `Placement.newSites`

 Number of output sites indexing the completed placement directory. 

### `Placement.owner`

 Natural base address of the column recording the owner of each old site. 

### `Placement.count`

 Natural base address of the column recording the number of children of each output site. 

### `Placement.row`

 Natural base address of the fixed-stride child-identifier rows. 

### `Placement.cap`

 Number of child identifiers reserved in each output site's row. 

### `Placement.reads`

 The planner's five placement expressions evaluate to the recorded site count, column bases
and row capacity. 

### `payload`

 The twelve metadata words at offsets 15 through 26, including the DFS stride, argument
frame, incidence pointers and child directory. 

### `field_values`

 Agreement with the DFS row stride, private arena, actual incidence pointers,
and the five placement operands. This statement allows arbitrarily different
old and new site counts. 

### `storeReport`

 The one-store worker's report, writing the given value at its destination and returning
cursor one. 

### `Source`

 The source relation retains the actual public bank, input cursor and
individual native budget of each visit. 

### `Source.packet`

 Each metadata row contributes one completed source scan and one real
worker run at its planner-supplied operands. 

### `publish_metadata`

 The three visits run on consecutive memory images. All other addresses,
including the original layer base, cursor frame, and both pointer banks,
retain their original values. 

### `next_layerBase`

 The prefix word advanced by the metadata worker is precisely the
ordinary DFS address of the next layer in the selected traversal. 

### `producingRole`

 A real selected substep determines the same producing-role word as the
traversal's layer list. 
