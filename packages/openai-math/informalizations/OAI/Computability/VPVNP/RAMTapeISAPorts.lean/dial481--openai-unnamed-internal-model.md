---
{
  "module": "OAI/Computability/VPVNP/RAMTapeISAPorts.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMTapeISAPorts.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMTapeISAPorts.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Stack bank and returning routines for fixed RAM instruction tables

The program counter is in finite control. Registers, the persistent word and
public words have distinct stack labels. The three stored private-log streams
share the address-log convention. Work ports 14 and 15 serve as scratch for
operand copies, independently of the arithmetic and address-log routines.


### `FiniteRoutine`

 A finite control packaged with its entry, so separately typed opcode
routines can form a single fixed program by sequencing. 

### `FiniteRoutine.State`

 Finite control-state type of the returning stack routine. 

### `FiniteRoutine.body`

 Stack routine on the specified ports and finite control states. 

### `ofRoutine`

 Package a returning stack routine with its finite control-state type. 

### `followedBy`

 Sequence two finite routines so the return from the first enters the second. 

### `ret`

 The finite routine that immediately returns. 

### `Runs`

 Execution of the routine from the input bank to the output bank in the given number of
steps. 

### `ofStackCode`

 Redirect the normal halts of a finite subprogram into the caller. Rejection
remains a rejecting halt. No extra step is charged for a normal return. 

### `Port`

 Architectural, public, persistent, scratch, and private write-log stack labels for a fixed
instruction table. 

### `logStacks`

 Encode a private write log by its keys, values, and occupancy marks, with the other log
ports empty. 

### `bank`

 Between instructions, every work stack and address-log scratch stack is
empty. The architectural bank is independent of the program-counter label. 

### `configBank`

 Encode the public words, persistent state, registers, and writes of a RAM configuration as
a stack bank. 
