---
{
  "module": "OAI/Computability/VPVNP/PrimedInputRAMOpcodes.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PrimedInputRAMOpcodes.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PrimedInputRAMOpcodes.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Fixed word code for the two input passes

The persistent cursor ranges first over the chosen-bit rectangle, then over
the assembled-input rectangle. A common dispatch computes the bit's source
and its owner flag. The port arithmetic routine supplies the sender site and
within-port offset. All other field handling, including the three supplied
cut lengths, is given by the explicit word instructions below.


### `Code`

 Structured word code for the primed input passes, with 48 private registers and 16 public
words. 

### `Reg`

 Index of a private register in the primed input dispatcher. 

### `Pub`

 Index of a public parameter word of the primed input dispatcher. 

### `line`

 Code for a single arithmetic or word-memory instruction. 

### `set`

 Load a two-bit literal into the destination register. 

### `load`

 Load the indexed public word into a private register. 

### `bin`

 Apply a binary word operation to two registers and store its result in the destination
register. 

### `copy`

 Copy a word by adding the source to register 0, which the parameter loader initializes to
zero. 

### `read`

 Read an external word at the address held in a register into the destination register. 

### `write`

 Write the source register's word to the external address held in the address register. 

### `sequence`

 Straight sequence of instructions or structured blocks. 

### `parameterTail`

 Constants, public geometry, persistent cursor, and the pair-specific
cut lengths supplied by the three external header words. 

### `loadParameters`

 Initialize the constants, load the persistent cursor and public layout words, then read the
three cut lengths from external memory. 

### `unpackCursor`

 Registers 21 through 24 hold the flat index, group, site and within-row
offset. Register 29 is the next persistent cursor and 30 is the output
address of the current pass. 

### `literalZero`

 Result registers are 26 (address or bit), 27 (fetch flag), 28 (owner
flag). Writing all three on each branch also covers a missing or padded bit. 

### `literalBit`

 Extract the indicated bit by shifting and masking, then mark the result as a literal
without a first-pass choice. 

### `fetched`

 Run the supplied address computation and flag the result as a memory fetch, recording
whether this cell owns a first-pass choice. 

### `indexField`

 Fetch the index bit of this very group, with zero beyond the supplied
fixed length. Header bit arrays start immediately after the length words. 

### `adviceBase`

 Compute the fixed base `3 + 2*indexLength` of the advice array. 

### `adviceField`

 Resolve the site's advice bit to its header address within the supplied advice length, and
to a literal zero beyond it. 

### `leftField`

 Resolve an incoming outer cut bit using the left cut length and its header offset
immediately after the advice. 

### `rightField`

 Resolve an outgoing outer cut bit using the right cut length and its header offset beyond
the reserved left cut array. 

### `middleField`

 A middle cut bit is read from the first group's outgoing slot. 

### `headerFields`

 Dispatch the four one-bit fields using their offset in register 25. 

### `portResult`

 Translate a raw transcript sender into its chosen-bit scratch address.
The port routine sets registers 32 (present), 33 (sender), 34 (offset). 

### `dispatch`

 Extract the address bit or identify one of the fixed-width header/port
intervals by comparisons against their exclusive ends. Register 35 holds
a temporary boundary; the port block can reuse it after entering. 

### `act`

 A designated cell has two different paths even if the stored value
already equals the chosen value. A nondesignated cell takes only the
deterministic skip. Second-pass cells always write one output word. 

### `dataCall`

 Fixed body of a data call. Its exit register is 29. The terminal cursor
may enter the next phase of the auxiliary machine. 

### `table`

 A physical opcode table with constant instruction count across lengths
when the port block is fixed. 

### `table_executes`

 The template executes the control graph with the true burst interpreter
for every raw memory and branch stream. 
