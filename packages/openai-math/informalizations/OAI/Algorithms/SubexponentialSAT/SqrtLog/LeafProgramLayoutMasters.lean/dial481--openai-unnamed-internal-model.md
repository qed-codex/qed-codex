---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLog/LeafProgramLayoutMasters.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/LeafProgramLayoutMasters.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/LeafProgramLayoutMasters.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 Layout/source metadata are parked outside the native arithmetic bank.
CRT and scalar arithmetic use several ports128..141 as scratch; these values
are therefore physically reloaded for each node and cleared before CRT. 
