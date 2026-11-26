---
{
  "module": "OAI/Computability/VPVNP/CompressorShrinkSelectedPlan.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorShrinkSelectedPlan.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorShrinkSelectedPlan.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Selected layout, placement, role and child-directory visits

The two scores and chosen layout bit follow the strided term array.
Four placement columns and the absolute arc role rows follow. The
preimage collector appends old sites in their numeric order after clearing
a counter for each new site. The one-shot score stages return cursor one
after writing their result to its designated cell.


### `Inputs`

 Counts, term-table dimensions and placement operands used to score both shrinking layouts
and build the chosen layout’s placement, arc-role and child tables. 

### `Inputs.oldSites`

 Expression for the number of old sites. It sets the length of each placement column and
  the number of calls to the preimage collector. 

### `Inputs.newSites`

 Expression for the number of packed sites after shrinking. Each packed site receives a
  child count and one row of old-site indices. 

### `Inputs.oldSlots`

 Expression for the number of old arc slots. The role pass visits each slot and reserves
  four words per absolute arc. 

### `Inputs.motifs`

 Expression for the number of motif term records scanned on each of the eight score
  coordinates. 

### `Inputs.termBase`

 Address expression for the first motif’s selected term record. The score passes read the
  repetition and supply fields relative to this base. 

### `Inputs.termStride`

 Distance in words between successive motif term records, used to locate each record and
  the score cells following the last one. 

### `Inputs.selectorBits`

 Number of selector bits per repetition. Each score pass adds the repetition count times
  this width to its coordinate’s payload width. 

### `Inputs.preliminary`

 The fourteen operand expressions for the preliminary placement pass. The selected pass
  reuses its dimensions and input columns, supplying the chosen layout bit and fresh output
  addresses. 

### `Inputs.oldActualOut`

 Address expression for the old incidence directory’s actual-out column, used by the role
  pass to find the target of each old arc. 

### `scoreBase`

 Start of the two layout-score accumulators, immediately after the strided array of motif
term records. 

### `layoutCell`

 Address of the chosen-layout bit, two words past the start of the score accumulators. 

### `layout`

 Load the chosen-layout bit from the cell written by the score comparison. 

### `placementBase`

 Start of the selected placement columns, immediately after the two scores and their
comparison bit. 

### `placementColumn`

 Base address of column `c` in the selected placement table. In order, the columns store the
owner, thick-site bit, assigned bundle and bundle target, with one word per old site. 

### `roleBase`

 Start of the four-word demand-role records indexed by absolute old arc, following the four
placement columns. 

### `roleEnd`

 First address after the old-arc role records and base of the child-count array indexed by
packed site. 

### `childRows`

 Base of the rectangular child table, just past the count word for the last packed site. 

### `preimageEnd`

 First address after the child table, which reserves one word for every old site across all
packed-site rows. 

### `clear`

 One-shot visit that zeros both layout-score accumulators before the coordinate scans and
returns cursor one. 

### `axisBank`

 Seven operands for score coordinate `j` comprise the term base and stride, score base,
selector width, coordinate index, layout side and relative-mass weight. 

### `axis`

 Scan all motif term records for coordinate `j`, adding the weighted square of each supply
width to that coordinate’s layout score. 

### `compareTable`

 The source comparison leaves one in register two on both outcomes. Its
published bit is still taken from register four. 

### `compare`

 Compare the two scores once and store one in the layout cell exactly when the second score
is smaller. The visit returns cursor one on either outcome. 

### `placementBank`

 Operands for recomputing placement. Slot 5 reads the winning layout bit, slots 10 through
13 point to the selected output columns, and the other slots come from preliminary
placement. 

### `placement`

 Scan the old sites with the chosen layout and write the owner, thick-site bit, assigned
bundle and bundle target for each site. 

### `rolesBank`

 Operands for the absolute arc-role pass, combining the preliminary dimensions, old
actual-out column, selected placement columns and role-table destination. 

### `roles`

 Visit every old arc slot and write its four-word demand-role record at the absolute arc
index using the selected placement. 

### `clearChildren`

 Zero the child counter for each packed site before the preimage collector begins appending
old sites. 

### `childBank`

 Six operands for collecting preimages comprise the old-site count, selected owner column,
packed-site count, child-count base, row capacity at exponent `a`, and child-row base. 

### `children`

 Visit old sites in increasing index order, appending each index to its selected owner’s
child row and incrementing that owner’s count. 

### `visits`

 The fourteen visits that clear the scores, scan eight supply coordinates, choose the
layout, write placement and arc roles, then clear the child counts and collect preimages. 

### `Reads`

 Relates the evaluated input expressions to a shrinking state’s site, arc and motif counts,
term base, actual-out column and preliminary operands, and requires the term stride to fit
in a word. 
