---
{
  "module": "OAI/Computability/VPVNP/PrimedStackRAMLeafVisit.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PrimedStackRAMLeafVisit.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PrimedStackRAMLeafVisit.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Terminal visits of the primed counter

For a fresh chosen position, the native instructions set the location mark,
fetch the actual row bit and increment exactly that production. Repeated
and out-of-range choices fail before reaching the increment.

