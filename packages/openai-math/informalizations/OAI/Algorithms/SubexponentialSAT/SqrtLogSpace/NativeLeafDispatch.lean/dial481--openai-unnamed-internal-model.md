---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/NativeLeafDispatch.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/NativeLeafDispatch.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/NativeLeafDispatch.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 Actual terminal dispatch for the disjoint counting DFS. The retained ambient
dimension determines the empty-formula count. The nonterminal command is composed
after the same concrete classifier and must supply its own execution proof. 

### `terminal_done`

 The terminal branch returns the canonical whole count, including n = 0. 

### `nonterminal_ready`

 Classification does not enlarge either persistent parameter word. 

### `command_execution`

 Actual classifier, terminal handling and nonterminal execution share one
uniform bound at every compiled prefix. The callback is an execution proof for
the explicit command argument, to be instantiated by the streamed leaf. 
