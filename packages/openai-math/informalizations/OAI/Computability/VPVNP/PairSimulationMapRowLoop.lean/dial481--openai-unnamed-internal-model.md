---
{
  "module": "OAI/Computability/VPVNP/PairSimulationMapRowLoop.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSimulationMapRowLoop.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSimulationMapRowLoop.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Resident motif rows throughout the private selector loop

After each decoded selector the native row advances every group offset. The
same invariant supplies the next row's read addresses and the final total
for each supply edge, including supply edges absent at the current party.


### `prefixWidth`

 Sum of the widths of the first `n` copies, with value zero when `n > u`. 

### `buffers`

 Endpoint buffers do not move. Demand groups have fixed stride and each
supply group has the stride selected at the preceding copy. 

### `RegisterLayout`

 A shared output register passes the returned ordinal directly to the driver.
All the other controller registers lie outside the row workspace. 

### `stable`

 Private labels are stored outside the original endpoint words. 

### `rowCap`

 Sum of the row instruction bounds over all selectors at grid point `z` and party `j`. 

### `OutsideRowWrites`

 Fixed labels, decoded fields, temporary words and advancing offsets may
be modified by a row. Other registers can be carried through the full scan. 

### `rowSteps`

 The single-copy clock sees only the wire bits, preceding decoded selectors,
and the fixed comparison table. 

### `rowRunsExactFramed`

 The actual row subroutine also preserves every requested exterior word
for the width test, histogram flush or enclosing vertex call. 

### `rowRunsFramed`

 The actual row subroutine also preserves every requested exterior word
for the width test, histogram flush or enclosing vertex call. 

### `rowRuns`

 Discharge the driver's row subroutine contract by following the actual
field reads, fixed label comparisons and group-offset opcodes. 
