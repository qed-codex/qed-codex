---
{
  "module": "OAI/Computability/VPVNP/CompressorSlotPhaseCosts.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorSlotPhaseCosts.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorSlotPhaseCosts.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Costs of the physical slot and slice passes of Appendix E

A pass is charged for every worker call and external probe, including visits to
empty records. The site count multiplies constants determined by the degree and
the subdivision template. Field widths affect the values stored in words, while
the directory allocations count fields and candidate intersections.


### `run_length`

 The native schedule consumes one branch record per executed worker. 

### `run_cap`

 Each report in a successful native segment obeys the segment worker cap. 

### `SliceInput`

 One family of concrete slice workspaces, each starting at the memory handed to it. 

### `SliceInput.oldBase`

 Base address of the old field widths supplied to the slice construction. 

### `SliceInput.newBase`

 Base address of the new field widths against which the slice construction intersects the
  old fields. 

### `SliceInput.scratch`

 Start of the workspace used to build field boundaries, copy records, and adjacency data
  for this slice. 

### `SliceInput.initial`

 Memory presented to the slice workers, containing the specified old and new width arrays. 

### `SliceInput.produces`

 Native segment executions and their physical output tables. 

### `SliceCosts`

 End-to-end resource bounds for the five passes, together with the resulting physical
tables. `M` and `N` bound the number of source and destination fields per invocation. 

### `sliceSites`

 All slice calls from actual input arrays, with costs summed across sites and a bound
on the largest row address. Empty fields and empty intersections are charged as well. 

### `demandSliceCosts`

 One demand slice invocation per packed bundle, on its actual thick and motif fields. 

### `subdivisionSliceCosts`

 Subdivision slice invocation for every surviving role edge in the selected template. 

### `refreshSliceCosts`

 A refresh bundle concatenates its original slot widths into a single external word. 

### `placementPreimages`

 From the actual chosen placement, allocate exactly one bounded row per packed site and
run the native preimage scan. There are `2^c*d` entries in every row, for either layout. 

### `orderedSlotAllocation`

 Scratch and immutable source arrays for the four ordered slot passes. The genuine
region includes every mixed-radix candidate, including subdivision and thick-wire holes. 

### `orderedSlotRun`

 Costs on the actual ordered directory. The candidate count includes holes and the
two sides of each genuine and cyclic padding arc. The scatter visits only the real rows. 

### `checked_scan`

 Accumulate the event counts of each successful call, including guarded workers
which reject invalid addresses. 

### `fixedScanCounts`

 Raw report statistics of a deterministic worker with fixed per-call counts. 

### `refreshSlotInstructions`

 Instructions of a refreshed incidence worker, including its return. 

### `refreshWrites`

 Raw costs of successive physical incidence-column scans. 

### `refreshPhaseCounts`

 The three external refresh passes followed by all actual incidence writebacks.
These totals apply to the chronologically joined report lists from `external_phases` and
`all_slots`, for any selected expander supplies and any widths. 

### `slotOwnerPreparation`

 The two preparation scans write the selected role offsets and the cyclic successor of
every packed site. The four subdivision constants belong to the fixed input template. 

### `slotLevelExactCost`

 Exact charged work of all five endpoint passes from the native segment executions
alone. A successful guarded append checks its owner and capacity before its two writes. 

### `slotLevelBounds`

 The five selected slot passes from `SlotLevel.run_selected`, including the lane-zero
base matching writeback. All counts and the highest allocated address are linear in the
number of packed sites, independently of the wire widths. 

### `gatheredRankCosts`

 Gathering one complete classified row and ranking each of its actual pivots. The result
includes each rank call's input memory, returned rank, and write to its physical destination.
For a thick row use `2^c*d/4` pivots. For a motif row use `pieceCount d c`. 

### `RankInput`

 The concrete input and gather trace for one row of thick-wire or motif keys. The rank
entry points use the physical source, destination, pivot and input memory of each call. 

### `RankInput.gatherBank`

 Public heads of the ID row, absolute key column, and output key row used by the gather
  worker. 

### `RankInput.arcCount`

 Number of absolute old arc widths covered by the gather's preservation guarantee. 

### `RankInput.widthBase`

 Start of the old arc width column retained during key gathering. 

### `RankInput.initial`

 Memory containing the collected arc IDs and their keys at the start of the gather scan. 

### `RankInput.gatherLog`

 Reports of the native calls that materialize one row of keys from its absolute arc IDs. 

### `RankInput.rankBank`

 Key-row base and rank destination supplied to each pivot's ranking call. 

### `RankInput.memory`

 External memory supplied at the entry to each pivot's ranking call. 

### `RankInput.pivot`

 Comparison key supplied to the ranking worker for each row entry. 

### `RankInput.rank`

 Rank word to be written for each pivot, counting the row keys strictly below it. 

### `RankInput.traffic`

 Actual gather and rank traffic for this row. 

### `RankInput.realizes`

 Each proposed event log executes the corresponding rank call, leaves the specified rank at
its destination, and has the exact instruction count. 

### `shrinkLocalTraffic`

 One packed shrinking stage's native local row traffic. There is one thick and one
motif key row per outgoing port, one demand slice pass per bundle, and one subdivision
slice pass per role edge of each actual motif. 

### `NativeScan`

 A concrete input memory and the resulting reports for a reset-cursor scan. 

### `NativeScan.initial`

 External memory at the start of this worker's deterministic scan from cursor zero. 

### `NativeScan.reports`

 Reports returned by executing the specified number of scan calls, each with an empty
  choice stream. 

### `ShrinkScans`

 The placement, preimage, classification, role-record and auxiliary-table scans feeding
the selected slot workers. Each trace starts from the memory at its actual entry point. 

### `ShrinkScans.placementBank`

 Public parameters for computing placement owners, thickness flags, assigned ports, and
  targets at old positions. 

### `ShrinkScans.preimageBank`

 Public parameters for appending old positions to the child rows of their packed owners. 

### `ShrinkScans.classifierBank`

 Public parameters for classifying old ports by bundle and computing their sorting keys. 

### `ShrinkScans.bundleBank`

 Public parameters for collecting absolute old port IDs into thick-wire and motif bucket
  rows. 

### `ShrinkScans.demandBank`

 Public radices and table addresses for writing three role sites and a CD flag for each
  old arc. 

### `ShrinkScans.roleBank`

 Layout selector and destination head for publishing the eight endpoint role offsets. 

### `ShrinkScans.successorBank`

 Lane and tag counts and destination head for the cyclic site successor scan. 

### `ShrinkScans.placement`

 Native scan computing a shrinking placement record for each old position. 

### `ShrinkScans.preimages`

 Native scan appending each old position to the preimage row of its packed owner. 

### `ShrinkScans.classifier`

 Native scan assigning each old outgoing port a bundle bucket and a sorting key. 

### `ShrinkScans.bundles`

 Native scan collecting the classified old port IDs into the corresponding bundle rows. 

### `ShrinkScans.demandRoles`

 Native scan visiting old outgoing ports and writing each role-site and CD record at its
  absolute old arc ID. 

### `ShrinkScans.roleOffsets`

 The eight native calls that publish one role selector for each edge type and side. 

### `ShrinkScans.successors`

 Native scan computing a cyclic tag successor for each packed site. 

### `ShrinkScans.reports`

 Concatenate the reports of the seven preparation scans in order for the shrinking phase's
traffic calculation. 

### `shrinkDescriptorTraffic`

 Combine the physical scans with the row work bounded by `shrinkLocalTraffic`. The
coefficient involves only the incoming and outgoing degrees, the color count, the
subdivision template, and the local row coefficient. 

### `shrinkTrafficFactor`

 Coefficient for all row, slot, and slice passes counted above at one selected shrink.
It uses only the degrees, colors, and four subdivision lengths. 

### `selectedShrinkTraffic`

 Total traffic for the native selected slot directory and all its checked bundle rows
and slice inputs. The numerical premises on the directory are returned by
`SlotLevel.run_selected`. The number of row invocations is proved from the selected
packing data. 
