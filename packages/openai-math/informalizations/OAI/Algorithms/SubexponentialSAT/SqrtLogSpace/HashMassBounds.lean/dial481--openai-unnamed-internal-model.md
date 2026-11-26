---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/HashMassBounds.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/HashMassBounds.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/HashMassBounds.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 Fixed polynomial overhead for the actual marked-mass command. The query
cost bound is charged for every original clause reference, including the last. 

### `reference_length`

 The actual generated unary index has at most m bits when its index is
strictly below m. No exponential reference table is present. 

### `massBudget_le`

 A fixed cube suffices for all paid reference production, parser, additions,
normalization, routing and cleanup around the uniformly charged query cost. 
