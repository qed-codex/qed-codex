---
{
  "module": "OAI/Computability/VPVNP/CompressorCatalogRates.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorCatalogRates.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorCatalogRates.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Native worker traffic at an actual compressor state

The greedy color and tag readers are charged per original base. Dense bundle
arrays are charged by the actual old-port count, and the refresh tie and supply
arrays by the counts of blocks, ports and expander arcs. The per-call caps
depend on the fixed degrees and tables.


### `greedyRate`

 Coefficient of the base count for one greedy preparer followed by its reader. 

### `greedyCap`

 Maximum instructions of either worker of a prepared greedy pass. 

### `greedyShrinkRate`

 Combined per-base-vertex charge for preparing and reading the greedy colors and
displacement tags at degree `d`. 

### `greedyShrinkCap`

 Maximum per-call instruction bound over the color and tag passes at degree `d`. 

### `greedyStateCounts`

 Both greedy scans on the original base graph. The rate uses the exact base count,
which is at most the number of physical positions. 

### `refreshRate`

 Catalog coefficient per refreshed position, using the number of tie coordinates as a
uniform upper bound on the dense demand scans per position. 

### `refreshStateCounts`

 External descriptors, every dense demand tie, every selected expander supply, and
all three output incidence columns. Motif term selection can intervene between the
prepared demand and supply scans. 

### `shrinkShape`

 The dimensions used by the selected shrinking workers, on the input state's actual
base enumeration and residual lanes. 

### `denseRankCap`

 Number of workers in a dense rank scan depends only on the motif row capacity. 

### `DenseShrinkScans`

 Physical dense key/rank scans. The two prefix rows partition the old arcs and the
motif-absolute writeback visits all old arcs. AB widths and dense demand pairs visit only
the compact motif rectangle. 

### `DenseShrinkScans.keyBank`

 Seven public operands used by the dense bundle key-gather scan. 

### `DenseShrinkScans.rankBank`

 Six public operands used to rank bundle entries by their gathered keys. 

### `DenseShrinkScans.widthBank`

 Five public operands used to scatter widths into rank order. 

### `DenseShrinkScans.absBank`

 Seven public operands used to compute absolute motif identifiers. 

### `DenseShrinkScans.thickBank`

 Five public operands used to scan prefix widths of the thick-wire entries. 

### `DenseShrinkScans.motifBank`

 Five public operands used to scan prefix widths of the motif entries. 

### `DenseShrinkScans.abBank`

 Five public operands used to compute the new AB widths. 

### `DenseShrinkScans.demandBank`

 Six public operands used to gather the shrinking motif demands. 

### `DenseShrinkScans.key`

 Native key-gather run on every dense bundle entry. 

### `DenseShrinkScans.rank`

 Native run assigning each dense bundle entry its rank. 

### `DenseShrinkScans.width`

 Native run scattering each entry's width to its ranked position. 

### `DenseShrinkScans.absolute`

 Native run materializing the absolute motif identifiers. 

### `DenseShrinkScans.thick`

 Native prefix scan of the sorted thick-wire widths in each bundle. 

### `DenseShrinkScans.motif`

 Native prefix scan of the motif widths in each bundle. 

### `DenseShrinkScans.ab`

 Native scan computing AB widths for the motif entries. 

### `DenseShrinkScans.demand`

 Native scan gathering demand rows for the shrinking motifs. 

### `DenseShrinkScans.all`

 The eight dense shrinking scans' reports concatenated in execution order. 

### `denseShrinkCounts`

 Exact physical traffic and call count for the eight dense shrinking passes. 

### `GreedyPrepared`

 The actual two prepared greedy passes, before the shrinking layout is populated. 

### `GreedyPrepared.j`

 Bit length of a displacement tag assigned to a base vertex. 

### `GreedyPrepared.tags`

 The selected displacement-tag word for each base vertex. 

### `GreedyPrepared.colorLayout`

 Layout of the greedy color descriptor rows in the base-vertex order. 

### `GreedyPrepared.tagLayout`

 Layout of the descriptor rows for the greedy displacement-tag pass. 

### `GreedyPrepared.colorMem`

 External memory supplying the operands and descriptors of the prepared color pass. 

### `GreedyPrepared.tagMem`

 External memory supplying the operands and descriptors of the prepared tag pass. 

### `GreedyPrepared.realizes`

 Reports of all four native greedy workers, with the two preparer-to-reader handoffs. 

### `bulkShrinkRate`

 Bound for bulk descriptor scans including the fixed global key gather, full-stride
rank worker, scatter, both prefixes, absolute indices, AB widths, and dense demand
pairs. The coefficient is independent of the number of lanes and the base size. 

### `bulkShrinkCap`

 The largest opcode budget among the bulk and greedy workers. 

### `shrinkStateBulkTraffic`

 All bulk shrink descriptors and both greedy scans on the actual incoming state.
The cost equality for the five endpoint passes is returned by `SlotLevel.run_selected`.
The rate counts the global rank scan once, alongside the fixed global key gather. 

### `stateInputScanCounts`

 The placement and bundle classifier feed the two bounded append scans. The two
append runs are the ones supplied by `placementPreimages` and `BundleLists.fill_run`. 

### `StateSliceInputs`

 Indexed input banks for the demand slice of each bundle and the subdivided output of
each role-edge. The widths in the old arrays come from the selected state. 

### `StateSliceInputs.number`

 The enumeration used to lay out the motif entries of each bundle. 

### `StateSliceInputs.order`

 The enumeration used to lay out the thick-wire entries of each bundle. 

### `StateSliceInputs.roleWidth`

 Width of each of the four selected roles at each packing motif. 

### `StateSliceInputs.demand`

 The slice-scan operands for intersecting ordered old thick-wire widths with ordered new
  AB widths in each bundle. 

### `StateSliceInputs.divide`

 The slice-scan operands for splitting each selected role width into its prescribed
  subdivisions. 

### `sliceRate`

 Per-position charge allowance for AB interval intersections and subdivision of the four
motif role widths. 

### `sliceRowsPerSite`

 The number of physical slice worker rows. Each native slice pass has five phases. 

### `stateSliceTraffic`

 Total traffic and row count of all local slice inputs of one actual state. 

### `shrinkRate`

 The coefficient for the shrinking descriptor catalog. The scheduler charges motif
coefficient evaluation and row framing separately. 

### `shrinkStateTraffic`

 End-to-end count of the physical preparation, greedy, slot, dense and slice workers
for one selected shrinking state. The report witnesses are retained for the scheduler. 
