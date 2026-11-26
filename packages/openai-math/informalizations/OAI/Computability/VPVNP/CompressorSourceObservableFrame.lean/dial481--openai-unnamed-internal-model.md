---
{
  "module": "OAI/Computability/VPVNP/CompressorSourceObservableFrame.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorSourceObservableFrame.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorSourceObservableFrame.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Recovering a write footprint from native replay and an external frame

Once a native schedule reads only its data region, the same reports execute
on every memory agreeing there. A write to an outside cell would force its
final value independently of its initial value. Thus a frame theorem valid
for all such initial memories excludes even temporary writes to the cell.


### `writes_of_replay`

 If the same log preserves every value in the complement, a native
instruction cannot have written there at any point of that log. 

### `replay_walk`

 A heterogeneous list of actual source calls replays under agreement on
all the addresses read by its complete event log. 
