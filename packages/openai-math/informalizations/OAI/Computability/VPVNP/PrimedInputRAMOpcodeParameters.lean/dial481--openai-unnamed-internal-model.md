---
{
  "module": "OAI/Computability/VPVNP/PrimedInputRAMOpcodeParameters.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PrimedInputRAMOpcodeParameters.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PrimedInputRAMOpcodeParameters.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Public words and the register state on entry to the input dispatcher

The fixed program prefix occupies the low bits of one public word. Each call
loads the dimensions of the two rectangles from the public words, reads the
three pair-specific cut lengths from RAM, and decodes its persistent cursor.


### `packedPrefix`

 Numeric value of the literal program prefix, least significant bit first. 

### `pubNat`

 Dimensions, fixed field widths, and the packed prefix in instruction-table order. 

### `pubWord`

 Encode a public layout parameter from the opcode table's ordered list as a width-`w` word. 

### `ParameterFit`

 Word-fit conditions beyond the tape and address bounds already in the layout. 

### `parameterFit_of_prefix`

 As soon as the site address is nonempty, the row contains a full sort block. 

### `eventually_parameterFit`

 At every sufficiently large length the fixed prefix and all public fields
fit the paper's word width, uniformly over all well-formed layouts. 

### `CutMemory`

 Memory invariant for the three cut-length words, independent of the rest of memory. 

### `Prepared`

 Exact state reached by the parameter-load and cursor-decoding instructions. 

### `load_unpack_exec`

 Every data call reaches the dispatch contract by 18 private loads, three
header reads and seven cursor arithmetic steps, leaving external memory intact. 
