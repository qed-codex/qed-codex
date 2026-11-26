---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLog/SupportProgramSupports.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/SupportProgramSupports.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/SupportProgramSupports.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 Exact finite-set interpretation of the masks emitted by the fixed support
program. No ordering assumption is needed by the moment consumer. 

### `supports`

 Decode only the already generated rows; this does not enumerate a powerset. 

### `primitive_supports`

 The actual primitive execution yields exactly M_J distinct support sets,
each with cardinality less than J, and emits their masks in the same order. 
