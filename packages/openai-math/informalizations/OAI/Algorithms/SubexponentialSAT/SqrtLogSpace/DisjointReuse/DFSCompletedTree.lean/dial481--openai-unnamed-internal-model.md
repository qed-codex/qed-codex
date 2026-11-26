---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/DisjointReuse/DFSCompletedTree.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/DisjointReuse/DFSCompletedTree.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/DisjointReuse/DFSCompletedTree.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 A completed concrete transition history determines a proof-only branch
forest backwards. This transfers the sharp tree-node bound to the actual
number of visits, without storing a tree or list of visits on the machine.


### `completed_tree`

 Exact visit count, independent of the physical selector's tie breaking. 

### `completed_visits_reciprocal`

 The parameter program produces the threshold for the reciprocal budget.
This form matches its natural-number output without rational representation
assumptions at the native interface. 

### `potential`

 A terminating proof measure, never a retained binary machine counter. 
