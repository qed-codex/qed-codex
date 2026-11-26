---
{
  "module": "OAI/Computability/VPVNP/LiveDeterministicReachable.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LiveDeterministicReachable.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LiveDeterministicReachable.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Address preservation on every continuing native history

A continuing history records every successful call which returned a cursor.
It may have no accepting extension. A verified prefix of empty-choice calls
can be removed when proving address preservation: the first report of each
such call is forced, and every continuing history beyond the prefix starts
from its actual cursor and memory.


### `Reached`

 All states and memories reached through a finite number of continuing calls. 

### `ProtectsAddress`

 Every returning call leaves this address unchanged, even on a history
whose subsequent calls may reject. 

### `ProtectsAddress.of_invariant`

 A state and memory invariant can establish the address frame on all
continuing histories by one-call induction. 

### `ReplayFrame`

 Replay each report on its actual input memory, preserving the protected address. 

### `ReplayFrame.after_eventLog`

 The memory reached after the full replay retains the protected cell. 

### `ReplayFrame.ofFn`

 An indexed sequence of actual intermediate memories supplies the frame
for every report along its replay. 

### `protects_after_replayed_prefix`

 A deterministic startup with address-preserving reports can precede any
address-preserving suffix. The post-startup memory is obtained by replaying
its complete event log, and its persistent word is the reported final cursor. 

### `protects_after_empty_prefix`

 The uniform memory frame implies the frame on the actual prefix. 
