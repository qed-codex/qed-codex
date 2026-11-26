---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLog/RingScanServiceBasic.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/RingScanServiceBasic.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/RingScanServiceBasic.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 Shared native coefficient-ring ABI. All service programs have fixed size. 

### `ServiceStore`

 Public ports are result0, modulus5, operands8/9, degree11, width12,
base scalar zero17, and cached k-major table22. Other fields are private work. 
