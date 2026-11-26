---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/DisjointReuse/DFSStartup.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/DisjointReuse/DFSStartup.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/DisjointReuse/DFSStartup.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 Concrete startup for the shared 80-register, 1220-stack DFS ABI.
The input frame already contains the normalized body and actual parameter words.
This module proves only startup; it does not assume or claim a completed DFS run.


### `startup_prefix_space`

 Startup is polynomial-time, so its own local time bounds every source
prefix. This estimate is never applied to the exponentially long DFS loop. 
