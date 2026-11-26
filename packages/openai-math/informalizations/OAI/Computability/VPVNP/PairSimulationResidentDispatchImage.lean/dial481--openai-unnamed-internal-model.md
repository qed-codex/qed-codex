---
{
  "module": "OAI/Computability/VPVNP/PairSimulationResidentDispatchImage.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSimulationResidentDispatchImage.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSimulationResidentDispatchImage.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# A relocatable finite image for resident map dispatch

The chosen enumerations are the term descriptor's demand-grid order and the
motif's party order. A single initialization row supplies zero. All succeeding
branches use the two checked ordinal chains and end at the corresponding map.


### `Address`

 Instruction positions for initialization, grid dispatch, and party dispatch within a grid. 

### `Image`

 The grid and party enumerations, instruction placement, targets, and dispatch registers. 

### `Image.grids`

 Grid identifiers in demand descriptor order. 

### `Image.parties`

 Party identifiers in motif order. 

### `Image.place`

 Machine address assigned to each dispatch instruction. 

### `Image.target`

 Entry address of the resident map for a given grid and party. 

### `Image.bad`

 Rejecting continuation shared by both dispatch tables. 

### `Image.grid`

 Register holding the grid ordinal. 

### `Image.party`

 Register holding the party ordinal. 

### `Image.zero`

 Register initialized to zero for the case tests. 

### `Image.one`

 Register supplying one for each ordinal decrement. 

### `partyCases`

 The comparison chain that selects a party's map target in grid `z`. 

### `gridCases`

 The comparison chain that transfers control to the selected grid's party table. 

### `program`

 The two-stage dispatch program assembled from the grid and party tables. 

### `text`

 The instruction at each image position, including the initial write to the zero register. 

### `Linked`

 Every dispatch instruction is installed at its assigned address at the machine's word width. 

### `Distinct`

 The grid, party, zero, and one registers are pairwise distinct. 

### `native`

 Execute the installed instructions on the actual encoded grid and party
numbers. The returned PC uses their values in the chosen descriptor orders. 
