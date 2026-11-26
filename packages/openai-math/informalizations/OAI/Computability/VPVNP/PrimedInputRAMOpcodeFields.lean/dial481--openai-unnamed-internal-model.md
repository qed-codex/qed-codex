---
{
  "module": "OAI/Computability/VPVNP/PrimedInputRAMOpcodeFields.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PrimedInputRAMOpcodeFields.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PrimedInputRAMOpcodeFields.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Native word instructions for literals and header fields

The four header fields choose between a literal zero and an address derived from the
loaded parameters. A middle-cut bit is owned only by the outgoing endpoint of group
zero. All paths in these blocks update only the payload, fetch flag, and owner flag.


### `fieldResult`

 Register output common to all field decisions. 

### `readBit_word`

 The shift-and-mask implements the mathematical bit, including shifts beyond
the end of the word. 

### `HeaderRegisters`

 Register values after loading the public dimensions and cut lengths and
decoding the current row's group, site, and header offset. 

### `exec_headerFields`

 Bounded, probe-free execution of all four supplied header fields. 
