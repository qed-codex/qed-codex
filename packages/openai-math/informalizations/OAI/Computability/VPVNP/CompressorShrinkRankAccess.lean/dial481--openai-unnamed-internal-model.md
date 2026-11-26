---
{
  "module": "OAI/Computability/VPVNP/CompressorShrinkRankAccess.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorShrinkRankAccess.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorShrinkRankAccess.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 # Physical read and write regions for bundle gather and rank

The stored lists prove that every followed ID belongs to the old port range.
The rank scan's owner array is still readable after ranking, which identifies
each scanned key row before the rank was written.

