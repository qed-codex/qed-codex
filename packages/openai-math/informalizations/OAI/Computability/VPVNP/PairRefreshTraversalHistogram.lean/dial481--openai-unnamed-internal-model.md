---
{
  "module": "OAI/Computability/VPVNP/PairRefreshTraversalHistogram.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairRefreshTraversalHistogram.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairRefreshTraversalHistogram.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Histogram of a successful terminal refresh

A successful refresh changes each private histogram cell by the number of
occurrences of its parameter in the emitted list. The statement applies to
arbitrary incoming DFS scratch, including the counters accumulated by earlier visits.

