---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/HighQueryReturnReplay.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/HighQueryReturnReplay.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/HighQueryReturnReplay.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 The complete fixed query has an actual same-step replay after erasing its
five suspended caller words. These lemmas transport the exact output contracts
and every prefix of that execution. They do not construct a query evaluator;
the actual marked or accepted execution is supplied by the count proof. 

### `restore`

 Proof-side restoration of exactly the bytes ignored by the fixed query. 

### `restore_workspace`

 Equality on all891 query workspace words survives restoration, including
the selector words which were erased for the source-only time proof. 

### `restore_accepted_stacks`

 The accepted output changes only788 in the original whole store. The
complete binary word and every opaque caller byte are retained exactly. 

### `restore_record`

 The parser reset survives replay, while320 is the original unread tail.
No size or content restriction is placed on that tail or accumulated mass322. 

### `marked_space`

 All actual marked prefixes, including the final halt, have the maximum
of the local workspace cap and the unchanged suspended caller-word cap. 

### `marked`

 The same fixed marked execution returns the canonical whole count, all
891 workspace words, both collector sources and the reset parser. Its step
count is exactly the step count of the actual shadow execution. 

### `accepted`

 The same fixed accepted execution changes precisely the whole count788.
The time bound needs no lengths of the five suspended caller words; their
lengths occur only in the independent maximum-prefix bound. 
