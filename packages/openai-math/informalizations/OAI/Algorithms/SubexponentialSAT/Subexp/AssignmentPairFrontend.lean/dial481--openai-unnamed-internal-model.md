---
{
  "module": "OAI/Algorithms/SubexponentialSAT/Subexp/AssignmentPairFrontend.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/Subexp/AssignmentPairFrontend.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/Subexp/AssignmentPairFrontend.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Physical raw-pair input for assignment setup

The actual all-vertex pair producer runs in a fixed private bank. Two stack
transfers place its bytes, in their original order, on assignment input 45.
The scope source and private bank are then cleared by actual instructions.

