---
{
  "module": "OAI/Computability/VPVNP/PrimedStackRAMBinaryVisit.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PrimedStackRAMBinaryVisit.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PrimedStackRAMBinaryVisit.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Internal visits of the primed counter

The range guards precede the counter update. An accepted internal choice
adds the dense binary production once and pushes the ordered children on
the external stack. All marks and all assembled input bits remain available.

