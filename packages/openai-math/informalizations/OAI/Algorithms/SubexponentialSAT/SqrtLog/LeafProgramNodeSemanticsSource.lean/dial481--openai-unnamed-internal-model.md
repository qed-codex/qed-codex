---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLog/LeafProgramNodeSemanticsSource.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/LeafProgramNodeSemanticsSource.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/LeafProgramNodeSemanticsSource.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 Original IDs and fixed-high constants are retained in the source path.
All summation variables are free coordinates. 

### `branchPath`

 The row bank is indexed by factor and original variable ID. 

### `branch_target_degree`

 The bound is on the actual source target made from these rows. 

### `branch_target_degree_lt`

 Neutral factors may enlarge the parameter count; they never enlarge the
source polynomial degree. 

### `liftedHashes`

 Lift a sparse input row coefficient by coefficient, not by a nonexistent
ring homomorphism from the residue field into the thickened ring. 
