---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/QuerySelectorControlFrames.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/QuerySelectorControlFrames.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/QuerySelectorControlFrames.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 Actual query control commands exclude every read, peek and write in the
retained selector bank768..831. Calls into the original768-stack bank are
covered by their genuine port ranges, independently of their internal code. 

### `lowProgram_avoids`

 Every actual instruction of a lifted lower-bank program is disjoint from
the persistent selector interval. 

### `nodeAppendPrepare_avoids`

 The exact paid scalar-cache copies are also used by the tuple-sum visitor. 
