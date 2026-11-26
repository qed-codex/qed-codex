---
{
  "module": "OAI/Computability/VPVNP/PairShrinkCallHeader.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairShrinkCallHeader.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairShrinkCallHeader.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Reading the selected shrink map header

The physical level contains a term head, a ten-word row stride, the selected
layout and the dense AB/CD pair head. The number of private hidden slots
comes from the actual base and residual lane counts of this level. Reading
the classified CD row and its source-thickness flag supplies the direct
pointers at C and D, including when the independent half-words disagree.


### `Operands`

 Live register expressions on entry to one resident map. 

### `Operands.level`

 External address of the selected old-level header. 

### `Operands.motif`

 Dense ordinal selecting this motif's term and row in the shrinking tables. 

### `Operands.arguments`

 Private start address of the argument frames indexed by absolute DFS node. 

### `Operands.argumentStride`

 Number of private words reserved between consecutive node argument frames. 

### `Operands.hidden`

 Start of the private shared supply-field slots, indexed by motif and role. 

### `Operands.slotStride`

 Distance in private words between adjacent shared or staged supply fields. 

### `Operands.hist`

 Private address of the histogram to which the evaluated map contributes. 

### `Operands.cell`

 Read a scalar or table pointer at the specified offset from the old-level header. 

### `Operands.count`

 The dense motif count is the product of absolute bundle count and piece count. 

### `Operands.staging`

 First private staging word after the four shared slots reserved for each motif. 

### `Operands.cdHeader`

 Assemble the published CD lookup expressions from the selected level, motif ordinal, old
argument geometry, and staging address. 

### `Operands.inputs`

 Build the map-field recipe, including the dynamic motif count and the oriented CD source
addresses at the old degree. 

### `noncomputable local instance : DecidableEq X.Base`

 Classical equality on old base vertices for interpreting the selected motif's native field
and bundle pointers. 

### `scratch`

 The private frame reserves four shared words per motif before the staged
AB and surviving endpoints. 

### `Level`

 The scalar slots and graph-array heads of the actual old level, read as
machine words at their offsets in the published header. 

### `Live`

 The incoming recipe expressions evaluate to the selected level, motif ordinal, argument
arena, scratch geometry, and histogram address. 

### `OldTables`

 Retained source data from the original port classifier, ranker, and
preliminary placement pass in the memory on which this resident executes. 

### `cdBase`

 Natural address of the old CD half used at C or D, with orientation determined by the
motif's old source thickness. 

### `Heads`

 Pointer expressions shared by the unsplit CD read and the AB frame scan. 

### `Geometry`

 Representability of the ranker's old ID and bucket arrays follows from
the allocated end of the ranking stage. 

### `fields_eval`

 The exact descriptor value for every field of the selected resident map. 

### `ab_recorded`

 At every genuine thick-wire row index, the canonical header and the final
bank recorded by the selected level meet the native column's operand contract. 

### `read_C`

 The descriptor's computed C operand points to the stored bit of the
selected old half-assignment. 

### `read_D`

 The descriptor's D operand selects the opposite physical end, using its
independent child packet even when source and target coincide. 
