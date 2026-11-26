---
{
  "module": "OAI/Computability/VPVNP/PairSimulationMapConsistency.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSimulationMapConsistency.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSimulationMapConsistency.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Native comparison of the inner selector arrays

The comparison in Theorem 6.1 reads one resident tag per copy from a port
and its anchor. It accumulates the bitwise OR of their differences. Thus a
later match cannot erase an earlier mismatch, and the same accumulator can
be passed from port to port. The scan takes seven private steps per copy
and one exit test, including for arbitrary inputs to a final-site call.


### `instruction`

 Registers hold the left cursor, exclusive left end, right cursor,
constant one, difference mask, and two scratch words. 

### `Linked`

 The enclosing machine embeds every comparison instruction at its designated label. 

### `Frame`

 The comparison only writes the two cursors, the mask and the two scratch registers. 

### `compareArrays`

 Execute the comparison on two private arrays. They may overlap and their
values need not be valid selector codes. The output mask is zero precisely
when the incoming mask was zero and every compared word agreed. 

### `compareTags`

 The two exit instructions test the accumulated difference mask. Each input
takes the same number of ticks, including an unused selector pattern or an
empty sequence. Selector validity is checked by the anchor's table lookup. 
