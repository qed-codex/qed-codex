---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/DifferencePairsRelational.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/DifferencePairsRelational.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/DifferencePairsRelational.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 Relational accumulator correctness for the existing four-stack pair DFS.
Only the proof invariant is generalized: the actual commands, branch order,
callback states and all-prefix space theorem are unchanged. 

### `CallbackSpec`

 The callback returns an actual dictionary representing the next semantic
value. No uniform choice of dictionary bytes is required. 

### `CallbackSpec.erased`

 Erasing the semantic value supplies exactly the existing resource
contract. Its auxiliary byte observation is the preserved depth controller;
the resource theorem does not require an off-controller output port. 

### `subtree`

 The same actual subtree traversal realizes the semantic fold, while its
dictionary witnesses may vary at every callback. 

### `command_eval`

 Actual command execution and semantic accumulator correctness, before
the single compiler halt step. 

### `program_resources`

 Relational correctness, exact native time and all-prefix space refer to
one execution of the unchanged pair iterator, including J=0 and J>N. 
