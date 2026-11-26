---
{
  "module": "OAI/Computability/VPVNP/PrimedCounterVisit.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PrimedCounterVisit.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PrimedCounterVisit.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Online traversal with a shared histogram

Each binary branch tape belongs to one node visit. The visit pops a frame,
decodes the choice at its actual degree, checks and sets the selected mark at
a leaf, pushes the ordered children and increments one shared production
counter. Successful traversals may start with arbitrary accumulated counts.


### `VisitState`

 Logical state for visiting grammar nodes one at a time while accumulating a production
histogram shared across sites. 

### `VisitState.pending`

 Stack of grammar nodes awaiting visits, with the next node at the head. 

### `VisitState.marked`

 Terminal positions already used by the current site's parse. 

### `VisitState.counts`

 Accumulated multiplicity of each production label from the nodes visited so far. 

### `markToken`

 The one-bit mark memory accessed at a terminal. 

### `visit`

 A single node call, including exactly one increment of the nominated
production's count. 

### `visits`

 Consume all node calls. The empty stack is required at completion. 

### `visits_eq`

 Online traversal produces the same labels and mark checks as the independent
stack and branch-stream decoders. Counts from preceding sites are retained. 

### `visits_accepts`

 Accepted complete binary streams are exactly the streams of the parsimonious
local traversal, including all successful positions of every terminal. 

### `visits_counts`

 The updated shared counters after a single site equal its incoming counts
plus the production histogram from the actual binary trace. 
