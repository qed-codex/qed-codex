---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/Enumerators.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/Enumerators.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/Enumerators.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

### `encoded_shape_length`

 The complete current tuple, including record delimiters, stays polynomial.
This is a bound on one word of data, not on the number of enumerated tuples. 

### `advance_stack_bound`

 A local increment has polynomial workspace independently of how many
other increments have preceded it. Every caller stack is included. 

### `visits_stack_bound`

 Every actual callback and controller prefix has one common storage bound.
The number of visits does not appear in the bound. 

### `enumerate_stack_bound`

 The iterator initialization and final halt preserve the loop's common
bound, so the theorem covers every prefix of the complete compiled program. 

### `countdown_visits_stack_bound`

 The binary countdown controller also retains a uniform stack bound for
arbitrarily many callbacks. Counter width is measured, never its numeric value. 

### `countdown_for_stack_bound`

 The initial zero test and final halt are included in the counted loop's
prefix bound. The test scans only the current bounded-length counter word. 

### `visits_reset_counter`

 A completed actual traversal resets every payload bit while retaining all
record widths. This lets successive scans reuse the same counter frame. 
