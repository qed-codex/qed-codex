---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLog/MomentsAssemblyProgramFrames.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/MomentsAssemblyProgramFrames.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/MomentsAssemblyProgramFrames.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 Native frame and list movement for the moment-assembly driver. The fixed
machine has the node worker's 40-register/768-stack size. The arithmetic core
uses stacks below 56; assignment/head/support/bucket streams live on 160+.
All payload lengths and iteration counts are runtime data. 

### `rawFrames`

 A raw list of framed records. The enclosing frame supplies its boundary. 

### `takeFrame`

 A frame is read into a reverse buffer and then physically moved forward. 
