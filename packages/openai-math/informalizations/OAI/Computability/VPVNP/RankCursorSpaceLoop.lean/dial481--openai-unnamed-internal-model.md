---
{
  "module": "OAI/Computability/VPVNP/RankCursorSpaceLoop.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RankCursorSpaceLoop.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RankCursorSpaceLoop.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Bounded stack space across the descending rank scan

The loop reuses the coefficient-and-cursor workspace at each bidegree. Its
peak stack length is the same cap certified for one iteration and the
ready banks, independently of the total number of requests.


### `scan_boundedRun`

 A simultaneous time and per-stack space certificate for the entire
scan. The returned register state encodes the maximum nonzero outer degree. 
