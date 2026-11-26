---
{
  "module": "OAI/Computability/VPVNP/PairResidentFrameColumn.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairResidentFrameColumn.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairResidentFrameColumn.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Native copying of all intervals of a resident operand

Each fixed local interval has a read-only pointer calculation, the three-word
slice header and a private copy loop. The direction selects which of the two
stored offsets belongs to the input. The instruction table is fixed before
the widths, descriptor addresses, or branch bits are supplied.


### `Setup`

 A physical copy uses three dynamic pointers and a statically known orientation. 

### `Setup.source`

 Expression that computes the base address of the source interval in private memory. 

### `Setup.destination`

 Expression that computes the destination buffer's base address before the header supplies
  its offset. 

### `Setup.frame`

 Expression that locates the first word of the external three-word slice header. 

### `Setup.reverse`

 When true, apply the first stored offset to the destination and the second to the source.
  When false, apply them in source–destination order. 

### `Setup.operands`

 Initialize the six header registers in order with the source base, zero, destination base,
unit increment, zero and frame address. 

### `Row`

 One resident copy interval, described by its two private buffer bases, its external header
address, the offset in each buffer and the bits to transfer. 

### `Row.source`

 Private buffer base to which the source offset is added before reading the first bit. 

### `Row.destination`

 Base of the private buffer into which the row's bits are copied. 

### `Row.frame`

 External address of this row's offset pair, followed by its length word at `frame + 2`. 

### `Row.sourceOffset`

 Number of private cells from the source base to the first bit of this slice. 

### `Row.targetOffset`

 Number of private cells from the destination base to the start of the copied slice. 

### `Row.bits`

 Payload in increasing address order. Its length is the number of private cells to copy. 

### `Row.write`

 Store the row's payload one bit per private cell, starting at `destination + targetOffset`. 

### `Row.reads`

 The private source cells starting at `source + sourceOffset` contain the word encodings of
the row's bits in order. 

### `Row.Recorded`

 The setup expressions evaluate to the row's three pointers and the external header fits the
address space and records the payload length. For a nonempty slice, its two offset words
agree with the setup's orientation. 

### `Row.ReadSafe`

 The physical read addresses needed by one compiled setup and its slice header. 

### `Row.Fits`

 The pivot separates source and destination buffers. Each nonempty source interval ends at
or before the pivot, the destination starts at or above it, and each nonempty destination
interval ends strictly below the word modulus. 

### `setCount`

 Number of compiled instructions that evaluate the six setup operands for row `i`. 

### `Label`

 Instruction labels indexed by row, with separate ranges for its variable-length setup,
eleven header instructions and seven private copy instructions. 

### `setPC`

 Program counter for setup line `j` of row `i`, falling through to the first header
instruction once the setup lines are exhausted. 

### `headPC`

 Relocate an index in row `i`'s eleven-instruction slice header to its machine program
counter. 

### `copyPC`

 Locate one of the seven instructions of the private bit-copy loop for row `i`. 

### `start`

 Entry counter for the row with ordinal `n`, or the supplied return counter once all rows
have been visited. 

### `reg`

 Embed the six output registers of row `i`'s compiled setup into the enclosing machine
register file for use by the header and copy loop. 

### `instruction`

 Decode a column label into a setup, oriented header or copy-loop instruction. Finishing a
slice transfers control to the following row or to the return counter. 

### `frameTrace`

 The complete trace of one gather frame, with arbitrary compiler registers normalized to zero. 

### `trace`

 The trace of a fixed row list in numerical visit order. 

### `work`

 Bounds of the generated setup and copy instructions for one visit. 

### `probes`

 Per-row upper bound on external probes, counting all loads in the setup expressions and up
to three reads of the slice header. 

### `writes`

 The actual private-memory result of a sequence of slice copies. 

### `Result`

 Execution contract for a row list. The trace reaches the return counter with the prescribed
private writes, preserves persistent state and registers outside the visited scratch banks,
consumes no choices, and satisfies the summed time and probe bounds. 

### `native_exact`

 Every successful execution of the column realizes the prescribed trace. 

### `native_reads`

 The finite column code copies every recorded interval in physical row order,
consumes no branch choices and preserves every register outside its scratch bank. 

### `native`

 The finite column code copies every recorded interval in physical row order,
consumes no branch choices and preserves every register outside its scratch bank. 
