---
{
  "module": "OAI/Computability/VPVNP/LiveHeaderPrefix.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LiveHeaderPrefix.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LiveHeaderPrefix.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Composable native header prefixes

Each prefix starts and ends at a particular stage and memory. This makes
the transfer write and cursor reset part of the interface between successive
blocks, including at the boundary between the index and advice scans.


### `StageTrace.Good`

 A full component run in the actual row, with enough budget for the
uniform outer instruction cap. 

### `StageTrace.Exec`

 The source stage runs from the given cursor zero and accepts. 

### `StagePrefix`

 A consecutive sequence of executed header stages whose transferred memory and next stage
match the entry to each succeeding call. 
