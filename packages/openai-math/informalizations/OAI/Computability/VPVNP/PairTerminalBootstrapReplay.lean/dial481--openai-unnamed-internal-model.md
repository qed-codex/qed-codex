---
{
  "module": "OAI/Computability/VPVNP/PairTerminalBootstrapReplay.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairTerminalBootstrapReplay.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairTerminalBootstrapReplay.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Packed addresses in the first two terminal phases

The 21 bootstrap stores, width column, prefix table and linked control cells
all lie at or above the workspace base. This supplies the protected-address
frame of those stages even on a terminal run with a rejecting suffix.


### `QuietPrefix.replayFrame_packedStart`

 Discharge all source and linker address conditions for the first two
stages from the actual packed layout and bootstrap data. 
