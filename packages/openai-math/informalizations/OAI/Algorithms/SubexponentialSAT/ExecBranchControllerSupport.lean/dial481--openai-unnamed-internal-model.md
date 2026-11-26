---
{
  "module": "OAI/Algorithms/SubexponentialSAT/ExecBranchControllerSupport.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/ExecBranchControllerSupport.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/ExecBranchControllerSupport.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 Actual copying, child calls, and framed output for the two-child controller.
Ports 0--6 hold pending work, leaves, both outputs, parent, core, and selection.
Ports 7--22 are a reusable 16-stack child workspace. 

### `buildChild_eval`

 Compose a measured execution of a concrete child table with the actual
input copies and frame writer. This lemma only links real instruction traces. 
