---
{
  "module": "OAI/Computability/VPVNP/PairTerminalQuietPrefix.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairTerminalQuietPrefix.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairTerminalQuietPrefix.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Deterministic terminal stages before the shared wire guesses

The first three blocks use the source bootstrap, prefix scan and selected
traversal-controller reports. Each block runs on the physical memory left by
the preceding block. Their only branch strings are empty. The shared-bit
worker starts on the resulting physical memory, with the linked handoff cells
excluded from the equality with the ordinary traversal memory.


### `quietPrefixOfRows`

 Compose the native row-construction burst sequence with the actual
bootstrap and final-width scans. Its physical post-memory agrees with the
row and tag construction on every cell available to the shared-bit worker. 
