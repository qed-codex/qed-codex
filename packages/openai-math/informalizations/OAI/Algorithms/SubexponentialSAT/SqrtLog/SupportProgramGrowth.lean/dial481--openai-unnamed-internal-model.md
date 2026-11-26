---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLog/SupportProgramGrowth.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/SupportProgramGrowth.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/SupportProgramGrowth.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 Each growth stage expands only the currently retained masks, then prunes.
The intermediate candidate list contains at most twice the final support count. 

### `grow`

 Prepending presentation of one breadth-first growth stage. 
