---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SubexpPolynomialAddService.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SubexpPolynomialAddService.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SubexpPolynomialAddService.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 Cached dense addition for the local CRT controller. The fixed service
copies operands 240/241, invokes the actual dense-add instruction table, and
moves its output to 244. All native workspace is restored. 
