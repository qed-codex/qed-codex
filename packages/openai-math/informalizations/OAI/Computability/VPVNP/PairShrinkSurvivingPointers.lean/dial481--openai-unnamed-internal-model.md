---
{
  "module": "OAI/Computability/VPVNP/PairShrinkSurvivingPointers.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairShrinkSurvivingPointers.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairShrinkSurvivingPointers.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Runtime pointers for surviving supply slices

The motif ordinal addresses a dense table of original CD arc numbers.
Recover the old base and lane, insert the role and subdivision digits, and
read the appropriate endpoint in the inverse sorted-field table. Removing
the direction digit gives the next state's actual port number.


### `Inputs`

 Runtime heads and dimensions of the retained shrinking tables. 

### `Inputs.dense`

 Dense motif ordinal indexing both the absolute CD lookup and the four role-specific
  interval records. 

### `Inputs.absoluteHead`

 Head of the table mapping each dense motif ordinal to its original CD arc number. 

### `Inputs.inverseHead`

 Head of the inverse sorted-slot table indexed by a surviving arc number and endpoint
  orientation. 

### `Inputs.lanes`

 Number of remaining lanes used to split and reassemble the absolute CD arc address. 

### `Inputs.oldBases`

 Count of old base arcs used to displace a surviving arc's base number by its role
  ordinal. 

### `Inputs.intervalHead`

 Start of the dense motif-by-role records containing the subdivision interval frames. 

### `Inputs.absolute`

 Read the original CD arc number at the dense motif's entry in the absolute-index table. 

### `Inputs.arc`

 Insert the role and subdivision between the old CD base and its absolute lane. 

### `Inputs.rect`

 Read a sorted endpoint from the inverse table at the two-field arc address. 

### `port`

 The sorted rows interleave outgoing and incoming owners at each site. 

### `Inputs.frame`

 Dense ordinal and role address the interval bank. Its header includes
two totals, two singleton cells and two subdivision columns. 

### `port_eval`

 Removing the side bit from a represented sorted endpoint returns its
site-major slot ID. This calculation uses the actual word divisions. 

### `absolute_eval`

 Read the absolute arc field at the selected dense motif ordinal. 

### `rect_eval`

 Evaluate the physical inverse-table read from the two-component field address. 

### `arc_eval`

 The genuine arc expression is the actual allocated rectangular record
number, with the original CD lane retained as its lowest digit. 

### `frame_eval`

 Exact frame address in the retained row for a dynamic dense motif ordinal. 
