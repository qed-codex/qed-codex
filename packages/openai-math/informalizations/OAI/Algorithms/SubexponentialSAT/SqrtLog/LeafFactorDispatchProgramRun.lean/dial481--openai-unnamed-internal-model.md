---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLog/LeafFactorDispatchProgramRun.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/LeafFactorDispatchProgramRun.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/LeafFactorDispatchProgramRun.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 Fixed native dispatcher: reverse the incoming ID, classify it, and scan
only the selected source. No selected payload is supplied as an input. 

### `baseStacks_leaf`

 The source master is exactly the existing executable leaf serialization. 

### `selectedPayload_leaf_marked`

 A marked factor returns the original clause's literal-code payload. 
