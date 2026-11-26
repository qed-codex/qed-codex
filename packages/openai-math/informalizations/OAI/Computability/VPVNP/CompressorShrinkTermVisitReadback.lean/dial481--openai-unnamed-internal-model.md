---
{
  "module": "OAI/Computability/VPVNP/CompressorShrinkTermVisitReadback.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorShrinkTermVisitReadback.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorShrinkTermVisitReadback.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Operand readback of the two actual shrinking term visits

The planner expressions read the published shrinking level and allocator
origin. Their evaluated operands, initial cursors and exclusive stops are
the ones used by the chronological native packets.

