---
{
  "module": "OAI/Computability/VPVNP/LiveEvaluatorAdviceBanks.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LiveEvaluatorAdviceBanks.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LiveEvaluatorAdviceBanks.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Little-endian rows of the evaluator's distributed advice

A row may be shorter than a machine word. Only the requested source bits
enter it, and all higher bits and bits past the end of the source are zero.
Writing one verified source bit with the RAM's shift and bitwise-or opcodes
extends this partially assembled row. The same operation packs the raw
evaluator prefix and the separate table of permutation ordinals.


### `packedPrefix`

 Pack the requested low-order source bits of one advice row into a machine word, zeroing
unused positions and absent source bits. 

### `packedWord`

 Pack a complete advice row at the specified field width, using zero padding past the end of
the raw advice. 

### `packedPrefix_succ`

 Inserting the next source bit is exactly one native shift followed by bitwise or. 

### `packedPrefix_skip`

 A cropped column past the end of the raw input leaves the row unchanged. 

### `packedWord_inputWord`

 Full-width output rows are the words the midpoint initialization actually reads. 

### `packedWord_arrayBits`

 Packing a serialized array row returns that ordinal, extended to the runtime word width. 
