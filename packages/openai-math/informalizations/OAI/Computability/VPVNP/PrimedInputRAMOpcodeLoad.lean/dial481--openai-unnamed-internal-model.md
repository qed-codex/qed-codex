---
{
  "module": "OAI/Computability/VPVNP/PrimedInputRAMOpcodeLoad.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PrimedInputRAMOpcodeLoad.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PrimedInputRAMOpcodeLoad.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Loading the parameters and decoding the persistent rectangle cursor

The three cut-length words are fetched from external memory on every data
call. Group numbers are only row selectors here: the bits of the actual
large group index are fetched at the designated header addresses.


### `parameterEvents`

 Trace of parameter loading, with eighteen private ticks followed by reads of the left,
middle and right cut lengths at addresses 0, 1 and 2. 

### `Loaded`

 Register state after the parameter loads. 

### `cursorRegs`

 Register state after decoding the persistent cursor into the rectangle index, row, group,
site, bit offset, successor cursor and destination address. 

### `Cursor`

 Rectangle coordinates in the bounded output registers. 
