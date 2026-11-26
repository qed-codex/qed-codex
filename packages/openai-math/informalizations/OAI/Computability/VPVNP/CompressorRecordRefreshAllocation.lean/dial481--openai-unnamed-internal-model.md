---
{
  "module": "OAI/Computability/VPVNP/CompressorRecordRefreshAllocation.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorRecordRefreshAllocation.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorRecordRefreshAllocation.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Packed allocation of one degree-refresh level

Seven equal-capacity segment columns are followed by dense demands, strided terms,
selected expander supplies, the two fixed expander columns, and the next state's six
incidence columns. The one-past-the-end word count bounds the complete allocation.


### `Plan`

 Dimensions and start address determining the packed segment, motif, expander, and refreshed
incidence arrays for one level. 

### `Plan.start`

 First address of the seven refresh segment columns. 

### `Plan.sites`

 Number of promoted sites, counting the base vertex, promoted port, and residual lane. 

### `Plan.blocks`

 Number of motif blocks, one for each old base vertex and residual lane. 

### `Plan.ports`

 Number of old ports promoted into the new base. 

### `Plan.expander`

 Number of expander slots at each promoted port. 

### `Plan.degree`

 Restored number of slots at each output site. 

### `Plan.ties`

 Number of ordered demand entries in one block's dense demand vector. 

### `Plan.stride`

 Number of words reserved for each block's selected term record. 

### `plan`

 Compute the refresh allocation dimensions from the old state, restored degree exponent,
expander degree, and record sizes. 

### `segments`

 Number of segment entries in each scratch column, one per promoted site and old port. 

### `capacity`

 Capacity of each output incidence column, one slot for each site and restored local slot
number. 

### `demand`

 First demand-vector address, immediately after the seven segment columns. 

### `term`

 First term-record address, following all blocks' dense demand vectors. 

### `supply`

 First selected-supply address, following the fixed-stride term records. 

### `targetPort`

 First expander target-port address, following the selected per-site supplies. 

### `reverseSlot`

 First expander reverse-slot address, following the target-port table. 

### `next`

 First address of the refreshed incidence columns, following both expander tables. 

### `stop`

 Exclusive end address of the allocation after the six output incidence columns. 

### `scratch`

 Public scratch operand zero gives the port count, and operands one through seven give the
segment-column addresses. 

### `inputs`

 The bundle-target, total-width, expander-target, reverse-slot, and supply pointers passed
to the actual-slot scans. 

### `output`

 The six output incidence pointers at consecutive column-capacity intervals starting at
`next`. 

### `scratch_regions`

 The scratch bases satisfy the external pass's common-capacity region convention. 

### `column_interval`

 Every actual or base output column lies inside the final six-column allocation. 

### `finish_layout`

 The packed address recipe meets every word-size and aliasing requirement for
post-term completion. No contents of the incoming memory enter the layout proof. 

### `outside_finish`

 The finish phase protects all earlier arrays, including the selected term headers,
and every address beyond the six next-state incidence columns. 
