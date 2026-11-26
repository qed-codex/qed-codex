---
{
  "module": "OAI/Computability/VPVNP/PairSimulationShrinkRowHistogram.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSimulationShrinkRowHistogram.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSimulationShrinkRowHistogram.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Histogram readback for a shrinking resident row

The selector and label arrays are disjoint from the counter bank. For a successful
entry, the descriptor, directory and gather writes also leave this bank intact.
Each emitted ordinal then increments its own counter, including repeated ordinals.


### `upper_histogram`

 On successful inputs the pure upper scratch update adds the exact number of emitted
occurrences at a live counter cell disjoint from the descriptor and pointer directory. 

### `gathered_histogram`

 A successful gather and map add the selected matrix multiplicities to the incoming counters. 

### `rowAction_histogram`

 A successful resident row adds its own parameter multiplicities to the incoming counters. 
