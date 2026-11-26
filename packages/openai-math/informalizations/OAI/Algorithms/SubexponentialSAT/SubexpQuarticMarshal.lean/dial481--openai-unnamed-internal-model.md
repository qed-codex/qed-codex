---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SubexpQuarticMarshal.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SubexpQuarticMarshal.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SubexpQuarticMarshal.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# A fixed word-to-constant-quartic marshaler

The base word is on stack 0 and the width shape on stack 1. The program
preserves the shape, appends three zero words to the base word, and clears
all three scratch stacks. Only Boolean stack instructions are executed.


### `zeroProgram`

 Each shape cell produces exactly three zero bits. 

### `program`

 The whole instruction table has 23 labels, for every word and width. 

### `run`

 Exact instruction count. No relationship between word and shape lengths
is required for the padding operation itself. 

### `run_bound`

 Convenient equal-width bound for the four-coordinate payload. 
