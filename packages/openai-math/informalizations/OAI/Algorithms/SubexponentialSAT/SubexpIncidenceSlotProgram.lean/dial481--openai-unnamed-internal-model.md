---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SubexpIncidenceSlotProgram.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SubexpIncidenceSlotProgram.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SubexpIncidenceSlotProgram.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Physical local-slot query

The three preserved inputs are the encoded scope family and unary factor and
vertex indices. A real mask pass selects the preceding factors, and the checked
incidence scan counts them. No slot map or selected prefix is supplied as input.

