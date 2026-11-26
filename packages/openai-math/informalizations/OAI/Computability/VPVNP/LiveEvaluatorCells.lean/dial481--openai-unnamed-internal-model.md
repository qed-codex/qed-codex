---
{
  "module": "OAI/Computability/VPVNP/LiveEvaluatorCells.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LiveEvaluatorCells.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LiveEvaluatorCells.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Semantics of all noninitial calls of one live evaluator group

The persistent cursor visits the old cells in each of the two tapes.
The comparison instruction has no nondeterministic choices. On memory
containing the published action, the complete scan verifies the two
tape conditions of that action, including the blank fields of a halt.


### `AllCells`

 Every noninitial call starts with fresh private registers and checks its
unique cell at the public one-based cursor. 

### `allCells_iff`

 For a selected nonrejecting instruction with matching target, the two
sweeps perform exactly the checks on that instruction in the semantic code. 
