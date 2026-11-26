---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/NativeLeafProgram.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/NativeLeafProgram.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/NativeLeafProgram.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 One fixed counting leaf, parameterized only by the fixed clause width.
The actual candidate queries and the separate history-only final query are
installed in the native greedy run. Terminal outer formulas use the checked
zero/power-of-two dispatcher. Semantic and resource composition is proved
separately; this file introduces no callback or evaluator parameter. 

### `localCommand`

 Physical preparation, all staged marked-query rounds, then the distinct
history-only accepted count. The full canonical result is written on788. 

### `command`

 Outer terminal classification retains ambient n. A nonterminal call
loads the disjoint leaf bank, executes the fixed local program, copies its
whole count to263, and physically clears the leaf bank before returning. 
