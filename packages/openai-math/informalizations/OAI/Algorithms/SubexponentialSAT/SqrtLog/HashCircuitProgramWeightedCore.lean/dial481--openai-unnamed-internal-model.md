---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLog/HashCircuitProgramWeightedCore.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/HashCircuitProgramWeightedCore.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/HashCircuitProgramWeightedCore.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 Shared native weighted sparse accumulation. This local56-stack core is
used by hash rows and head moments. It retains the source dictionary41,
consumes the flat coefficient44, and replaces accumulator42 by the normalized
weighted sum. Its output restores all temporary work used by these phases. 

### `command`

 Both subphases are concrete fixed bit programs. 
