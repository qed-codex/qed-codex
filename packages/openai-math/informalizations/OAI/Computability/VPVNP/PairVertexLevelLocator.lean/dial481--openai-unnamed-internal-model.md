---
{
  "module": "OAI/Computability/VPVNP/PairVertexLevelLocator.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairVertexLevelLocator.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairVertexLevelLocator.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# The hosted level locator for a nonleaf visit

The popped row selects the level and the packed site. The only shared register read
by the locator is DFS register seven. Its 35 fixed instructions obtain the old header
and the child directory from the eleven actual public words and the published tables.


### `bootPC`

 Place the 24 bootstrap instructions at the start of the level locator's program-counter
range. 

### `scanPC`

 Place the six descending-scan instructions immediately after the level bootstrap. 

### `finishPC`

 Place the five locator finishing instructions after both bootstrap and scan. 

### `segment`

 The 35-instruction, fourteen-register level locator used by a noninitial DFS role. 

### `trace`

 Full trace of a level lookup, combining header initialization, descending tests, and five
finishing ticks. 

### `run`

 On a selected noninitial level, the actual finite locator recovers both indices and
the exact header. All private cells, all enclosing registers and the pending choice stream
are preserved. 
