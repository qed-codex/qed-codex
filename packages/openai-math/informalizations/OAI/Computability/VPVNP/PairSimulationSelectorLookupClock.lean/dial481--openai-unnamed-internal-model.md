---
{
  "module": "OAI/Computability/VPVNP/PairSimulationSelectorLookupClock.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSimulationSelectorLookupClock.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSimulationSelectorLookupClock.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Exact instruction counts for one selector lookup

The fixed selector table compares a single field per row, stopping at its
first match. Its clock is determined by the raw selector word and the
ordered public code table, including on a missing code.


### `selectorTicks`

 Each tested row uses a public load and a comparison. The last
instruction transfers to the rejecting or matching continuation. 

### `selectorTicks_of_mem`

 A successful table ordinal uses two instructions for each preceding
row and two for its own row, followed by the public ordinal load. 

### `native_selector_exact`

 Run the linked selector lookup for its computed instruction count. 

### `native_tag_exact`

 A tag is read with exactly six instructions per bit and one final guard,
then looked up with the clock of its actual word. 
