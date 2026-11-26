---
{
  "module": "OAI/Computability/VPVNP/RAMTapeWordDivision.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMTapeWordDivision.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMTapeWordDivision.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Restoring binary division on a word tape

Process the dividend from its most significant bit to its least significant
bit. At each iteration one subtract-with-borrow scan of width `w+1`
determines the quotient bit. The next remainder is the low `w` bits of the
difference or of the restored candidate. Zero divisor follows the natural
word convention of the RAM instruction table.


### `divideStep`

 Return the quotient bit and new remainder. The high zero on the divisor
allows the left-shifted candidate to use its carry bit. 

### `dividePass`

 The recursive result on the tail is the result on the already consumed
higher-order prefix. Quotient bits are consed in little-endian order. 

### `divideWords`

 Both outputs have the width of the input words. For division by zero the
quotient is all zeros and the remainder is the original dividend. 

### `divideWords_wordBits`

 The output bit stacks are the words returned by the RAM's division and
remainder opcodes, including at zero width. 
