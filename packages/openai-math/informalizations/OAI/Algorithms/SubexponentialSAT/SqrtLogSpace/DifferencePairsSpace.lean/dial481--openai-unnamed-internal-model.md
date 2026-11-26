---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/DifferencePairsSpace.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/DifferencePairsSpace.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/DifferencePairsSpace.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 Every source prefix of the actual pruned pair traversal. The two masks
carry the DFS phases; the resource invariant counts all caller stacks as well
as the four controller stacks. Callback time never contributes to the space
bound. 

### `callback_prefix`

 The callback branch has three control instructions before the callback and
two register updates after it. The callback's own uniform bound is retained. 

### `body_resources`

 One real DFS body step preserves the bounded controller geometry and all
persistent stack bounds. The only unbounded-time branch is split around its
actual callback. 

### `loop_stack_bound`

 The complete actual loop has a bound independent of the number of pairs.
The conserved depth and strict budget bound every DFS controller word. 

### `program_stack_bound`

 Initialization, every DFS iteration, and the concrete final halt share one
space bound on the same actual source execution. Zero budget performs no
callback and is covered as well. 

### `program_resources`

 Exact callback fold, the measured pair-count budget, and every source
prefix bound hold for one and the same finite-program run. The concrete query
callback must instantiate the explicit correctness and resource contracts. 
