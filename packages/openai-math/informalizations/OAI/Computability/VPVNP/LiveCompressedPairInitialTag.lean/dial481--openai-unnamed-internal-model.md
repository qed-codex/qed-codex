---
{
  "module": "OAI/Computability/VPVNP/LiveCompressedPairInitialTag.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LiveCompressedPairInitialTag.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LiveCompressedPairInitialTag.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# The compressed pair starts in its row-count stage

The linker uses the first old-state word, immediately after the grammar and
motif counters. The header's zero suffix covers this cell. The nomination,
auxiliary initialization and shadow-copy calls preserve it through pair entry.

