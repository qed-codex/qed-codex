---
{
  "module": "OAI/Computability/VPVNP/CompressorSlicePreparation.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorSlicePreparation.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorSlicePreparation.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Preparing the interval-scan workspace

The workspace consists, in order, of two totals, two incidence-count arrays
and two field-start arrays. A single clearing sweep initializes both totals
and both count arrays. Two prefix sweeps then produce the starts from the
original external width arrays. The pair records begin immediately after this
workspace.


### `clearOps`

 Clear the cell at the public base plus the persistent index, then advance. 

### `clearReport`

 Native report for zeroing one workspace cell and advancing the clearing cursor. 

### `clearPass_run`

 The clearing segment starts from arbitrary memory and writes each visited
cell once. All addresses outside its interval retain their original contents. 

### `PreparationRegions`

 Public input widths can be supplied in any two arrays disjoint from the
workspace. Their bounds and the first pair-record address fit the word size. 

### `oldPrefixData`

 Start and total cells of the source fields. 

### `newPrefixData`

 Start and total cells of the target fields. 

### `Prepared`

 Exact contents and footprint of the initialized workspace. 

### `preparationAfter`

 Compose the physical memory effects of the three native segments. 

### `PreparationRuns`

 The three actual segments with their exact transfer of memory and
instruction and probe totals. The persistent word starts at zero in each segment. 

### `preparation_run`

 From the original width arrays and arbitrary workspace contents, produce
both indexed start arrays and zero counts for all source and target fields. 
