---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SubexpNegationProgram.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SubexpNegationProgram.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SubexpNegationProgram.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# A finite modular-negation program

The runtime words are little-endian Boolean stacks. Stack 0 holds the operand,
stack 5 the positive modulus, and stack 8 a prepared word of value modulus - 1.
All other stacks start empty. A preserving copy supplies the second operand of
the verified multiplication program; both the modulus and the prepared word
survive the call. No reducedness assumption is made about the operand.


### `negationProgram`

 A fixed table: eight copy labels followed by 141 verified multiplication labels. 

### `negation_execute`

 The complete finite execution preserves both supplied constant words. 

### `negation_value`

 Numeric modular negation, including inputs at least as large as the modulus. 
