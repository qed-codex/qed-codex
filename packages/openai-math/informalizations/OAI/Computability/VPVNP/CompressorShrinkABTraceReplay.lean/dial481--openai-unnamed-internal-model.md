---
{
  "module": "OAI/Computability/VPVNP/CompressorShrinkABTraceReplay.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorShrinkABTraceReplay.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorShrinkABTraceReplay.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Replay of an admitted AB trace with another clock and header snapshot

The flattened parameters depend only on the eight planner head values.
Thus the accepted deterministic trace is unique even when the graph
builder and the online packet maker use different source clocks or
equivalent saved header memories.


### `walk_unique`

 Accepted native AB schedules with the same installed heads give the
same report list and memory endpoint, independently of the source cap. 
