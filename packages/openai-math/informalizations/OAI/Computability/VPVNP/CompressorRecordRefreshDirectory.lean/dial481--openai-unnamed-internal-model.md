---
{
  "module": "OAI/Computability/VPVNP/CompressorRecordRefreshDirectory.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorRecordRefreshDirectory.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorRecordRefreshDirectory.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Constructing the degree-refresh bundle directory

The degree refresh in Appendix E enumerates bundles by base arc and residual lane.
The base slot table contains the destination arc and the old binary displacement.
One native call unpacks these words, translates the lane, and writes the destination
bundle number, the port shift and the initial concatenation offset.


### `bundleOrder`

 Enumerate each base arc's bundles in increasing order of the remaining lane. 

### `visit`

 Parameter zero is the lane count. Tables one and five are the old base target and
displacement. Tables two, three and four are the output columns shared with the segment scan. 

### `cell`

 Read a word at the indexed offset from a refresh column's public base address. 

### `sourceArc`

 Decode a bundle ordinal to its old base arc by dividing out the residual lanes. 

### `shiftWord`

 Read the old base arc's packed binary displacement from the shift column. 

### `portShift`

 Extract the high-order port shift from the packed displacement by dividing by the residual
lane count. 

### `targetWord`

 Encode the destination bundle from the old base mate and the residual lane translated by
XOR. 

### `update`

 Write the translated bundle number and port shift, and initialize the bundle's running
width total to zero. 

### `events`

 The 27-event directory visit reads the old mate and shift and writes the target, port
shift, and zero total. 

### `visit_native`

 The actual table executes from its normal entry and advances the persistent bundle cursor. 

### `BaseTables`

 The base displacement is stored as a port in the high bits and a residual-lane shift
in the low bits. These columns are shared by all the lanes of a base arc. 

### `BaseTables.ofOld`

 The old graph's ordinary binary displacement cell supplies the packed displacement
required by the directory, after splitting the old lane into port and residual coordinates. 

### `translated_row`

 Decoding an actual source bundle yields precisely its translated target and port shift. 

### `Layout`

 The two base columns have one entry per old base arc. Each output column has
one entry per bundle. Only overlaps involving a write need to be ruled out. 

### `Layout.ofRegions`

 Equal-capacity regions in the existing refresh layout satisfy the weaker
bounds for the two read-only base tables. 

### `Outside`

 Addresses outside the output columns through a given cursor. 

### `Prefix`

 The constructed rows through the cursor, together with the surviving base tables. 

### `scan_run`

 The native scan from an arbitrary prefix extends that prefix by its call count.
Memory outside the output rows through the final cursor keeps its incoming value. 

### `directory_pass`

 Complete directory initialization from the old base slot tables. It costs six calls
plus probes per bundle and writes only the target, shift and total arrays. 

### `liveBundle_lt`

 Every bundle read by a live source segment is inside the constructed directory. 

### `Prefix.external_start`

 The constructed directory and gathered widths give exactly the initial state of the
external segment scan. Only totals at live bundle numbers need initialization. 
