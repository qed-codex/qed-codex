---
{
  "module": "OAI/Computability/VPVNP/SliceArithmeticWord.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/SliceArithmeticWord.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/SliceArithmeticWord.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Prime-field coefficient arithmetic on bit stacks

The advice supplies the modulus and the canonical coefficients in registers.
A fixed pair of word instructions computes each operation. The first instruction
forms an ordinary integer sum, product or difference at a width large enough
to retain it. The second reduces this word modulo the advised modulus.


### `workingWidth`

 Word width sufficient for a sum or product of two canonical residues and
the modulus itself. The routine also accepts any wider register bank. 

### `limb`

 Embed a canonical residue in a register. 

### `Op`

 The residue operations supported by the fixed word routine for field arithmetic. 

### `Op.eval`

 Evaluate the chosen operation modulo `p`, using only the first operand for negation. 

### `routine`

 Both the opcode table and the port assignment are independent of the
prime and of the word width. The destination is reused as the intermediate. 

### `routine_runs`

 A clean architectural bank returns with only the destination register
updated. Input registers can alias the destination, since the first
instruction stages its operands before writeback. 
