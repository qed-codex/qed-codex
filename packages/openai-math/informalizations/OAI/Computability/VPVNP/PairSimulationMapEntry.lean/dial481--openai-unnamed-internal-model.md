---
{
  "module": "OAI/Computability/VPVNP/PairSimulationMapEntry.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSimulationMapEntry.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSimulationMapEntry.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Executing an entire grouped motif entry in private RAM

All incident half-wires may be arbitrary. The native program checks selectors,
loads each selected matrix row, compares the full width vector, and increments
one counter per output label. The rejecting paths leave every counter intact.


### `Workspace`

 All per-call numerical locations, including separate selector and label arrays. 

### `Workspace.portBase`

 Private word address of each incident supply half-wire's first bit, used with its payload
  width to locate the selector suffix. 

### `Workspace.directory`

 Private base address of the incident-port directory whose entries point to the selector
  suffixes. 

### `Workspace.base`

 Private base address of each demand or supply endpoint's bit slice, used when reading a
  selected matrix row. 

### `Workspace.source`

 Start address of the private selector ordinal array written by the decoder and read by
  the row driver. 

### `Workspace.target`

 Start address of the private parameter label array written by the row driver and read by
  the histogram loop. 

### `Workspace.hist`

 Base address of the private counters indexed by parameter ordinal. 

### `Ready`

 Resident pointers, bit data, zero offsets and full-vector comparison targets.
Every deterministic stage may now execute even if the incident data are invalid. 

### `Effect`

 The exit and the value of each histogram cell on this particular path. 

### `Runs`

 Value and histogram effect of the entire map entry, on the very same
machine for all inputs, up to its success or failure continuation. 

### `RunsFramed`

 The same path both executes the map and preserves each saved private cell. 

### `Outside`

 The map writes only the selector, label and histogram arrays. 

### `RunsPost`

 Exact postconditions and the exterior frame hold on the same native prefix. 

### `successMemory`

 Exact memory on a successful map: selector ordinals and labels are stored in
copy order before each emitted label increments its histogram bin. 

### `Success`

 The successful selector and its complete width vector determine every written word. 

### `driverTicks`

 The exact row-driver clock depends on input bits, decoded selectors, and the fixed
public table. The argument bases and the contents of exterior memory play no role. 

### `runSelectedRows`

 Run the selected rows once and expose the private labels, widths, and histogram operands
together with the exact number of executed instructions. 

### `native_post`

 Every path uses genuine finite-table instructions and its cap includes
the rejecting paths on disagreement, unused tags and false payload totals. 

### `native_framed`

 Project the exterior-cell guarantee from the exact native post-state. 

### `native`

 Project the exact map result and histogram from its framed native path. 
