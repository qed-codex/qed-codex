---
{
  "module": "OAI/Computability/VPVNP/RAMPrivateLog.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMPrivateLog.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMPrivateLog.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Linear-scan private memory

A fresh call has an empty list of writes. Storing a word conses an address and
value, while loading scans from the head and defaults to zero. A write to a
previously used address therefore supersedes its older entries. Each scan
compares full words without ever iterating up to a supplied address.


### `CallAction.mapState`

 Change only the private continuations of an instruction, including both
binary continuations and every possible read answer. 

### `WriteLog`

 A newest-first list of private address-value writes. Looking up the first matching address
recovers its latest word. 

### `WriteLog.scan`

 A scan returns the newest value and a charge for testing the list, reading
the address, comparing it, and either advancing or copying the value. 

### `WriteLog.memory`

 The total memory function represented by the log. 

### `LogConfig`

 Private RAM configuration with its program counter, persistent word, registers and a
newest-first log of writes. 

### `LogConfig.pc`

 Instruction address currently selected in the private machine's finite program table. 

### `LogConfig.persistent`

 Persistent word carried in the current private call configuration. 

### `LogConfig.reg`

 Current contents of the private word registers. 

### `LogConfig.writes`

 Newest-first list of private stores since the beginning of the call. 

### `LogConfig.denote`

 Interpret a logged configuration as an ordinary RAM configuration by evaluating its write
log as a private memory. 

### `Instr.nextLog`

 A store extends the log once. Every other opcode retains the current log. 

### `Instr.runLogged`

 Use the instruction's register and control updates unchanged. In the
input configuration the private read operation is the linear scan, and in
every continuing output the writes are kept as a list. 

### `Instr.runLogged_correct`

 The logged dispatcher implements all of the direct-memory opcodes. 

### `Machine.logProgram`

 Resetting the private log is independent of the width of the address
space. Public data and the persistent state have the native interpretation. 
