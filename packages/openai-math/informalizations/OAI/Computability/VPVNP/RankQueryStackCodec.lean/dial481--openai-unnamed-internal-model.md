---
{
  "module": "OAI/Computability/VPVNP/RankQueryStackCodec.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RankQueryStackCodec.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RankQueryStackCodec.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Encoding a Schur continuation as ten registers

The direction distinguishes waiting for the left or right operand. Six registers
hold the parent query, followed by the remaining summand index and two packed
extension-field scalars. The unused left operand in a waiting-left frame is
zero. All numeric registers are little-endian words of a common width.


### `readWords`

 Decode the tag, checking all index, block and degree bounds. 

### `words_le`

 One uniform bound on all six query registers, including the empty matrix. 

### `SchurFrame`

 Evaluator frame specialized to a Schur query key and an encoded extension-field scalar. 

### `words`

 Fields in order: direction, query, remaining summands, accumulator, saved left operand. 

### `remaining`

 Remaining product-scan index saved in either kind of Schur frame. 

### `words_fit`

 Width conditions for the exact scalar and control words, with a separate
bound for the summand index supplied by the arity estimate. 

### `bits`

 All registers use the same width; the tag occupies a register too. 
