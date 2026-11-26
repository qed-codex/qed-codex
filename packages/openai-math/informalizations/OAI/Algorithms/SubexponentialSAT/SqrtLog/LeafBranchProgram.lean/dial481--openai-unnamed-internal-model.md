---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLog/LeafBranchProgram.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/LeafBranchProgram.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/LeafBranchProgram.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 The branch callback is a real residual-count program followed by the native
binary adder. Semantic branch counts occur only in its verification contract. 

### `ResidualSpec`

 A residual count must actually run and emit a bounded binary word. 

### `body_step`

 The native callback both adds the computed count and empties its input. 

### `fixedPorts`

 Concrete shared ports used inside the marked-clause collector. 
