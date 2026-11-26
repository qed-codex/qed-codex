---
{
  "module": "OAI/Computability/VPVNP/CompressorSlotMateColumns.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorSlotMateColumns.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorSlotMateColumns.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# The three remaining incidence permutations

After the base-target scan, invert its permutation and expand both directions
to all binary lanes. Each pass starts with the previous pass's physical memory.
The base mate, inverse, displacement and two actual mate columns coexist in
the final memory; older tables and the reserved width region are preserved.


### `Mates`

 Memory represents the next state's forward and inverse base matching, base displacements,
and both directions of actual port incidence in canonical port order. 

### `MateReports`

 Reports for the base inverse scan followed by the two scans that lift the matching to every
residual lane. 

### `MateReports.baseIn`

 Reports that invert the base-target permutation, giving the source base port at each
  incoming base port. 

### `MateReports.actualOut`

 Reports that expand the forward base matching and displacements into the outgoing
  actual-port mate column. 

### `MateReports.actualIn`

 Reports that expand the inverse base matching and source displacements into the incoming
  actual-port mate column. 

### `MateReports.all`

 Concatenate the base inverse, actual forward, and actual inverse reports in execution
order. 

### `MateReports.final`

 Memory after replaying the base inverse and the two actual mate scans in sequence. 

### `MateReports.Native`

 The three mate report lists arise from their native workers starting at cursor zero on
successive memory states. 

### `MateReports.Cursors`

 The base inverse scan returns the base port count and both lifted mate scans return the
actual port count. 

### `writeMates`

 The three passes share and preserve the prior target and displacement
columns. Their total cost is linear in the numbers of base and actual ports. 
