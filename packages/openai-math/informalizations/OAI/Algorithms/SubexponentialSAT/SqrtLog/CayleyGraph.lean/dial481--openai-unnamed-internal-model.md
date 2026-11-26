---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLog/CayleyGraph.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/CayleyGraph.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/CayleyGraph.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 A bipartite regular Cayley multigraph with explicit ordered ports.
Every pair `(x,i)` is a separate edge, including repeated shifts. 

### `graph`

 The involutive port rotation retains the port even for parallel edges. 

### `hasMixing_of_smallWalsh`

 Small nonconstant Walsh sums imply the edge mixing inequality used by
Tanner-code distance. This includes the zero-dimensional cube and empty ports. 
