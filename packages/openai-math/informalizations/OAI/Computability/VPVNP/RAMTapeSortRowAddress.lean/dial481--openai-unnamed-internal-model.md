---
{
  "module": "OAI/Computability/VPVNP/RAMTapeSortRowAddress.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMTapeSortRowAddress.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMTapeSortRowAddress.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 # The bitonic sorter’s finite row-address machine

The global wire has the row bits followed by the site bits in little-endian
order. The phase and stride are unary counters on the tape. Two indexed reads
supply the direction. A third pass toggles the stride bit within the row, if
present, and converts the resulting offset to a unary record count.


### `Axis`

 The phase and stride bit positions queried in the global wire address to determine the
comparator orientation. 

### `Port`

 Ports for the row and site indices, stage parameters, orientation and partner decisions,
and scratch for bit scans and unary conversion. 

### `Port.phase`

 The unary index of the phase bit to read from the concatenated row and site address. 

### `Port.stride`

 The unary index of the stride bit used for both orientation and partner selection. 

### `routine`

 All input-dependent parameters are bit stacks. The instruction table is fixed. 

### `initial`

 Initialize the row-address machine with the given row and site bits, unary phase and
stride, and empty work stacks. 

### `final`

 The three outputs are a one-bit orientation, a one-bit local stride indicator,
and the unary record offset. The original row, site and both counters are retained. 

### `budget`

 Tick allowance for the indexed phase and stride reads and conversion of the possibly
toggled h-bit row index to a unary offset. 

### `runs_bits`

 The maximum phase, equal to the total width, reads a zero direction bit.
This also covers empty row and site words. 

### `runs_framed`

 Running the row-address program in a caller's register bank changes only
the three designated output stacks. 

### `lt_partner_iff`

 The lower-numbered wire in an XOR pair is the one with a zero stride bit. 

### `select_eq_comparator`

 The machine's orientation chooses precisely the output assigned by the
bitonic comparator, with the row's own record as the first input. 

### `cross_siteBit`

 A nonlocal stride changes precisely bit `j-h` of the site. The allocated
physical field specifies the same peer as the global wire calculation. 
