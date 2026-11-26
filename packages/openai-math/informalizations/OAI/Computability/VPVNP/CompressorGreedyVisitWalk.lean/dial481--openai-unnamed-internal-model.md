---
{
  "module": "OAI/Computability/VPVNP/CompressorGreedyVisitWalk.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorGreedyVisitWalk.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorGreedyVisitWalk.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Six consecutive native visits that compute the shrinking directory

The tag projection and zero publication precede the color directory. Both
offset visits begin in the post-memory of the color reader. Each packet keeps
its exact native program, public parameters, cursor interval and choice tapes.


### `Stage`

 The six native stages used to build the shrinking level's greedy color and tag directories. 

### `stages`

 Execution order of the greedy stages, beginning with shift extraction and ending with the
tag scan. 

### `visit`

 Planner visit implementing a greedy stage at the specified level and scratch origin. 

### `start`

 Initial cursor for a greedy stage. Record readers start at their first record address and
the other stages start at zero. 

### `stop`

 Exclusive cursor bound for the stage, expressed as a row count or the address past the
final walk record. 

### `fuel`

 Private instruction budget for one worker call of the given greedy stage and degree
exponent. 

### `choices`

 Empty choice tapes for the deterministic greedy calls, with one tape per row visited by the
stage. 

### `params`

 Concrete public operands of the installed worker, obtained from the greedy arena and its
incidence tables. 

### `values`

 These equalities identify the worker ABI at any memory in which the
descriptor parameters have their specified values. 

### `Source`

 Evidence that the native stage produces the stated reports from its input memory and
advances to its prescribed stop cursor. 

### `packetReports`

 Chronological reports emitted by the chosen stage of the greedy shrinking pass. 

### `packetInput`

 Input memory for the given stage after applying the reports of its predecessors in the
greedy walk. 

### `indexed_walk`

 Each stage names its own input memory and report slice in the walk. 

### `walk`

 Six actual native segments, including the guard proof for every call. 
