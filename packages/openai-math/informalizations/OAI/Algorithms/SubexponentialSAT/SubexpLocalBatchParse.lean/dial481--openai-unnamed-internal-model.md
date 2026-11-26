---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SubexpLocalBatchParse.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SubexpLocalBatchParse.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SubexpLocalBatchParse.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Preserving parsing of one local-basis batch

The master on stack 0 contains three consecutive frames: unary dimension,
unary kernel dimension, and the coordinate-major scalar table. This fixed
program copies and decodes those actual bytes, then computes the complement
dimension by one real pop for each item of the copied kernel dimension.

Outputs are stacks 1, 2, 3, and 4; scratch 5--11 is restored. Subtraction
saturates at zero, including when the second dimension exceeds the first.


### `drop_visits`

 Exact control trace for arbitrary data and counter bits, including an
empty source. Popping an empty stack leaves it empty. 

### `Clean`

 All local output and scratch stacks are initially empty. 

### `command_eval`

 Parsing, copying, subtraction, and every internal return are counted. 

### `program_run`

 Complete execution has a linear bound in the actual preserved payload. 
