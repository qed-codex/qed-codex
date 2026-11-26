---
{
  "module": "OAI/Computability/VPVNP/RAMTapeWordSimple.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMTapeWordSimple.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMTapeWordSimple.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Arithmetic and logical RAM opcodes in the finite scan control

Addition and subtraction discard the final overflow bit. Parallel Boolean
operations use a dummy flag. The same subtraction run retains the unsigned
comparison result in its final state.


### `ScanOp`

 RAM operations computable by scanning pairs of corresponding bits with a single Boolean
carry or borrow. 

### `ScanOp.opcode`

 Identify the bit-scan operation with the corresponding binary RAM opcode. 

### `ScanOp.step`

 Compute one output bit and the next carry or borrow. Bitwise logical operations compute the
output without a carry. 

### `ScanOp.word_run`

 Literal bit-stack executions of all five linear-time binary opcodes. 

### `subScan_borrow`

 Unsigned comparison of the operands can branch directly on the final
borrow of the subtraction scan. 
