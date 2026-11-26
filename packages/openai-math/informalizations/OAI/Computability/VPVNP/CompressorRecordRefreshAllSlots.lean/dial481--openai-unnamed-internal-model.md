---
{
  "module": "OAI/Computability/VPVNP/CompressorRecordRefreshAllSlots.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorRecordRefreshAllSlots.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorRecordRefreshAllSlots.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# All actual incidence columns of a degree refresh

In increasing local-slot order, each native table visits all the new sites.
The scans share external memory. The incoming link is indexed by the target
half-slot, which can have a different local number on an expander arc.


### `entry`

 The expected incidence row for one local slot and site, computed from the reference memory
and that slot's public operands. 

### `Runs`

 Native executions of consecutive slot scans. Each scan starts at site zero
with the actual external memory left by its predecessor. 

### `Layout`

 The slot scans have disjoint inputs and outputs, and each output address identifies its
slot, site, and column uniquely. 

### `Reads`

 The memory agrees with the immutable input tables of every scan. 

### `Completed`

 Rows and frame of the visits for the listed slots. 

### `runList`

 Any list of local-slot passes, including repeated slots, executes against
one set of physical inputs and writes exactly the indicated rows. 

### `Tables`

 Addresses of the five read-only tables used to write all refreshed arcs. 

### `Tables.target`

 Base address of the table mapping each external bundle to its destination. 

### `Tables.total`

 Base address of the total width of each external bundle. 

### `Tables.targetPort`

 Base address of the expander destination-port table, indexed by source port and local
  expander slot. 

### `Tables.reverseSlot`

 Base address of the corresponding reverse expander slot numbers at the destination ports. 

### `Tables.supply`

 Base address of the internal widths selected for each site and expander slot. 

### `words`

 The physical output arrays are those of the incidence-directory interface. 

### `columnBase`

 Select the outgoing mate, incoming mate, or width column from the actual incidence
directory. 

### `rowIndex`

 Choose the destination slot for an incoming-column write and the source slot for
outgoing-mate and width writes. 

### `InputsApart`

 Every source operand lies outside the three output regions. 

### `Outside`

 A memory address outside all three output regions. 

### `site_count`

 This extent is the unchanged number of physical sites. 

### `SourceTables`

 Contents of the inputs, including the selected motif's supply widths. 

### `SourceTables.ofExternal`

 Use the final target and total of the native external segment pass. The
remaining inputs are the fixed expander table and the selected motif width
table. 

### `Fits`

 Word-size bounds for port count, residual lane count, refreshed degree, and all packed
actual slot identifiers. 

### `source`

 Recover the source arc from its two scan counters. 

### `actualPort_eq`

 The state-independent directory and the native slot writer use the same
port identifiers, even though the new base-index codomain is a cardinality cast. 

### `all_slots`

 Starting with the concatenation directory, fixed expander and chosen supply
table, execute every slot scan and obtain all three actual fields of the
refreshed state's incidence directory. Every other memory cell is preserved. 
