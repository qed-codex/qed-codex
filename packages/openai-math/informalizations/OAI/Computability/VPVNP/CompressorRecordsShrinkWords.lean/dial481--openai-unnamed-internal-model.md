---
{
  "module": "OAI/Computability/VPVNP/CompressorRecordsShrinkWords.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorRecordsShrinkWords.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorRecordsShrinkWords.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Word correctness of the shrinking owner computation

The native directory arithmetic is carried out modulo the machine word size. Only
the low-field XOR and the color-bit test need a nonwrapping intermediate. Addresses
of the four inputs are taken in the actual external memory.


### `word`

 Encode a natural number as a machine word by reducing it modulo `2^w`. 

### `Params`

 Conditions on the shrinking worker's public radices, last color, and layout selector that
justify decoding the low field and testing the color bit in a machine word. 

### `column`

 Read the natural value in a column at the given index, adding the index to its public base
address in word arithmetic. 

### `decode_exact`

 Decode the fixed-width old position into its base, mask, slot and low lane. 

### `outputs_row`

 Numeric correctness for one native position. Output addresses remain words, so
only values used inside bit-field operations require a fit bound. 

### `outputs_exact`

 Word values written by the opcode table on a genuine old position, in the
numbering used by the next level's site and incidence directories. 
