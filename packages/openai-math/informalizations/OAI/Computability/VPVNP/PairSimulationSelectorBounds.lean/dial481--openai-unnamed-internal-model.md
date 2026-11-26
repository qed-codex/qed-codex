---
{
  "module": "OAI/Computability/VPVNP/PairSimulationSelectorBounds.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSimulationSelectorBounds.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSimulationSelectorBounds.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Binary size of the descriptor scans

At a shrinking level the motifs are a subset of the old actual arcs. At
a refresh level there is one motif per port block. Each consumes a fixed
number of checked coordinates whose bit length is logarithmic in the
largest incoming width. The estimates here sum the concrete selector
stream and the old site and slot lists along the actual execution branch.


### `outerReaders`

 Extract the term-selector reader at each pass of an execution, following its selected
continuation to form the reader for a whole descriptor path. 

### `scanUnits`

 Number of old site records and outgoing-slot records scanned once, plus
the number of binary guesses made by the actual outer-term parser. 

### `PassScanBound`

 For every term choice, the next state has at most as many positions as the old one. The
number of old site and slot records plus selector bits is at most `positions * K * (K +
Nat.clog 2 (maxWireWidth + 1))`. 

### `ScanBound`

 Require the same per-pass scan constant at every branch of a state execution. 

### `ProcedureScanBound`

 A uniform per-pass scan bound for every execution of a procedure, over all admissible lane
counts and input states. 

### `scanConstant`

 Uniform coefficient for a scan in the fixed block. The width
constant is determined by the two templates; the multiplicities by
the degree schedule and the expander. 

### `execute_scanUnits`

 Scan size on an actual complete selector path. This includes the old
site and outgoing arc records at each pass, and all its choice bits. 

### `executeOuterReader`

 The descriptor phase reads exactly the admitted sequence of term
choices of the original repeated execution. 
