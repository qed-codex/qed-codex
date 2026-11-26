---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SubexpKeyPadProgram.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SubexpKeyPadProgram.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SubexpKeyPadProgram.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 A fixed five-instruction routine copies a forward key for exactly the
number of bits in a unary width counter. Empty input reads as false, so the
same routine truncates long keys and zero-pads short keys. 
