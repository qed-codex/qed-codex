---
{
  "module": "OAI/Computability/VPVNP/CompressorShrinkGatherDispatch.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorShrinkGatherDispatch.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorShrinkGatherDispatch.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Dispatching the shrinking width gather

The finite width worker reads only its two sorted rectangles. Its
writes stay within the dense demand pairs. The same reports can thus
be replayed after the online scheduler has prepared the active frame.


### `ReadRegion`

 Union of the two source rectangles from which the gather worker may read across `B` rows,
each with its own base and stride. 

### `WriteRegion`

 Dense output interval for the width pairs, containing two words for each of the `B * Q`
visited motifs. 

### `footprints`

 All reads can be transported across control-memory changes. All writes
are confined to the dense output even for the last pair. 

### `valid_trace`

 The complete dense gather satisfies every exclusive guard and preserves
the frame, tag, ordinal and row count of the online dispatcher. 
