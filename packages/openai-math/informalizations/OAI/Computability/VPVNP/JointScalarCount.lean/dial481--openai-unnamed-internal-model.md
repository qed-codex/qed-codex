---
{
  "module": "OAI/Computability/VPVNP/JointScalarCount.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/JointScalarCount.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/JointScalarCount.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Counting the witnesses of the signed joint row checker

Fixing the row address selects one witness bank. The other two banks must be
all zero, so summing the physical bit witnesses gives precisely the active
count. Both signs of each motif coefficient use the same comparison table.

