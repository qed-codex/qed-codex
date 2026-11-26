---
{
  "module": "OAI/Computability/VPVNP/PairSimulationMapRowFields.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSimulationMapRowFields.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSimulationMapRowFields.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Preparing the registers of a fixed motif row

Every endpoint has its own base address, exclusive end and output register.
Both endpoints of a group use the same current offset. Four instructions
initialize the padded field reader from these resident registers and a fixed
width port. The resulting loop preserves the register fields already read.


### `Slot`

 Fixed register allocation for row extraction, including both endpoint directions. 

### `Registers`

 Inject the endpoint data and query slots, shared group offsets, and working registers for
one row into the machine's physical registers. 

### `readerRegs`

 The padded reader writes the field's query register directly. 

### `setup`

 Absolute field start, fixed width, exclusive high cursor and zero accumulator. 

### `Slices`

 Resident bit slices and current group offsets for one iteration. A zero-length
slice represents an absent port and yields zero at any offset. 

### `Slices.len`

 Number of resident bits for each endpoint slice. An absent endpoint has length zero. 

### `Slices.bits`

 The bit at each in-range position of an endpoint's resident slice. 

### `Slices.base`

 Private start address of each endpoint's resident bit slice. 

### `Slices.offset`

 Current bit offset shared by the endpoints of each demand or supply group. 

### `Resident`

 Layout and cursors are resident before the scan and survive it intact. 

### `Fits`

 Full end and high cursor fit also for padded reads and malformed final totals. 

### `Frame`

 Frame on every register outside the scratch words and the current output fields. 

### `digit`

 The natural digit stored in the word-sized query register. 

### `oneField`

 The four setup instructions and the padded field loop for one endpoint. 

### `Sites`

 Each field's four setup rows and seven reader rows occupy fixed program counters. 

### `Sites.setupPC`

 Four program counters per endpoint for setting up its padded field read. 

### `Sites.readerPC`

 Seven program counters per endpoint for the padded reader that writes the query digit. 

### `Sites.first`

 Enter the setup block of the first field in the list, transferring directly to `stop` when
the list is empty. 

### `Linked`

 Instruction-level links, with each field reader going straight to the next setup. 

### `steps`

 Every path for a selected base motif pays for exactly its fixed endpoint widths. 

### `native`

 All queried digits are simultaneously available at the lookup entry. Private bits,
resident geometry and every register outside the stated frame are preserved. 
