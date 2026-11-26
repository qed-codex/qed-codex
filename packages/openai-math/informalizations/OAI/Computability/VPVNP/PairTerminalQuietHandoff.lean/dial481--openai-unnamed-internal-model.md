---
{
  "module": "OAI/Computability/VPVNP/PairTerminalQuietHandoff.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairTerminalQuietHandoff.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairTerminalQuietHandoff.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 # Controller validity after a completed physical terminal phase 

### `Phase.handoffValid`

 A completed phase writes the actual next-stage tag and its zero cursor
before the following phase. The original worker can start from arbitrary
values at both controller addresses. 

### `QuietPrefix.valid_sharedBits`

 Every completed deterministic prefix provides the actual entry to the
shared-bit stage, regardless of which vertex paths subsequently succeed. 
