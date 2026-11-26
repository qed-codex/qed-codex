---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SubexpLEFactorSystem.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SubexpLEFactorSystem.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SubexpLEFactorSystem.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# The factor system matching little-endian materialized chunks

Only the local chunk embedding changes. Chunk scopes, occurrence bounds,
and the exact number of satisfying assignments are preserved. Clause tables
include local-label validity, including the shorter final chunk.


### `system`

 The actual label convention used by the bit materializer. 
