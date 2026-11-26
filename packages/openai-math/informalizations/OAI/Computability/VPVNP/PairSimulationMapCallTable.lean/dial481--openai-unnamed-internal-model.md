---
{
  "module": "OAI/Computability/VPVNP/PairSimulationMapCallTable.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSimulationMapCallTable.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSimulationMapCallTable.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Complete motif call table including initialization

A single fixed table loads the operand expressions from the private descriptor,
constructs the port directory, and enters the grouped map interpreter. The
expression compiler writes directly into the interpreter's allocated registers.
The descriptor pointer and the directory temporaries occupy distinct registers.


### `formulas`

 Map-call register initialization expressions using the field of this party's anchor port to
locate its selector suffix. 

### `Layout`

 Register layout for the compiler bank and the map, including their shared outputs. 

### `Layout.core`

 Register and public-word allocation, with supply-edge order, for the grouped map
  interpreter entered after call initialization. 

### `Layout.args`

 Number the fields of the private call descriptor so each argument can be loaded by its
  word offset. 

### `Layout.slots`

 Number the map interpreter's logical registers to identify the corresponding
  initialization outputs. 

### `Layout.vm`

 Place the expression compiler's output and scratch registers in the physical register
  file. Each output aliases its designated map register. 

### `Layout.ptr`

 Register containing the base address of the private call descriptor during register
  initialization. 

### `Layout.scratch`

 Two temporary registers for the port directory writer, holding the current directory cell
  and the selector-suffix pointer to store there. 

### `allocate`

 Allocate the output and expression scratch bank, then two directory temporaries
and the descriptor pointer. The seed supplies the public ports and edge order. 

### `lines`

 Ordered assignments emitted by the expression compiler to initialize the map registers from
the private descriptor. 

### `Address`

 Instruction addresses of the complete map call, partitioned into descriptor setup, port
directory construction, and grouped map evaluation. 

### `corePC`

 Relocate an instruction address of the grouped map interpreter into the complete call
table. 

### `dirPC`

 Relocate an address of the incident port directory initializer into the complete call
table. 

### `initPC`

 Program counter for a compiled register assignment, with the end of the assignment list
transferring control to the directory initializer. 

### `text`

 Emit the instruction at a call-table address, linking the last setup assignment to the
directory writer and the directory writer to the map's selector scan. 

### `installed`

 Keep the successful exit available as the caller's continuation. 

### `locations`

 Finite numbering of all descriptor setup, directory, and map interpreter addresses in this
layout. 

### `template`

 Standalone template for a complete map call, starting with descriptor setup and using the
finite address numbering for all jump targets. 

### `links`

 These are the precise instruction-level links of initialization and execution. 

### `native_post`

 Execute the installed finite table, including the operand and directory prefix. 

### `native_framed`

 The exact memory update implies preservation outside the written cells. 

### `native`

 The histogram and exit semantics of the native call. 

### `run_entryInput_post`

 The very same instruction and public-data bank implements the map for all live
inputs. Only the resident raw descriptor and the actual input bit slices are required. 

### `run_entryInput_framed`

 The exterior memory frame at a recorded native call. 

### `run_entryInput`

 The same physical path evaluated on an actual recorded template invocation. 
