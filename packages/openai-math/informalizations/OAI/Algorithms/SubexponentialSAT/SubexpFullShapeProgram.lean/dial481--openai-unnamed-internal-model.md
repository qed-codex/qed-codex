---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SubexpFullShapeProgram.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SubexpFullShapeProgram.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SubexpFullShapeProgram.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# The physical shape for the uniform padded chunk array

The existing fixed block-copy program is used with a chunk-width word as its
table and an actual unary chunk count as its loop counter. It produces a word
of length `D * ell`, preserves the width word, and consumes the count. Caller
data such as the declared-variable shape are preserved through fixed port maps.


### `inputState`

 Width on 0, empty output 1 and scratch 2, actual unary count on 3. 

### `outputState`

 Width is preserved, the completed shape occupies 1, and work is empty. 

### `lifted_eval`

 The same physical program can be placed in any fixed caller frame. 

### `caller_stack_preserved`

 In particular, a caller's `nShape` master stays unchanged when its port
is outside the four working ports. 

### `canonical_length_bounds`

 Ceiling-sized allocation contains every input bit and fewer than one
extra chunk of padding, including when the input has no variables. 
