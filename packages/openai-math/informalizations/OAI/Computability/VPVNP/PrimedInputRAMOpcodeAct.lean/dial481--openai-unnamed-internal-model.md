---
{
  "module": "OAI/Computability/VPVNP/PrimedInputRAMOpcodeAct.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PrimedInputRAMOpcodeAct.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PrimedInputRAMOpcodeAct.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Choice and copy instructions at the end of each data call

The owner flag controls one genuine burst-RAM choice. Nonowner cells of the
first pass skip the write. Second-pass cells write the literal or the word
obtained from one read. The next persistent cursor remains in register 29.

