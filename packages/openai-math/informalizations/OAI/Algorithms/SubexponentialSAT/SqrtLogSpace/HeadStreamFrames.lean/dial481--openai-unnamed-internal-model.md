---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/HeadStreamFrames.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/HeadStreamFrames.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/HeadStreamFrames.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 The actual head scan neither reads nor writes the retained collector words.
This syntactic certificate supports replay with exactly the same number of steps. 

### `head_avoids`

 Every head-controller access is accounted for, including losing gates,
all binary counter tests and decrements, and final reclamation. 
