---
{
  "module": "OAI/Computability/VPVNP/CompressorGreedyPrepareHeaderAccess.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorGreedyPrepareHeaderAccess.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorGreedyPrepareHeaderAccess.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 # Addresses touched by the relocated greedy initializer

The control-word prefix runs entirely in registers. The next block clears
one label and writes the two words at the beginning of the vertex record.
The final block increments the private cursor.


### `Interval`

 Membership in the half-open interval of physical addresses from `lo` to `hi`. 
