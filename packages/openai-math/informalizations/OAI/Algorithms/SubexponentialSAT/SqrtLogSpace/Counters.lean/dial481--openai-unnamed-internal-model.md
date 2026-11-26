---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/Counters.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/Counters.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/Counters.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

### `wordEquiv`

 Fixed-width words and their in-range numeric indices are equivalent.
This specification is not a retained list of the enumerated words. 

### `fuel_bits_length`

 The binary word of an exponentially large fuel has only linear width. 

### `bits_length_le_of_le_pow`

 The canonical binary encoding of a number at most the assignment count is short. 

### `increment_word`

 The actual ripple increment remains the next fixed-width word before overflow. 

### `ripple_prefix_stack_bound`

 The local routine is linear in the current word, even when its value is exponential. 

### `incrementCmd`

 Generic actual increment call on the same finite ports as countdown. 

### `incrementResult_stacks`

 Every off-counter caller stack is preserved, including cleared scratch. 

### `powerTwoProgram`

 Consume a length witness and construct the binary fuel `2^h` by pushing
one zero per witness bit. The finite control never stores `h` or `2^h`. 

### `powerTwo_prefix_stack_bound`

 Every prefix of fuel construction has linear storage, including scratch. 
