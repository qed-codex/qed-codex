---
{
  "module": "OAI/Computability/VPVNP/PairNativeFrameReads.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairNativeFrameReads.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairNativeFrameReads.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 # Reading the terminal vertex's six descriptor words

The surrounding ordinal dispatch passes the address of the terminal header
in register zero and the role offset in register one. Only the six named
descriptor offsets cause external probes. The addresses are computed with
the two-bit literals available to the fixed pair program.


### `R`

 Register indices for the 24-word work bank shared by the header reader and frame
arithmetic. 

### `Code`

 Native instruction flows for the terminal frame, with 24 work registers and eleven public
operands. 

### `destinations`

 Header registers 3, 17, 4, 5, 6 and 8 receive the absolute row base,
row words, row stride, base radix, lane radix and auxiliary shadow span. 

### `offsets`

 Header offsets for the absolute row base, row word count, row stride, base radix, lane
radix and shadow span, in read order. 

### `readField`

 Copy the header pointer from register zero, advance it by `off` unit steps, and load the
addressed external word into `dst`. 

### `fieldEvents`

 Trace for reading one header field, with one pointer-copy tick, `off` increment ticks, and
a read carrying the value from memory. 

### `reads`

 Initialize the unit register and load all six terminal descriptor words into their assigned
work registers. 

### `readEvents`

 Ordered event trace for the complete header reader, starting with the unit initialization
and ending with the shadow-span read. 

### `loaded`

 Work bank after the header reader sets register 15 to one and installs the six external
field values in their destinations. 
