---
{
  "module": "OAI/Computability/VPVNP/RAMTapeWordShiftMove.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMTapeWordShiftMove.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMTapeWordShiftMove.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Stack transfers in the variable-shift machine

Each transfer pops the source and pushes its bits onto the destination.
The final empty-stack test accounts for one step beyond the two steps per
bit. Discarding the remaining shift amount needs only the pops.

