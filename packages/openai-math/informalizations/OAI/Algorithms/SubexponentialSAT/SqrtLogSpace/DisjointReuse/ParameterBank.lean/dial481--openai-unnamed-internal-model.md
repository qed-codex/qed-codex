---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/DisjointReuse/ParameterBank.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/DisjointReuse/ParameterBank.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/DisjointReuse/ParameterBank.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 Fixed Boolean-stack arithmetic in a 19-word data bank and 13 scratch stacks. 

### `resetLogRegisters`

 Reset the local logarithm program's three Boolean registers. 

### `clogCmd`

 The input word is preserved and the logarithm overwrites its fresh copy. 

### `compareCmd`

 Consumes both selected words and returns their strict comparison in register zero. 

### `clog_le_word_length`

 A padded binary input still bounds its ceiling logarithm by its bit length. 

### `power_eval_bounded`

 Exponentiation is polynomial here because both the numerical exponent and
all actual operand lengths are bounded. 

### `sequence`

 Sequential composition of a fixed finite list of commands. 
