---
{
  "module": "OAI/Computability/VPVNP/PairTraversalControllerRun.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairTraversalControllerRun.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairTraversalControllerRun.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Chronological execution of the traversal controller

The active site calls advance the packed persistent ordinal by one. The
extra call at the end of each layer resets the site digit and starts the
next phase-level. The final sentinel accepts. Every call receives the
post-memory of the preceding call, including across reset boundaries.


### `Segment`

 A native interval of deterministic controller calls, with its complete
post-memory, returned ordinal, and external probe total. 

### `lift_sites`

 Lift all active calls of a single layer, using the actual pre-memory
of each reference report. A zero-site layer has the empty active segment. 

### `AtPrefixes`

 At every prefix, the resident schedule still supplies the same layer
counts and worker operands. 

### `ActiveCalls`

 Successful native execution and report conditions for every active site of this traversal
pass from a ready memory. 

### `ClosingCall`

 Native execution and report conditions for the closing call after the traversal pass has
processed its last site. 

### `lift_passes`

 Concatenate every physical pass with its own reset. The zero-size case
still executes that reset. Each wrapped site has the same post-memory as its
reference site, so the very next call reads the correct live data. 

### `RunInputs`

 A resident header supplies every actual worker lookup throughout the
prefixes of the selected reference run. 

### `run_reference`

 The single finite controller runs every reference burst in chronological
order. The final report accepts, the external memory is exactly the native
arena image, and the probe overhead counts every setup, reset and acceptance. 

### `Segment.accepted_unique`

 Every accepting tape for this deterministic controller gives the same
reports as the chronological run, including the reset and acceptance calls. 
