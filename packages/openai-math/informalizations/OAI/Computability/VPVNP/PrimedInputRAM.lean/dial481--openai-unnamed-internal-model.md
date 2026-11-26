---
{
  "module": "OAI/Computability/VPVNP/PrimedInputRAM.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PrimedInputRAM.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PrimedInputRAM.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Two-pass assembly of the inputs to the primed coefficient counter

The first pass branches at every internal bit's designated physical cell.
The second pass reads one fixed header or scratch address when needed,
then writes the resulting bit to a separate rectangular input array. The
proof identifies the result, at every parse leaf, with the full primed
coefficient-machine input. No validator is called on any shared bit string.


### `positions`

 Number of input cells in one rectangular pass, with n bits per site in each of two groups
of 2^r sites. 

### `Layout`

 The two rectangular arrays are placed after the auxiliary headers.
The three supplied cut lengths have addresses 0, 1, 2. The histogram
may occupy reserved addresses beyond the bit arrays before `scratchBase`. 

### `Layout.program`

 Universal-machine program whose literal prefix is embedded in every assembled processor
  input. 

### `Layout.scratchBase`

 Beginning of the first-pass choice rectangle in external memory. 

### `coordinates`

 The loop counters range over row-major cells of the `2R` full tapes. 

### `owns`

 Whether this rectangular position is the designated location that chooses a shared internal
bit. 

### `internalOwner`

 Exact equivalence between internal summation indices and branch cells
of the actual flattened first-pass loop. 

### `bitAddress`

 Injective word address of a first-pass scratch cell, obtained by offsetting its rectangular
index from the scratch base. 

### `outputAddress`

 Injective word address in the second-pass output rectangle immediately following first-pass
scratch. 

### `readHeader`

 Word address of the specified header field below the scratch rectangle. 

### `assignment`

 Inverse of the chosen-address map for the branch stream. 

### `streamEquiv`

 All admissible branch streams, including those encoding inconsistent
primed messages, are enumerated exactly once. 

### `refSource`

 Resolve a literal, header reference or shared internal bit to the immediate word or RAM
address used by the copy pass. 

### `source`

 Source of the second-pass copy for this rectangular input position. 

### `assemble`

 Store the chosen bits and perform all deterministic copies. 

### `assembled`

 Final RAM after storing the given internal bit assignment at its owners and copying every
processor-input cell. 

### `assembled_input`

 After the two passes, the grammar parser can fetch the selected leaf bit
in a single word read. This holds for every internal assignment. 

### `twoPass_cost`

 Number of calls plus probes of the two passes. The first pass makes at
most one write per cell. The second makes at most one read and one write. 
