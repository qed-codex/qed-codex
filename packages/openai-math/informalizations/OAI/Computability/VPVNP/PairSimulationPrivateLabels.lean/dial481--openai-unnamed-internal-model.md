---
{
  "module": "OAI/Computability/VPVNP/PairSimulationPrivateLabels.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSimulationPrivateLabels.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSimulationPrivateLabels.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Accumulating one map's labels in private memory

The motif interpreter emits one ordinal per copy, including repeated
ordinals. Seven opcodes visit these private words in sequence and increment
the corresponding private counters. This is the array read by the external
histogram flush at the end of the final-site call.


### `instruction`

 Registers hold the label cursor, its exclusive end, histogram base, one,
a label/address, and a count. The same table works at every word width. 

### `Linked`

 The machine contains the seven instructions that scan emitted label ordinals and increment
their private histogram cells. 

### `accumulate`

 The folded histogram uses a separate update for each emitted occurrence. 

### `run_separated`

 The complete native scan has no probes or binary choices. Its private
state contains every histogram update and preserves every other cell. 

### `run`

 A forward allocation with the counter bank above its label words. 

### `count_entry`

 Counting copies in the emitted list recovers the formal map exponent. 

### `run_flush`

 The last private scan of a vertex links directly to the common external
histogram suffix. Previously accumulated maps and every copy of the last
map are both present when the suffix is flushed. 
