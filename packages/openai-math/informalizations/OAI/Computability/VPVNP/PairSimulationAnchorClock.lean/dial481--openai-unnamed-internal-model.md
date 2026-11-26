---
{
  "module": "OAI/Computability/VPVNP/PairSimulationAnchorClock.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSimulationAnchorClock.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSimulationAnchorClock.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Exact native clock of a successful anchor scan

The descending loop visits each validated selector once. For each copy
the cost includes its preparation, padded field read, lookup and store.
The terminating cursor comparison takes one more instruction.


### `visitTicks`

 Exact cost of a single successful copy, including its ordinal store. 

### `successTicks`

 All copy clocks and the final empty-loop guard. 

### `native_success`

 Successful anchor decoding takes the same computed number of ticks
for every compatible entry configuration. It returns all validated
selector ordinals at their designated private addresses. 
