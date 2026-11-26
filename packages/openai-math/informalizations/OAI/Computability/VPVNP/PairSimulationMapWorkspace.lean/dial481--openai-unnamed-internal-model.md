---
{
  "module": "OAI/Computability/VPVNP/PairSimulationMapWorkspace.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSimulationMapWorkspace.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSimulationMapWorkspace.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Physical workspace of a selected map call

The live-word capacity estimates of Section 13 apply to every payload offset
of every selector sequence, including sequences ultimately rejected by the
width guards. Given the physical slice positions and separated scratch blocks,
these estimates construct the workspace consumed by the executable map.


### `Capacity`

 Capacity available throughout the numerically bounded workspace of one selected node. 

### `Regions`

 Natural addresses of the operand slices and scratch blocks. The histogram may be
shared across successive calls. 

### `Regions.base`

 Natural start address of each demand or supply endpoint's raw bit slice in private
  memory. 

### `Regions.directory`

 Natural base address of the incident-port directory that stores pointers to the supply
  selector suffixes. 

### `Regions.source`

 Natural start address of the private array of decoded selector ordinals, one per copy. 

### `Regions.target`

 Natural start address of the private array of parameter labels returned by the selected
  rows. 

### `Regions.hist`

 Natural base address of the parameter histogram whose counters may be shared across map
  calls. 

### `rawWidth`

 Actual raw half-wire width, including all selector suffix bits on supply. 

### `Ordered`

 All physical ranges fit in a common prefix. The source and target sides
may use the same addresses wherever their values agree. 

### `workspace`

 Construct the full native workspace using a bound on copy count and the physical
address inequalities. All selector-dependent obligations follow from capacity. 

### `histogram_apart`

 The histogram may be below the directory or above the label staging. Either
physical ordering prevents setup stores from changing any histogram counter. 

### `input`

 A raw descriptor and the actual stored half-wire bits suffice to build the
initializer's input. The physical ordering proves all directory disjointness tests. 

### `eventually_selected_capacity`

 Every node in every selected descriptor branch has the map capacity required above.
The threshold is chosen before the branch, its coefficient specialization, and the node. 

### `eventually_capacity`

 A polynomial upper limit on the shared scratch region also supports every field
read in the whole prefix. This covers operands materialized above the node's own frame. 
